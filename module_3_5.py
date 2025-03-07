print(f"{"Задача"} {'"Рекурсивное умножение цифр"'}")

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print("Первый вариант:")
print(result)


#второй вариант

def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    while str_number.endswith('0'):
            str_number = str_number[:len(str_number)-1]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits('40203')
print("\nВторой вариант:")
print(result)

