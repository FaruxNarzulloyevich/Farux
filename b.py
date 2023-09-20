spisok = []
while True:
    a = input('Vvedite imya:  ')
    if a in spisok:
        print('Takoy username imeeyetsya')
    else:
        spisok.append(a)
        print("Username uspeshna dabavlen")