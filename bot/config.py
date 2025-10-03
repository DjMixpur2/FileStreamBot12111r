from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", "12850056"))
    API_HASH = env.get("TELEGRAM_API_HASH", "15564ec4a1a2cbef87c9aa9e40b34")
    OWNER_ID = int(env.get("OWNER_ID", "770434685"))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Kgfdghffbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "8235989253:AAGF6Yd7ayEV102wAQyHXNOVD0brfO8K-fo")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", "-1002479847516"))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", "24"))

class Server:
    BASE_URL = env.get("BASE_URL", "http://65.108.9.125:8081")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", "8081"))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}










