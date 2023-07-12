import bap


async def main():
    service = bap.Bap('<ad provider api key>')
    # sending telegram update data
    needHandle = await service.handle_update({
        'update_id': 123,
        # ...
    })
