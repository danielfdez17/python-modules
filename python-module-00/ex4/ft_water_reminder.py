def ft_water_reminder():
	try:
		days = int(input("Days since last watering: "))
		if days > 2:
			print("Water the plants!")
		else:
			print("Plant are fine")
	except:
		print("Seems you didn't entered number values!")
if __name__ == "__main__":
	ft_water_reminder()