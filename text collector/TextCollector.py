#Program that store each and every letter with punctuation that is typed by a user and store it into a new file.
Text=[]
textlist=""
on=True
while on:
    t=input()
    if t=="@":
        on=False
    else:
        textenter=t+"\n"
        text=Text.append(textenter)

if on==False:
    for i in Text:
        textli="".join(Text)
        textspace=(textli+"\n")
        textlist=textspace

        with open("storedTxt.txt", "w") as f:
            f.write(textlist)
