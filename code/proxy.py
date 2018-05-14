from wxpy import *
from log import WXLogger
from config import config


logger = WXLogger().logger


class Proxy:

    def __init__(self):
        # init
        self.bot = Bot(cache_path=True)
        self.bot.enable_puid(config.PUIDPath)

    def load_list(self):
        fs = self.bot.friends()
        for idx in range(len(fs)):
            f = fs[idx]
            logger.info("PUID= %s\tName= %s\tNickName= %s\tRemarkName= %s\tSex= %s\tProvince= %s\tCity= %s",
                        f.puid, f.name, f.nick_name, f.remark_name, f.sex, f.province, f.city)

    def proxy(self):
        @self.bot.register()
        def print_all(msg):
            logger.info("receive: %s", msg)
            c = msg.text

            # FAQ
            if c.startswith("FAQ"):
                return 'Answer[' + c[3:] + ']'

            # Listen
            senderName = msg.sender.name
            # logger.info("%s: %s", senderName, c)
            if senderName in config.ListenFilter:

                cxt = c + "\nPROXY" + msg.sender.puid + "[" + senderName + "]"
                logger.info("send [%s] to %s", cxt, config.RootName)
                self.bot.friends().search(config.RootName)[0].send(cxt)

            # Proxy
            if c.startswith("PROXY"):

                # init
                try:
                    lIdx = c.index('[')
                    rIdx = c.rindex(']')
                except:
                    return "请求格式异常，请参照\n\tPROXYpuid{8}[username]response.content"
                toPuid = c[5:lIdx]
                toUserName = c[lIdx+1: rIdx]
                cxt = c[rIdx+1:]
                success = False
                logger.info("%s[%s]: %s", toUserName, toPuid, cxt)

                # filter
                fs = self.bot.friends().search(toUserName)
                try:
                    f = ensure_one(fs)
                    f.send("Proxy.Send: " + cxt)
                    success = True
                except ValueError as e:
                    for f in fs:
                        if f.puid == toPuid:
                            f.send("Proxy.Send: " + cxt)
                            success = True
                    pass

                # end
                if not success:
                    return "fail to work"

    def embed(self):
        embed()

    def send(FPuid, TPuid, ctx):
        pass
