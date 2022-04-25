# from nis import match


def addLine(name,surname,contact):
    f = open("contacts.txt", "a+")
    f.write(name+"-"+surname+"-"+contact+"\n")
    f.close()
    msg = ""
    print("Adding "+ name+" "+surname+" "+contact+" was successful")
    msg="Adding "+ name+" "+surname+" "+contact+" was successful"
    # msg +="<tr><td>" + i[0]+"</td><td>"+i[1]+"</td><td>"+i[2]+"</td></tr>"
    return msg