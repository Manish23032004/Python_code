def check_age(age):
    if age> 18:
        print("eligible for vote")
    else:
        raise ValueError("age less than 18")
    
val = int(input("enter your age"))
try:
    check_age(val)
except ValueError as e:
    print(f"{e}")