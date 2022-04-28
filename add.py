from search import searchContact


def addLine(name,surname,contact):
    f = open("contacts.txt", "r+")
    topology_list = f.readlines()
    found = False
    line = name+"-"+surname+"-"+contact+"\n"
    for i in topology_list:
        print("testing", i, "and", line, i==line)
        if(i==line):
            print("found")
            found = True
            break
    f.close()
    print("found is:", found)
    if found==False: 
        f = open("contacts.txt", "a+")
        f.write(name+"-"+surname+"-"+contact+"\n")
        f.close()
        msg = ""
        print("Adding "+ name+" "+surname+" "+contact+" was successful")
        msg="Adding "+ name+" "+surname+" "+contact+" was successful"
        f.close()
        return msg
    else:
        msg1="Contact Already Exist"
        return msg1