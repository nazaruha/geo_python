import math_operation as math
from math_operation import mult as moMul
import numpy as np

def mult():
    pass

class Person:
    def __init__(self, name, age): # contructor. self - посилання на поточний екз. классу
        self.name = name
        self.age = age
        pass

    def getData(self): # public
        return f"Name: {self.name}; Age: {self.age}"
    
    def _getName(self): # protected. Треба _ на початку     
        return f"Name: {self.name}"
    
    #private. Треба __ на початку. Але домовились таке старатись не юзать, бо __ вважається магічним методом. Такі як: __init__, __main__ etc.

    #Всі ці доступи приватності не працюють по суті, просто домовленність між програмістами така
    
class Worker(Person): # унаслідування Person
    def __init__(self, name, age, job):
        super().__init__(name, age) # батьківський конструктор
        self.job = job
    
    def getData(self):
        return super().getData() + f"; Works as: {self.job}" # поліморфізм


if __name__ == "__main__": # __main__ - він буде викликатись якщо ти будеш викликати цей файл(модуль) main.py
    # this one-line comment
    """
    this is n-line comment
    """
    ### Different vars, operations and data types. ВСЕ Є ЕКЗЕМПЛЯРОМ КЛАСУ
    # test_var = 12
    # test_float = 7.1E-4
    # bool_var = 4 <= 3 <= 8
    # print(bool_var)
    # test_var = "\"test\""
    # print(test_var)
    # print(0.1 + 0.2)
    # print(True and True)
    # print(True or False)
    # print(not True)
    # a = b = 0 # множинне присвоєння
    # a, b = b, a
    # print (a, b)
    # if not (a < b): булівське не. Є ще or, and


    ### Conditions
    # a = 11
    # b = 10
    # if a < b: # use () if u use more than 1 action/checks
    #     print(f"{a} < {b}") # "...".format(a, b)
    # elif a == b:
    #     print(f"{a} = {b}")
    # else:
    #     print(f"{a} > {b}")
    # print("Will be executeed always")

    # print(f"{a} = {b}" if a == b else f"{a} != {b}") #тернарний оператор. Коли якась проста умова юзаєм


    ###List and Tuples
    """
    Прості типи даних - це числа, булевські типи даних.
    Складні - стрічки, списки (диннамічні), кортежі, словники. Среде складних є незмінні - стрічки і кортежі. Остальні змінні
    """
    # lst = [1, "data", True, 7.1E4] # list
    # print(lst)
    # tuple = (1, "data", True, 7.1E4) # cortege
    # print(tuple)
    # lst.append(2424)
    # print(lst)
    # print(lst[1], tuple[-1]) # -1 index - the first element from the end of the list/tuple etc.
    # # del lst[1] # не рекомендовано, бо в процесі роботи може не те видалитись просто. В чомусь легкому буде збс працювати. В основному юзають ЗАВЖДИ потрібні значення
    # print(lst[0:3]) # SLICES. from 0 to 2 indexes
    # print(lst[0:3:2]) # the last number its iteration (step)
    # print(lst[::-1]) # reversed list


    ### Dicts
    # my_dict = {"key1": 1, "key2": 2, 3: "value3", (1,2): "this is tuple key"}
    # print(my_dict[(1,2)])
    # my_dict["key5"] = 5
    # print(my_dict)
    # #del my_dict["key1"] # просто видаляє значення. Можна, але тоже краще юзати
    # my_dict.pop("key1") # а це видаляє и виводить це значення
    # my_dict.get("key7", "NoData") # якщо не найде цей ключ то виведе NoData
    # # list(my_dict.keys())
    # # tuple(my_dict.values())
    # print(type(my_dict.keys())) # не можна юзати методи list бо ми не перетворили його явно в тип list
    # print(type(list(my_dict.values()))) # можна юзати методи list


    ### Strings - люба робота над стрічками створює нову, а не модифікує поточну
    # my_str = "test string"
    # print(my_str)
    # print(my_str + 'a') # concatanation
    # print(my_str)
    # my_str += 'a'
    # print(my_str)
    # print(my_str[0:7:3])
    # print(my_str[::-1]) 
    # print('test'.join(["my", " ", "string"]))
    # print(my_str.replace('t', 'X'))
    # print(my_str.split(" ")) # розбиває на list по символу 


    ### Cycles
    #цикл з передумовою
    # i = 0
    # while i < 5:
    #     print(i)
    #     i += 1

    #цикл з параметром
    # my_list  = [x**2 for x in range(0, 10, 3)] # range(0, 10) -- від 0 до 9 range виводить
    # print(my_list) # [0, 9, 36, 81]
    # """value - параметр циклу"""
    # for value in my_list: 
    #     if value % 2 == 0:
    #         print(value)
    #     else:
    #         print(value / 2.)


    ### Funtions (def - define). Функція - повертає значення. Процедура - не повертає значення
    # def my_cool_functions(arg1, arg2):
    #     #print(arg1 * arg2)
    #     return arg1 * arg2
    # #None - empty value
    
    # print(my_cool_functions(3, 5))
    # multiply = my_cool_functions
    # print(multiply(3, 5))
    # print(type(multiply))
    # # лямбда функція
    # print(lambda x: x + 6)
    # my_clasificator = lambda x, y: x > y # анонімна(лямбда) функція
    # print(my_clasificator(7, 6))


    ###Files
    # file = open("./test.txt", "a")
    # file.write("some more usefull information")
    # file.close()

    # file = open("./test.txt", "r") # r,w,a - режими роботи з файлом. Не обов'язковий
    # print(file.read())
    # file.close()

    # with open(".test.txt", "r") as file: # контекс менеджер - сам буде закривати файл
    #     print(file.read())


    ### Modules
    print(math.add(3, 5))
    print(mult()) # функція з main.py
    print(moMul(7, 8))
    my_array = np.array([1, 2])
    my_array2 = np.array([2, 1])
    print(my_array * my_array2) # множення масивів



    ### OOP. Classes
    # person = Person("John", 36)
    # print(person.getData())

    # worker = Worker("Alison", 25, "Manager")
    # print(worker.getData())

    

