all_products = {'Ves sklad':{}}
korzina = []
while True:
    admin = input('Chto vi xotite sdelat? ')
    if admin.lower() == 'dabavit':
        product_name = input('Vvedite nazvaniya produkta: ')
        product_count = int(input('Vvedite kolichestvo: '))
        all_products['Ves sklad'][product_name] = product_count
        print('Praduct uspeshna dabavlen')
    elif admin.lower() == 'produkti':
        print(all_products)
    elif admin.lower() == 'kupit':
        print(all_products)
        user_choise = input('Kakoy tavar vi bereti? ')
        if user_choise in all_products['Ves sklad']:
            user_count = int(input('Skolka jelayete? '))
            all_products['Ves sklad'][user_choise] -= user_count
            order = (user_choise, user_count)
            korzina.append(order)
            print('Vash zakaz dabavlen v karzinu! ')
        else:
            print('Takogo produkta net! ')

