def ft_harvest_total() -> None:
	Total = 0
	i = 1

	while i <= 3:
		Total += int (input(f"Day {i} harvest: "))
		i += 1

	print("Total harvest:", Total)