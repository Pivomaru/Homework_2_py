# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата


HEX_SYS = 16
num: int = int(input("\nВведите целое число:"))

def transfer_system(num: int) -> str:
    result: str = ''

    while num > 0 :
        mod: str = str(num % HEX_SYS)
        result = mod + result
        num //= HEX_SYS

    return result

transf: int = transfer_system(num)
print(f'\nРезультат: {transf}')
print(f'\nЧисло в шестнадцатеричной системе: {hex(num)}')
