pizzaSlice = 32
guests = int(input("Number of guests: "))
divide = pizzaSlice / guests
left_over = pizzaSlice % guests
all_divide = pizzaSlice / guests
print(f"Option 1: {round(divide)} slices each, {left_over} left over")
print(f"Option 2: {all_divide} slices each")