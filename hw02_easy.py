# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз


fruits_list = ["яблоко", "банан", "киви", "арбуз"]

string_length = 0

##for itm in fruits_list:
# для нумерации можно использовать i +=1; но решил использовать новый метод


string_length = 0
for key, itm in list(enumerate(fruits_list)):
    if (len(itm) > string_length):
        string_length = len(itm)

    print(str(key+1)+'.', itm.rjust(string_length))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


first_list  = ["dsadsad", "киви", "арбуз"]
second_list = ["яблоко", "банан", "киви", "арбуз"]

for itm in first_list:
    if itm in second_list:
        first_list.remove(itm)
print(first_list)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


num_list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num_res_list = []
for itm in num_list:
    if (itm % 2 == 0):
        num_res_list.append(itm / 4)
    else:
        num_res_list.append(itm * 2)
print(num_res_list)