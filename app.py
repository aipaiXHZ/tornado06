import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import define, options

from apps.users.handlers import LoginHandler,RegisterHandler

define("port", default="9999", help="Listening port", type=int)#这句代码可以python app.py --port=8801在执行python文件的时候，添加额外参数

class Application(tornado.web.Application): #tornado配置，比如静态文件
    def __init__(self):
        handlers = [
            # (r"/", IndexHandler),
            # (r"/expore", ExploreHandler),
            # (r"/post/(?P<post_id>[0-9]+)", PostHandler),
            (r"/register", RegisterHandler),
            (r"/login", LoginHandler),
        ]
        settings = dict(
            debug=True,
            template_path="templates",
            static_path='static',
            pycket={
                'engine': 'redis',
                'storage': {
                    'host': 'localhost',
                    'port': 6379,
                    'db_sessions': 5,
                    'max_connections': 2 ** 31,
                },
                'cookies': {
                    'expires_days': 14,
                    # 'expires':None#秒
                },
            },
            cookie_secret='fsdfsdag gagfagadfa 11548418 +_+_--()',
        )

        super().__init__(handlers, **settings)

if __name__ == "__main__":  #只有在当前文件运行的时候才会执行
    tornado.options.parse_command_line()    # 命令行
    application = Application()  # 实例化，一般括号里啥都不写的啦
    application.listen(options.port)
    #application.redis=StrictRedis(db=5,decode_responses=True)这种东西等用到再来写，在我们设置里面的application里添加键值对的话，在视图中，直接self.application.redis.set()这么来用
    tornado.ioloop.IOLoop.current().start() #开启tornado服务，这句不就相当于协程列表最后执行的那句