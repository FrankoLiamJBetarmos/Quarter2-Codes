print("Welcome to the Travel Itinerary App!")
destinations = []

for i in range(5):
    place = input(f"Enter destination #{i+1}: ")
    destinations.append(place)


print("\nYour original travel destinations:")
print(destinations)


new_second = input("\nEnter a new destination to replace the 2nd one: ")
new_fifth = input("Enter a new destination to replace the 5th one: ")


destinations[1] = new_second
destinations[4] = new_fifth 


print("\nYour updated travel itinerary:")
for i, place in enumerate(destinations, start=1):
    print(f"{i}. {place}")
