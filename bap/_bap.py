import json
import logging
import socket
from datetime import date, datetime

log = logging.getLogger(__name__)


class Bap(object):
    _ADDR = ('api.production.bap.codd.io', 8080)
    _API_VERSION = 3
    _BAP_PREFIX = '/__bap'

    def __init__(self, api_key: str):
        self._api_key = api_key
        self._socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    @staticmethod
    def json_serial(obj):
        if isinstance(obj, (datetime, date)):
            return int(round(obj.timestamp()))
        raise TypeError(f'Type {type(obj)} not serializable')

    @staticmethod
    def validate_update(update: dict) -> bool:
        if not isinstance(update, dict):
            log.error('Update is not a dict')
            return False

        if update.get('update_id') is None:
            log.error('Update has no update_id')
            return False

        return True

    def is_bap_update(self, update: dict) -> bool:
        """Check if callback data has BAP prefix"""
        return (
            update.get('callback_query') is not None
            and update['callback_query'].get('data') is not None
            and update['callback_query']['data'].startswith(self._BAP_PREFIX)
        )

    def _send_to_bap(self, update: dict, method: str):
        """
        Send data to the BAP API using the specified method.

        Parameters:
            update (dict): The update data to be sent to the BAP API.
            method (str): The method to be used in the API call, such as 'activity' or 'advertisement'.
        """
        data = {
            'api_key': self._api_key,
            'version': self._API_VERSION,
            'update': update,
            'method': method,
        }
        serialized_data = json.dumps(data, default=self.json_serial)
        self._socket.sendto(serialized_data.encode('utf-8'), self._ADDR)

    async def handle_update(self, update: dict) -> bool:
        """
        HandleUpdate handles the update received from the BAP API.

        Return false, if you do not need to handle this update (because it is a bap command).
        """
        if not self.validate_update(update):
            return True

        self._send_to_bap(update, 'activity')

        return not self.is_bap_update(update)

    async def send_advertisement(self, update: dict):
        """Send advertisement to the BAP API, allows you to immediately display ads"""
        if not self.validate_update(update):
            return

        if self.is_bap_update(update):
            return

        self._send_to_bap(update, 'advertisement')
