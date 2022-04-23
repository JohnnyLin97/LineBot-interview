from linebot.models import TextSendMessage

# Handling project user chose 
def projects_handler(content):
    if content == '<projects_qsticker>':
        f = open('LineBot_interview/response_data/qsticker_info.txt', 'r', encoding='utf-8')
        return TextSendMessage(text=f.read())

    elif content == '<projects_aicup>':
        f = open('LineBot_interview/response_data/aicup_info.txt', 'r', encoding='utf-8')
        return TextSendMessage(text=f.read())

    elif content == '<projects_fin>':
        f = open('LineBot_interview/response_data/fin_info.txt', 'r', encoding='utf-8')
        return TextSendMessage(text=f.read())