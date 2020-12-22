#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re


# In[5]:


def linear_solver(AM, BM):
    n = len(AM)
    indices = list(range(n)) # гибкие ссылки на строки
    for fd in range(n): # fd означает диагональ фокуса
        fdScaler = 1.0 / AM[fd][fd]
        # масштабируtv строку fd с инверсией fd
        for j in range(n): # Используйте j для обозначения зацикливания столбцов
            AM[fd][j] *= fdScaler
        BM[fd][0] *= fdScaler
        # работаем со всеми строками, кроме строки fd
        for i in indices[0:fd] + indices[fd+1:]: # пропустить строку fd
            crScaler = AM[i][fd] # cr означает текущая строка
            for j in range(n): # cr - crScaler*fdRow
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
            BM[i][0] = BM[i][0] - crScaler * BM[fd][0]
    return BM


# In[6]:


def linear_to_matrix(linears):
    A, B = [], []
    all_vars = list(re.sub('[^a-z]', '', "".join(linears)))
    vars = []
    for i in all_vars:
        if i not in vars:
            vars.append(i)
    for i in linears:
        i = i.replace("+ ", "").replace("- ", "-").split(" = ")
        li = i[0].split()
        li = [''.join(filter(lambda x: x.isdigit() or x in "+-", i.replace("*", ""))) for i in li]
        li = [float(i) if i else 1.0 for i in li]
        A.append(list(map(float, li)))
        ri = i[1].split()
        B.append(list(map(float, ri)))
    linear_res = [str(i[0]) for i in linear_solver(A, B)]
    res = dict(zip(vars, linear_res))
    print("\n\nРешения линейных уравнений:")
    print(res)
    return res


# In[7]:


def non_linear_solver(non_linear):
    all_vars = list(re.sub('[^a-z]', '', non_linear))
    non_linear = non_linear.replace("+ ", "").replace("- ", "-").split(" = ")
    li = non_linear[0].split()
    calcs = [i for i in li if any(j not in i for j in all_vars)]
    chars = [i for i in li if any(j in i for j in all_vars)]
    chars_temp = chars[0].split("**")
    if len(chars_temp) > 1:
        chars_power = chars_temp[1]
    else:
        chars_power = 1
    chars_val = chars_temp[0].split("*")[0]
    if chars_val == all_vars[0]:
        chars_val = 1
    tosum = []
    for i in calcs:
        temp1 = i.split("**")
        if len(temp1) > 1:
            temp2 = temp1[0].split("*")
            if len(temp2) > 1:
                print(temp2)
                tosum.append((float(temp2[1])**float(temp1[1]))*float(temp2[0]))
            else:
                tosum.append(float(temp2[0])**float(temp1[1]))
        else:
            temp2 = i.split("*")
            if len(temp2) > 1:
                tosum.append(float(temp2[1])*float(temp2[0]))
            else:
                tosum.append(float(temp2[0]))
    non_linear_res = []
    temp = (sum(tosum)*-1)/float(chars_val)
    if float(chars_power) == 4:
        temp1 = temp**(1/2)
        temp2 = (temp**(1/2))*-1
        temp3 = temp1**(1/2)
        temp4 = (temp1**(1/2))*-1
        temp5 = temp2**(1/2)
        temp6 = (temp2**(1/2))*-1
        non_linear_res.append([temp3, temp4, temp5, temp6])
    elif float(chars_power) == 2:
        temp1 = temp**(1/2)
        temp2 = (temp**(1/2))*-1
        non_linear_res.append([temp1, temp2])
    else:
        temp1 = temp**(1/float(chars_power))
        non_linear_res.append(temp1)
    res = dict(zip(all_vars, non_linear_res))
    print("\n\nРешение нелинейного уравнения:")
    print(res)
    return res


# In[8]:


def get_answer(inp):
    non_linear = [i for i in inp if "**" in i][0]
    linears = [i for i in inp if "**" not in i]
    linear_res = linear_to_matrix(linears)
    for i, j in linear_res.items():
        non_linear = non_linear.replace(i, j)
    non_linear_res = non_linear_solver(non_linear)
    res = {**linear_res, **non_linear_res}
    return res


# In[9]:


def main(command = ""):
    if not command:
        print("1 - Ввести систему уравнений\n2 - Считать систему уравнений из файла input.txt")
        command = int(input("Ввод: "))
    if command == 1:
        print("\nПример системы уравнений\n[INPUT]: x**2 + 5*y + z = -5\n[INPUT]: x + y = 0\n[INPUT]: 8*x + 5*y = -6\n[INPUT]: .\n\nЧтобы завершить систему введите точку")
        inputs = []
        inp = input("[INPUT]: ")
        while inp != ".":
            inputs.append(inp)
            inp =  input("[INPUT]: ")
    elif command == 2:
        print("\nСистема уравнений взята из файла input.txt")
        with open("input.txt", "r", encoding="utf-8") as f:
            inputs = [i.rstrip() for i in f.readlines()]
        print("\n".join(inputs))
        inputs = inputs[:-1]
    result = get_answer(inputs)
    print("\n\nИтоговый ответ:")
    print(result)


# In[11]:


main()


# In[ ]:




