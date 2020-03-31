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
    if event.object.chat not in chats:  # Если UID чата нет в словаре, то добавляем.
        chats[event.object.chat] = await get_chat(event.message.date)
        await send_msg(peer_id=chats[event.object.chat], message="Чат привязан!")

dp.run_app()