import random

# Define shopping categories with nested lists
shopping_categories = {
    "Clothes": [
        {"item": "T-shirt", "price": 25.99},
        {"item": "Jeans", "price": 49.99},
        {"item": "Dress", "price": 79.99},
        {"item": "Sweater", "price": 45.50},
        {"item": "Jacket", "price": 89.99},
        {"item": "Shoes", "price": 69.99},
        {"item": "Socks", "price": 8.99},
        {"item": "Hat", "price": 19.99}
    ],
    "Gadgets": [
        {"item": "Wireless Earbuds", "price": 89.99},
        {"item": "Phone Case", "price": 24.99},
        {"item": "Power Bank", "price": 39.99},
        {"item": "Smartwatch", "price": 199.99},
        {"item": "USB Cable", "price": 12.99},
        {"item": "Bluetooth Speaker", "price": 59.99},
        {"item": "Headphones", "price": 79.99},
        {"item": "Screen Protector", "price": 15.99}
    ],
    "Snacks": [
        {"item": "Chips", "price": 3.99},
        {"item": "Chocolate Bar", "price": 2.50},
        {"item": "Popcorn", "price": 4.99},
        {"item": "Cookies", "price": 5.99},
        {"item": "Nuts", "price": 6.99},
        {"item": "Energy Drink", "price": 3.25},
        {"item": "Granola Bar", "price": 2.99},
        {"item": "Fruit Snacks", "price": 4.50}
    ],
    "Books": [
        {"item": "Novel", "price": 14.99},
        {"item": "Cookbook", "price": 24.99},
        {"item": "Manga", "price": 9.99},
        {"item": "Self-Help Book", "price": 19.99},
        {"item": "Magazine", "price": 6.99},
        {"item": "Notebook", "price": 8.99},
        {"item": "Journal", "price": 12.99},
        {"item": "Pens Set", "price": 7.99}
    ],
    "Home Decor": [
        {"item": "Candle", "price": 15.99},
        {"item": "Picture Frame", "price": 22.99},
        {"item": "Throw Pillow", "price": 29.99},
        {"item": "Vase", "price": 34.99},
        {"item": "Wall Art", "price": 45.99},
        {"item": "Plant", "price": 19.99},
        {"item": "Rug", "price": 89.99},
        {"item": "Lamp", "price": 49.99}
    ]
}


def generate_shopping_list(budget):
    """Generate a random shopping list within the specified budget"""
    shopping_list = []
    remaining_budget = budget
    attempts = 0
    max_attempts = 100  # Prevent infinite loops

    # Create a flat list of all items for easier random selection
    all_items = []
    for category, items in shopping_categories.items():
        for item in items:
            all_items.append({
                "category": category,
                "item": item["item"],
                "price": item["price"]
            })

    # Randomly select items until budget is filled
    while remaining_budget > 0 and attempts < max_attempts:
        # Filter items that fit within remaining budget
        affordable_items = [item for item in all_items if item["price"] <= remaining_budget]

        if not affordable_items:
            break  # No more items that fit the budget

        # Randomly select an item
        selected_item = random.choice(affordable_items)

        # Add to shopping list
        shopping_list.append(selected_item)
        remaining_budget -= selected_item["price"]
        attempts += 1

    return shopping_list, remaining_budget


def display_shopping_list(shopping_list, total_budget, remaining_budget):
    """Display the final shopping list with costs"""
    if not shopping_list:
        print("No items could be added within your budget. Try increasing your budget!")
        return

    # Calculate total spent
    total_spent = total_budget - remaining_budget

    # Group items by category
    categorized_items = {}
    for item in shopping_list:
        category = item["category"]
        if category not in categorized_items:
            categorized_items[category] = []
        categorized_items[category].append(item)

    # Build the final shopping list string by joining lists
    print(f"\n🛍️  YOUR SHOPPING LIST (Budget: ${total_budget:.2f})")
    print("=" * 60)

    # Join items by category
    for category, items in categorized_items.items():
        print(f"\n{category.upper()}:")
        print("-" * 30)

        # Join individual items with their prices
        item_lines = []
        for item in items:
            item_lines.append(f"  • {item['item']}: ${item['price']:.2f}")

        # Join all items in this category
        print("\n".join(item_lines))

    # Join summary information
    summary_lines = [
        f"\n💰 SUMMARY:",
        f"Total Budget: ${total_budget:.2f}",
        f"Total Spent: ${total_spent:.2f}",
        f"Remaining Budget: ${remaining_budget:.2f}",
        f"Number of Items: {len(shopping_list)}"
    ]

    print("\n".join(summary_lines))


def show_all_categories():
    """Display all available shopping categories and items"""
    print("\n📋 AVAILABLE SHOPPING CATEGORIES:")
    print("=" * 50)

    for category, items in shopping_categories.items():
        print(f"\n{category}:")
        # Join item names with commas
        item_names = [item["item"] for item in items]
        print(f"  {', '.join(item_names)}")


def main():
    """Main function to run the shopping budget planner"""
    print("🛒 WELCOME TO THE SHOPPING BUDGET PLANNER! 🛒")
    print("=" * 50)

    # Get user budget
    try:
        budget = float(input("Enter your shopping budget: $"))
        if budget <= 0:
            print("Please enter a positive budget amount!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    # Show available categories
    show_all_categories()

    # Generate shopping list
    print(f"\n🎲 Generating random shopping list within ${budget:.2f} budget...")
    shopping_list, remaining_budget = generate_shopping_list(budget)

    # Display the final shopping list
    display_shopping_list(shopping_list, budget, remaining_budget)

    # Option to regenerate
    if remaining_budget > 0 and len(shopping_list) > 0:
        print(f"\n💡 You still have ${remaining_budget:.2f} left!")
        try_again = input("Would you like to try again for a different selection? (y/n): ").lower()
        if try_again == 'y':
            print("\n🔄 Generating alternative shopping list...")
            shopping_list, remaining_budget = generate_shopping_list(budget)
            display_shopping_list(shopping_list, budget, remaining_budget)


if __name__ == "__main__":
    main()
