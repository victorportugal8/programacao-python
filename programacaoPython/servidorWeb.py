import web

urls = ('/', 'hello')

class hello:
    def GET(self):
        name = "Victor"
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()