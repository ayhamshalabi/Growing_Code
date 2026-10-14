def ft_count_harvest_recursive(Days: int = 1, harvest_time: int | None = None) -> None:
    if harvest_time is None:
        harvest_time = int(input("Days until harvest: "))

    if harvest_time < Days:
        print("Harvest time!")
        return

    print(f"Day {Days}")
    ft_count_harvest_recursive(Days + 1, harvest_time)
