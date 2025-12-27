"""
Simple calculator module with some bug patterns
"""
import ast
import json

def divide(a, b):
    """Divide two numbers - FIXME: No zero division check"""
    return a / b

def calculate_average(numbers):
    """Calculate average of a list of numbers"""
    # Bug: doesn't handle empty list
    total = sum(numbers)
    return total / len(numbers)

def get_user_by_id(users, user_id):
    """Get user from list by ID"""
    # Bug: assumes user exists
    for user in users:
        if user['id'] == user_id:
            return user
    return users[0]  # HACK: return first user if not found

def process_data(data):
    """Process data dictionary"""
    # Bug: no validation that 'value' key exists
    result = data['value'] * 2
    return result

def read_file(filename):
    """Read file contents"""
    # Bug: file handle not closed properly
    f = open(filename, 'r')
    content = f.read()
    return content

class DatabaseConnection:
    """Database connection class"""

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected = False

    def connect(self):
        """Connect to database"""
        # TODO: Implement actual connection
        print(f"Connecting to {self.host}:{self.port}")
        self.connected = True

    def query(self, sql):
        """Execute SQL query"""
        # Bug: no check if connected
        # Bug: SQL injection vulnerability
        return f"Executing: {sql}"

    def close(self):
        """Close connection"""
        self.connected = False

def parse_config(config_string):
    """
    Parse configuration string safely.

    Args:
        config_string: JSON string or Python literal to parse

    Returns:
        Parsed configuration dictionary

    Raises:
        ValueError: If config_string is not valid JSON or Python literal
    """
    # Fixed: Use safe alternatives instead of eval()
    try:
        # First try JSON parsing (most common for config files)
        config = json.loads(config_string)
    except json.JSONDecodeError:
        try:
            # Fall back to ast.literal_eval for Python literals
            # This is safe - only evaluates literal structures
            config = ast.literal_eval(config_string)
        except (ValueError, SyntaxError) as e:
            raise ValueError(f"Invalid configuration string: {e}")
    return config

if __name__ == "__main__":
    # Example usage
    print(divide(10, 2))
    print(calculate_average([1, 2, 3, 4, 5]))
