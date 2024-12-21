import datetime


def contoller_1(weight):
    print("Работает контроллер 1")
    return 'Продукт пропущен' if weight in range(1000, 1101) else 'Продукт не пропущен'

def contoller_2(weight):
    print("Работает контроллер 2")
    return 'Продукт пропущен' if weight in range(950, 1051) else 'Продукт не пропущен'
        
def get_active_contoller():
    today = datetime.datetime.today()
    return contoller_1 if today.day % 2 else contoller_2
    

def check_good(good):
    active_controller = get_active_contoller()
    return active_controller(good)

print(check_good(int(input('Введите вес продкции: '))))
