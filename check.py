import codecs,string
def detect_language(character):
    maxchar = max(character)
    if u'\u0900' <= maxchar <= u'\u097f':
        return 'hindi'
def fileReader(location):
    temp = " "
    location2 = "" + location + ""
    fo = open("output.txt", "w", encoding='utf-8')
    with codecs.open(location2, encoding='utf-8') as f:
        input = f.read()
        for i in input:
            isEng = detect_language(i)
            if isEng == "hindi":
                #Hindi Character
                #add this to another file
                if temp==" ":
                    fo.write(" "+i)
                else:
                    fo.write(i)
            if i==" ":
                temp=" " 
            else:
                temp="n"	
    return True   