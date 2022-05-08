from vk import write_msg
from vk_person import user_search
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

f = open('token.txt', 'r')
token = f.readline()

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

def reter():
    count = 0
    base = user_search().copy()

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:
                request = event.text

                if request.lower() == 'дальше':
                    keybord = VkKeyboard(one_time=True)
                    keybord.add_button('Дальше', VkKeyboardColor.SECONDARY)
                    write_msg(event.user_id, f"|{base[count][0]}| - {base[count][1]} {base[count][2]}", keybord)
                    count += 1


reter()