from ..types.methods import Method
from ..types import objects

from .handler import Handler
from . import server

import logging
import asyncio
import typing


logger = logging.getLogger(__name__)


class Dispatcher:

    def __init__(self, secret: str, user_id: int, *, loop: asyncio.AbstractEventLoop = None):
        self.loop = loop if loop else asyncio.get_event_loop()
        self.secret: str = secret
        self.user_id: int = user_id
        self.handlers: typing.List[Handler] = []

    def register_event_handler(self, event_type: Method, coro: typing.Callable):
        handler = Handler(coro, event_type)
        self.handlers.append(handler)
        logging.info("Handler successfully registered!")

    def event_handler(self, event_type: Method):
        """
        Регистрирует event_handler в приложении.
        :param event_type: -> Method
        :return: -> None
        """
        def decorator(coro: typing.Callable):
            self.register_event_handler(event_type, coro)

        return decorator

    async def process_event(self, event: dict):
        """ Функция, отвечающая за обработку эвента.
        :param event: -> dict
        :return: -> None
        """
        _event = await self.get_event_type(event)
        for handler in self.handlers:
            if handler.event_type.value == _event.method:
                try:
                    await handler.notify_handler(_event)
                except Exception as e:
                    logging.exception(f"Error in handler: {e}")

    async def process_events(self, events: typing.List[dict]):
        for event in events:
            self.loop.create_task(self.process_event(event))

    def run_app(self, host: str = "0.0.0.0", port: int = 8080, path: str = "/"):
        """
        :param host: IP адресс, где будет запущен сервер: Пример: "127.0.0.1"
        :param port: Порт, на котором будет запущен сервер: Пример 8000
        :param path: Путь, куда Ирис будет отсылать POST запросы: Пример "/bot"
        :return: -> None
        """
        app = server.get_app(self, self.secret, self.user_id)
        server.run_app(app, host, port, path)

    @staticmethod
    async def get_event_type(event: dict):
        """ What the bullshit I made...
        :param event: -> dict
        :return: object
        """
        event_type = Method(event["method"])
        ev = None
        if event_type is Method.PING:
            ev = objects.Ping(**event)

        if event_type is Method.BIND_CHAT:
            ev = objects.BindChat(**event)

        if event_type is Method.BAN_EXPIRED:
            ev = objects.BanExpired(**event)

        if event_type is Method.ADD_USER:
            ev = objects.AddUser(**event)

        if event_type is Method.IGNORE_MESSAGES:
            ev = objects.IgnoreMessages(**event)

        if event_type is Method.SUBSCRIBE_SIGNALS:
            ev = objects.SubscribeSignals(**event)

        if event_type is Method.DELETE_MESSAGES:
            ev = objects.DeleteMessages(**event)

        if event_type is Method.DELETE_MESSAGES_FROM_USER:
            ev = objects.DeleteMessagesFromUser(**event)

        if event_type is Method.PRINT_BOOKMARK:
            ev = objects.PrintBookmark(**event)

        if event_type is Method.FORBIDDEN_LINKS:
            ev = objects.ForbiddenLinks(**event)

        if event_type is Method.SEND_SIGNAL:
            ev = objects.SendSignal(**event)

        if event_type is Method.SEND_MY_SIGNAL:
            ev = objects.SendSignal(**event)

        if event_type is Method.HIRE_API:
            ev = objects.HireApi(**event)

        if event_type is Method.BAN_GET_REASON:
            ev = objects.BanGetReason(**event)

        if event_type is Method.TO_GROUP:
            ev = objects.ToGroup(**event)

        return ev
