import random

# Define the data using nested lists by continent
continents = ["Europe", "Asia", "North America"]

# Individual lists for each category
cities = {
    "Europe": ["Paris", "Rome", "Berlin", "Madrid"],
    "Asia": ["Tokyo", "Bangkok", "Beijing", "Delhi"],
    "North America": ["New York", "Los Angeles", "Toronto", "Mexico City"]
}

activities = {
    "Europe": ["Visit the Eiffel Tower", "Explore the Colosseum", "Tour the Berlin Wall", "Stroll through Retiro Park"],
    "Asia": ["Visit the Tokyo Tower", "Explore the Grand Palace", "Tour the Forbidden City", "Visit the Taj Mahal"],
    "North America": ["Visit Central Park", "Explore Hollywood", "Tour the CN Tower", "Visit the Zocalo"]
}

foods = {
    "Europe": ["Croissant", "Pasta", "Schnitzel", "Paella"],
    "Asia": ["Sushi", "Pad Thai", "Peking Duck", "Biryani"],
    "North America": ["Bagel", "Taco", "Poutine", "Chilaquiles"]
}

hotels = {
    "Europe": ["Hotel de Paris", "Hotel Roma", "Berlin Marriott", "Hotel Madrid"],
    "Asia": ["Shinjuku Granbell Hotel", "Banyan Tree Bangkok", "The Peninsula Beijing", "Taj Mahal Hotel"],
    "North America": ["The Ritz-Carlton New York", "The Hollywood Roosevelt", "Fairmont Royal York", "Hotel Zocalo"]
}


# Function to generate a random itinerary
def generate_itinerary(days=5):
    itinerary = []

    for day in range(1, days + 1):
        # Randomly select a continent
        continent = random.choice(continents)

        # Use indexing to select specific items from the lists
        city_index = random.randint(0, len(cities[continent]) - 1)
        activity_index = random.randint(0, len(activities[continent]) - 1)
        food_index = random.randint(0, len(foods[continent]) - 1)
        hotel_index = random.randint(0, len(hotels[continent]) - 1)

        daily_plan = {
            "Day": day,
            "Continent": continent,
            "City": cities[continent][city_index],
            "Activity": activities[continent][activity_index],
            "Food": foods[continent][food_index],
            "Hotel": hotels[continent][hotel_index]
        }

        itinerary.append(daily_plan)

    return itinerary


# Function to display the full itinerary with joined lists
def display_itinerary(itinerary):
    # Join all day plans into a complete itinerary string
    itinerary_lines = []

    for day in itinerary:
        day_summary = f"Day {day['Day']} - {day['Continent']} Adventure!"
        day_details = f"  City: {day['City']}"
        day_activity = f"  Activity: {day['Activity']}"
        day_food = f"  Food Recommendation: {day['Food']}"
        day_hotel = f"  Hotel: {day['Hotel']}"

        # Join the day's details
        day_complete = "\n".join([day_summary, day_details, day_activity, day_food, day_hotel])
        itinerary_lines.append(day_complete)

    # Join all days together with a separator
    full_itinerary = "\n\n".join(itinerary_lines)
    print(full_itinerary)
    print(f"\n🎉 Enjoy your {len(itinerary)}-day adventure!")
    return full_itinerary


# Function to select a specific day's activity (indexing)
def get_specific_day_activity(itinerary, day_number):
    if 1 <= day_number <= len(itinerary):
        day = itinerary[day_number - 1]  # Using indexing to access specific day
        return f"Day {day_number} Activity: {day['Activity']} in {day['City']}"
    else:
        return "Invalid day number!"


# Function to show all cities grouped by continent (nested lists)
def show_cities_by_continent():
    print("\n🌍 Cities Grouped by Continent:")
    print("=" * 40)
    for continent in continents:
        print(f"\n{continent}:")
        # Join cities for this continent with comma separation
        cities_list = ", ".join(cities[continent])
        print(f"  {cities_list}")


# Generate and display the itinerary
print("✈️ Welcome to the Travel Itinerary Generator! ✈️")
print("=" * 50)

# Generate a 5-day itinerary
random_itinerary = generate_itinerary(5)

print("\n📝 Your Random 5-Day Travel Itinerary:")
print("=" * 50)
full_itinerary_text = display_itinerary(random_itinerary)

# Demonstrate indexing - get activity for a specific day
print("\n🔍 Specific Day Selection:")
print("=" * 50)
print(get_specific_day_activity(random_itinerary, 2))  # Get activity for Day 2
print(get_specific_day_activity(random_itinerary, 3))  # Get activity for Day 3

# Show nested lists - cities grouped by continent
show_cities_by_continent()

# Save the full itinerary to a variable (joining all information)
print(f"\n💾 Your complete itinerary has been generated with {len(full_itinerary_text.split())} words!")
