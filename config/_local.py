import os

# Server info
DEBUG = ''
SERVER_URL = ''
SERVER_NAME = ''
IS_TEMP = ''

# MySQL database connection
DATABASES = {
    'default': {
        'ENGINE': '',
        'NAME': '',
        'HOST': '',
        'PORT': '',
        'USER': '',
        'PASSWORD': '',
        'OPTIONS': {
            'sql_mode': '',
            'init_command': '',
            'charset': ''
        },
        'TEST': {
            'CHARSET': '',
            'COLLATION': '',
        }
    }
}

# Email Info
SUPPORT_EMAIL = []
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = ''
EMAIL_USE_SSL = ''

# Ip stack
IP_STACK_ACCESS_KEY = ''

# Dialogflow settings
DIALOG_FLOW_ID = ''
DIALOG_FLOW_FILE_NAME = ''
GEORGE_SUPPORT_PROJECT_ID = ''
CLOONY_CLIENT_PROJECT_ID = ''
DF_AGENT_LANG = ''

# Django cache
CACHES = {
    "default": {
        "BACKEND": "",
        "LOCATION": "",
        "OPTIONS": {
            "CLIENT_CLASS": ""
        },
        "KEY_PREFIX": ""
    }
}

# Django channels redis layer
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': '',
        'CONFIG': {
            "hosts": '',
            "prefix": ''
        },
    },
}

# Broker url for Celery
os.environ['BROKER_URL'] = ''
