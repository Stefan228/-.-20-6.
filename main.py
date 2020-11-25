import csv, json # Имортируем модули csv и json


def ex1(teacher_id, group_id):
    teachers_input = csv.DictReader(open('teachers.csv'), delimiter=";") # Получаем все из файла учителей
    teacher = [i for i in teachers_input if i['id'] == teacher_id]
    if not teacher: return None
    students_input = csv.DictReader(open('students.csv'), delimiter=";") # Получаем все из файла студентов
    students = [i for i in students_input if i['group_id'] == group_id] # Получаем всех студентов по id группы
    subjects_input = csv.DictReader(open('subjects.csv'), delimiter=";") # Получаем все из файла предметов
    results_input = csv.DictReader(open('results.csv'), delimiter=";") # Получаем все из файла результаты
    res = {}
    for subject in subjects_input:
        results = [i for i in results_input if i['subject'] == subject['id'] and i['teacher_id'] == teacher_id]
        five, four, three, two = 0, 0, 0, 0
        if results:
            for student in students:
                result = [i for i in results if i['student_id'] == student['id']]
                if result:
                    total = int(result[0]['total']) # Получаем итоговeю
                    if 86 <= total <= 100: five += 1
                    elif 70 <= total <= 85: four += 1
                    elif 50 <= total <= 69: three += 1
                    elif total <= 50: two += 1
                    item = {subject['subject_name']: {'5':five, '4': four, '3': three, '2':two}} # Формируем данные
                    res.update(item) # Добавляем данные по студенту в return функции
    if res:
        return res
    else:
        return False


def ex2(last_name, first_name, middle_name, to_json=False):
    teachers_input = csv.DictReader(open('teachers.csv'), delimiter=";") # Получаем все из файла учителей
    teacher_id = next(i for i in teachers_input if i['last_name'] == last_name and i['first_name'] == first_name and i['middle_name'] == middle_name)['id'] # Забираем id группы
    groups_input = csv.DictReader(open('groups.csv'), delimiter=";") # Получаем все из файла групп
    res = {}
    for group in groups_input:
        value = ex1(teacher_id, group['id'])
        if value:
            item = {group['name']: value} # Формируем данные
            res.update(item) # Добавляем данные по студенту в return функции
    if to_json: # Если указано имя файла
        with open(to_json, "w", encoding="utf-8") as file: # Откроем
            json.dump(res, file) # Сохраняем return в файл
        return True  # Возращаем True
    return res # Возвращаем словарь


def ex3(entry_year, subject_name, to_json=False):
    groups_input = csv.DictReader(open('groups.csv'), delimiter=";") # Получаем все из файла групп
    groups = [i for i in groups_input if i['entry_year'] == entry_year] # Забираем группы
    subjects_input = csv.DictReader(open('subjects.csv'), delimiter=";") # Получаем все из файла предметов
    subject_id = next(i for i in subjects_input if i['subject_name'] == subject_name)['id'] # Забираем id предмета по имени
    results_input = csv.DictReader(open('results.csv'), delimiter=";") # Получаем все из файла результаты
    results = [i for i in results_input if i['subject'] == subject_id]
    res = {}
    for group in groups:
        students_input = csv.DictReader(open('students.csv'), delimiter=";") # Получаем все из файла студентов
        students = [i for i in students_input if i['group_id'] == group['id']] # Получаем всех студентов по id группы
        five, four, three, two = 0, 0, 0, 0
        for student in students:
            result = [i for i in results if i['student_id'] == student['id']]
            if result:
                total = int(result[0]['total']) # Получаем итоговeю
                if 86 <= total <= 100: five += 1
                elif 70 <= total <= 85: four += 1
                elif 50 <= total <= 69: three += 1
                elif total <= 50: two += 1
                item = {group['id']: {'group_name': group['name'], 'stats': {'5':five, '4': four, '3': three, '2':two}}} # Формируем данные
                res.update(item) # Добавляем данные по студенту в return функции
    if to_json: # Если указано имя файла
        with open(to_json, "w", encoding="utf-8") as file: # Откроем
            json.dump(res, file) # Сохраняем return в файл
        return True  # Возращаем True
    return res # Возвращаем словарь

def ex4(student_id):
    results_input = csv.DictReader(open('results.csv'), delimiter=";") # Получаем все из файла студентов
    result = next(i for i in results_input if i['student_id'] == student_id) # Забираем id предмета по имени
    res = {'att1': result['att1'], 'att2': result['att2'], 'exam': result['exam'], 'total': result['total']}
    return res

def ex5(thread, test='total', to_json=False):
    groups_input = csv.DictReader(open('groups.csv'), delimiter=";") # Получаем все из файла групп
    groups_ids = [i['id'] for i in groups_input if i['name'][0:2] == thread[0:2] and i['entry_year'] == thread[2:]] # Забираем группы
    if not groups_ids:
        return None
    students_input = csv.DictReader(open('students.csv'), delimiter=";") # Получаем все из файла студентов
    students = [i for i in students_input if i['group_id'] in groups_ids] # Получаем всех студентов по id группы
    results_input = csv.DictReader(open('results.csv'), delimiter=";") # Получаем все из файла студентов
    res = {}
    for student in students:
        result = next(i for i in results_input if i['student_id'] == student['id'])[test] # Забираем id предмета по имени
        item = {result: {**student, **ex4(student['id'])}} # Формируем данные
        res.update(item) # Добавляем данные по студенту в return функции
    res = dict(sorted(res.items()))
    res_keys = list(res.keys())[-1::-1]
    for i in range(len(res)):
        res[i+1] = res.pop(res_keys[i])
    if to_json: # Если указано имя файла
        with open(to_json, "w", encoding="utf-8") as file: # Откроем
            json.dump(res, file) # Сохраняем return в файл
        return True  # Возращаем True
    return res # Возвращаем словарь

def ex6(group_name, entry_year, subject_name, to_json=False):
    groups_input = csv.DictReader(open('groups.csv'), delimiter=";") # Получаем все из файла групп
    group_id = next(i for i in groups_input if i['name'] == group_name and i['entry_year'] == entry_year)['id'] # Забираем id группы по имени и году поступления
    subjects_input = csv.DictReader(open('subjects.csv'), delimiter=";") # Получаем все из файла предметов
    subject_id = next(i for i in subjects_input if i['subject_name'] == subject_name)['id'] # Забираем id предмета по имени
    students_input = csv.DictReader(open('students.csv'), delimiter=";") # Получаем все из файла студентов
    students = [i for i in students_input if i['group_id'] == group_id] # Получаем всех студентов по id группы
    results_input = csv.DictReader(open('results.csv'), delimiter=";") # Получаем все из файла результаты
    res = {} # Генерируем пока пустой return функции
    for student in students: # Пробегаемся по всем студентам
        total = next(i for i in results_input if i['student_id'] == student['id'] and i['subject'] == subject_id)['total'] # Получаем все итоговые студентов по id студента и id прелмета
        item = {student['id']: {'last_name': student['last_name'], 'first_name': student['first_name'].replace("\xa0", ""), 'total': total}} # Формируем данные по полному имени и результатам студента
        res.update(item) # Добавляем данные по студенту в return функции
    if to_json: # Если указано имя файла
        with open(to_json, "w", encoding="utf-8") as file: # Откроем
            json.dump(res, file) # Сохраняем return в файл
        return True  # Возращаем True
    return res # Возвращаем словарь


print(ex1('5', '13'))
print(ex1('7', '13'))

print(ex2('Посашков', 'Сергей', 'Александрович'))
print(ex2('Чернышев', 'Лев', 'Николаевич'))

print(ex3('2018', 'Web-программирование'))
print(ex3('2017', 'Web-программирование'))
print(ex3('2015', 'Web-программирование'))

print(ex4('180101'))

print(ex5('ПИ2018'))

print(ex6('ПИ1-4', '2018', 'Алгоритмы и структуры данных'))
print(ex6('ПИ1-4', '2018', 'Алгоритмы и структуры данных', 'test.txt'))
