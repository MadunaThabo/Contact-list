def searchContact(na,sur):
    name = na
    surname = sur
    found = False
    f = open("contacts.txt", "r")
    topology_list = f.readlines()
    msg = "<table class=table1><tr><th>Name</th><th>Surname</th><th>Cellphone Number</th></tr>"
    for i in topology_list:
        record = i.split("-")
        if(name == record[0]):
            if(surname == record[1]):
                found = True
                i = i.split("-")
                msg +="<tr><td>" + i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td></tr>"
    msg += "</table>" 
    f.close()
    if(found == False):
        print()
        msg ="<h1>searched contact is not found</h1>"
        return msg
    else:
        print("table:", msg)
        return msg
   