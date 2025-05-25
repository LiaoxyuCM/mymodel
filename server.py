from http import server # * import server
from random import randint

class SimpleHTTPRequestHandlerWithErrorPage(server.SimpleHTTPRequestHandler):
    # * this is an error msg
    error_message_404 = """
<!DOCTYPE html>
<html>
<head>
<title>Oops!</title>
<style>
* {
    color: white;
    font-family: Alex Brush;
    font-size: 45px;
    transition: 0.7s;
}
a:hover{
    text-shadow: 5px 5px 5px black, 10px 10px 10px black;
}
p {text-align: center;}
ul {text-align: center; list-style-type: none;}
a {text-decoration: none; color: white;}

body {background-image: linear-gradient(90deg, rgb(84, 30, 36) 0%, rgb(209, 26, 45) 90%, rgb(238, 63, 77) 100%);}
</style>
</head>
<body>
<p>Oops!<br>The page is not found!</p>
<ul>
<li><a href="..">Return</a></li>
</ul>
</body>
</html>
"""
    def send_error(self, code, message=None):
        if code == 404:
            self.send_response(code)
            self.send_header('Content-type', 'text/html')
            self.send_header('Content-Length', str(len(self.error_message_404)))
            self.end_headers()
            self.wfile.write(bytes(self.error_message_404, 'utf-8'))
        else:
            super().send_error(code, message)

def run(port: int = 8000):
    if (port <= 49151) and (port >= 1024):
        serverClass = server.HTTPServer # * create server
        handlerClass = SimpleHTTPRequestHandlerWithErrorPage # * create handler
        serverAddress = ('', port) # * set address
        httpd = serverClass(serverAddress, handlerClass) # * run server
        print(f'visit http://localhost:{port}') # ? tell user where is the server
        httpd.serve_forever() # ! run server forever
    else: raise TypeError("use sign port (1024~49151), that's good")

# // def auto(): return random.randint(1024, 49151)
# ? we can use "lambda" to define a function
auto = lambda: randint(1024, 49151)

if __name__ == '__main__': 
    run(1028)
