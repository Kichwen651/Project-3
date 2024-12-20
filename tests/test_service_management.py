from unittest import mock
from unittest.mock import MagicMock
from database import create_connection
from service_management import add_service, view_all_services

# Test for adding a service
@mock.patch('service_management.sqlite3.connect')  # Mock the sqlite3.connect method in service_management
def test_add_service(mock_connect):
    # Create a mock database connection
    mock_db = MagicMock()
    
    # Mock the cursor to simulate behavior of connection.cursor()
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    
    # Arrange: Data to be inserted
    description = "Oil Painting"
    cost = 150.0
    client_id = 1
    artist_id = 2
    
    # Set the mock connection to be returned by sqlite3.connect
    mock_connect.return_value = mock_db
    
    # Act: Call the add_service function with the mock database connection
    add_service(mock_db, description, cost, client_id, artist_id)
    
    # Assert: Check if execute() was called with the expected query and parameters
    expected_query = "INSERT INTO services (description, cost, client_id, artist_id) VALUES (?, ?, ?, ?)"
    expected_args = (description, cost, client_id, artist_id)

    # Ensure the correct execute() call
    mock_cursor.execute.assert_called_once_with(
        expected_query,
        expected_args
    )


# Test for viewing all services
@mock.patch('service_management.sqlite3.connect')  # Mock the sqlite3.connect method in service_management
def test_view_all_services(mock_connect):
    # Create a mock database connection
    mock_db = MagicMock()
    
    # Mock the cursor to simulate the database result
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        ("Oil Painting", 150.0, 1, 2)
    ]
    
    # Set the mock connection to be returned by sqlite3.connect
    mock_connect.return_value = mock_db
    
    # Act: Call the function to view all services
    services = view_all_services(mock_db)
    
    # Assert: Check if the returned data matches the expected result
    assert len(services) == 1
    assert services[0] == ("Oil Painting", 150.0, 1, 2)
