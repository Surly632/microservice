import logging
from logging.handlers import RotatingFileHandler
from uvicorn.config import LOGGING_CONFIG

log_file_name = 'myapp.log'
log_file_size = 100*1024*1024
log_backup_count = 5

formatter = {
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'datefmt': '%Y-%m-%d %H:%M:%S'
}

LOGGING_CONFIG['handlers'] = {
    'console': {
        'class': 'logging.StreamHandler',
        'formatter': 'default'
    },
    'file': {
        'class': 'logging.handlers.RotatingFileHandler',
        'level': 'INFO',
        'formatter': 'default',
        'filename': f'{log_file_name}',
        'maxBytes': log_file_size,
        'backupCount': log_backup_count
    }
}

LOGGING_CONFIG['loggers'] = {
    'uvicorn.error': {
        'handlers': ['console', 'file'],
        'level': 'ERROR',
        'propagate': False
    },
    'uvicorn.access': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
        'propagate': False
    },
    '': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG'
    }
}

LOGGING_CONFIG['formatters'] = {
    'default': formatter
}

logging.config.dictConfig(LOGGING_CONFIG)

log = logging.getLogger(__name__)