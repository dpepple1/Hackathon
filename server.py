import tornado.ioloop
import tornado.options
import tornado.web
import json
import os

PORT = 9999

class signinHandler(tornado.web.RequestHandler):
    def get(self):
        data = get_json('fakedata.json')
        self.render('signin.html', data=data)
        result = self.get_argument("servings", "")
        print(result)

class homeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('HomePage.html')

class reccommendationsHandler(tornado.web.RequestHandler):
    def get(self):
        #name = self.get_argument('name', '')

        data = get_json('fakedata.json')
        self.render('today.html', data=data)     # Render template with arguments

#TODO
class submitHandler(tornado.web.RequestHandler):
    def get(self):
        #name = self.get_argument('name', '')

        data = get_json('fakedata.json')
        self.render('submit.html', data=data)     # Render template with arguments

class todayMenuHandler(tornado.web.RequestHandler):
    def get(self):
        data = get_json('fakedata.json')
        self.render('todays_menu.html', data=data)

class statsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('stats.html')



def get_json(PATH):
    with open(PATH, 'r') as fh:
        data = json.load(fh)
        return data
        
def main():

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static")
    }
    application = tornado.web.Application([
        (r'/', signinHandler),
        (r'/HomePage.html', homeHandler),
        (r'/today.html',reccommendationsHandler),
        (r'/todays_menu.html', todayMenuHandler),
        (r'/submit.html', submitHandler),
        (r'/stats.html', statsHandler)
    ], **settings)
    application.listen(PORT)

    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()