#寄送Email的程式
#準備訊息物件設定
import smtplib
import email.message
msg = email.message.EmailMessage()
msg["From"] = "emailaddress1"
msg["To"] = "emailaddress2"
msg["subject"] = "寄件測試"
#寄送純文字內容
msg.set_content("mail測試")
#寄送較多樣式的內容-html
msg.add_alternative("<h3>多媒體</h3>html內容測試",subtype = "html")
#連線到SMTP Server. 驗證寄件人身分並發送郵件
#到網路上搜尋 gmail smtp server or yahoo smtp serer
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("emailaddress","password")
server.send_message(msg)
server.close()
