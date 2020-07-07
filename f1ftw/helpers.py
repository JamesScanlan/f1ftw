from objects.person_name import person_name

def parse_person_name(name):
    pos = name.find(" ")
    if(pos>-1):
        return person_name(name[0:pos],name[pos+1:len(name)])
    else:
        return person_name(None,name)
