# 1) create tuple with 5 items:

travel_bag = (
    "shirt", "pants", "socks", "undies", "shoes",
)

# Print second and fourth items in your bag.
print(travel_bag[2])
print(travel_bag[4])

# 3) Check if "shoes" if in your travel bag, if not print "you forgot your shoes"
if "shoes" in travel_bag:
    print("You are ready to walk!")

# 4) Make a new tuple called essentials with 3 must have items

essentials = (
    "Toothbrush", "glasses", "soap"
)

# 5) combine both tuples into one called final_bag
final_bag = (travel_bag + essentials)
print(final_bag)

# 6) Print how many items total
print(len(final_bag))

print(final_bag[-1])