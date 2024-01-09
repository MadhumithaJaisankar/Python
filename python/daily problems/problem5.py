def cons(a, b):
    return lambda f: f(a, b)

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)


my_pair = cons(6,7)
result_car = car(my_pair)
result_cdr = cdr(my_pair)

print(result_car) 
print(result_cdr)  
