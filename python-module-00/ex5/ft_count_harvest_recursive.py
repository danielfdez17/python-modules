def ft_count_harvest_recursive():
	try:
		days = int(input("Days until harvest: "))
		def recursive(day = 0):
			if day == days:
				return
			print(f"Day {day + 1}")
			recursive(day + 1)

		recursive()
		print("Harvest time!")
	except:
		print("Seems you didn't entered number values!")
if __name__ == "__main__":
	ft_count_harvest_recursive()