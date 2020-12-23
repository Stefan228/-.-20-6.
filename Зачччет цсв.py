import csv
def availability(name_of_book, adress_of_store):
    
    store_id = ''
    try:
        with open('shops.csv') as f:
            reader = csv.reader(f, delimiter=';')
            head = next(reader)
            body = [line for line in reader]
        for store in body:
            if store[1] == adress_of_store:
                store_id = store[0]
                
        with open('books.csv') as f:
            reader = csv.reader(f, delimiter=';')
            head = next(reader)
            body = [line for line in reader]
        for book in body:
            if name_of_book == book[1] and store_id in book[3].split(','):
                return True
            else:
                return False
    except:
        return 'Произошла ошибка, проверьте введенные данные.'