# vernam cipher
#question4






alpha_dict={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13,

 'o':14, 'p':15,'q':16,'r':17, 's':18,'t':19,'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
#correct

inv_map={a:b for b, a in alpha_dict.items()}
#corect

plainText=input("Enter plain text: ")
key=input("Enter the key: ")

plaintext_alphalist=list(plainText)
print(plaintext_alphalist)
key_alphalist=list(key)
#correct

val_list=list(alpha_dict.values())
key_list=list(alpha_dict.keys())
#correct

combine_list=[]
combine_sublist=[]
plaintext_numlist=[]
key_numlist=[]
ciphertext_list=[]
cipher_string=""
#position=""
#correct

def vernamCipher(plainText,key):
    cipher_string=""
    for i in range(0,len(plaintext_alphalist)):
        print(plainText[i])
        plaintext_numlist.append(alpha_dict.get(plaintext_alphalist[i]))
    #correct

    for j in range(0,len(key_alphalist)):
        key_numlist.append(alpha_dict.get(key_alphalist[j]))
    #correct

    print(plaintext_numlist)
    print(key_numlist)
    #Corect

    for k in range(0,len(plaintext_numlist)):
        combine_list.append(plaintext_numlist[k]+key_numlist[k])
    print(combine_list)
    #correct

    for n in range(0,len(combine_list)):
        if combine_list[n]>26:
            combine_list[n]=combine_list[n]-26
        else:
            continue
    print(combine_list)
    #corect

    for m in range(0,len(combine_list)):
        ciphertext_list.append(inv_map.get(combine_list[m]))
    print(ciphertext_list)
    #correct

    for o in range(0,len(ciphertext_list)):
        cipher_string=cipher_string+ciphertext_list[o]
    print(cipher_string)
    # CORRECT!!!!!!










vernamCipher(plainText,key)