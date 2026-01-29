def ft_plant_age():
	try:
		days = int(input("Enter plant age in days: "))
		if days > 60:
			print("Plant is ready to harvest!")
		else:
			print("Plant needs more time to grow.")
	except:
		print("Seems you didn't entered number values!")
if __name__ == "__main__":
	ft_plant_age()