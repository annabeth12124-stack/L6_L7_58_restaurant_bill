def clean_dish_name(name):
    """
    Removes the chef's-special markers (*, #, ~) and title-cases the name.
    Returns an empty string if name is not a string.
    """
    if not isinstance(name, str):
        return ""
    name = name.strip()
    for ch in ['*', '#', '~']:
        name = name.replace(ch, '')
    return name.title()


def parse_item_prices(text):
    """
    Parses comma-separated prices into a list of ints.
    Returns [] if text is not a string; entries that are not
    whole numbers are skipped.
    """
    if not isinstance(text, str):
        return []
    prices = []
    for price in text.split(','):
        try:
            prices.append(int(price))
        except ValueError:
            continue
    return prices


def split_amount(text):
    """
    Splits 'TOTAL/PEOPLE' into the amount each person pays.
    Returns None if the input is malformed or people is less than 1.
    """
    if not isinstance(text, str):
        return None
    parts = text.split('/')
    if len(parts) != 2:
        return None
    try:
        total = int(parts[0])
        people = int(parts[1])
    except ValueError:
        return None
    if people < 1:
        return None
    return total // people


def main():
    print("==== Running clean_dish_name ====")
    value = input("Enter a dish name from the menu (e.g. *paneer tikka*): ")
    print("Dish name:", clean_dish_name(value))

    print("\n==== Running parse_item_prices ====")
    value = input("Enter item prices separated by commas (e.g. 250,180,320): ")
    print("Item prices:", parse_item_prices(value))

    print("\n==== Running split_amount ====")
    value = input("Enter the bill and number of people as TOTAL/PEOPLE (e.g. 1200/4): ")
    print("Each person pays:", split_amount(value))


if __name__ == "__main__":
    main()