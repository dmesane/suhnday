"""
Tests for calculator module - verifying parse_config fix
"""
from calculator import parse_config

def test_parse_config_with_json():
    """Test parse_config with valid JSON string"""
    config_str = '{"host": "localhost", "port": 8080}'
    result = parse_config(config_str)
    assert result == {"host": "localhost", "port": 8080}

def test_parse_config_with_python_literal():
    """Test parse_config with Python literal (dict)"""
    config_str = "{'host': 'localhost', 'port': 8080}"
    result = parse_config(config_str)
    assert result == {"host": "localhost", "port": 8080}

def test_parse_config_with_list():
    """Test parse_config with list"""
    config_str = '[1, 2, 3, 4, 5]'
    result = parse_config(config_str)
    assert result == [1, 2, 3, 4, 5]

def test_parse_config_rejects_code_execution():
    """Test that parse_config safely rejects code execution attempts"""
    # This would have been dangerous with eval()
    malicious_str = "__import__('os').system('echo hacked')"

    try:
        parse_config(malicious_str)
        raise AssertionError("Should have raised ValueError")
    except ValueError:
        pass  # Expected

def test_parse_config_invalid_string():
    """Test parse_config with invalid string"""
    try:
        parse_config("not valid json or literal")
        raise AssertionError("Should have raised ValueError")
    except ValueError:
        pass  # Expected

if __name__ == "__main__":
    # Run basic tests
    test_parse_config_with_json()
    print("✓ JSON parsing works")

    test_parse_config_with_python_literal()
    print("✓ Python literal parsing works")

    test_parse_config_with_list()
    print("✓ List parsing works")

    test_parse_config_rejects_code_execution()
    print("✓ Code execution blocked (security fix verified)")

    test_parse_config_invalid_string()
    print("✓ Invalid input rejected properly")

    print("\nAll tests passed! Security vulnerability fixed.")
