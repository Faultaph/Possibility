def cleanandlexer(script):
    instring = False
    for at in range(len(script)):
        if script[at] == '\'':
            if instring == True:
                instring == False
            else:
                instring == True
    if script[at] == '\n':
        if instring == False:
            script[at].replace('\n', '')
    elif script[at] == ' ':
        if instring == False:
            script[at].replace(' ', '')
