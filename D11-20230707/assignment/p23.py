for i in range(1,101):
    if i%3==0:
        print(f"{i} fizz")
    elif i%5==0:
        print(f"{i} Buzz")
    if i%3 and i%5==0:
        print(f"{i} FizzBuzz")
    else:
        print(i)

