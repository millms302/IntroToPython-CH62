# 1) create 2 sets

invited_friends = {"Alex", "Sam", "Leo", "Mina"}
rsvped = {"Mina", "Sam", "Jordan"}

# 2) Print everyone who was invited (union), Everyone who rsvped (rsvped), and havent replied yet (difference)
print(invited_friends.union(rsvped))
print(rsvped)
print(invited_friends.difference(rsvped))

# 3) Add 2 names to invited_friends
invited_friends.update(["Mike", "Duane"])
print(invited_friends)

# 4) One of the people cancelled, remove from rsvped
rsvped.remove("Mina")
print(rsvped)

# 5) Print total number of guests that are confirmed.
print(len(rsvped))

# 6) Check if "Leo is still coming"
print("Leo" in rsvped)