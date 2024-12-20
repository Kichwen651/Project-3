from unittest import mock
from transaction_management import add_transaction, view_all_transactions
from unittest.mock import MagicMock
from datetime import datetime

# Test for adding a transaction
@mock.patch('transaction_management.sqlite3.connect')  # Mock the sqlite3.connect method
def test_add_transaction(mock_db):
    # Arrange
    service_id = 1
    amount = 100.0
    payment_status = "Paid"
    
    # Create a mock cursor object
    mock_cursor = MagicMock()
    mock_db.cursor.return_value = mock_cursor  # Ensure cursor method returns the mock cursor
    
    # Act: Call the function under test
    add_transaction(mock_db, service_id, amount, payment_status)
    
    # Assert that execute was called once with the correct parameters
    expected_query = "INSERT INTO transactions (service_id, amount, payment_status, transaction_date) VALUES (?, ?, ?, ?)"
    expected_args = (service_id, amount, payment_status, mock.ANY)  # Use mock.ANY for datetime.now() comparison
    
    # Normalize the actual query string to ignore extra spaces and newlines
    actual_query = mock_cursor.execute.call_args[0][0].strip().replace("\n", " ").replace("  ", " ")

    # Ensure the execute method is called with the expected query and arguments
    assert actual_query == expected_query, f"Expected: {expected_query}, but got: {actual_query}"
    mock_cursor.execute.assert_called_once_with(
        expected_query,
        expected_args
    )

# Test for viewing all transactions
@mock.patch('transaction_management.sqlite3.connect')  # Mock the sqlite3 connection
def test_view_all_transactions(mock_db):
    # Arrange: Mock fetch_all to return one transaction
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = [
        (1, 100.0, "Paid", datetime.now())  # The exact datetime will be replaced by mock.ANY in the assertion
    ]
    
    # Act: Call the function under test
    transactions = view_all_transactions(mock_db)
    
    # Assert that the correct transactions are returned
    assert len(transactions) == 1
    assert transactions[0] == (1, 100.0, "Paid", mock.ANY)  # mock.ANY allows any datetime value here
