import pytest
from unittest.mock import MagicMock, patch
from database import create_connection

@pytest.fixture
def mock_db():
    mock_connection = MagicMock()
    return mock_connection

# Test for create_connection function
@patch('sqlite3.connect')  # Mock sqlite3.connect
def test_create_connection(mock_connect, mock_db):
    # Arrange
    db_file = 'test.db'  # Mock database file path
    
    # Make sqlite3.connect return the mock connection
    mock_connect.return_value = mock_db
    
    # Act
    connection = create_connection(db_file)
    
    # Assert that the connection is the mocked connection
    mock_connect.assert_called_once_with(db_file)  # Ensure connect was called with the correct db file
    assert connection is mock_db  # Assert that the returned connection is the mock connection
