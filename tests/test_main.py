from io import StringIO
from unittest.mock import patch

from app import main


def test_sample_function():
    """Test sample_function with various inputs."""
    assert main.sample_function(1, 1) == 2
    assert main.sample_function(10, 20) == 30
    assert main.sample_function(-5, 5) == 0


def test_main():
    """Test main() returns correct exit code and prints output."""
    captured_output = StringIO()
    with patch("sys.stdout", new=captured_output):
        result = main.main()

    assert result == 0
    assert "Hello World." in captured_output.getvalue()
