s = input('Введите текст:\n').lower().split()
col1 = s.count('a')
col2 = s.count('the')
col3 = s.count('an')
print('Общее количество артиклей:', col1 + col2 + col3)
