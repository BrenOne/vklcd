from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.exceptions import ApiError
import lcddriver
display = lcddriver.lcd()

C_VK = 198427451
C_TOKEN_ME = "8694df0df2f331c0bfddbf73425f40000000000000000b6004658d13c74844f56dffc73c9e65422c157c3"
vk_me = vk_api.VkApi(token=C_TOKEN_ME)
longpoll = VkBotLongPoll(vk_me, C_VK)
upload = vk_api.VkUpload(vk_me)
keyboard1 = VkKeyboard(one_time=False)
def send_msg(peer_id, textsend):
    vk_me.method('messages.send',
                 {'user_id': peer_id,
                  'random_id': r.randint(0, 2**64),
                  'message': textsend})
while True:
    try:
        try:
            for event in longpoll.listen():
                from_id = event.obj.peer_id
                if event.type == VkBotEventType.MESSAGE_NEW:
                    send_msg(peer_id, "LCD wrote!")
                    display.lcd_display_string(event.message[:16], 1)
                    display.lcd_display_string(event.message[16:], 2)
        except ApiError as ex:
            print('VK_EROR: ' + str(ex))
    except Exception as ex:
            print('PYTHON_EROR: ' + str(ex))
