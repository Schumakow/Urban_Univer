

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:

        if sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        else:
            # .com" ".ru" ".net"
            if '@' not in recipient and '@' not in sender:
                print(f"1) - Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
            else:
                count = 0
                for i in [".com", ".ru", ".net"]:
                    if i in recipient:
                        count += 1
                    if i in sender:
                        count += 1
                if count < 2:
                    print(f"2) - Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

                # elif i not in sender:
                #         print(f"3) - Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
                else:
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')




print(1)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print(2)
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print(3)
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk') # Невозможно
print(4)      # отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
