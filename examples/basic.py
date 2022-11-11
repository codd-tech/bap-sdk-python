import bap


def main():
    service = bap.Bap('<ad provider api key>')
    # sending telegram update data
    service.handle_update({
        'update_id': 123
        # ...
    })
