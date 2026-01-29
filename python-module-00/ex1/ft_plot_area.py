def ft_plot_area():
	try:
		length = int(input("Enter length: "))
		width = int(input("Enter width: "))
		print(f"Plot area: {length * width}")
	except:
		print("Seems you didn't entered number values!")
if __name__ == "__main__":
	ft_plot_area()