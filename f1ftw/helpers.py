from objects.person_name import PersonName

def parse_person_name(name):
    pos = name.find(" ")
    if(pos>-1):
        return PersonName(name[0:pos],name[pos+1:len(name)])
    else:
        return PersonName(None,name)
