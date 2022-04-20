from django.shortcuts import render

# import 必要的函式庫
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, StickerMessage

from LineBot_interview.msg_factory.confirm import get_confirm
from LineBot_interview.msg_factory.carousel import get_menu

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)  #在 line_developer取得
parser = WebhookParser(settings.LINE_CHANNEL_SECRET) #在 line_developer取得

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                request_content = event.message.text

                if request_content == "no":
                    line_bot_api.reply_message(
                        event.reply_token,
                        get_confirm()
                    )
                
                elif request_content == "<confirm_yes>":
                    line_bot_api.reply_message(
                        event.reply_token,
                        get_menu()
                    )

                else:
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )


        return HttpResponse()

    else:
        return HttpResponseBadRequest()
