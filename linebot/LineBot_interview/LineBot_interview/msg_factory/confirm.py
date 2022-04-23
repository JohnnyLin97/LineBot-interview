from cProfile import label
from click import confirm
from linebot.models import ConfirmTemplate, TemplateSendMessage, MessageTemplateAction
from matplotlib.pyplot import text

'''
Confirm-Template message made here
'''

# Make message that confirm user's purpose
def get_confirm():
    confirm_msg = TemplateSendMessage(
        alt_text = 'Confirm Template',
        template = ConfirmTemplate(
            text = 'To know me better',
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