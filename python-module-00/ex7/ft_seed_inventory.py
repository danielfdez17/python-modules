def ft_seed_inventory(seed, amount, type):
	if type == "packets":
		print(f"{seed.capitalize()} seeds: {amount} packets available")
	elif type == "grams":
		print(f"{seed.capitalize()} seeds: {amount} grams total")
	elif type == "area":
		print(f"{seed.capitalize()} seeds: covers {amount} square meters")
	else:
		print(f"Type {type} is not covered")


if __name__ == "__main__":
	ft_seed_inventory("tomato", 15, "packets")
	ft_seed_inventory("carrot", 8, "grams")
	ft_seed_inventory("lettuce", 12, "area")