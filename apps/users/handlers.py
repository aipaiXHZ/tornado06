import tornado.web

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('users/login.html')

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('users/register.html')
