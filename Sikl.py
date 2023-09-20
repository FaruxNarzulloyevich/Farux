imya = ['alisher','Diyor','JOni']
nomer = ['+9989012431245','+998994564515','+99895454645']
usluga = ['obmen valyut','oplata','kredit']

while True:
    a = input()
    b =input()
    c =input()
    if a == 'imya':
     imya.append(b)
     nomer.append(c)
     print(imya)
     print(nomer)
    elif a == 'momer':
     nomer.append(b)
     print(nomer)
    elif a == 'usluga':
     usluga.append(b)
     print(usluga)

