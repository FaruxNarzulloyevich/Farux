while True:
    slova = input('Vvedite slova: ')
    if slova == slova[ ::-1]:
        print('Eto palindrom')
    else:
        print('Eto ne polindrom')