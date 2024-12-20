import pytest
from unittest import mock
from client_management import add_client, view_all_clients, update_client, delete_client

# Test add_client function
@mock.patch('sqlite3.connect')  # Mock the sqlite3 connection
def test_add_client(mock_connect):
    # Arrange
    connection = mock.Mock()  # Mock the connection object
    mock_connect.return_value = connection  # Mock the connect method to return our mock connection

    cursor = mock.Mock()  # Mock the cursor object
    connection.cursor.return_value = cursor  # Mock the cursor method to return our mock cursor

    name = "James Donien"
    email = "jamesdoe@example.com"
    phone_number = "123456789"
    preferred_style = "Modern"
    
    # Act: Call the function under test
    add_client(connection, name, email, phone_number, preferred_style)

    # Assert: Check if execute was called with the correct parameters
    cursor.execute.assert_called_once_with(
        "INSERT INTO clients (name, email, phone_number, preferred_style) VALUES (?, ?, ?, ?)",
        (name, email, phone_number, preferred_style)
    )
    
    # Check that commit was called
    connection.commit.assert_called_once()

# Test view_all_clients function
@mock.patch('sqlite3.connect')  # Mock the sqlite3 connection
def test_view_all_clients(mock_connect):
    # Arrange: mock cursor and fetchall to return expected data
    mock_cursor = mock.MagicMock()
    mock_db = mock.MagicMock()
    mock_db.cursor.return_value = mock_cursor  # Ensure cursor() returns a mock cursor
    mock_connect.return_value = mock_db  # Ensure connect() returns our mock_db
    mock_cursor.fetchall.return_value = [
        ("John Doe", "johndoe@example.com", "123456789", "Modern")
    ]
    
    # Act: Call the function under test
    clients = view_all_clients(mock_db)
    
    # Assert: Verify the returned list contains one client
    assert len(clients) == 1
    assert clients[0] == ("John Doe", "johndoe@example.com", "123456789", "Modern")

# Test for updating client information
@mock.patch('sqlite3.connect')
def test_update_client(mock_connect):
    # Arrange
    connection = mock.Mock()
    mock_connect.return_value = connection

    cursor = mock.Mock()
    connection.cursor.return_value = cursor

    client_id = 1
    new_name = "John Doe Updated"
    email = "johnupdated@example.com"
    phone_number = "987654321"
    preferred_style = "Contemporary"

    # Act: Call the function under test
    update_client(connection, client_id, new_name, email, phone_number, preferred_style)

    # Assert: Ensure execute() was called with the correct query and parameters
    cursor.execute.assert_called_once_with(
        "UPDATE clients SET name = ?, email = ?, phone_number = ?, preferred_style = ? WHERE id = ?",
        (new_name, email, phone_number, preferred_style, client_id)
    )
    
    # Also, check that commit was called
    connection.commit.assert_called_once()

# Test for deleting a client
@mock.patch('sqlite3.connect')
def test_delete_client(mock_connect):
    # Arrange
    connection = mock.Mock()
    mock_connect.return_value = connection

    cursor = mock.Mock()
    connection.cursor.return_value = cursor

    client_id = 1

    # Act: Call the function under test
    delete_client(connection, client_id)

    # Assert: Ensure execute() was called with the correct query and parameters
    cursor.execute.assert_called_once_with(
        "DELETE FROM clients WHERE id = ?", (client_id,)
    )
    
    # Also, check that commit was called
    connection.commit.assert_called_once()

