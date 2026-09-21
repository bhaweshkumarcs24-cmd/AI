def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

for i in range(6):
    status = rooms[location]
    action = vacuum_agent(location, status)

    print(f"Location: {location}, Status: {status}, Action: {action}")

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"
