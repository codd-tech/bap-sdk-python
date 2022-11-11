from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import Update

from bap import Bap


class BapMiddleware(BaseMiddleware):
    def __init__(self, api_key: str):
        self._bap = Bap(api_key)
        super(BapMiddleware, self).__init__()

    async def on_process_update(self, update: Update, data):
        await self._bap.handle_update(update.to_python())
