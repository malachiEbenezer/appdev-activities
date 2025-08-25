# importing random module to implement randomness
import random

# Defining the travel data based on continents
travelData = {
    "Africa": {
        "cities": ["Cairo", "Cape Town", "Marrakech", "Nairobi", "Lagos",
                   "Casablanca", "Accra", "Johannesburg", "Zanzibar", "Addis Ababa"],
        "activities": [
            "Visit Pyramids and Nile Cruise",
            "Tour Table Mountain and Robben Island",
            "Explore souks and Jardin Majorelle",
            "Safari in Maasai Mara and Giraffe Center",
            "See National Museum and Freedom Park",
            "Visit Hassan II Mosque and medina",
            "Tour Independence Square and Kwame Nkrumah Museum",
            "Explore Apartheid Museum and Gold Reef City",
            "Relax on beaches and spice farms",
            "Visit National Museum and Entoto Hills"
        ],
        "foods": ["Koshari", "Bunny Chow", "Tagine", "Ugali", "Jollof Rice",
                  "Couscous", "Fufu", "Bobotie", "Zanzibar Pizza", "Injera"],
        "hotels": ["Cairo Nile Hotel", "Cape Town Harbor Hotel", "Marrakech Riad Hotel",
                   "Nairobi Safari Lodge", "Lagos City Hotel", "Casablanca Ocean Hotel",
                   "Accra Heritage Hotel", "Johannesburg Gold Hotel", "Zanzibar Beach Hotel",
                   "Addis Ababa Hills Hotel"],
        "transportation": ["Camels", "Metro system", "Taxi", "Safari jeep",
                           "Bus system", "Walking tour", "Car rental", "Ferry boat", "Train", "Uber"]
    },

    "Asia": {
        "cities": ["Tokyo", "Seoul", "Bangkok", "Beijing", "Singapore",
                   "Bali", "Kuala Lumpur", "Manila", "New Delhi", "Dubai"],
        "activities": [
            "Visit Shibuya Crossing and Tokyo Tower",
            "Explore Gyeongbokgung Palace and Myeongdong",
            "Ride a tuk-tuk and visit the Grand Palace",
            "Walk the Great Wall and explore Forbidden City",
            "Stroll at Marina Bay Sands and Gardens by the Bay",
            "Relax at beaches and rice terraces",
            "Visit Petronas Towers and Batu Caves",
            "Tour Intramuros and Rizal Park",
            "See Taj Mahal and Red Fort",
            "Go up Burj Khalifa and desert safari"
        ],
        "foods": ["Sushi", "Korean BBQ", "Pad Thai", "Peking Duck", "Chili Crab",
                  "Nasi Goreng", "Satay", "Adobo", "Curry", "Shawarma"],
        "hotels": ["Tokyo Shinjuku Hotel", "Seoul Palace Hotel", "Bangkok Riverside Hotel",
                   "Beijing Grand Hotel", "Singapore Marina Hotel", "Bali Beach Resort",
                   "KL City Hotel", "Manila Bay Hotel", "Delhi Heritage Hotel", "Dubai Skyline Hotel"],
        "transportation": ["Bullet train", "Metro system", "Tuk-tuk", "High-speed rail",
                           "MRT", "Scooter rental", "LRT", "Jeepney", "Rickshaw", "Taxi/Uber"]
    },

    "Australia": {
        "cities": ["Sydney", "Melbourne", "Auckland", "Wellington", "Brisbane",
                   "Perth", "Adelaide", "Gold Coast", "Fiji Islands", "Tahiti"],
        "activities": [
            "See Sydney Opera House and Harbour Bridge",
            "Explore Federation Square and Great Ocean Road",
            "Tour Sky Tower and Waitomo Caves",
            "Visit Te Papa Museum and Botanical Gardens",
            "Relax at beaches and Lone Pine Koala Sanctuary",
            "Explore Kings Park and Cottesloe Beach",
            "See Adelaide Hills and Barossa Valley",
            "Surfing at Surfers Paradise",
            "Snorkeling in Coral reefs",
            "Enjoy Polynesian dance and black sand beaches"
        ],
        "foods": ["Meat Pie", "Fish and Chips", "Hangi", "Lamingtons", "Pavlova",
                  "Vegemite Toast", "Seafood Platter", "BBQ", "Kava", "Tropical Fruits"],
        "hotels": ["Sydney Harbour Hotel", "Melbourne Central Hotel", "Auckland Bay Hotel",
                   "Wellington Hills Hotel", "Brisbane River Hotel", "Perth Sunset Hotel",
                   "Adelaide Wine Hotel", "Gold Coast Surf Hotel", "Fiji Island Resort", "Tahiti Beach Hotel"],
        "transportation": ["Ferry", "Train", "Tram", "Taxi", "Bus system",
                           "Scooter rental", "Walking tour", "Bike rental", "Domestic flight", "Uber"]
    },

    "Europe": {
        "cities": ["Paris", "Rome", "Barcelona", "Amsterdam", "Prague",
                   "Vienna", "Budapest", "Athens", "Berlin", "London"],
        "activities": [
            "Visit the Eiffel Tower and Louvre Museum",
            "Explore the Colosseum and Vatican City",
            "Stroll through La Rambla and see Sagrada Familia",
            "Tour the canals and visit Van Gogh Museum",
            "Walk across Charles Bridge and see Prague Castle",
            "Visit Schönbrunn Palace and St. Stephen's Cathedral",
            "Relax in thermal baths and see Parliament Building",
            "Explore the Acropolis and Ancient Agora",
            "See Brandenburg Gate and Berlin Wall",
            "Ride the London Eye and visit Big Ben"
        ],
        "foods": ["Croissant", "Pasta", "Tapas", "Stroopwafels", "Goulash",
                  "Wiener Schnitzel", "Chimney Cake", "Gyros", "Bratwurst", "Fish and Chips"],
        "hotels": ["Hotel de Paris", "Hotel Roma", "Barcelona Arts Hotel", "Amsterdam Canal Hotel",
                   "Prague Castle Hotel", "Vienna Imperial", "Budapest Thermal Hotel",
                   "Athens Acropolis View", "Berlin Central Hotel", "London Royal Hotel"],
        "transportation": ["High-speed train", "Metro system", "Bicycle rental", "Tram network",
                           "Walking tour", "River cruise", "Hop-on hop-off bus", "Local taxi",
                           "Subway", "Double-decker bus"]
    },

    "North America": {
        "cities": ["New York", "Los Angeles", "Toronto", "Vancouver", "Mexico City",
                   "Cancun", "Chicago", "Havana", "Las Vegas", "Montreal"],
        "activities": [
            "See Times Square and Statue of Liberty",
            "Walk Hollywood Boulevard and Venice Beach",
            "Visit CN Tower and Niagara Falls",
            "Explore Stanley Park and Granville Island",
            "Visit Teotihuacan Pyramids and Frida Kahlo Museum",
            "Relax at beaches and explore Chichen Itza",
            "Walk Millennium Park and Willis Tower",
            "Ride classic cars and tour Old Havana",
            "See The Strip and Bellagio Fountains",
            "Tour Old Montreal and Notre-Dame Basilica"
        ],
        "foods": ["Burger", "Tacos", "Poutine", "Hot Dog", "Bagel",
                  "Nachos", "Steak", "Lobster Roll", "Cuban Sandwich", "Maple Syrup Pancakes"],
        "hotels": ["NYC Central Hotel", "LA Sunset Hotel", "Toronto Lakeview Hotel",
                   "Vancouver Pacific Hotel", "Mexico City Plaza Hotel", "Cancun Beach Resort",
                   "Chicago Skyline Hotel", "Havana Colonial Hotel", "Vegas Strip Hotel", "Montreal Downtown Hotel"],
        "transportation": ["Subway", "Car rental", "Bus system", "Bicycle rental",
                           "Walking tour", "Taxi/Uber", "Tram", "Tour bus", "Light rail", "Airport shuttle"]
    },

    "South America": {
        "cities": ["Rio de Janeiro", "São Paulo", "Buenos Aires", "Lima", "Bogotá",
                   "Quito", "Santiago", "Cusco", "Montevideo", "La Paz"],
        "activities": [
            "Visit Christ the Redeemer and Copacabana Beach",
            "Explore Ibirapuera Park and Paulista Avenue",
            "See the Obelisk and Tango shows",
            "Tour Machu Picchu and Plaza de Armas",
            "Visit Gold Museum and Monserrate",
            "Stand at the Equator line and visit Old Town",
            "Explore Andes mountains and Plaza de Armas",
            "Hike to Machu Picchu and Sacred Valley",
            "Relax at Rambla and visit Independence Plaza",
            "See Valle de la Luna and Witches' Market"
        ],
        "foods": ["Feijoada", "Empanadas", "Ceviche", "Arepas", "Churrasco",
                  "Locro", "Asado", "Chicha Morada", "Dulce de Leche", "Quinoa Soup"],
        "hotels": ["Rio Beach Hotel", "São Paulo City Hotel", "Buenos Aires Tango Hotel",
                   "Lima Coast Hotel", "Bogotá Plaza Hotel", "Quito Andes Hotel",
                   "Santiago Central Hotel", "Cusco Inca Hotel", "Montevideo Bay Hotel", "La Paz Mountain Hotel"],
        "transportation": ["Cable car", "Metro system", "Taxi", "Walking tour",
                           "Bus system", "Bike rental", "Train", "Jeep ride", "Tour bus", "Uber"]
    }
}


def getDesiredContinent():
    # Welcome message for the user
    # 🌏✨ emojis for designs
    print("✨WELCOME TO TRAVEL-ACROSS WORLD🌏 ITINERARY GENERATOR!✨")
    print("-" * 70)
    print("\nAvailable continents to explore:")

    # Display the list of available continents
    conts = list(travelData.keys())
    for i, cont in enumerate(conts, 1):
        print(f"{i}. {cont}")

    # Getting user choice
    while True:
        try:
            # sel variable to hold the selected continent of the user
            sel = int(
                input(f"\nWhich continent would you like to explore?\nEnter number between 1 and {len(conts)}:\t\t"))
            if sel >= 1 and sel <= len(conts):
                selCont = conts[sel - 1]
                # 🎉👏 emojis for design
                print(f"\n🎉Excellent choice!🎉\nLet's explore {selCont}!👏")
                return selCont
            else:
                print(f"Please enter a number between 1 and {len(conts)} only.")
        except ValueError:
            print("Please enter what is in the selection only.")


# method for generating itinerary on a five-day basis
def genItinerary(cont, days=5):
    # condition if the continent is not in the travel data
    if cont not in travelData:
        return []

    # when continent is in travel data
    contData = travelData[cont]
    itinerary = []
    usedCities = set()

    # secure enough unique cities available for the itinerary
    availCities = contData["cities"].copy()
    # implement randomness
    random.shuffle(availCities)

    # enter looping for automatic generation of itinerary from the list
    for day in range(1, days + 1):  # start with 1 and increment after
        # Selecting a city -- using unique cities first
        if availCities:
            city = availCities.pop()
            usedCities.add(city)
        else:
            # if there is no unique cities available, reuse city
            city = random.choice(contData["cities"])

        # Getting the corresponding city using indexing
        cityIndex = contData["cities"].index(city)

        # Setting the daily itinerary
        dailyPlan = {
            "Day": day,
            "Continent": cont,
            "City": city,
            "Activity": contData["activities"][cityIndex % len(contData["activities"])],
            "Food": contData["foods"][cityIndex % len(contData["foods"])],
            "Hotel": contData["hotels"][cityIndex % len(contData["hotels"])],
            "Transportation": contData["transportation"][cityIndex % len(contData["transportation"])]
        }

        #inserting daily plan into list of the itinerary
        itinerary.append(dailyPlan)

    return itinerary