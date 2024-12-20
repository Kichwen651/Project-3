import sqlite3

def add_client(connection, name, email, phone_number, preferred_style):
    """Add a new client to the database."""
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO clients (name, email, phone_number, preferred_style)
        VALUES (?, ?, ?, ?)
    ''', (name, email, phone_number, preferred_style))
    connection.commit()

def view_all_clients(connection):
    """Retrieve all clients from the database."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM clients")
    return cursor.fetchall()

def update_client(connection, client_id, new_name, email, phone_number, preferred_style):
    """Update a client's information in the database."""
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE clients
        SET name = ?, email = ?, phone_number = ?, preferred_style = ?
        WHERE id = ?
    ''', (new_name, email, phone_number, preferred_style, client_id))
    connection.commit()

def delete_client(connection, client_id):
    """Delete a client from the database."""
    cursor = connection.cursor()
    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    connection.commit()
