import logging
import logging.config

# 服务配置


class Config:

    # TODO add.puid
    def __init__(self, RootName='ROOT', PUIDPath='D:\\work\\git\\yao\\python\\Product_Python_WXBot\\config/wxpy_puid.pkl', ListenFilter=['好久不见']):
        self.RootName = RootName
        self.PUIDPath = PUIDPath
        self.ListenFilter = ListenFilter


class Setting:
    def __init__(self):
        # 日志配置
        self.logConfig = {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s %(levelname)10s %(message)s'
                },
            },
            'handlers': {
                'default': {
                    'level': logging.INFO,
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                },
                'stdFile': {
                    'level': logging.DEBUG,
                    'formatter': 'standard',
                    'class': 'logging.FileHandler',
                    'filename': '../log/wx-bot.log'
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': logging.INFO,
                    'propagate': False
                },
                'appuser': {
                    'handlers': ['stdFile'],
                    'level': logging.DEBUG,
                    'propagate': True
                },
            }
        }


# 全局参数
config = Config()
setting = Setting()
