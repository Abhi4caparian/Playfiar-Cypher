#playfair
alpha='abcdefghiklmnopqrstuvwxyz'
a='goodmorningall'
#a='abhishekpunjabi'
#a='engieering'
a=a.lower()
pla=[]
for i in a:
    if(i=='j'):
        pla.append('i')
    else:
        pla.append(i)
b='monarchym'
k=b.lower()
z=list(k)
output = []
for x in z:
    if x not in output:
        output.append(x)
a = [[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]
cntr=0;
for x in alpha:
    if x not in output:
        output.append(x)
for i in range(0,5):
    for j in range(0,5):
        a[i][j]=output[cntr]
        cntr=cntr+1;        
print(a)
# inserted properly
cntr=0
l=len(pla)
if(l%2==1):
    pla.append('x')
l=len(pla)
cntr=0;
e=[]
while(cntr<=l):
    if(cntr>(l-2)):
        pla.append('x')
    if(pla[cntr]==pla[cntr+1]):
        e.append(pla[cntr])
        e.append('x')
        cntr=cntr+1
    else:
        e.append(pla[cntr])
        cntr=cntr+1;
        e.append(pla[cntr])
        cntr=cntr+1;
if(len(e)%2==1):
    e.append('x')
print('Plain Text in proper format=',e,len(e))
#encipher
cntr=0
mark=['','']
d=[]
b=[list(i) for i in zip(*a)]
while(cntr<len(e)):
    mark[0]=e[cntr]
    cntr=cntr+1
    mark[1]=e[cntr]
    cntr=cntr+1
    flag=1
    #row right shift 1
    for i in range(0,5):
        if(mark[0] in a[i] and mark[1] in a[i]):
            flag=0
            q1=a[i].index(mark[0])
            q2=a[i].index(mark[1])
            if(q1==4):
                d.append(a[i][0])
            else:
                d.append(a[i][q1+1])
            if(q2==4):
                d.append(a[i][0])
            else:
                d.append(a[i][q2+1])
        elif(mark[0] in b[i] and mark[1] in b[i]):#column shift 1
            flag=0

            q1=b[i].index(mark[0])
            q2=b[i].index(mark[1])
            if(q1==4):
                d.append(b[i][0])
            else:
                d.append(b[i][q1+1])
            if(q2==4):
                d.append(b[i][0])
            else:
                d.append(b[i][q2+1])
        else:
            for j in range(0,5):
                if(mark[0]==a[i][j]):
                    r1=i
                    c1=j
                elif(mark[1]==a[i][j]):
                    r2=i
                    c2=j
    if(flag==1):
        d.append(a[r1][c2])#storing mark[0] value
        d.append(a[r2][c1])#storing mark[1] value
print('\nCIPHER =',d)
c=''
for i in d:
    c=c+i;
print('CIPHER =',c)
p=[]
cntr=0
#Decription 
while(cntr<len(c)):
    mark[0]=d[cntr]
    cntr=cntr+1
    mark[1]=d[cntr]
    cntr=cntr+1
    flag=1
    #row right shift 1
    for i in range(0,5):
        if(mark[0] in a[i] and mark[1] in a[i]):
            flag=0
            q1=a[i].index(mark[0])
            q2=a[i].index(mark[1])
 
            if(q1==0):
                p.append(a[i][4])
            else:
                p.append(a[i][q1-1])
            if(q2==0):
                p.append(a[i][4])
            else:
                p.append(a[i][q2-1])
        elif(mark[0] in b[i] and mark[1] in b[i]):#column shift 1
            flag=0
            q1=b[i].index(mark[0])
            q2=b[i].index(mark[1])
            if(q1==0):
                p.append(b[i][4])
            else:
                p.append(b[i][q1-1])
            if(q2==0):
                p.append(b[i][4])
            else:
                p.append(b[i][q2-1])
        else:
            for j in range(0,5):
                if(mark[0]==a[i][j]):
                    r1=i
                    c1=j
                elif(mark[1]==a[i][j]):
                    r2=i
                    c2=j
    if(flag==1):
        p.append(a[r1][c2])#storing mark[0] value
        p.append(a[r2][c1])#storing mark[1] value
print('Decipher =',p)
t=''
for i in p:
    if(i!='x'):
        t=t+i
print('Decipher =',t)
