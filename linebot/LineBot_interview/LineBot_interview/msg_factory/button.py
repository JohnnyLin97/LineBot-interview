from linebot.models import ButtonsTemplate, TemplateSendMessage, MessageTemplateAction
from matplotlib.pyplot import text

'''
Button-Template message made here
'''

# Make projects-list
def get_projects():
    introduction_msg = TemplateSendMessage(
        alt_text = 'Projects List',
        template = ButtonsTemplate(
            title = 'My projects',
            text = 'Followings are my projects, press button to have more details',
            actions = [
                MessageTemplateAction(
                    label = 'QSticker',
                    text = '<projects_qsticker>'
                ),
                MessageTemplateAction(
                    label = 'AI Cup',
                    text = '<projects_aicup>'
                ),
                MessageTemplateAction(
                    label = 'FIN. Data Analysis',
                    text = '<projects_fin>'
                )
            ]

        )
    )

    return introduction_msg