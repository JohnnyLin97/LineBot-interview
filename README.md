# LineBot - TsungWei Lin

## QRcode
掃描此QRcode加入LineBot

![image](https://qr-official.line.me/sid/L/594nioxz.png)

## 環境
Django: 4.0.4
Python: 3.9.9
line-bot-sdk: 2.2.1
localtunnel


## 程式架構
程式主要可以分為msg_handler、msg_factory、reponse_data
views.py中的callback()接收到request之後，會依照訊息內容呼叫不同handler，handler再依要回傳的內容去msg_factory製作回傳訊息


![image](https://scontent.ftpe3-1.fna.fbcdn.net/v/t39.30808-6/279020522_5185139964841409_9197961846053232020_n.jpg?_nc_cat=100&ccb=1-5&_nc_sid=730e14&_nc_ohc=f6g7ejbguhQAX-ubuPc&_nc_ht=scontent.ftpe3-1.fna&oh=00_AT8W2ByLBmx4UcoZpAxGkg0I7flYi9PuKSsTtZgBncUuRQ&oe=626A375D)

* views.py
    * callback()
        接收來自user的request，讀出訊息內容並分流處理

* msg_handler
    * menu.py
        處理選單相關的訊息
    * projects_list.py
        處理projects選項的訊息
    * unknown.py
        處理非預設的訊息內容，含貼圖

* msg_factory
    此部分依照使用的template分檔製作
    * carousel.py
    * button.py
    * confirm.py

* response_data
    回傳訊息的內容，並集中管理連結至links.py