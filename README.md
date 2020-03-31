# IrisPY
> Асинхронная и быстрая библиотека для Iris Callback API.

С помощью Iris Callback API вы можете получать сигналы из бесед, на которые вы подписались. Это поможет вам обрабатывать информацию способом, который удобен для вас без каких-либо ограничений.

Для этого необходимо создать свой сервер, который будет принимать запросы от серверов Iris.

## Установка

1. Новейшая версия:
<br/>`pip install irispy==1.2`

2. С помощью установщика pip из GitHub:
<br/>`pip install https://github.com/zpodushkin/irispy/archive/master.zip --upgrade`

### Кастомизация

<a href="https://github.com/Delgan/loguru"><img alt="downloads" src="https://img.shields.io/static/v1?label=powered%20by&message=loguru&color=orange"></a>
<a href="https://github.com/timoniq/vbml"><img alt="downloads" src="https://img.shields.io/static/v1?label=powered%20by&message=vbml&color=blue"></a>
<a href="https://github.com/timoniq/vkbottle"><img alt="downloads" src="https://img.shields.io/static/v1?label=powered%20by&message=vkbottle&color=green"></a>

После установки `irispy` рекомендуется сразу же установить дополнительные модули `loguru` и `vbml`.
<br/>С ними фреймворк работает лучше и быстрее.

Установите `loguru` и `vbml` с помощью команд:

```sh
pip install loguru
pip install vbml
```

## Примеры использования

```python
from irispy import Dispatcher
from irispy import objects
from random import randint

import typing

dp = Dispatcher(
    secret="<your_secret>",
    user_id="<your_user_id>",
    token="<your_vk_token>"  # Получить можно здесь: https://vkhost.github.io/ (Kate Mobile)
)
chats = {}  # Синхронизация чатов с Ирисом


async def send_msg(peer_id: int, message: str, attachment: str = "", **kwargs):
    """ Метод для отправки сообщения.
    :param peer_id: Айди беседы: Пример: 2000000666
    :param message: Текст сообщения
    :param attachment: Вложение: Пример: photo1_4545
    :return:
    """
    await dp.api.messages.send(
        peer_id=peer_id,
        message=message,
        attachment=attachment,
        random_id=randint(-2e9, 2e9),
        **kwargs
    )


async def get_chat(date: int) -> typing.Union[None, int]:
    """ Получение айди чата через
    метод "messages.search" с параметрами:
    :param date: Дата в timestamp
    :return: Айди чата: Пример: 2000000001
    """
    try:
        items = (await dp.api.messages.search(
            q="!связать",
            count=5
        ))["items"]  # Получаем список чатов, в которых было найдено сообщение "!связать"
        for i in items:  # Проходим по ним циклом
            if i["date"] == date:  # Если дата отправки сообщения равна нашей дате
                return i["peer_id"]  # То возвращаем айди чата
    except Exception as e:
        print("Error: ", e)
        return


@dp.event.sendSignal(text="повтори <text>", lower=True)
async def executor(event: objects.SendSignal, text: str):
    await send_msg(peer_id=chats[event.event.object.chat], message=f"Повторяю: {text}")


@dp.event.bindChat()
async def bind(event: objects.BindChat):
    if event.object.chat not in chats:  # Если UID чата нет в словаре, то добавляем.
        chats[event.object.chat] = await get_chat(event.message.date)
        await send_msg(peer_id=chats[event.object.chat], message="Чат привязан!")

dp.run_app()
```

Больше примеров в папке [/examples](./examples)

## Документация

* [Iris Callback API 2.0 (Статья)](https://vk.com/@iris_cm-api2)
* [Подробная информация по посадке](https://vk.com/@llordrall-chat-faq)
* [Язык разметки VBML (Документация)](https://github.com/timoniq/vbml)

## История релизов

* 1.0
    * Первый деплой!
* 1.0.1
    * Добавление логов и обработка ошибок
* 1.0.5
    * Валидация в методах `sendSignal` и `sendMySignal`
    * Изменение структуры хендлеров
* 1.1
    * Валидаторы VBML!
    * Первый и официальный релиз!
* 1.1.1
    * Не работали валидаторы без аргументов. Исправлено
    * Модуль «IrisPY» был загружен на PyPi!
* 1.2
    * Добавлена поддержка VK API
    * Добавлен User LP
* 1.2.1
    * Небольшие фиксы в логгере
    * Добавлен пример для User LP

## Contributing

ПР поддерживаются! Мне приятно видеть ваш вклад в развитие библиотеки
<br/>Задавайте вопросы в блоке [issues](https://github.com/zpodushkin/irispy/issues) и в чате [VK](https://vk.cc/ardXwL)!

## Лицензия

Copyright © 2019-2020 [zpodushkin](https://github.com/zpodushkin).  
Этот проект имеет [GPL-3.0](./LICENSE.txt) лицензию.
