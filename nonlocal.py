def outer():
    name = "mahesh"

    def inner():
        nonlocal name
        print(name)
        name = "ankit"

    inner()
    print(name)


outer()
