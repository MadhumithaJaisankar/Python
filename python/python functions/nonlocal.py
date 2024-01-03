def outer_function():
    outer_variable = 10

    def inner_function():
        nonlocal outer_variable
        inner_variable = 5

        print("Inner function - accessing outer_variable:", outer_variable)
        print("Inner function - local variable:", inner_variable)

        # modifying the nonlocal variable
        outer_variable += 1
        print("Inner function - modified outer_variable:", outer_variable)

    inner_function()
    print("Outer function - accessing outer_variable:", outer_variable)

outer_function()
