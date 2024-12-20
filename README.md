# Art Client Management System (ACMS)
## Owner: Victor Kichwen
# Date: 17-12-2024

# Overview
The Art Client Management System (ACMS) is a Python-based application designed to help manage clients, artists, art services, and transactions within an art gallery, studio, or art consultancy. It integrates with a MySQL database to store data and provides an interactive command-line interface (CLI) to perform various operations related to client management, artist assignments, and art transactions.

# Features
1. Manage Clients: Add, view, update, and delete clients.
2. Manage Artists: Add, view, update, and delete artists.
3. Manage Art Services: Add, view, update, and delete art services like commissions, purchases, or consultations.
4. Track Transactions: Record sales, commissions, and payments for art services.
5. Manage Artist Assignments: Assign artists to specific art services or client projects.
# Prerequisites
Before using the system, ensure that the following software is installed
Install Python 3.x if it’s not already installed on your system. You can download Python from the official website here.

# MySQL
 To install MySQL, follow the steps below:
On Ubuntu:
1. sudo apt update
2. sudo apt install mysql-server
3. Once installed, start MySQL:
4. sudo systemctl start mysql
5. Secure the MySQL installation:
sudo mysql_secure_installation
Set a password for the MySQL root user when prompted.

MySQL Connector for Python
You need the mysql-connector-python package to interact with MySQL in Python. To install it, run:
bash
Copy code
pip install mysql-connector-python
Installation Steps
1. Install MySQL Server
Follow the installation steps mentioned above under the "MySQL" section to install MySQL on your system.

2. Install Python and Dependencies
Ensure Python 3.x is installed on your system. If not, install it as follows:

sudo apt install python3 python3-pip
3. Create a Virtual Environment and Install Dependencies:
bash
Copy code
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install MySQL connector for Python
pip install mysql-connector-python
4. Create the Database and Tables
Log into MySQL to create the database and required tables:

sudo mysql -u root -p
Once logged in, execute the following SQL commands:


CREATE DATABASE ArtClientManagement;

USE ArtClientManagement;

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(50),
    art_style VARCHAR(255)
);

CREATE TABLE artists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    specialization VARCHAR(255),
    contact VARCHAR(255)
);

CREATE TABLE art_services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    cost INT,
    artist_id INT,
    client_id INT,
    FOREIGN KEY (artist_id) REFERENCES artists(id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_id INT,
    price INT,
    payment_status VARCHAR(50),
    FOREIGN KEY (service_id) REFERENCES art_services(id)
);
5. Configure MySQL Connection
Ensure that the MySQL connection details are correctly set in the code (in db.py or a similar file):

python
Copy code
import mysql.connector

def get_connection():
    """Establish and return a connection to the MySQL database."""
    connection = mysql.connector.connect(
        host='localhost',
        database='ArtClientManagement',  # Database name
        user='root',  # MySQL user
        password='1234'  # MySQL password
    )
    return connection
6. Run the Application
Once your database is set up and dependencies are installed, run the main.py file to launch the interactive CLI:

python3 main.py
Usage
1. Menu Options
Once the program starts, you’ll see a menu with the following options:

1. Manage Clients
2. Manage Artists
3. Manage Art Services
4. Track Transactions
5. Exit

2. Manage Clients
Add a Client:
Choose "Manage Clients", then select "Add Client". Provide the client's name, email, phone, and preferred art style.

View Clients:
Choose "Manage Clients", then select "View Clients" to view all clients in the system.

Update a Client:
Choose "Manage Clients", then select "Update Client". Provide the client ID and new details.

Delete a Client:
Choose "Manage Clients", then select "Delete Client". Provide the client ID to delete the client.

3. Manage Artists
Add Artist:
Choose "Manage Artists", then select "Add Artist". Provide the artist's name, specialization, and contact information.

View Artists:
Choose "Manage Artists", then select "View Artists" to view all artists.

Update Artist:
Choose "Manage Artists", then select "Update Artist". Provide the artist ID and new details.

Delete Artist:
Choose "Manage Artists", then select "Delete Artist". Provide the artist ID to delete the artist.

4. Manage Art Services
Add Art Service:
Choose "Manage Art Services", then select "Add Art Service". Provide the service description, cost, client ID, and artist ID.

View Art Services:
Choose "Manage Art Services", then select "View Art Services" to see all services provided.

Update Art Service:
Choose "Manage Art Services", then select "Update Art Service". Provide the service ID and updated details.

Delete Art Service:
Choose "Manage Art Services", then select "Delete Art Service". Provide the service ID to remove it.

5. Track Transactions
Add Transaction:
Choose "Track Transactions", then select "Add Transaction". Provide the service ID, price, and payment status.

View Transactions:
Choose "Track Transactions", then select "View Transactions" to see all transactions made.

6. Exit
To exit the application, simply select "Exit" from the main menu.

Example Usage
Adding a New Client:
Choose "Manage Clients" > "Add Client".
Enter the client's details (e.g., name: Alice, email: alice@example.com, phone: 123-456-7890, art style: Contemporary).

Viewing Clients:
Choose "Manage Clients" > "View Clients" to see all clients in the system.

Adding a New Art Service:
Choose "Manage Art Services" > "Add Art Service".
Enter the service description (e.g., custom art commission), cost (e.g., 2000), client ID, and artist ID.

Recording a Transaction:
Choose "Track Transactions" > "Add Transaction".
Enter the service ID, price (e.g., 2000), and payment status (e.g., Paid).

# Error Handling
If the application cannot connect to the MySQL database, check the following:

# Ensure MySQL is running.
Verify the database and tables exist.
Check if the MySQL user and password are correctly set in db.py.
To start MySQL, run:

sudo systemctl start mysql
If MySQL doesn’t start, check its status:
sudo systemctl status mysql



# Access MySQL Command Line
You can access the MySQL command line interface with:
mysql -u root -p

# Demonstrations
For the slides one can access using the following link:
https://docs.google.com/presentation/d/19PFdfAqOMR2zTPBptic8dSIjLq5UDhPUx5GmcqIyhIg/edit?usp=sharing


