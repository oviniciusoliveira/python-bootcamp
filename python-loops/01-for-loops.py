for number in range(4):
    print(f"The for loop has run for {number} time(s)")

print("\n")

for number in range(10, 15):
    print(f"The for loop has run for {number} time(s)")

print("\n")

for number in range(20, 30, 2):
    print(f"The for loop has run for {number} time(s)")

print("\n")

status = False
for number in range(1, 5):
    print(f"Attempt {number}")

    if status:
        print("Success!")
        break
    else:
        print("Boom!")
else:
    print("No more chance")
