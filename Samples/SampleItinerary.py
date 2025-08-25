import random

# Define comprehensive travel data by continent
travel_data = {
    "Europe": {
        "cities": ["Paris", "Rome", "Barcelona", "Amsterdam", "Prague", "Vienna", "Budapest", "Athens"],
        "activities": [
            "Visit the Eiffel Tower and Louvre Museum",
            "Explore the Colosseum and Vatican City",
            "Stroll through La Rambla and see Sagrada Familia",
            "Tour the canals and visit Van Gogh Museum",
            "Walk across Charles Bridge and see Prague Castle",
            "Visit Schönbrunn Palace and St. Stephen's Cathedral",
            "Relax in thermal baths and see Parliament Building",
            "Explore the Acropolis and Ancient Agora"
        ],
        "foods": ["Croissant and coffee", "Authentic pasta and gelato", "Tapas and paella", "Stroopwafels and cheese",
                  "Trdelník and goulash", "Wiener Schnitzel and Sachertorte", "Goulash and chimney cake",
                  "Gyros and baklava"],
        "hotels": ["Hotel de Paris", "Hotel Roma", "Barcelona Arts Hotel", "Amsterdam Canal Hotel",
                   "Prague Castle Hotel", "Vienna Imperial", "Budapest Thermal Hotel", "Athens Acropolis View"],
        "transportation": ["High-speed train", "Metro system", "Bicycle rental", "Tram network",
                           "Walking tour", "River cruise", "Hop-on hop-off bus", "Local taxi"]
    },
    "Asia": {
        "cities": ["Tokyo", "Bangkok", "Seoul", "Singapore", "Bali", "Hong Kong", "Kyoto", "Taipei"],
        "activities": [
            "Visit Shibuya Crossing and Tokyo Skytree",
            "Explore Grand Palace and floating markets",
            "Discover Gyeongbokgung Palace and Myeongdong",
            "Experience Gardens by the Bay and Sentosa",
            "Relax on beaches and visit Uluwatu Temple",
            "Ride Star Ferry and visit Victoria Peak",
            "See Fushimi Inari Shrine and Arashiyama Bamboo Forest",
            "Explore Taipei 101 and night markets"
        ],
        "foods": ["Sushi and ramen", "Pad Thai and mango sticky rice", "Korean BBQ and bibimbap",
                  "Chili crab and Hainanese chicken rice", "Nasi goreng and satay", "Dim sum and egg tarts",
                  "Kaiseki and matcha", "Beef noodle soup and bubble tea"],
        "hotels": ["Tokyo Skyline Hotel", "Bangkok Riverside Resort", "Seoul Palace Hotel", "Marina Bay Sands",
                   "Bali Beach Resort", "Hong Kong Harbour View", "Kyoto Traditional Ryokan", "Taipei 101 Hotel"],
        "transportation": ["Bullet train", "Tuk-tuk ride", "Subway system", "MRT network",
                           "Scooter rental", "Star Ferry", "Local bus", "High-speed rail"]
    },
    "North America": {
        "cities": ["New York", "Los Angeles", "Toronto", "Vancouver", "Chicago", "San Francisco", "Mexico City",
                   "Miami"],
        "activities": [
            "Visit Times Square and Statue of Liberty",
            "Explore Hollywood and Santa Monica Pier",
            "See CN Tower and Distillery District",
            "Visit Stanley Park and Capilano Suspension Bridge",
            "Explore Millennium Park and Art Institute",
            "Walk across Golden Gate Bridge and see Alcatraz",
            "Visit Zócalo and National Anthropology Museum",
            "Relax on South Beach and explore Art Deco District"
        ],
        "foods": ["New York pizza and bagels", "California burgers and tacos", "Poutine and maple treats",
                  "Fresh seafood and poutine", "Deep dish pizza and hot dogs", "Sourdough bread and clam chowder",
                  "Tacos and mole poblano", "Cuban sandwiches and key lime pie"],
        "hotels": ["New York Skyline Hotel", "Hollywood Luxury Resort", "Toronto Downtown Hotel",
                   "Vancouver Waterfront",
                   "Chicago Magnificent Mile", "San Francisco Bay Hotel", "Mexico City Historic Hotel",
                   "Miami Beach Resort"],
        "transportation": ["Subway system", "Ride-sharing services", "Streetcar network", "SeaBus ferry",
                           "L train system", "Cable cars", "Metrobus system", "Miami Metromover"]
    },
    "South America": {
        "cities": ["Rio de Janeiro", "Buenos Aires", "Lima", "Cusco", "Santiago", "Bogotá", "Quito", "Cartagena"],
        "activities": [
            "Visit Christ the Redeemer and Copacabana Beach",
            "Explore La Boca and see Tango show",
            "Experience culinary tour and Larco Museum",
            "Visit Machu Picchu and Sacred Valley",
            "See Cerro San Cristóbal and wine valleys",
            "Explore Monserrate and Gold Museum",
            "Visit Middle of the World and historic center",
            "Walk through walled city and visit Castillo San Felipe"
        ],
        "foods": ["Feijoada and caipirinha", "Asado and empanadas", "Ceviche and pisco sour",
                  "Lomo saltado and quinoa dishes", "Empanadas and Chilean wine", "Ajiaco and bandeja paisa",
                  "Llapingachos and canelazo", "Arepas and fresh seafood"],
        "hotels": ["Rio Beachfront Hotel", "Buenos Aires Tango Hotel", "Lima Culinary Hotel", "Cusco Mountain Lodge",
                   "Santiago Wine Hotel", "Bogotá Andean Hotel", "Quito Historic Hotel", "Cartagena Colonial Hotel"],
        "transportation": ["Cable car to Sugarloaf", "Subte system", "Local combi buses", "Inca Trail hiking",
                           "Metro system", "TransMilenio bus", "TelefériQo cable car", "Horse carriage rides"]
    }
}


def get_user_continent():
    """Ask user which continent they want to explore"""
    print("🌍 WELCOME TO THE CONTINENT EXPLORER ITINERARY GENERATOR! 🌍")
    print("=" * 60)
    print("\nAvailable continents to explore:")

    # Display available continents
    continents = list(travel_data.keys())
    for i, continent in enumerate(continents, 1):
        print(f"{i}. {continent}")

    # Get user choice
    while True:
        try:
            choice = int(input("\nWhich continent would you like to explore? (Enter number): "))
            if 1 <= choice <= len(continents):
                selected_continent = continents[choice - 1]
                print(f"\n🎉 Excellent choice! Let's explore {selected_continent}!")
                return selected_continent
            else:
                print(f"Please enter a number between 1 and {len(continents)}")
        except ValueError:
            print("Please enter a valid number!")


def generate_continent_itinerary(continent, days=5):
    """Generate a 5-day itinerary for the selected continent"""
    if continent not in travel_data:
        return []

    continent_data = travel_data[continent]
    itinerary = []
    used_cities = set()

    # Ensure we have enough unique cities for the itinerary
    available_cities = continent_data["cities"].copy()
    random.shuffle(available_cities)

    for day in range(1, days + 1):
        # Select a city (try to use unique cities first)
        if available_cities:
            city = available_cities.pop()
            used_cities.add(city)
        else:
            # If we run out of unique cities, reuse one
            city = random.choice(continent_data["cities"])

        # Get corresponding items using indexing
        city_index = continent_data["cities"].index(city)

        daily_plan = {
            "Day": day,
            "Continent": continent,
            "City": city,
            "Activity": continent_data["activities"][city_index % len(continent_data["activities"])],
            "Food": continent_data["foods"][city_index % len(continent_data["foods"])],
            "Hotel": continent_data["hotels"][city_index % len(continent_data["hotels"])],
            "Transportation": continent_data["transportation"][city_index % len(continent_data["transportation"])]
        }

        itinerary.append(daily_plan)

    return itinerary


def display_continent_itinerary(itinerary):
    """Display the 5-day continent itinerary"""
    if not itinerary:
        print("No itinerary could be generated. Please try again.")
        return

    continent = itinerary[0]["Continent"]

    print(f"\n📋 YOUR 5-DAY {continent.upper()} ADVENTURE ITINERARY")
    print("=" * 70)

    # Build the complete itinerary by joining daily plans
    itinerary_lines = []

    for day in itinerary:
        day_header = f"DAY {day['Day']}: {day['City']} - {day['Continent']}"
        day_details = [
            f"🏨 Accommodation: {day['Hotel']}",
            f"🚗 Transportation: {day['Transportation']}",
            f"🎯 Main Activity: {day['Activity']}",
            f"🍽️  Culinary Experience: {day['Food']}"
        ]

        # Join day details
        day_complete = "\n".join([day_header, "─" * 50] + day_details)
        itinerary_lines.append(day_complete)

    # Join all days together
    full_itinerary = "\n\n".join(itinerary_lines)
    print(full_itinerary)

    # Add summary
    cities_visited = [day["City"] for day in itinerary]
    unique_cities = set(cities_visited)

    summary_lines = [
        f"\n📊 ITINERARY SUMMARY:",
        f"Total days: {len(itinerary)}",
        f"Cities visited: {', '.join(cities_visited)}",
        f"Unique destinations: {len(unique_cities)}",
        f"Continent explored: {continent}"
    ]

    print("\n".join(summary_lines))


def show_continent_highlights(continent):
    """Show highlights of the selected continent"""
    if continent not in travel_data:
        return

    print(f"\n🌟 {continent.upper()} HIGHLIGHTS:")
    print("=" * 40)

    data = travel_data[continent]

    # Join and display highlights
    highlights = [
        f"🏙️  Major Cities: {', '.join(data['cities'][:4])}...",
        f"🎯 Top Activities: {data['activities'][0].split(' and ')[0]}, {data['activities'][1].split(' and ')[0]}...",
        f"🍽️  Local Cuisine: {data['foods'][0].split(' and ')[0]}, {data['foods'][1].split(' and ')[0]}...",
        f"🚗 Transportation: {data['transportation'][0]}, {data['transportation'][1]}..."
    ]

    print("\n".join(highlights))


def main():
    """Main function to run the continent explorer"""
    # Get user's continent choice
    selected_continent = get_user_continent()

    # Show continent highlights
    show_continent_highlights(selected_continent)

    # Generate 5-day itinerary
    print(f"\n🗓️  Generating your personalized 5-day {selected_continent} itinerary...")
    itinerary = generate_continent_itinerary(selected_continent, 5)

    # Display the complete itinerary
    display_continent_itinerary(itinerary)

    # Option to generate another itinerary
    print(f"\n🔄 Would you like to explore another continent?")
    try_again = input("Enter 'y' to try another continent or any other key to exit: ").lower()

    if try_again == 'y':
        main()
    else:
        print("\n✨ Thank you for using the Continent Explorer! Safe travels! ✈️")


if __name__ == "__main__":
    main()
