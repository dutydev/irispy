# IrisPY
> Асинхронная и быстрая библиотека для Iris Callback API.

С помощью Iris Callback API вы можете получать сигналы из бесед, на которые вы подписались. Это поможет вам обрабатывать информацию способом, который удобен для вас без каких-либо ограничений.

Для этого необходимо создать свой сервер, который будет принимать запросы от серверов Iris.

## Установка

С помощью установщика pip из GitHub:
<br/>`pip install https://github.com/zpodushkin/irispy/archive/master.zip --upgrade`

### Кастомизация

<a href="https://github.com/Delgan/loguru"><img alt="downloads" src="https://img.shields.io/static/v1?label=powered%20by&message=loguru&color=orange"></a>

После установки `irispy` рекомендуется сразу же установить дополнительный модуль `loguru`, без него логи не настраиваемы.

Установите `loguru` с помощью команды:

```sh
pip install loguru
```

## Примеры использования

```python
from irispy import Dispatcher
from irispy import objects

dp = Dispatcher(secret="<your_secret>", user_id=0)


@dp.event.sendMySignal(text=["test", "hello"])
async def wrapper(event: objects.SendMySignal):
    """ Функция, которая ловит сигнал
    при отправке сообщений: .с; !сигнал ...
    :param event: Объект эвента
    :return:
    """
    print(event.object)


@dp.event.sendSignal(text=["ананас", "test"])
async def executor(event: objects.SendSignal):
    print(event.object)


@dp.event.bindChat()
async def bind(event: objects.BindChat):
    print(event)

dp.run_app(host="0.0.0.0", port=80)
```

Больше примеров в папке [/examples](./examples)

## Документация

* [Iris Callback API 2.0 (Статья)](https://vk.com/@iris_cm-api2)
* [Подробная информация по посадке](https://vk.com/@llordrall-chat-faq)

## История релизов

* 1.0
    * Первый деплой!
* 1.0.1
    * Добавление логов и обработка ошибок
* 1.0.5
    * Валидация в методах sendSignal и sendMySignal
    * Изменение структуры хендлеров

## Contributing

ПР поддерживаются! Мне приятно видеть ваш вклад в развитие библиотеки
<br/>Задавайте вопросы в блоке [issues](https://github.com/zpodushkin/irispy/issues) и в чате [VK](https://vk.cc/ardXwL)!

## Лицензия

Copyright © 2019-2020 [zpodushkin](https://github.com/zpodushkin).  
Этот проект имеет [GPL-3.0](./LICENSE.txt) лицензию.
