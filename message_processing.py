def processTickets(tickets):
    current_time = max(ticket["timestamp"] for ticket in tickets)  # Determine current time
    print('current_time',current_time)
    updated_tickets = []

    for ticket in tickets:
        # Calculate waiting time
        wait_time = current_time - ticket["timestamp"]

        # If wait time > 30 minutes, elevate priority by 1 (if possible) 
        if wait_time > 30 and ticket["priority"] > 1:
            updated_tickets.append({"priority": ticket["priority"] - 1, "timestamp": ticket["timestamp"]})
        else:
            updated_tickets.append(ticket)
    print("updated_tickets:",updated_tickets)
    # Sort tickets by priority, then timestamp
    updated_tickets.sort(key=lambda x: (x["priority"], x["timestamp"]))

    return updated_tickets


# Example Input
tickets1 = [
    {"priority": 3, "timestamp": 0},
    {"priority": 4, "timestamp": 15},
    {"priority": 2, "timestamp": 45},
]

print(processTickets(tickets1))

