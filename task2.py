# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

tmp = input('Введите логическое значение X  ')
x = 0
if tmp == 'true':
   x = 1

tmp = input('Введите логическое значение Y  ')
y = 0
if tmp == 'true':
   y = 1

tmp = input('Введите логическое значение Z  ')
z = 0
if tmp == 'true':
   z = 1

if ~(x or y or z) == ~x and ~y and ~z:
    print('True')
else:
    print('False')
