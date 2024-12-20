import sqlite3

# Function to add a new artist to the database
def add_artist(connection, name, specialization, contact_info):
    """Add a new artist to the database."""
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO artists (name, specialization, contact_info)
        VALUES (?, ?, ?)
    ''', (name, specialization, contact_info))
    connection.commit()


# Function to view all authors (though you mentioned authors, assuming you meant artists)
def view_all_artists(connection):
    """View all artists from the database."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM artists")
    artists = cursor.fetchall()
    for artist in artists:
        print(f"ID: {artist[0]}, Name: {artist[1]}, Specialization: {artist[2]}, Contact Info: {artist[3]}")
    cursor.close()


# Function to update an artist's information in the database
def update_artist(connection, artist_id, name, specialization, contact_info):
    """Update an artist's information in the database."""
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE artists
        SET name = ?, specialization = ?, contact_info = ?
        WHERE id = ?
    ''', (name, specialization, contact_info, artist_id))
    connection.commit()


# Function to delete an artist from the database
def delete_artist(connection, artist_id):
    """Delete an artist from the database."""
    cursor = connection.cursor()
    cursor.execute("DELETE FROM artists WHERE id = ?", (artist_id,))
    connection.commit()

# Example of using these functions (for demonstration)
if __name__ == '__main__':
    db_file = "main.db"  # SQLite database file

    # Establish a connection
    connection = sqlite3.connect(db_file)

    # Example usage of the functions
    add_artist(connection, "John Doe", "Painter", "john@example.com")
    view_all_artists(connection)  # Assuming you want to view artists, not authors
    update_artist(connection, 1, "John Doe", "Sculptor", "john@newemail.com")
    delete_artist(connection, 1)  # Delete the artist with ID = 1

    # Close the connection
    connection.close()
