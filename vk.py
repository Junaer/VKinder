import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from random import randrange



f = open('token.txt', 'r')
token = f.readline()

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message, keyboard=None):
    post = {
        'user_id': user_id,
        'message': message,
        'random_id': randrange(10 ** 7),
        'keyboard': keyboard.get_keyboard()
        }

    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()
    else:
        post = post

    vk.method('messages.send', post)

def chat():
    # Получаем id пользователя
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text

                if request.lower() == "привет":
                    person = event.user_id
                    keybord = VkKeyboard(one_time=True)
                    keybord.add_button('Начать', VkKeyboardColor.SECONDARY)
                    write_msg(event.user_id, "Нажмите на кнопку 'начать'", keybord)
                    return person
                elif request.lower() == "найти пару":
                    person = event.user_id
                    keybord = VkKeyboard(one_time=True)
                    keybord.add_button('Начать', VkKeyboardColor.SECONDARY)
                    write_msg(event.user_id, "Нажмите на кнопку 'начать'", keybord)
                    return person
                elif request.lower() == "пока":
                    write_msg(event.user_id, "Пока((")
                    break
                else:
                    person = event.user_id
                    keybord = VkKeyboard(one_time=True)
                    keybord.add_button('Начать', VkKeyboardColor.SECONDARY)
                    write_msg(event.user_id, "Нажмите на кнопку 'начать'", keybord)
                    return person


# Возвращаем список с данными пользователя где [0]- id пола, [1]- возраст, [2]- id города.
def user_information():
    user_ids = chat()
# Получение даты и определение возраста пользователя
    data = vk.method("users.get", {"user_ids":user_ids, "fields":"bdate"})
    year = time.asctime()[-4:]
    data_age = data[0]['bdate'][-4:]
    age = int(year) - int(data_age)
# Определение пола пользователя и противопоставление его полу
    sex_person = vk.method("users.get", {"user_ids":user_ids, "fields":"sex"})
    if sex_person[0]['sex'] == 2:
        part = 'Девушка'
        sex = 1
    elif sex_person[0]['sex'] == 1:
        part = 'Мужчина'
        sex = 1
    else:
        part = 'Ваш пол не определён'
# Получаем пол пользователя
    city_person = vk.method("users.get", {"user_ids":user_ids, "fields":"city"})
# Запрос запуска и указание критериев поиска и получение данных для поиска
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text

                if request.lower() == "начать":
                    keybord = VkKeyboard(one_time=True)
                    keybord.add_button('Дальше', VkKeyboardColor.SECONDARY)
                    write_msg(event.user_id, f"Поиск будет происходить по этим критериям {part}, Возраст от {age-3} до {age+3}, город {city_person[0]['city']['title']}.", keybord)
                    return [sex, age, city_person[0]['city']['id']]














