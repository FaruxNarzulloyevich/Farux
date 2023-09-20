# kamen byot nojnisu       k>n
# bumaga pobejdayet kamen  b>k
# nojnisa rejet bumagu      n>k
a = input('kamen,nojnisa,bumaga ')
b = input('kamen,nojnisa,bumaga ')
if a== 'kamen' and b == 'nojnisa':
    print('kamen byot nojnisu')
elif a== 'nojnisa' and b== 'kamen':
    print('kamen byot nojnisu')
elif a== 'kamen' and b == 'bumaga':
    print('bumaga pobejdayet kamnya')
elif a == 'bumaga' and b =='kamen':
    print('bumaga pobejdayet kamen')

elif a== 'nojnisa' and b == 'bumaga':
    print('nojnisa rejet bumagu')
elif a == 'bumaga' and b=='nojnisa':
    print('nojnisa rejet bumagu')
else:
    print('nichya')