#23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#o[2, 3, 4, 5, 6] => [12, 15, 16];
#o[2, 3, 5, 6] => [12, 15]
 

def product_of_numbers():
     list = [2,3,4,5,6]
     index1 = 0
     my_list = []
     while index1 < len(list)/2:
         index2 = (index1+1)*-1
         my_list.append(list[index1]*list[index2])
         index1 += 1
     return 'Произведение пар чисел:', my_list

print(product_of_numbers())