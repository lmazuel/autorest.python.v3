import logging
import sys

from jsonrpc import dispatcher, JSONRPCResponseManager

_LOGGER = logging.getLogger()

@dispatcher.add_method
def Process(*args, **kwargs):
    _LOGGER.info(f"Received a process order: {args} {kwargs}")


@dispatcher.add_method
def GetPluginNames():
    return ["remodeler"]

def main():

    while True:
        order = sys.stdin.readline()
        response = JSONRPCResponseManager.handle(order, dispatcher)
        print(response.json)

if __name__ == "__main__":
    main()