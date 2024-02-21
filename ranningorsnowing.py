#is it ranning or Snowing? (True if either is true)
R=input("is it is ranning(yes/No):")
S=input("is it is snowing(Yes/No):")

is_ranning = R == "yes"

is_snowing = S == "yes"

if is_ranning and is_snowing:
    print("it is both ranning and snowing")

elif is_ranning:
    print("it is ranning")
elif is_snowing:
    print("it is snowing")
else:
    print("it is neither ranning and nor snowing")