"""

Пример работы с User LP

"""

from irispy import Dispatcher
from irispy import objects
from vkbottle.user import types
from vkbottle.rule import VBMLUserRule
from time import time

dp = Dispatcher(
    token="токен_от_вк",
    secret="секретное_слово",
    user_id="айди_дежурного",
    longpoll=True
)


@dp.event.sendMySignal(text=["банан", "огурец"], lower=True)
async def get_fruits(event: objects.SendMySignal):
    print(f"Вау, я тоже люблю {event.object.value}!")


@dp.on.message_new(VBMLUserRule("пинг", lower=True))
async def ping(ans: types.Message):
    received = ans.date
    await ans(
        f"Понг\n"
        f"Ответ сервера: {round(time() - received, 2)} сек."
    )


dp.run_app()

