def ft_count_harvest_iterative() -> None:
	harvest_time = int(input("Days until harvest: "))

	for Day in range(1, harvest_time + 1):
		print(f"Day {Day}")

	print("Harvest time!")
