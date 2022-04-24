from linebot.models import TextSendMessage

'''
Handle unknown message
'''

def not_text():
    return TextSendMessage(text='Umm... What do you mean?')

def unknown_text():
    return TextSendMessage(text='Enter "hey" to wake me up\nEnter "menu" to get more info')