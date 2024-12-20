import os
from database import create_connection, create_tables
from client_management import add_client, view_all_clients, update_client, delete_client
from artist_management import add_artist, view_all_artists, update_artist, delete_artist
from service_management import add_service, view_all_services, update_service, delete_service
from transaction_management import add_transaction, view_all_transactions, update_transaction, delete_transaction

# Function to clear the screen
def clear_screen():
    # Clear the console screen (platform-dependent)
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu for the application
def main_menu():
    db_file = "main.db"  # Define the database file name
    connection = create_connection(db_file)  # Create a database connection
    
    # Create tables if they do not exist
    create_tables(connection)
    
    while True:
        clear_screen()
        print("Arts Client Management System")
        print("1. Manage Clients")
        print("2. Manage Artists")
        print("3. Manage Services")
        print("4. Manage Transactions")
        print("5. Exit")

        choice = input("Choose an option: ")
        clear_screen()
        
        if choice == '1':
            client_menu(connection)
        elif choice == '2':
            artist_menu(connection)
        elif choice == '3':
            service_menu(connection)
        elif choice == '4':
            transaction_menu(connection)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            clear_screen()

# Client management menu
def client_menu(connection):
    while True:
        print("Client Menu")
        print("1. Add Client")
        print("2. View All Clients")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. Back")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            preferred_style = input("Enter preferred art style: ")
            add_client(connection, name, email, phone_number, preferred_style)
            clear_screen()
        elif choice == '2':
            clients = view_all_clients(connection)
            for client in clients:
                print(client)
            input("Press Enter to go back.")
            clear_screen()
        elif choice == '3':
            client_id = int(input("Enter client ID: "))
            new_name = input("Enter new name (Leave blank if unchanged): ")
            email = input("Enter new email (Leave blank if unchanged): ")
            phone_number = input("Enter new phone number (Leave blank if unchanged): ")
            preferred_style = input("Enter new preferred style (Leave blank if unchanged): ")
            
            update_client(connection, client_id, new_name or None, email or None, phone_number or None, preferred_style or None)
            clear_screen()
        elif choice == '4':
            client_id = int(input("Enter client ID: "))
            delete_client(connection, client_id)
            clear_screen()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Try again.")
            clear_screen()

# Artist management menu
def artist_menu(connection):
    while True:
        print("Artist Menu")
        print("1. Add Artist")
        print("2. View All Artists")
        print("3. Update Artist")
        print("4. Delete Artist")
        print("5. Back")

        choice = input("Choose an option: ")
        clear_screen()
        
        if choice == '1':
            name = input("Enter name: ")
            specialization = input("Enter specialization: ")
            contact_info = input("Enter contact information: ")
            add_artist(connection, name, specialization, contact_info)
            clear_screen()
        elif choice == '2':
            artists = view_all_artists(connection)
            if not artists:
                print("No artists found.")
            else:
                for artist in artists:
                    print(f"ID: {artist[0]}, Name: {artist[1]}, Specialization: {artist[2]}, Contact Info: {artist[3]}")
            input("Press Enter to go back.")
            clear_screen()
        elif choice == '3':
            artist_id = int(input("Enter artist ID: "))
            name = input("Enter new name: ")
            specialization = input("Enter new specialization: ")
            contact_info = input("Enter new contact info: ")
            update_artist(connection, artist_id, name, specialization, contact_info)
            clear_screen()
        elif choice == '4':
            artist_id = int(input("Enter artist ID: "))
            delete_artist(connection, artist_id)
            clear_screen()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Try again.")
            clear_screen()

def service_menu(connection):
    while True:
        print("Service Menu")
        print("1. Add Service")
        print("2. View All Services")
        print("3. Update Service")
        print("4. Delete Service")
        print("5. Back")

        choice = input("Choose an option: ")
        clear_screen()
        
        if choice == '1':
            description = input("Enter service description: ")
            cost = float(input("Enter service cost: "))
            client_id = int(input("Enter client ID: "))
            artist_id = int(input("Enter artist ID: "))
            add_service(connection, description, cost, client_id, artist_id)
            print("Service added successfully.")
            input("Press Enter to continue.")
            clear_screen()
        elif choice == '2':  # View all services
            services = view_all_services(connection)
            if services:  # Check if any services were returned
                print("\nServices List:")
                for service in services:
                    # Displaying service details
                    print(f"Service ID: {service[0]}")
                    print(f"Description: {service[1]}")
                    print(f"Cost: {service[2]}")
                    print(f"Client ID: {service[3]}")
                    print(f"Artist ID: {service[4]}")
                    print('-' * 30)
            input("Press Enter to continue.")
            clear_screen()
        elif choice == '3':  # Update service
            service_id = int(input("Enter service ID: "))
            description = input("Enter new description: ")
            cost = float(input("Enter new cost: "))
            client_id = int(input("Enter new client ID: "))
            artist_id = int(input("Enter new artist ID: "))
            updated_service = update_service(connection, service_id, description, cost, client_id, artist_id)
            
            if updated_service:
                print(f"Service with ID {service_id} has been updated successfully.")
            input("Press Enter to continue.")
            clear_screen()
        elif choice == '4':  # Delete service
            service_id = int(input("Enter service ID to delete: "))
            delete_service(connection, service_id)
            print(f"Service with ID {service_id} has been deleted.")
            input("Press Enter to continue.")
            clear_screen()
        elif choice == '5':  # Go back to previous menu
            return
        else:
            print("Invalid choice. Try again.")
            clear_screen()

# Transaction management menu
def transaction_menu(connection):
    while True:
        print("Transaction Menu")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Back")

        choice = input("Choose an option: ")
        clear_screen()
        
        if choice == '1':
            service_id = int(input("Enter service ID: "))
            amount = float(input("Enter amount: "))
            payment_status = input("Enter payment status: ")
            add_transaction(connection, service_id, amount, payment_status)
            clear_screen()
        elif choice == '2':
            transactions = view_all_transactions(connection)
            for transaction in transactions:
                print(transaction)
            input("Press Enter to go back.")
            clear_screen()
        elif choice == '3':
            transaction_id = int(input("Enter transaction ID: "))
            service_id = int(input("Enter new service ID: "))
            amount = float(input("Enter new amount: "))
            payment_status = input("Enter new payment status: ")
            update_transaction(connection, transaction_id, service_id, amount, payment_status)
            clear_screen()
        elif choice == '4':
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_transaction(connection, transaction_id)
            clear_screen()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Try again.")
            clear_screen()

# Main execution
if __name__ == "__main__":
    main_menu()
