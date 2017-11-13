from objects.person_name import PersonName

def ParsePersonName(name):
    pos=name.find(" ")
    if(pos>-1):
        return PersonName(name[0:pos],name[pos+1:len(name)])
    else:
        return PersonName(None,name)
