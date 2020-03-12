from ..types.methods import Method

import typing


class Handler:

    def __init__(self, handler: typing.Callable, event_type: Method):
        self.event_type = event_type
        self.handler = handler

    async def notify_handler(self, event):
        await self.handler(event)