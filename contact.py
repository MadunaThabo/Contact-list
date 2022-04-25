from http import server
from http.server import HTTPServer,BaseHTTPRequestHandler
from http.server import HTTPServer
from delete import deleteContact
from modify import modifyContact

from viewAll import viewAll
from add import addLine
from search import searchContact


HOST = 'localhost'
PORT = 5550
result = ""
searchTable=""
counter=0
class HTTPR(BaseHTTPRequestHandler):
    def do_GET(self):
        global result
        global counter
        global searchTable
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
           
            span.fixed{
                span{
                top: -35px;
                }
            }
            }
            
            </style>
            </head>
            <body>                
                <h1>Search Contact</h1>
                    <form method="get">
                        <label for="SearchName">Name:</label>
                        <input type="text" id="searchName" name="searchName">
                        <label for="searchSName">&nbsp;&nbsp;&nbsp;&nbsp;Surname:</label>
                        <input type="text" id="searchSName" name="searchSName">&nbsp;&nbsp;&nbsp;&nbsp;
                        <input type="submit" value="Search contact"><br/>
                    </form>"""+ searchTable + """
                <h1>Add Contacts</h1>
                    <form method="get">
                        <label for="addName">Name:</label>
                        <input type="text" id="addName" name="addName">
                        <label for="addSName">&nbsp;&nbsp;&nbsp;&nbsp;Surname:</label>
                        <input type="text" id="addSName" name="addSName">
                        <label for="addNum">&nbsp;&nbsp;&nbsp;&nbsp;Numbers:</label>
                        <input type="text" id="addNum" name="addNum">&nbsp;&nbsp;&nbsp;&nbsp;
                        <input type="submit" value="add contact"><br/>
                    </form>
                    
                <h1>Delete Contact</h1>
                    <form method="get">
                        <label for="delName">Name:</label>
                        <input type="text" id="delName" name="delName">
                        <label for="delSName">&nbsp;&nbsp;&nbsp;&nbsp;Surname:</label>
                        <input type="text" id="delSName" name="delSName">&nbsp;&nbsp;&nbsp;&nbsp;
                        <input type="submit" value="delete contact"><br/>
                    </form>
                
                    <h1>Modify Contact</h1>
                    <form method="get">
                        <label for="modifyName">Name:</label>
                        <input type="text" id="modifyName" name="modifyName">
                        <label for="modifySName">&nbsp;&nbsp;&nbsp;&nbsp;Surname:</label>
                        <input type="text" id="modifySName" name="modifySName"><br/><br/>
                        <label for="newName">New Name:</label>
                        <input type="text" id="newName" name="newName">
                        <label for="newSName">&nbsp;&nbsp;&nbsp;&nbsp;New Surname:</label>
                        <input type="text" id="newSName" name="newSName">
                        <label for="modifyNum">&nbsp;&nbsp;&nbsp;&nbsp;New Numbers:</label>
                        <input type="text" id="modifyNum" name="modifyNum">&nbsp;&nbsp;&nbsp;&nbsp;
                        <input type="submit" value="Modify contact"><br/>
                    </form>

                <h1> """+ result + """</h1>
                <h1>Contact List</h1>
                    <table class="table1">
                    <tr>
                        <th>Name</th>
                        <th>Surname</th>
                        <th>Cellphone Number</th>
                    </tr>
                    """+ viewAll() + """    
                </table>
            </body></html>\r\n\r\n""","utf-8"))
        if(counter==0):
            htmlWrite()
            counter=counter+1
        else:
            if self.path.find("addName") > -1:
                print("self.path: ", self.path)
                str1=self.path.split("=")[1]
                name=str1.split("&")[0]
                str1=self.path.split("=")[2]
                surname=str1.split("&")[0]
                contact=self.path.split('=')[3]
                result=addLine(name,surname,contact)
                htmlWrite()
            elif self.path.find("delName") > -1:
                str1=self.path.split("=")[1]
                name=str1.split("&")[0]
                surname=self.path.split("=")[2]
                result = ""
                result = deleteContact(name,surname)
                htmlWrite()
            elif self.path.find("searchName") > -1:
                str1=self.path.split("=")[1]
                name=str1.split("&")[0]
                surname=self.path.split("=")[2]
                searchTable = searchContact(name,surname)
                htmlWrite()
            elif self.path.find("modifyName") > -1:
                name = self.path.split("=")[1]
                name = name.split("&")[0]
                surname = self.path.split("=")[2]
                surname = surname.split("&")[0]
                nName = self.path.split("=")[3]
                nName = nName.split("&")[0]
                nSurname = self.path.split("=")[4]
                nSurname = nSurname.split("&")[0]
                nNumber = self.path.split("=")[5]
                print("input ", name, surname, nName, nSurname, nNumber)
                result = modifyContact(name, surname, nName, nSurname, nNumber)
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
       
            