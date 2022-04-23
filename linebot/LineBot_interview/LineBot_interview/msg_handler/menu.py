from LineBot_interview.msg_factory.button import get_projects
from linebot.models import TextSendMessage

# Handling column user chose 
def menu_handler(content):
    if content == '<menu_projects>':
        return get_projects()

    elif content == '<menu_why>':
        f = open('LineBot_interview/response_data/why_info.txt', 'r', encoding='utf-8')
        return TextSendMessage(text=f.read())

    elif content == '<menu_intro>':
        return
    
    elif content == '<menu_hobby>':
        f = open('LineBot_interview/response_data/hobby_info.txt', 'r', encoding='utf-8')
        return TextSendMessage(text=f.read())