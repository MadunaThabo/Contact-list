from http import server
from http.server import HTTPServer,BaseHTTPRequestHandler
from http.server import HTTPServer

from viewAll import viewAll


HOST = 'localhost'
PORT = 5556
result = ""
counter=0
class HTTPR(BaseHTTPRequestHandler):
    def do_GET(self):
        global result
        global counter
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

        def htmlWrite():
            self.wfile.write(bytes("""<html>
            <head>
            <title>Calculator</title>
            <style>
            body{
                background-image:url(https://images.unsplash.com/uploads/1413222992504f1b734a6/1928e537?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80);
            }

            // Fonts

            @import url(https://fonts.googleapis.com/css?family=Indie+Flower);

            h1{
                color: #fff;
                font-family: 'Indie Flower', cursive;
                font-weight: normal;
                text-align: center;
                width: 100%;
            }

            
            }
            table.table1{
                margin-left: auto;
                margin-right: auto;
            }
           
            input{
                float: left;
                width: 460px;
                height: 40px;
                padding: 0 10px;
                border: 0;
                border-bottom: 3px solid #fff;
                background-color: transparent;
                color: #fff;
                font-family: 'Indie Flower', cursive;
                font-size: 22px;
                position: relative;
                z-index: 99;
                &:focus{
                outline: 0;
                }
                &.white{
                background-color: #E74C3C;
                }
            }

            input:focus + span{
                span{
                cursor: initial;
                position: absolute;
                top: -35px;
                color: #2C3E50;
                }
                &:before{
                width: 50%;
                }
                &:after{
                width: 50%;
                }
            }

            span.fixed{
                span{
                top: -35px;
                }
            }
            }
            
            </style>
            </head>
            <body>
                <h1>Contact List</h1>
               <table class="table1">
                    <tr>
                        <th>Name</th>
                        <th>Surname</th>
                        <th>Cellphone Number</th>
                    </tr>
                """+ viewAll()+ """    
                </table>           
            </body></html>\r\n\r\n""","utf-8"))
        if(counter==0):
            htmlWrite()
            counter=counter+1
        else:
            if(self.path.endswith("=")):
                i = 0
                zero=0
                while(i in range(len(result))):
                    if(result[i] == "/"):
                        if(result[i+1]=="0"):
                            result = "Error" 
                            zero=1
                    i =i+1      
                if(zero==0):
                    result=str(eval(result))

            elif(self.path.endswith("0")):
                result+="0"
            elif(self.path.endswith("1")):
                result+="1"
            elif(self.path.endswith("2")):
                result+="2"
            elif(self.path.endswith("3")):
                result+="3"
            elif(self.path.endswith("4")):
                result+="4"
            elif(self.path.endswith("5")):
                result+="5"
            elif(self.path.endswith("6")):
                result+="6"
            elif(self.path.endswith("7")):
                result+="7"
            elif(self.path.endswith("8")):
                result+="8"
            elif(self.path.endswith("9")):
                result+="9"
            elif(self.path.endswith("X")):
                result+="X"
            elif(self.path.endswith("+")):
                result+="+"
            elif(self.path.endswith("-")):
                result+="-"
            elif(self.path.endswith("/")):
                result+="/"
            elif(self.path.endswith("del")):
                result = result[:-1]
            elif(self.path.endswith("clear")):
                result = ""
            elif(self.path.endswith("")):
                htmlWrite()
            htmlWrite()

# def serve_forever(self):
#   while not self.stopped:
#     server = HTTPServer((HOST,PORT),HTTPR)
#     print("server has started")
#     self.handle_request()
# def force_stop(self):
#   self.server_close()

server = HTTPServer((HOST,PORT),HTTPR)
print("server has started")
print("http://localhost:"+str(PORT))
server.serve_forever()
server.server_close()
       
            