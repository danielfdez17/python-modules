def ft_count_harvest_iterative():
	try:
		days = int(input("Days until harvest: "))
		for i in range(days):
			print(f"Day {i + 1}")
		print("Harvest time!")
	except:
		print("Seems you didn't entered number values!")
if __name__ == "__main__":
	ft_count_harvest_iterative()