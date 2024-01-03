def squares_generator(n):
    for i in range(n):
        yield i ** 2

# Using the squares_generator
for square in squares_generator(5):
    print(square)
