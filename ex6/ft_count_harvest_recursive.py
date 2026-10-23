def ft_count_harvest_recursive(
    days: int = 1,
    harvest_time: int | None = None
) -> None:
    if harvest_time is None:
        harvest_time = int(input("Days until harvest: "))

    if harvest_time < days:
        print("Harvest time!")
        return

    print(f"Day {days}")
    ft_count_harvest_recursive(days + 1, harvest_time)
