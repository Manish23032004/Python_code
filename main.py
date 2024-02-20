def greet():
    name="sipun"
    def print_greet():
        nonlocal name
        print(name)
        name='ankit'
    print_greet()
    print(name)
greet()