def replaceL(searchedString):
    import os
    with open("contacts.txt", "r+") as input:
        with open("temp.txt", "w+") as output:
            for line in input:
                if line != searchedString:
                    output.write(line)
    os.replace('temp.txt', 'contacts.txt')
    return
    

def deleteContact(n,sur):
    name = n
    surname = sur
    f = open("contacts.txt", "r")
    topology_list = f.readlines()
    j=0 #index
    s=0
    delete = False
    for i in topology_list:
        record = i.split("-")
        if(name == record[0]):
            if(surname == record[1]):
                delete = True
                replaceL(i)
                s=s+1
        j=j+1
    f.close()
    if(delete==False):
        # print("sorry your contact is not found\n")
        msg = "sorry your contact is not found>"
        return msg
    else:
        msg = n + " " + sur + "was removed from the contact list"
        return msg
    




