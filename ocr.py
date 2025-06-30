from http.server import HTTPServer, BaseHTTPRequestHandler

class Request(BaseHTTPRequestHandler):
    #通过类继承，新定义类
    timeout = 5
    server_version = 'Apache'

    def do_GET(self):
        #在新类中定义get的内容（当客户端向该服务端使用get请求时，本服务端将如下运行）
        self.send_response(200)
        self.send_header("type","get") #设置响应头，可省略或设置多个
        self.end_headers() 

        msg = 123 #要返回给客户端的信息
        msg = str(msg).encode() #转为str再转为byte格式

        self.wfile.write(msg) #将byte格式的信息返回给客户端

    def do_POST(self):
        #在新类中定义post的内容（当客户端向该服务端使用post请求时，本服务端将如下运行）
        data = self.rfile.read(int(self.headers['content-length'])) #获取从客户端传入的参数（byte格式）
        data =  data.decode() #将byte格式转为str格式

        self.send_response(200)
        self.send_header("type","post") #设置响应头，可省略或设置多个
        self.end_headers()

        msg = int(data)*2 #要返回给客户端的信息（将str转为int再x2）  
        msg = str(msg).encode() #转为str再转为byte格式
        self.wfile.write(msg) #将byte格式的信息返回给客户端


host = ('localhost',8888) #设定地址与端口号，'localhost'等价于'127.0.0.1'
server = HTTPServer(host, Request) #根据地址端口号和新定义的类，创建服务器实例
server.serve_forever() #开启服务