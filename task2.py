class ServiceTicketSystem:
    def __init__(self):
        self.service_tickets = {
            "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
            "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
        }
        self.ticket_counter = 3

    def open_ticket(self, customer, issue):
        ticket_id = f"Ticket{self.ticket_counter:03d}"
        self.service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
        self.ticket_counter += 1
        print(f"Opened new ticket: {ticket_id}")

    def update_status(self, ticket_id, status):
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = status
            print(f"Updated status of {ticket_id} to {status}.")
        else:
            print(f"Ticket {ticket_id} not found.")

    def display_tickets(self, status=None):
        if status:
            filtered_tickets = {tid: details for tid, details in self.service_tickets.items() if details["Status"] == status}
            if not filtered_tickets:
                print(f"No tickets with status '{status}'.")
            else:
                for tid, details in filtered_tickets.items():
                    print(f"{tid}: {details}")
        else:
            for tid, details in self.service_tickets.items():
                print(f"{tid}: {details}")


def main():
    ticket_system = ServiceTicketSystem()

    while True:
        print("\n1. Open New Ticket")
        print("\n2. Update Ticket Status")
        print("\n3. Display All Tickets")
        print("\n4. Display Tickets by Status")
        print("\n5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer = input("Enter customer name: ")
            issue = input("Enter issue description: ")
            ticket_system.open_ticket(customer, issue)
        elif choice == '2':
            ticket_id = input("Enter ticket ID: ")
            status = input("Enter new status (open/closed): ")
            ticket_system.update_status(ticket_id, status)
        elif choice == '3':
            ticket_system.display_tickets()
        elif choice == '4':
            status = input("Enter status to filter by (open/closed): ")
            ticket_system.display_tickets(status)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
