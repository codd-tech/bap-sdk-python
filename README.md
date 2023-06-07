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

### API Key

**API key is not your Telegram bot token.**

API key must be obtained from [socialjet.pro](https://publisher.socialjet.pro/)

## About

### Submitting bugs and feature requests

Bugs and feature request are tracked on [GitHub](https://github.com/codd-tech/bap-sdk-python)

### License

Bot Advertising Platform SDK is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
