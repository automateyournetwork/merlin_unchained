from channels import route
from viewer import consumers

channel_routing = [
    route("websocket.connect", consumers.ws_connect, path=r"^/viewer/"),
    route("websocket.receive", consumers.ws_receive, path=r"^/viewer/"),
]