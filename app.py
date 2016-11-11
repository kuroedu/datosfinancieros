import web

render = web.template.render('views/')

urls = (
    '/','index',
    '/datos(.*)', 'datos'
)

class index:
    def GET(self):
        return render.index()

class datos:
    def GET(self, datos):
        año = ['2013','2014','2015']
        return render.(datos)
        
if __name__ == '__main__' :
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()