import vk_api
from vk_api.keyboard import VkKeyboard
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randrange

f = open('token.txt', 'r')
token_vk_group = f.readline()
token_vk_person = f.readline()