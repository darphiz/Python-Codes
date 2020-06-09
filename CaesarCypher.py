al = "abcdefghijklmnopqrstuvwxyz"
alp = list(al)
def get_nxt(let):
    #get the next alphabet
    num = alp.index(let)
    new_num = num+1
    if new_num > 25 :
        nxt_let ='a'
    else:
        nxt_let = alp[new_num]
    return nxt_let

def convert(sentence):
    lw = sentence.lower()
    words = lw.split(',')
    for eachword in words:
        #convert eachword to a list
        wordlist = list(eachword)
    return wordlist

def decrypt(something):
    lists = convert(something)
    for letter in lists:
        if letter not in alp:
            print("")
            continue
        word = print(get_nxt(letter))
    
    return word
    
print(decrypt("how are you"))
