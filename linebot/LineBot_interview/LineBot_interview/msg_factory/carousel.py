from turtle import width
from linebot.models import (CarouselTemplate, 
                            CarouselColumn, 
                            TemplateSendMessage, 
                            MessageTemplateAction, 
                            BubbleContainer)

def get_menu():
    menu_msg = TemplateSendMessage(
        alt_text = 'Menu',
        image_size = '20',
        template = CarouselTemplate(
            columns = [

                CarouselColumn(
                    title = 'Self-intro',
                    text = 'More about me',
                    thumbnail_image_url='https://lh3.googleusercontent.com/4jEe8cBTS8kWhCTM0odzrT4IQkCZfzk-8cUBjJwo-2FvrHRnsjQUQGEmFcaV_Gla2YlkQ1cux2vCuASOzYZikoZmZhoFXVi7D_ZrWXBNCaEClCD9pGXmYjQ_-sxMpOfAvE0RNegdW2NE58EP1NhzHDe9Uy0wqU-oaSKequTHTf0WaOnwMza9fp5BgNiD1X3Z1SUxCbMQ2Brf_q11JpLsIZKoQfXhc8rITge_H0YPfLpw-itw9DOdlgIarOBrS1tR-RlFyXysp1kq39hzW6QPVLrrb3BGig_P5bgyROgkb1mA4uM2Iv6HheBeOZm1iSujulMpm1gjN7dLYK1LbJrFd6s5BNavsmVU4qLWZYh3qTlwVHcPcpbYsH0Vj--iH411hDCmgIgpNFaLTZ3IN3gxuv0PbnzySxnQq7-r0slvnzrZ1LwfWH5zYeRDKt5vdZnawD23p6_N-Isov8hLMGV2j5c39ciX1lxhto-a_CoJ_2uY1Di6BQ_TMSw2-FN8pZQprthflU7Sq18x1stdwmj_NOIvjdx01zBjo4lWjNY0Dx1-0emuemdOBpXWsetyaUwjaMLJaegm5JXJ04UToLQ5Q3Gp7Jx_H_FkHRdqpPIjB-mK4o8-ftwjPqJ_LzWAOQ6EKBTSZeO2l3xc11vSMDgGW7Yjp39Fy0QxNQYs8uIG0CfMDLxFl11Wq-vHitlGPDOHKupe7KWKN4boy4-ClQl0K87grKTt_Uu6ADk9HyPlchVOsiwUMPXq5oXWRv54mSoa9FRrW4cCJ6m23dgxylHr_x_VZx9iiF3g=w1666-h937-no?authuser=0',
                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_intro>'
                        )
                    ]
                ),
                CarouselColumn(
                    title = 'Projects',
                    text = 'Project Introduction',
                    thumbnail_image_url='https://lh3.googleusercontent.com/4jEe8cBTS8kWhCTM0odzrT4IQkCZfzk-8cUBjJwo-2FvrHRnsjQUQGEmFcaV_Gla2YlkQ1cux2vCuASOzYZikoZmZhoFXVi7D_ZrWXBNCaEClCD9pGXmYjQ_-sxMpOfAvE0RNegdW2NE58EP1NhzHDe9Uy0wqU-oaSKequTHTf0WaOnwMza9fp5BgNiD1X3Z1SUxCbMQ2Brf_q11JpLsIZKoQfXhc8rITge_H0YPfLpw-itw9DOdlgIarOBrS1tR-RlFyXysp1kq39hzW6QPVLrrb3BGig_P5bgyROgkb1mA4uM2Iv6HheBeOZm1iSujulMpm1gjN7dLYK1LbJrFd6s5BNavsmVU4qLWZYh3qTlwVHcPcpbYsH0Vj--iH411hDCmgIgpNFaLTZ3IN3gxuv0PbnzySxnQq7-r0slvnzrZ1LwfWH5zYeRDKt5vdZnawD23p6_N-Isov8hLMGV2j5c39ciX1lxhto-a_CoJ_2uY1Di6BQ_TMSw2-FN8pZQprthflU7Sq18x1stdwmj_NOIvjdx01zBjo4lWjNY0Dx1-0emuemdOBpXWsetyaUwjaMLJaegm5JXJ04UToLQ5Q3Gp7Jx_H_FkHRdqpPIjB-mK4o8-ftwjPqJ_LzWAOQ6EKBTSZeO2l3xc11vSMDgGW7Yjp39Fy0QxNQYs8uIG0CfMDLxFl11Wq-vHitlGPDOHKupe7KWKN4boy4-ClQl0K87grKTt_Uu6ADk9HyPlchVOsiwUMPXq5oXWRv54mSoa9FRrW4cCJ6m23dgxylHr_x_VZx9iiF3g=w1666-h937-no?authuser=0',

                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_projects>'
                        )
                    ]
                ),
                CarouselColumn(
                    title = 'Personality',
                    text = 'My Personality',
                    thumbnail_image_url='https://lh3.googleusercontent.com/4jEe8cBTS8kWhCTM0odzrT4IQkCZfzk-8cUBjJwo-2FvrHRnsjQUQGEmFcaV_Gla2YlkQ1cux2vCuASOzYZikoZmZhoFXVi7D_ZrWXBNCaEClCD9pGXmYjQ_-sxMpOfAvE0RNegdW2NE58EP1NhzHDe9Uy0wqU-oaSKequTHTf0WaOnwMza9fp5BgNiD1X3Z1SUxCbMQ2Brf_q11JpLsIZKoQfXhc8rITge_H0YPfLpw-itw9DOdlgIarOBrS1tR-RlFyXysp1kq39hzW6QPVLrrb3BGig_P5bgyROgkb1mA4uM2Iv6HheBeOZm1iSujulMpm1gjN7dLYK1LbJrFd6s5BNavsmVU4qLWZYh3qTlwVHcPcpbYsH0Vj--iH411hDCmgIgpNFaLTZ3IN3gxuv0PbnzySxnQq7-r0slvnzrZ1LwfWH5zYeRDKt5vdZnawD23p6_N-Isov8hLMGV2j5c39ciX1lxhto-a_CoJ_2uY1Di6BQ_TMSw2-FN8pZQprthflU7Sq18x1stdwmj_NOIvjdx01zBjo4lWjNY0Dx1-0emuemdOBpXWsetyaUwjaMLJaegm5JXJ04UToLQ5Q3Gp7Jx_H_FkHRdqpPIjB-mK4o8-ftwjPqJ_LzWAOQ6EKBTSZeO2l3xc11vSMDgGW7Yjp39Fy0QxNQYs8uIG0CfMDLxFl11Wq-vHitlGPDOHKupe7KWKN4boy4-ClQl0K87grKTt_Uu6ADk9HyPlchVOsiwUMPXq5oXWRv54mSoa9FRrW4cCJ6m23dgxylHr_x_VZx9iiF3g=w1666-h937-no?authuser=0',

                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_personality>'
                        )
                    ]
                ),
                CarouselColumn(
                    title = 'About Bot',
                    text = 'How I Built this LineBot',
                    thumbnail_image_url='https://lh3.googleusercontent.com/4jEe8cBTS8kWhCTM0odzrT4IQkCZfzk-8cUBjJwo-2FvrHRnsjQUQGEmFcaV_Gla2YlkQ1cux2vCuASOzYZikoZmZhoFXVi7D_ZrWXBNCaEClCD9pGXmYjQ_-sxMpOfAvE0RNegdW2NE58EP1NhzHDe9Uy0wqU-oaSKequTHTf0WaOnwMza9fp5BgNiD1X3Z1SUxCbMQ2Brf_q11JpLsIZKoQfXhc8rITge_H0YPfLpw-itw9DOdlgIarOBrS1tR-RlFyXysp1kq39hzW6QPVLrrb3BGig_P5bgyROgkb1mA4uM2Iv6HheBeOZm1iSujulMpm1gjN7dLYK1LbJrFd6s5BNavsmVU4qLWZYh3qTlwVHcPcpbYsH0Vj--iH411hDCmgIgpNFaLTZ3IN3gxuv0PbnzySxnQq7-r0slvnzrZ1LwfWH5zYeRDKt5vdZnawD23p6_N-Isov8hLMGV2j5c39ciX1lxhto-a_CoJ_2uY1Di6BQ_TMSw2-FN8pZQprthflU7Sq18x1stdwmj_NOIvjdx01zBjo4lWjNY0Dx1-0emuemdOBpXWsetyaUwjaMLJaegm5JXJ04UToLQ5Q3Gp7Jx_H_FkHRdqpPIjB-mK4o8-ftwjPqJ_LzWAOQ6EKBTSZeO2l3xc11vSMDgGW7Yjp39Fy0QxNQYs8uIG0CfMDLxFl11Wq-vHitlGPDOHKupe7KWKN4boy4-ClQl0K87grKTt_Uu6ADk9HyPlchVOsiwUMPXq5oXWRv54mSoa9FRrW4cCJ6m23dgxylHr_x_VZx9iiF3g=w1666-h937-no?authuser=0',
                    actions = [
                        MessageTemplateAction(
                            label = 'Go',
                            text = '<menu_bot>'
                        )
                    ]
                ),
                CarouselColumn(
                    title = 'Why Line?',
                    text = 'Why Line is my dream company',
                    thumbnail_image_url='https://e7.pngegg.com/pngimages/631/883/png-clipart-thumb-signal-blue-computer-icons-thumbs-up-miscellaneous-text.png',
                    image_background_color='#EA0000',
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