# is the number 10 even AND prime?(False)
def prime(data):
    if data == 2:
        print("it is a prime and even number")

        for i in  range(2,data):
            if data % i ==0:
                return "its not a prime number"
            
            return "this is a prime number"
        
        print(prime(2))