def fizzbuzz():
    for i in range(1, 101):
        output = "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)
        print(output or i)
