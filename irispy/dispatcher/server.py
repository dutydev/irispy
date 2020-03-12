from aiohttp import web

import logging


logger = logging.getLogger(__name__)


class IrisHandler(web.View):

    _methods = ["ping", "subscribeSignals", "banExpired",
                "addUser", "deleteMessages", "hireApi",
                "deleteMessagesFromUser", "printBookmark",
                "forbiddenLinks", "sendSignal", "toGroup",
                "sendMySignal", "banGetReason", "bindChat",
                "ignoreMessages"]

    async def get(self):
        """ Метод принимающий GET запросы.
        Но он нам нахер не нужен, поэтому кидаем
        HTTPForbidden адресату.
        :return: -> None
        """
        raise web.HTTPForbidden

    async def post(self):
        event = await self.request.json()
        method = event.get("method")
        if not method:
            raise web.HTTPForbidden

        secret = event.get("secret")
        user_id = event.get("user_id")

        if secret != self.request.app["secret"]:
            raise web.HTTPForbidden

        if user_id != self.request.app["user_id"]:
            raise web.HTTPForbidden

        await self.request.app["dp"].process_events([event])
        if method in self._methods:
            return web.Response(text="ok")


def get_app(dp, secret: str, user_id: int):
    app = web.Application(logger=logger, loop=dp.loop)
    app["dp"] = dp
    app["secret"] = secret
    app["user_id"] = user_id
    return app


def run_app(app: web.Application, host: str, port: int, path: str):
    app.router.add_view(path=path, handler=IrisHandler)
    web.run_app(app, host=host, port=port)