from unittest import mock
import pytest
import sqlite3
from artist_management import add_artist, update_artist, delete_artist, view_all_artists

# Test for add_artist
@mock.patch('sqlite3.connect')  # Mock sqlite3.connect
def test_add_artist(mock_connect):
    # Arrange
    connection = mock.Mock()  # Mock the connection object
    mock_connect.return_value = connection  # Mock the connect method to return our mock connection

    cursor = mock.Mock()  # Mock the cursor object
    connection.cursor.return_value = cursor  # Mock the cursor method to return our mock cursor

    name = "Vincent Van Gogh"
    specialization = "Impressionism"
    contact_info = "vincent@vangogh.com"

    # Act: Call the function under test
    add_artist(connection, name, specialization, contact_info)

    # Assert: Check if execute was called with correct parameters
    cursor.execute.assert_called_once_with(
        "INSERT INTO artists (name, specialization, contact_info) VALUES (?, ?, ?)",
        (name, specialization, contact_info)
    )

# Test for update_artist
@mock.patch('sqlite3.connect')
def test_update_artist(mock_connect):
    # Arrange
    connection = mock.Mock()
    mock_connect.return_value = connection

    cursor = mock.Mock()
    connection.cursor.return_value = cursor

    artist_id = 1
    new_name = "Claude Monet"
    new_specialization = "Impressionism"
    new_contact_info = "claude@monet.com"

    # Act: Call the function under test
    update_artist(connection, artist_id, new_name, new_specialization, new_contact_info)

    # Assert: Ensure execute() was called with the correct query and parameters
    cursor.execute.assert_called_once_with(
        "UPDATE artists SET name = ?, specialization = ?, contact_info = ? WHERE id = ?",
        (new_name, new_specialization, new_contact_info, artist_id)
    )

# Test for delete_artist
@mock.patch('sqlite3.connect')
def test_delete_artist(mock_connect):
    # Arrange
    connection = mock.Mock()
    mock_connect.return_value = connection

    cursor = mock.Mock()
    connection.cursor.return_value = cursor

    artist_id = 1

    # Act: Call the function under test
    delete_artist(connection, artist_id)

    # Assert: Ensure execute() was called with the correct query and parameters
    cursor.execute.assert_called_once_with(
        "DELETE FROM artists WHERE id = ?",
        (artist_id,)
    )

# Test for view_all_artists
@mock.patch('sqlite3.connect')  # Correctly patch sqlite3.connect used in artist_management
def test_view_all_artists(mock_connect):
    # Arrange
    mock_db = mock.Mock()
    mock_connect.return_value = mock_db
    mock_cursor = mock.Mock()
    mock_db.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [
        ("Vincent Van Gogh", "Impressionism", "vincent@vangogh.com")
    ]

    # Act: Call the function under test
    artists = view_all_artists(mock_db)

    # Assert: Ensure the function returns the correct data
    assert len(artists) == 1
    assert artists[0] == ("Vincent Van Gogh", "Impressionism", "vincent@vangogh.com")
