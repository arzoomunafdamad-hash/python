def is_armstrong(num):
    
    num_str = str(num)
    power = len(num_str)
    
    
    total_sum = sum(int(digit) ** power for digit in num_str)
    
    
    return total_sum == num


user_num = int(input("Enter a number: "))

if is_armstrong(user_num):
    print(f"{user_num} is an Armstrong number.")
else:
    print(f"{user_num} is not an Armstrong number.")
