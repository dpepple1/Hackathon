class Application(tornado.web.Application):
    """Tornado web class. Create all the routes used by tornado_start"""

    def __init__(self):
        handlers = [
            (r"/", Index),
            (r"/explicit_action_url/", ActionHandler)
        ]
...

class ActionHandler(tornado.web.RequestHandler):
    def get(self):
        print("button click")


class Index(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")