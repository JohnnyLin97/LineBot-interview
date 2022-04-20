from cProfile import label
from click import confirm
from linebot.models import ConfirmTemplate, TemplateSendMessage, MessageTemplateAction
from matplotlib.pyplot import text

def get_confirm():
    confirm_msg = TemplateSendMessage(
        alt_text = 'Confirm Template',
        template = ConfirmTemplate(
            text = '想更了解我嗎?',
            actions = [
                MessageTemplateAction(
                    label = 'Yes',
                    text = '<confirm_yes>'
                ),
                MessageTemplateAction(
                    label = 'No',
                    text = '<confirm_no>'
                )
            ]
        )
    )

    return confirm_msg