import sqlite3

# Function to create a database connection
def create_connection(db_file):
    """Create a database connection."""
    conn = sqlite3.connect(db_file)
    return conn

# Function to create tables
def create_tables(connection):
    """Create tables for clients, artists, services, and transactions."""
    cursor = connection.cursor()

    # Create clients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone_number TEXT,
            preferred_style TEXT
        )
    ''')

    # Create artists table with 'specialization' column
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            specialization TEXT,
            contact_info TEXT
        )
    ''')

    # Create services table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            cost REAL NOT NULL,
            client_id INTEGER NOT NULL,
            artist_id INTEGER NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id),
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        )
    ''')

    # Create transactions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service_id INTEGER,
            amount REAL,
            payment_status TEXT,
            transaction_date TEXT,
            FOREIGN KEY (service_id) REFERENCES services(id)
        )
    ''')

    # Commit the changes
    connection.commit()
    print("Tables created successfully.")
