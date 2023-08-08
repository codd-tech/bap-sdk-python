## Bot Advertising Platform SDK

[![PyPi Package Version](https://img.shields.io/pypi/v/bapsdk.svg?style=flat-square)](https://pypi.python.org/pypi/bapsdk)
[![Supported python versions](https://img.shields.io/pypi/pyversions/bapsdk.svg?style=flat-square)](https://pypi.python.org/pypi/bapsdk)

This repository holds SDK related to
[Bot Advertising Platform](https://publisher.socialjet.pro/).

## Requirements

- Python >=3.7

## Installation

Install the latest version with

```bash
$ pip install bapsdk
```

The BAP SDK uses the UDP protocol for data transfer to ensure minimal SDK overhead for the user.

### Usage

See [examples](./examples)

- [Basic usage](examples/basic.py)
- [Usage with aiogram](examples/aiogram_bot.py)

#### Interrupting control flow

At times, BAP may introduce telegram updates within its advertisement flow. To maintain the logical consistency of your bot, it is necessary to ignore such updates.

The `BAP.handle_update` method returns a boolean value indicating whether you should proceed with handling the request or skip it as an internal BAP request.

When the method returns `false`, it signifies that the current request should not be processed by your bot.

For manual advertisement mode (Should be turned on in settings) call following in the desired ad placements.

```python
bap.send_advertisement(update)
```

### API Key

**API key is not your Telegram bot token.**

API key must be obtained from [socialjet.pro](https://publisher.socialjet.pro/)

## About

### Submitting bugs and feature requests

Bugs and feature request are tracked on [GitHub](https://github.com/codd-tech/bap-sdk-python)

### License

Bot Advertising Platform SDK is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
