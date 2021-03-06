# Данный файл содержит крупные текстовые уведомления бота

bot_greeting =  str('Привет, я HSE_Running Bot! Твой персональный помощник для учета пробежек! \n'
                    'Записывай пробежки в формате:\n'
                    'Дистанция (км), Время (мин), Локация, Дата (дд.мм.гггг)\n\n'
                    'Пример:\n2 км, 10 мин, Москва, 12.10.2021 \n\n'
                    'Ты также можешь записать в пробежку только дистанцию и время пробежки.\n\n'
                    'Пример:\n2 км, 10 мин\n'
                    'Но в таком случае я не смогу учесть такие пробежки при показе активности за последний месяц или '
                    'при показе пробежек за определенный период.\n\n'
                    'Если у тебя уже есть записи пробежек в файлах, можешь загрузить их сюда выбрав пункт "Импорт записей"')

wrong_format = str("================\n"
                   "УВЕДОМЛЕНИЕ\n"
                   "* Вы вашем списке пробежек есть пробежка в нерекомендуемом формате!\n"
                   "* Пробежка в нерекомендуемом формате не влияет на работу бота, однако данные из данной"
                   " пробежки никак не будут учтены\n"
                   "* Рекомендуется удалить данную пробежку:\n")

add_run = str('Давайте добавим пробежку! Напишите ее в чат.\n'
                                       'Помните, что пробежку нужно записать в формате:\n'
                                       'Дистанция (км), Время (мин), Локация, Дата (дд.мм.гггг)\n\n'
                                       'Пример:\n2 км, 10 мин, Москва, 12.10.2021 \n\n'
                                       'Если нажали на команду по ошибке, нажмите "Назад" на клавиатуре')

import_runs = str('Давайте добавим ваши записи пробежек! Нажмите на скрепку и прикрепите файл!\n'
                               'Я умею работать только с файлами .txt или .docx\n '
                               'Желательно, чтобы записи пробежек были на отдельных строках и в формате:\n'
                               'Дистанция (км), Время (мин), Локация, Дата (дд.мм.гггг)\n\n'
                               'Если нажали на команду по ошибке, нажмите "Назад" на клавиатуре')
