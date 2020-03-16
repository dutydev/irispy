from irispy import Dispatcher
from irispy import objects

import vk_api
import typing

dp = Dispatcher(secret="<your_secret>", user_id=0)
vk = vk_api.VkApi(token="токен_от_вк")
chats = {}  # Синхронизация чатов с Ирисом


async def send_msg(peer_id: int, message: str, attachment: str = ""):
    """ Метод для отправки сообщения.
    :param peer_id: Айди беседы: Пример: 2000000666
    :param message: Текст сообщения
    :param attachment: Вложение: Пример: photo1_4545
    :return:
    """
    vk.method("messages.send", {
        "peer_id": peer_id,
        "message": message,
        "attachment": attachment,
        "random_id": 0
    })


async def get_chat(date: int) -> typing.Union[None, int]:
    """ Получение айди чата через
    метод "messages.search" с параметрами:
    :param date: Дата в timestamp
    :return: Айди чата: Пример: 2000000001
    """
    try:
        items = vk.method("messages.search", {
            "q": "!связать",
            "count": 5
        })["items"]  # Получаем список чатов, в которых было найдено сообщение "!связать"
        for i in items:  # Проходим по ним циклом
            if i["date"] == date:  # Если дата отправки сообщения равна нашей дате
                return i["peer_id"]  # То возвращаем айди чата
    except vk_api.VkApiError:
        return


@dp.event.sendMySignal(text=["повтори <text>"], lower=True)
async def wrapper(event: objects.SendMySignal, text: str):
    """ Функция, которая ловит сигнал
    при отправке сообщений: .с; !сигнал ...
    :param text:
    :param event: Объект эвента
    :return:
    """
    await send_msg(
        peer_id=chats[event.object.chat],
        message=f"Повторяю: {text}"
    )


@dp.event.sendSignal(text="повтори <text>", lower=True)
async def executor(event: objects.SendSignal, text: str):
    print(event, text)


@dp.event.bindChat()
async def bind(event: objects.BindChat):
    if event.object.chat not in chats.keys():
        chats[event.object.chat] = await get_chat(event.message.date)
        await send_msg(peer_id=chats[event.object.chat], message="Чат привязан!")

dp.run_app(host="0.0.0.0", port=80)