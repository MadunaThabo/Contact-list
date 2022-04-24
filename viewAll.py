def viewAll():
    f = open("contacts.txt", "r")
    topology_list = f.readlines()
    msg = ""
    for i in topology_list:
        print("sending contact for view")
        i = i.split("-")
        msg +="<tr><td>" + i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td></tr>" 
    f.close()
    return msg

    