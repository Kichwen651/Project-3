import sqlite3
from datetime import datetime
from contextlib import closing

# Function to add a new transaction
def add_transaction(connection, service_id, amount, payment_status):
    """Add a new transaction, including the current date."""
    transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current date and time
    with closing(connection.cursor()) as cursor:  # Automatically closes the cursor
        query = """
            INSERT INTO transactions (service_id, amount, payment_status, transaction_date)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (service_id, amount, payment_status, transaction_date))
        connection.commit()  # Commit the transaction

# Function to view all transactions
def view_all_transactions(connection):
    """View all transactions in the database."""
    with closing(connection.cursor()) as cursor:  # Automatically closes the cursor
        query = "SELECT * FROM transactions"
        cursor.execute(query)
        transactions = cursor.fetchall()
        return transactions

def update_transaction(connection, transaction_id, service_id, amount, payment_status):
    query = """
    UPDATE transactions
    SET service_id = ?, amount = ?, payment_status = ?
    WHERE transaction_id = ?
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, (service_id, amount, payment_status, transaction_id))
        connection.commit()
        print("Transaction updated successfully.")
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")
        print("Please check if the column 'transaction_id' exists in the 'transactions' table.")

def delete_transaction(connection, transaction_id):
    """Delete a transaction from the database."""
    with closing(connection.cursor()) as cursor:  # Automatically closes the cursor
        # Make sure to use the correct column name `transaction_id` in the WHERE clause
        cursor.execute("DELETE FROM transactions WHERE transaction_id = ?", (transaction_id,))
        connection.commit()  # Commit the changes
        print(f"Transaction with ID {transaction_id} has been deleted.")
