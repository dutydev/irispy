# IrisPY
> Асинхронная и быстрая библиотека для Iris Callback API.

С помощью Iris Callback API вы можете получать сигналы из бесед, на которые вы подписались. Это поможет вам обрабатывать информацию способом, который удобен для вас без каких-либо ограничений.

Для этого необходимо создать свой сервер, который будет принимать запросы от серверов Iris.

## Установка

С помощью установщика pip из GitHub:
<br/>`pip install https://github.com/zpodushkin/irispy/archive/master.zip --upgrade`

## Примеры использования

```python
from irispy import Dispatcher, Method
from irispy import objects

dp = Dispatcher(secret="<your_secret>", user_id=0)  # Вместо <your_secret> и 0 подставляем свои значения


@dp.event_handler(Method.SEND_MY_SIGNAL)
async def wrapper(event: objects.SendMySignal):
    """ Функция, которая ловит сигнал
    при отправке сообщений: .с; !сигнал ...
    :param event: Объект эвента
    :return:
    """
    print(event.object)


dp.run_app(host="0.0.0.0", port=8080)
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

## Contributing

ПР поддерживаются! Мне приятно видеть ваш вклад в развитие библиотеки
<br/>Задавайте вопросы в блоке [issues](https://github.com/zpodushkin/irispy/issues) и в чате [VK](https://vk.cc/ardXwL)!

## Лицензия

Copyright © 2019-2020 [zpodushkin](https://github.com/zpodushkin).  
Этот проект имеет [GPL-3.0](./LICENSE.txt) лицензию.
