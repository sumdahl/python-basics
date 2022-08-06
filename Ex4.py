minutes = int(input("Enter the number of minutes worked: "))
hour = minutes / 60
in_minutes = minutes % 60
#round() round up the decimal.
print(f"{minutes} minutes becomes {round(hour)} hours and {in_minutes} minutes.")
