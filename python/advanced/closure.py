def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure1 = outer_function(10)
closure2 = outer_function(5)

result1 = closure1(5)
result2 = closure2(10)

print(result1)
print(result2)
