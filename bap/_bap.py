import json
import logging
import socket

log = logging.getLogger(__name__)


class Bap(object):
    _ADDR = ('api.production.bap.codd.io', 8080)
    _API_VERSION = 2
    _BAP_PREFIX = '/__bap'

    def __init__(self, api_key: str):
        self._api_key = api_key
        self._socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    async def handle_update(self, update: dict) -> bool:
        """HandleUpdate sends the update data to the BAP API.

        Args:
            update (dict): update

        Returns:
            bool: boolean value indicating whether you should proceed with handling
            the request or skip it as an internal BAP request.
        """
        if update.get('update_id') is None:
            log.error('Update has no update_id')
            return True

        data = json.dumps(
            {
                'api_key': self._api_key,
                'version': self._API_VERSION,
                'update': update,
            }
        )
        self._socket.sendto(bytes(data, 'utf-8'), self._ADDR)

        if (
            update.get('callback_query') is not None
            and update['callback_query'].get('data') is not None
            and update['callback_query']['data'].startswith(self._BAP_PREFIX)
        ):
            return False

        return True
