def ft_harvest_total() -> None:
    total = 0
    i = 1

    while i <= 3:
        total += int(input(f"Day {i} harvest: "))
        i += 1

    print("Total harvest:", total)
