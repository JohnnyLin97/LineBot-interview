import LineBot_interview.response_data.links as links
from turtle import width
from linebot.models import (CarouselTemplate, 
                            CarouselColumn, 
                            TemplateSendMessage, 
                            MessageTemplateAction, 
                            URITemplateAction)

'''
Carousel-Template message made here
'''

# Make menu carousel message
def get_menu():
    menu_msg = TemplateSendMessage(
        alt_text = 'Menu',
        image_size = '20',
        template = CarouselTemplate(
            columns = [

                # Self-introduction column
                CarouselColumn(
                    title = 'Self-intro',
                    text = 'More about me',
                    thumbnail_image_url = links.SELF_PHOTO,
                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_intro>'
                        )
                    ]
                ),

                # Projects list column
                CarouselColumn(
                    title = 'Projects',
                    text = 'Project Introduction',
                    thumbnail_image_url = links.PROJECT_ICON,
                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_projects>'
                        )
                    ]
                ),

                # Hobby
                CarouselColumn(
                    title = 'Hobby',
                    text = "Let's pick some easy topics",
                    thumbnail_image_url = links.HOBBY_ICON,
                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_hobby>'
                        )
                    ]
                ),

                # GitHub of this LineBot
                CarouselColumn(
                    title = 'About Bot',
                    text = 'How I Built this LineBot',
                    thumbnail_image_url = links.GITHUB_ICON,
                    actions = [
                        URITemplateAction(
                            label = 'View on GitHub',
                            uri = links.LINEBOT_GITHUB
                        )
                    ]
                ),

                # Reason of choosing Line
                CarouselColumn(
                    title = 'Why Line?',
                    text = 'The reason why Line is my dream company',
                    thumbnail_image_url=links.LINE_ICON,
                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_why>'
                        )
                    ]
                )
            ]
        )
    )

    return menu_msg