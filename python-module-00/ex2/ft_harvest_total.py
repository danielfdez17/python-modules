def ft_harvest_total():
	try:
		total_harvest = 0
		harvest = 0
		for i in range(3):
			harvest = int(input(f"Day {i + 1} harvest: "))
			total_harvest += harvest
		print(f"Total harvest: {total_harvest}")
	except:
		print("Seems you didn't entered number values!")
if __name__ == "__main__":
	ft_harvest_total()