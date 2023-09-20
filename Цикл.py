names = []
numbers = []
services = []

while True:
    user = int(input('1- dabavit imya , 2-dabavit nomer, 3-dabavit uslugu '))
    if user == 2:
        num = input('Vvedite nomer: ')
        numbers.append(num)
        print('Nomer uspeshno dabavlen')
    elif user == 1:
        name = input('Vvedite imya: ')
        names.append(name)
        print('Imya uspeshna dabavlena')
    elif user == 3:
        service = input('Vvedite uslugu: ')
        services.append(service)
        print('Usluga uspeshna dabavlena')
    else:
        print("Neizvesnaya operatsiya")


