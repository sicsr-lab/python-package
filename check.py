import string,io
def detect_language(character):
    maxchar = max(character)
    if (u'\u0900' <= maxchar <= u'\u097f') or (maxchar == '\n') or (maxchar == u'\u0020'):
        return 'hindi'

def detect_language_punctuation(character):
    maxchar = max(character)
    if (u'\u0900' <= maxchar <= u'\u097f') or (u'\u0020' <= maxchar <= u'\u002f') or (maxchar == '\n'):
        return 'hindi'

def detect_language_processed(character):
    maxchar = max(character)
    if (u'\u0900' <= maxchar <= u'\u097f'):
        return 'hindi'

def fileReader(location):
    location2 = "" + location + ""
    fo = io.open("output.txt", "w", encoding='utf-8')
    with io.open(location2, encoding='utf-8') as f:
        input = f.read()
        for i in input:
            isEng = detect_language(i)
            if isEng == "hindi":
                #Hindi Character
                #add this to another file
                fo.write(i)
    fo.close()
    f.close()
    check = processedText()

def punctuation(location):
    location2 = "" + location + ""
    fo = io.open("output.txt", "w", encoding='utf-8')
    with io.open(location2, encoding='utf-8') as f:
        input = f.read()
        for i in input:
            isEng = detect_language_punctuation(i)
            if isEng == "hindi":
                #Hindi Character
                #add this to another file
                fo.write(i)
    fo.close()
    f.close()
    check = processedText()

def processedText():
    with io.open("output.txt", encoding='utf-8') as f:
        para=""
        lines=f.readlines()
        for line in lines:
            check=0
            for i in line:
                isEng = detect_language_processed(i)
                if isEng == "hindi":
                    check=1
                    break
            if check==1:
                line=line.lstrip(" ")
                para=para+line
    fo = io.open("output.txt", "w", encoding='utf-8')
    fo.write(para)
