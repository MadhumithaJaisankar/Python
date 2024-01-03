def sumstok(numbers,target):
    used_numbers=set()
    for number in numbers:
        difference=target-number
        if difference in used_numbers:
            return True
        used_numbers.add(number)
    return False

List_numbers=[10,15,3,7]
target_sum=17
print(sumstok(List_numbers,target_sum))