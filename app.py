import web
render = web.template.render('templates/')

urls = (
    '/health', 'health',
    '/count', 'count',
    '/(.*)', 'index'
)

class count:
    def GET(self):
        total = 0
        i = web.input(num=10, start=1)
        return render.count(int(i.num), int(i.start))


class index:
    def GET(self, name):
        return render.index(name)

class health:
    def GET(self):
        return "I am running"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
