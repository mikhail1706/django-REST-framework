import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'large': {
            'format': '%(asctime)s %(levelname)s %(process)d %(pathname)s %(funcName)s %(lineno)d %(message)s',
            'datefmt': "%d/%b/%Y %H:%M:%S"
        }, },
    'handlers': {
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f"{os.path.join(LOGS_DIR)}/error_{time.strftime('%Y_%m')}.log",
            'formatter': 'large',
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f"{os.path.join(LOGS_DIR)}/info_{time.strftime('%Y_%m')}.log",
            'formatter': 'large',
        },
    },
    'loggers': {
        'error_logger': {
            'level': 'ERROR',
            'handlers': ['error'],
            'propagate': False,
        },
        'info_logger': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'handlers': ['info'],
            'propagate': True,
        },
        'warning_logger': {
            'level': 'INFO',
            'handlers': ['info'],
            'propagate': True,
        },
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['info'],
            'propagate': True,
        },
    },
}
