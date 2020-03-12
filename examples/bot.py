from irispy import Dispatcher, Method
from irispy import objects

dp = Dispatcher(secret="<your_secret>", user_id=0)


@dp.event_handler(Method.SEND_MY_SIGNAL)
async def wrapper(event: objects.SendMySignal):
    """ Функция, которая ловит сигнал
    при отправке сообщений: .с; !сигнал ...
    :param event: Объект эвента
    :return:
    """
    print(event.object)


dp.run_app(host="0.0.0.0", port=8080)