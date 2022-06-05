def main():
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    # expect answer:[8,9,9,9,0,0,0,1]
    if len(l1) >len(l2):
        # length = len(l1)
        for num in range (len(l1) -len(l2)):
            l2.append(0)
    else:
        # length = len(l2)
        for num in range (len(l2) -len(l1)):
            l1.append(0)
            
    l1.reverse()
    l2.reverse()  
    stringL1=''
    stringL2=''
    for i in range(len(l1)):
        stringL1+=str(l1[i])
        stringL2+=str(l2[i])
    strL3=str(int(stringL1)+int(stringL2))
    l3=[]
    for j in range(len(strL3)):
        l3.append(int(strL3[j]))
    l3.reverse()
    print(l3)

main()
