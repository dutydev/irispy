import typing

from ..dispatcher.handler import Handler, SelfHandler
from ..types.exceptions import HandlerError
from ..utils import logger

from inspect import iscoroutinefunction
from .methods import Method


class Event:

    def __init__(self):
        self.handlers: typing.List[Handler] = []
        self.event_handlers: typing.List[SelfHandler] = []

    def __register_event_handler(self, event_type: Method, coro: typing.Callable):
        if not iscoroutinefunction(coro):
            raise HandlerError("Функция обработчик должна быть асинхронной!")
        handler = Handler(coro, event_type)
        self.handlers.append(handler)
        logger.debug(f"Registered new handler {coro.__name__}")

    def __register_self_handler(
            self,
            event_type: Method,
            coro: typing.Callable,
            commands: typing.List[str],
            lower: bool
    ):
        if not iscoroutinefunction(coro):
            raise HandlerError("Функция обработчик должна быть асинхронной!")
        handler = SelfHandler(coro, event_type, commands, lower)
        self.event_handlers.append(handler)
        logger.debug(f"Registered new self handler {coro.__name__}")

    def ping(self):
        def decorator(func):
            self.__register_event_handler(Method.PING, func)

        return decorator

    def subscribeSignals(self):
        def decorator(func):
            self.__register_event_handler(Method.SUBSCRIBE_SIGNALS, func)

        return decorator

    def banExpired(self):
        def decorator(func):
            self.__register_event_handler(Method.BAN_EXPIRED, func)

        return decorator

    def addUser(self):
        def decorator(func):
            self.__register_event_handler(Method.ADD_USER, func)

        return decorator

    def deleteMessages(self):
        def decorator(func):
            self.__register_event_handler(Method.DELETE_MESSAGES, func)

        return decorator

    def hireApi(self):
        def decorator(func):
            self.__register_event_handler(Method.HIRE_API, func)

        return decorator

    def deleteMessagesFromUser(self):
        def decorator(func):
            self.__register_event_handler(Method.DELETE_MESSAGES_FROM_USER, func)

        return decorator

    def printBookmark(self):
        def decorator(func):
            self.__register_event_handler(Method.PRINT_BOOKMARK, func)

        return decorator

    def forbiddenLinks(self):
        def decorator(func):
            self.__register_event_handler(Method.FORBIDDEN_LINKS, func)

        return decorator

    def toGroup(self):
        def decorator(func):
            self.__register_event_handler(Method.TO_GROUP, func)

        return decorator

    def banGetReason(self):
        def decorator(func):
            self.__register_event_handler(Method.BAN_GET_REASON, func)

        return decorator

    def bindChat(self):
        def decorator(func):
            self.__register_event_handler(Method.BIND_CHAT, func)

        return decorator

    def ignoreMessages(self):
        def decorator(func):
            self.__register_event_handler(Method.IGNORE_MESSAGES, func)

        return decorator

    def sendMySignal(self, text: typing.Union[str, typing.List[str]], lower: bool = False):
        def decorator(func):
            commands = text if isinstance(text, list) else [text]
            self.__register_self_handler(
                event_type=Method.SEND_MY_SIGNAL,
                coro=func,
                commands=commands,
                lower=lower
            )

        return decorator

    def sendSignal(self, text: typing.Union[str, typing.List[str]], lower: bool = False):
        def decorator(func):
            commands = text if isinstance(text, list) else [text]
            self.__register_self_handler(
                event_type=Method.SEND_SIGNAL,
                coro=func,
                commands=commands,
                lower=lower
            )

        return decorator