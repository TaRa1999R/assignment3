print (" 🧐 LET'S COUNT THE NIMBER OF WORDS IN A SENTERNCE 🧐 ")

sentence = input (" Please enter your sentence : ")
words = 1

for i in range ( len ( sentence )) :
    if sentence[i] == " " :
        words += 1

print (" Your sentece has ", words, " words 🙂 ")