CONSTANT = 100

first_number = int(input('Insira o primeiro número: '))
second_number = int(input('Insira o segundo número: '))
third_number = int(input('Insira o terceiro número: '))

sum_numbers: int = (first_number + second_number + third_number)

if (sum_numbers > CONSTANT):
    print(True)
else:
    print(False)