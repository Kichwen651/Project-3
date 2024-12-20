import sqlite3

def add_service(connection, description, cost, client_id, artist_id):
    """Add a new service to the database."""
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO services (description, cost, client_id, artist_id)
        VALUES (?, ?, ?, ?)
    ''', (description, cost, client_id, artist_id))
    connection.commit()
    print("New service added successfully.")

def view_all_services(connection):
    """Retrieve all services from the database and display details."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM services")
    services = cursor.fetchall()

    if not services:
        print("No services found.")  # Added message if no services are found
    else:
        print("Services List:")
        for service in services:
            # Printing each service's details with client_id and artist_id
            print(f"Service ID: {service[0]}")
            print(f"Description: {service[1]}")
            print(f"Cost: {service[2]}")
            print(f"Client ID: {service[3]}")
            print(f"Artist ID: {service[4]}")
            print('-' * 30)  # Separator for better readability

    return services

def update_service(connection, service_id, description, cost, client_id, artist_id):
    """Update a service's details in the database."""
    cursor = connection.cursor()
    
    # First, check if the service exists
    cursor.execute('SELECT * FROM services WHERE id = ?', (service_id,))
    service = cursor.fetchone()
    
    if service:
        # If service exists, update it including client_id and artist_id
        cursor.execute('''
            UPDATE services
            SET description = ?, cost = ?, client_id = ?, artist_id = ?
            WHERE id = ?
        ''', (description, cost, client_id, artist_id, service_id))
        connection.commit()
        
        print(f"Service with ID {service_id} has been updated.")
    else:
        print(f"Service with ID {service_id} not found.")
        
def delete_service(connection, service_id):
    """Delete a service from the database."""
    cursor = connection.cursor()
    cursor.execute("DELETE FROM services WHERE id = ?", (service_id,))
    connection.commit()
    print(f"Service with ID {service_id} has been deleted.")