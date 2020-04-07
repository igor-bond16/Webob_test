from webob import Request,Response

html = """
<form method="POST">state:
<input type="text" name="state" value="%s">
<input type="submit" name="button" value="set">
"""

class WebApp(object):
    def __call__(self,environ,start_response):
        req = Request(environ)
        if req.path == '/':
            state = int(req.params.get('state','0'))
            print(str(state))
        else:
            resp = Response()
            
        return resp(environ,start_response)
    
application = WebApp()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 8080
    httpd = make_server('',port,application)
    print('Serving HTTP on port %s...' %port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass