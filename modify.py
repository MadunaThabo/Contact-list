import os

def replaceL(i, nName, nSurname, nNumber):
    searchedString = i
    print("searchedString is: " + searchedString)
    with open("contacts.txt", "r+") as input:
        with open("temp.txt", "w+") as output:
            for line in input:
                if line != searchedString:
                    output.write(line)
                else:
                    name1 = nName
                    surname1 = nSurname
                    number1 = nNumber
                    print("input in replace is: ", nName, nSurname, nNumber)
                    output.write(name1+"-"+surname1+"-"+number1+"\n")
    os.replace('temp.txt', 'contacts.txt')

def modifyContact(na , sur, nName, nSur, nNum):
    name = na
    surname = sur
    f = open("contacts.txt", "r")
    topology_list = f.readlines()
    found = False
    for i in topology_list:
        record = i.split("-")
        if(name == record[0]):
            if(surname == record[1]):
                found = True
                replaceL(i, nName, nSur, nNum)
    f.close()
    if(found == False):
        print("contact is not found\n")
        msg = "sorry your contact is not found\n"
        return msg
    else:
        msg = "change "+ na +" "+ sur + " to "+ nName + " " + nSur + " " + nNum
        return msg
    