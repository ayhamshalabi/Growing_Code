def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = seed_type.capitalize()
    if unit == "packets":
        print(f"{name} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{name} seeds: {quantity} {unit} total")
    else:
        print(f"{name} seeds: covers {quantity} square meters")
