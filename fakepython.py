import tornado.ioloop
import tornado.options
import tornado.web
import json

PORT = 9999

class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        #name = self.get_argument('name', '')

        data = get_json('fakedata.json')

        name = data['banana']['name']
        score = data['banana']['score']
        pros = data['banana']['positives']
        cons = data['banana']['negatives']

        self.render('fakewebsite.html', name=name, score=score, pros=pros, cons=cons)     # Render template with arguments


class ArgumentsTestHandler(tornado.web.RequestHandler):
    def get(self):
        #name = self.get_argument('name', '')

        data = get_json('fakedata.json')
        self.render('fakewebsite2.html', data=data)     # Render template with arguments


# Main Execution


def get_json(PATH):
    with open(PATH, 'r') as fh:
        data = json.load(fh)
        return data
        


def main():
    application = tornado.web.Application([
        (r'/', ArgumentsTestHandler),
    ])
    application.listen(PORT)

    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()