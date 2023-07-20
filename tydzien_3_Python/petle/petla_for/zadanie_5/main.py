"""Zadanie 5
Spróbuj wyświetlić choinkę z trójkątów w taki sposób, aby każdy poziom choinki był o 1 wiersz dłuższy:

#
##
#
##
###
#
##
###
####
"""

count = 3
for i in range(3):
  for j in range(1, count):
    print(j * "#")
  count += 1
  