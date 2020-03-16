from ..types.methods import Method
from typing import Callable, List
from vbml import Pattern

import re


class Handler:

    def __init__(self, handler: Callable, event_type: Method):
        self.event_type = event_type
        self.handler = handler

    async def notify_handler(self, event):
        await self.handler(event)


class SelfHandler(Handler):

    def __init__(
            self,
            handler: Callable,
            event_type: Method,
            commands: List[str],
            lower: bool
    ):
        self.event_type: Method = event_type
        self.handler: Callable = handler
        self.commands: List[str] = commands
        self.lower: bool = lower
        self.patterns: List[Pattern] = []
        for i in self.commands:
            self.patterns.append(
                Pattern(
                    text=i,
                    flags=re.IGNORECASE if lower else None
                )
            )
        super().__init__(handler, event_type)