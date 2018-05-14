
from log import WXLogger
from proxy import Proxy

# Params

proxy = Proxy()
logger = WXLogger().logger


def main():
    # proxy.load_list()
    proxy.proxy()
    proxy.embed()


    # call
if __name__ == "__main__":
    main()
