def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return 'ZeroDivisionError: Nolga bo\'lish mumkin emas!'

print(divide(a=12, b=0)) 
print(divide(a=12, b=3)) 

def get_element_by_index(nums, index):
    try:
        return nums[index]
    except IndexError:
        return 'IndexError: Indeks mavjud emas!'

nums = [1, 2, 3, 4, 5]
print(get_element_by_index(nums, 5))  
print(get_element_by_index(nums, 2))  

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return 'ValueError: Int ma\'lumot turiga aylantirib bo\'lmaydi!'

print(convert_to_int('hello'))  
print(convert_to_int('245'))    
