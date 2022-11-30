#Yarışmacıların isim, soyisim ve önceki yarışmalardan elde ettiği derecelerin bulunduğu dosya okunarak veri seti incelenmiştir.
import pandas as pd
data=pd.read_csv("Full Name-Rating.txt", header=None, names=["Full Name","Rating"])
print(f"Rankings of competitors from previous competitions\n\n{data}\n\n\n\n\nSwiss System Chess Tournament\n\nStart of the first round...\n")

dosya=open("Full Name-Rating.txt","r",encoding = "utf-8")
Values1=dosya.read().splitlines() 

Values2=[ ]
for line in Values1: 
    name,rating=line.split(",")
    rating=float(rating)
    Values2.append(["Name",name,"Rating",rating])
    
dosya.close()  

Values2.sort(key=lambda x: x[1])   #Değerler Rating ve Full Name'e göre sıralandı 
Values2.sort(key=lambda x: x[3], reverse=True)
#print(Values2)

# Sıralama yapıldıktan sonra rating değerlerine ihtiyacım kalmadı
sıralama=[Values2[i][1] for i in range(len(Values2))] 
#print(sıralama)

Group0=[]
if (len(sıralama) % 2 == 1): #İkiye böldüğümde dışarıda kalan varsa Group0 adında listeye attım.Bu şekilde sıralamalar bittiğinde erişebileceğim.
    Group0.append(sıralama[-1])        
    sıralama.remove(sıralama[-1])
    Group1, Group2 = sıralama[:len(sıralama) // 2], sıralama[len(sıralama) // 2:]  
#    print(f"Group0 : {Group0}\nGroup1 : {Group1}\nGroup2 :{Group2}\n")
else:
    Group1, Group2 = sıralama[:len(sıralama) // 2], sıralama[len(sıralama) // 2:] 
#    print(f"Group1 : {Group1}\nGroup2 : {Group2}\n")

yerles0, yerles, yerles2=[], [], []

for line in Group0:  #Dışarıda kalan oyuncu 1 puan alacağı için gerekli bilgileri yazdım.Daha sonra sıralamada kullanıcağım.
    name,score,colour=line,float("1"),"No colour" 
    yerles0.append([name,score,colour])     
for line in Group1: #İlk oyunda herkesin score değerleri 0 olacağı için bu şekilde 0 değerini atadım.
    name,score=line, float("0")
    yerles.append([name,score])
for line in Group2:
    name,score=line, float("0")
    yerles2.append([name,score])     
#print(f"{yerles0}\n{yerles}\n{yerles2}\n")      

if (len(yerles) % 2 == 1): #Eğer ikinci kez listeyi ikiye böldüğümde dışarıda kalan oluyorsa ,ikinci grubun başına atıyorum.
    if len(yerles2) > 0 :
        yerles2.insert(0,yerles[-1])
        yerles.remove(yerles[-1])
        Group11, Group22, Group111, Group222 = yerles[:len(yerles) // 2], yerles[len(yerles) // 2:], yerles2[:len(yerles2) // 2], yerles2[len(yerles2) // 2:]
        
elif (len(yerles) % 2 == 0):   
    Group11, Group22, Group111, Group222 = yerles[:len(yerles) // 2], yerles[len(yerles) // 2:], yerles2[:len(yerles2) // 2], yerles2[len(yerles2) // 2:] 
    #Yukarıda ikiye böldüğüm listenin birincisini ikiye böldüm bu şekilde iki ayrı liste oluştu.Bu iki listeyi birleştirerek kurallara uygun karşılaşma düzenini sağlamış oldum.
#print(f"\n{Group11}\n{Group22}\n{Group111}\n{Group222}")

Group11y, Group22y, Group111y, Group222y = [], [], [], []

def renk_atama(grup_adı):
    for line in grup_adı:  #Masalardaki ilk oyunculara siyah rengi atadım.
        name,score=line
        colour="Black" if (grup_adı == Group11 or grup_adı == Group111) else "White"
        if grup_adı==Group11:
            Group11y.append([name,score,colour])
        elif grup_adı==Group22:  
            Group22y.append([name,score,colour])
        elif grup_adı==Group111:  
            Group111y.append([name,score,colour])
        else:  
            Group222y.append([name,score,colour])    

renk_atama(Group11) 
renk_atama(Group22) 
renk_atama(Group111) 
renk_atama(Group222) 
#print(f"Group11 : {Group11y}\nGroup22 : {Group22y}\nGroup111 :{Group111y}\nGroup222 : {Group222y}\n")

zipped, zipped2 = zip(Group11y,Group22y), zip(Group111y,Group222y) #renk ataması yaptığım grupları birleştirdim
Masalar1, Masalar2 = (list(zipped)),(list(zipped2))       
print(f"\n\nMatch List(First Round):\n\n\nGroup 1 : {Masalar1}\n\n\nGroup 2 : {Masalar2}\n\n\n") #() içi her bir eşleşmeyi ifade etmektedir

#Kullanıcıdan maç sonucunu değer alarak skorların güncel durumunu sağladım.
def masa_skor(masa_no):
    for i in range(0,len(masa_no)): 
        while(True):
            print(f"\nEnter the result of the {i+1}. match. If the first player wins (1) or second player wins (2) or draw (12).")
            Response = input()
            if (Response not in ["1","2","12"]):
                print("Please enter valid command(1, 2, 12)")
            else:
                if (Response =="1"):
                    masa_no[i][0][1]=masa_no[i][0][1]+1
                elif (Response =="2"):    
                    masa_no[i][1][1]=masa_no[i][1][1]+1
                elif (Response =="12"):
                    masa_no[i][0][1]=masa_no[i][0][1]+0.5
                    masa_no[i][1][1]=masa_no[i][1][1]+0.5     
                break
masa_skor(Masalar1)  
masa_skor(Masalar2)  
#print(f"\nMasalar 1(Skor) : {Masalar1}\n\nMasalar 2(Skor) : {Masalar2}\n")

Masalar12=(Masalar1+Masalar2) #İki ayrı olan grubu tek grup haline getirdim
Masalar12= [ item for i in Masalar12 for item in i] #eşleşme bazından kişi bazına indirgedim
#print(Masalar12)

def sort_d1(masa_birlesim): #bu turnuvada elde edilen rating ve isime göre sıralama yapıldı
    masa_birlesim.sort(key=lambda x: x[0])
    masa_birlesim.sort(key=lambda x: x[1], reverse=True)
#    print(f"\n{masa_birlesim}\n")
    
if (len(Group0) >= 1): #Açıkta kalan oyuncuyu Group0'a atmıştım Masalar12 listesine ekledim,son durumda sıralamaya katılmasını sağladım.
    Masalar12.append(yerles0[0])
    sort_d1(Masalar12)
elif (len(Group0) == 0):
    sort_d1(Masalar12) 

df = pd.DataFrame (Masalar12,columns = ["Full Name","Rating","Colour"])
print(f"{df}\n\nThe first round of the competition is over.The results of the first round are given above.\nStart of the second round...\n")

import random
#2.turun başlangıcında en fazla 1 puan olacağı için ,sırasıyla puan değerlerini içeren boş liste oluşturdum.
ikincitur0, ikincitur05, ikincitur1 = [], [], []

for line in Masalar12:
    name,score=line[0],line[1]
    colour=(random.choice(["Black","White"])) #İkinci turda taşlarının renklerini random olarak atadım.
    if score==float(1):
        ikincitur1.append([name,score,colour])
    elif score==float(0.5):
        ikincitur05.append([name,score,colour])
    elif score==float(0):
        ikincitur0.append([name,score,colour])   
#print(f"\nikincitur1 : {ikincitur1}\n\nikincitur0.5 : {ikincitur05}\n\nikincitur0: {ikincitur0}")

#Eğer 1 puan alanlar listesinde 1 kişi dışarıda kalıyorsa onu bir sonraki 0.5 puan alanların olduğu listenin 0.indexine atadım .Bu şekilde 1puan alanların en güçsüzüyle ,0puan alanların en güçlüsünü eşleştirdim.  
def puan1_dışarıdakalan(score1, score2, score3):
    if (len(score1) % 2 == 1): 
        if len(score2) > 0 :
            score2.insert(0,score1[-1])
            score1.remove(score1[-1])
        else:
            score3.insert(0,score1[-1]) #Eğer 0.5 puan alanların olduğu liste boşsa,0 puan alanların olduğu listeye atadım.
            score1.remove(score1[-1])
                           
if (len(ikincitur1) % 2 == 0):   
    Group1, Group2 = ikincitur1[:len(ikincitur1) // 2], ikincitur1[len(ikincitur1) // 2:] 
else:        
    puan1_dışarıdakalan(ikincitur1, ikincitur05, ikincitur0) 
    Group1, Group2 = ikincitur1[:len(ikincitur1) // 2], ikincitur1[len(ikincitur1) // 2:] 
    
def renk_degis(first_player,second_player):#Eğer aynı renk gelirse,ikinci oyuncunun rengi değiştirilmekte
    for x in range(len(first_player)): 
        if first_player[x][2] == ("Black") :
            second_player[x][2]=second_player[x][2].replace("Black","White")
        elif first_player[x][2] == ("White") :
            second_player[x][2]=second_player[x][2].replace("White","Black")
renk_degis(Group1, Group2)

zipped = zip(Group1,Group2)
Masalar1=(list(zipped))
#print("Group 1:",Masalar1)

skoralan=[] #boşta kalanların atıldığı liste

def puan05_dışarıdakalan(score1, score2):
    if (len(score1) % 2 == 1): #0.5 puan alanlar
        if len(score2) > 0 :
            score2.insert(0,score1[-1])
            score1.remove(score1[-1])
        else:
            skoralan.append(score1[-1]) #Eğer 0 puan alanlar listesi boşsa ,skoralan adındaki listeye atıyorum bu şekilde listenin içindeki kişi 1 puan alıyor.
            score1.remove(score1[-1])
            
if (len(ikincitur05) % 2 == 0):   
    Group11, Group22 = ikincitur05[:len(ikincitur05) // 2], ikincitur05[len(ikincitur05) // 2:] 
else:        
    puan05_dışarıdakalan(ikincitur05,ikincitur0)  
    Group11, Group22 = ikincitur05[:len(ikincitur05) // 2], ikincitur05[len(ikincitur05) // 2:]   
     
renk_degis(Group11, Group22) 

zipped = zip(Group11,Group22)
Masalar2=(list(zipped))
#print("Group 2:",Masalar2) 

def puan0_dışarıdakalan(score1):
    if (len(score1) % 2 == 1): #0puan alanlar
        skoralan.append(score1[-1])#Skoralan adındaki listeye atıyorum bu şekilde listenin içindeki kişi 1 puan alıyor.
        score1.remove(score1[-1])

if (len(ikincitur0) % 2 == 0):   
    Group111, Group222 = ikincitur0[:len(ikincitur0) // 2], ikincitur0[len(ikincitur0) // 2:] 
else:        
    puan0_dışarıdakalan(ikincitur0)   
    Group111, Group222 = ikincitur0[:len(ikincitur0) // 2], ikincitur0[len(ikincitur0) // 2:]          

renk_degis(Group111, Group222)  

zipped = zip(Group111,Group222)
Masalar3=(list(zipped))
#print("Group 3:",Masalar3)

print(f"\n\nMatch List(Second Round):\n\n\nGroup 1 : {Masalar1}\n\n\nGroup 2 : {Masalar2}\n\n\nGroup 3 : {Masalar3}")

#Dışarıda kalan oyuncu 1 puan alacağı için gerekli bilgileri yazdım.Bu şekilde daha sonra sıralamada kullanıcağım.
yerlesskor=[]
for line in skoralan:  
    name,score,colour=line[0],line[1],line[2]
    score += float(1)
    yerlesskor.append([name,score,colour]) 

masa_skor(Masalar1)  
masa_skor(Masalar2)
masa_skor(Masalar3)
#print(f"\nMasalar 1(Skor) : {Masalar1}\n\nMasalar 2(Skor) : {Masalar2}\n\nMasalar 3(Skor) : {Masalar3}\n")

Masalar12=(Masalar1+Masalar2+Masalar3)
Masalar12= [ item for i in Masalar12 for item in i]  

if (len(skoralan) >= 1):
    Masalar12.append(yerlesskor[0]) #Yukarıda oluşturduğum yerlesskor listesini kullanıyorum bu şekilde açıkta kalan oyuncuya ana listeye atıyorum.
    sort_d1(Masalar12)

elif (len(skoralan) == 0):
    sort_d1(Masalar12)
    
df2 = pd.DataFrame (Masalar12,columns = ["Full Name","Rating","Colour"])
print(f"{df2}\n\nThe second round of the competition is over.The results of the second round are given above.\nStart of the second round...\n")

ücüncütur0, ücüncütur05, ücüncütur1, ücüncütur15, ücüncütur2=[], [], [], [], [] 
#3.turun başlangıcında en fazla 2 puan olacağı için ,sırasıyla puan değerlerini içeren boş liste oluşturdum.
for line in Masalar12:
    name,score=line[0],line[1]
    colour=(random.choice(["Black","White"])) #İkinci turda taşlarının renklerini random olarak atadım.
    if score==float(2):
        ücüncütur2.append([name,score,colour])
    elif score==float(1.5):
        ücüncütur15.append([name,score,colour])
    elif score==float(1):
        ücüncütur1.append([name,score,colour])
    elif score==float(0.5) :
        ücüncütur05.append([name,score,colour])
    elif score==float(0):ücüncütur0.append([name,score,colour])      
#print(f"\nucuncutur2 : {ücüncütur2}\n\nucuncutur1.5 : {ücüncütur15}\n\nucuncutur1: {ücüncütur1}\n\nucuncutur0.5: {ücüncütur1}\n\nucuncutur0: {ücüncütur05}\n\nucuncutur0: {ücüncütur0}")

#2 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(ücüncütur2) % 2 == 0):   
    Group1, Group2 = ücüncütur2[:len(ücüncütur2) // 2], ücüncütur2[len(ücüncütur2) // 2:] 
else:        
    puan1_dışarıdakalan(ücüncütur2, ücüncütur15, ücüncütur1) 
    Group1, Group2 = ücüncütur2[:len(ücüncütur2) // 2], ücüncütur2[len(ücüncütur2) // 2:] 

renk_degis(Group1, Group2)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1,Group2)
Masalar1=(list(zipped))
#print("Group 1:",Masalar1)

#1.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(ücüncütur15) % 2 == 0):   
    Group11, Group22 = ücüncütur15[:len(ücüncütur15) // 2], ücüncütur15[len(ücüncütur15) // 2:] 
else:        
    puan1_dışarıdakalan(ücüncütur15, ücüncütur1, ücüncütur05) 
    Group11, Group22 = ücüncütur15[:len(ücüncütur15) // 2], ücüncütur15[len(ücüncütur15) // 2:] 

renk_degis(Group11, Group22)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group11,Group22)
Masalar2=(list(zipped))
#print("Group 2:",Masalar2)

#1 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(ücüncütur1) % 2 == 0):   
    Group111, Group222 = ücüncütur1[:len(ücüncütur1) // 2], ücüncütur1[len(ücüncütur1) // 2:] 
else:        
    puan1_dışarıdakalan(ücüncütur1, ücüncütur05, ücüncütur0) 
    Group111, Group222 = ücüncütur1[:len(ücüncütur1) // 2], ücüncütur1[len(ücüncütur1) // 2:] 

renk_degis(Group111, Group222) #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group111,Group222)
Masalar3=(list(zipped))
#print("Group 3:",Masalar3)

skoralan=[] #boşta kalanların atıldığı liste
#0.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak  

if (len(ücüncütur05) % 2 == 0):   
    Group1111, Group2222 = ücüncütur05[:len(ücüncütur05) // 2], ücüncütur05[len(ücüncütur05) // 2:] 
else:        
    puan05_dışarıdakalan(ücüncütur05,ücüncütur0)  
    Group1111, Group2222 = ücüncütur05[:len(ücüncütur05) // 2], ücüncütur05[len(ücüncütur05) // 2:] 


renk_degis(Group1111, Group2222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1111,Group2222)
Masalar4=(list(zipped))
#print("Group 4:",Masalar4) 

#0 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak  
if (len(ücüncütur0) % 2 == 0):   
    Group11111, Group22222 = ücüncütur0[:len(ücüncütur0) // 2], ücüncütur0[len(ücüncütur0) // 2:] 
else:        
    puan0_dışarıdakalan(ücüncütur0)     
    Group11111, Group22222 = ücüncütur0[:len(ücüncütur0) // 2], ücüncütur0[len(ücüncütur0) // 2:] 


renk_degis(Group11111, Group22222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group11111,Group22222)
Masalar5=(list(zipped))
#print("Group 5:",Masalar5)

print(f"\n\nMatch List(Third Round):\n\n\nGroup 1 : {Masalar1}\n\n\nGroup 2 : {Masalar2}\n\n\nGroup 3 : {Masalar3}\n\n\nGroup 4 : {Masalar4}\n\n\nGroup 5 : {Masalar5}")

#Dışarıda kalan oyuncu 1 puan alacağı için gerekli bilgileri yazdım.Bu şekilde daha sonra sıralamada kullanıcağım.
yerlesskor=[]
for line in skoralan:  
    name,score,colour=line[0],line[1],line[2]
    score += float(1)
    yerlesskor.append([name,score,colour]) 

masa_skor(Masalar1)  
masa_skor(Masalar2)
masa_skor(Masalar3)
masa_skor(Masalar4)
masa_skor(Masalar5)
#print(f"\nMasalar 1(Skor) : {Masalar1}\n\nMasalar 2(Skor) : {Masalar2}\n\nMasalar 3(Skor) : {Masalar3}\n\nMasalar 4(Skor) : {Masalar4}\n\nMasalar 5(Skor) : {Masalar5}\n")

Masalar12=(Masalar1+Masalar2+Masalar3+Masalar4+Masalar5)
Masalar12= [ item for i in Masalar12 for item in i]  

if (len(skoralan) >= 1):
    Masalar12.append(yerlesskor[0]) #Yukarıda oluşturduğum yerlesskor listesini kullanıyorum bu şekilde açıkta kalan oyuncuya ana listeye atıyorum.
    sort_d1(Masalar12)

elif (len(skoralan) == 0):
    sort_d1(Masalar12)
    
df3 = pd.DataFrame (Masalar12,columns = ["Full Name","Rating","Colour"])
print(f"{df3}\n\nThe third round of the competition is over.The results of the third round are given above.\nStart of the fourth round...\n")

dördüncütur0, dördüncütur05, dördüncütur1, dördüncütur15, dördüncütur2, dördüncütur25, dördüncütur3=[],[],[],[],[],[],[]  
#4.turun başlangıcında en fazla 3 puan olacağı için ,sırasıyla puan değerlerini içeren boş liste oluşturdum.
for line in Masalar12:
    name,score=line[0],line[1]
    colour=(random.choice(["Black","White"])) #İkinci turda taşlarının renklerini random olarak atadım.
    if score==float(3):
        dördüncütur3.append([name,score,colour])
    elif score==float(2.5):
        dördüncütur25.append([name,score,colour])
    elif score==float(2):
        dördüncütur2.append([name,score,colour])
    elif score==float(1.5) :
        dördüncütur15.append([name,score,colour])
    elif score==float(1):
        dördüncütur1.append([name,score,colour])
    elif score==float(0.5):
        dördüncütur05.append([name,score,colour])
    elif score==float(0):
        dördüncütur0.append([name,score,colour])    

#3 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(dördüncütur3) % 2 == 0):   
    Group1, Group2 = dördüncütur3[:len(dördüncütur3) // 2], dördüncütur3[len(dördüncütur3) // 2:] 
else:        
    puan1_dışarıdakalan(dördüncütur3, dördüncütur25, dördüncütur2) 
    Group1, Group2 = dördüncütur3[:len(dördüncütur3) // 2], dördüncütur3[len(dördüncütur3) // 2:] 

renk_degis(Group1, Group2)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1,Group2)
Masalar1=(list(zipped))
#print("Group 1:",Masalar1)

#2.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(dördüncütur25) % 2 == 0):   
    Group11, Group22 = dördüncütur25[:len(dördüncütur25) // 2], dördüncütur25[len(dördüncütur25) // 2:] 
else:        
    puan1_dışarıdakalan(dördüncütur25, dördüncütur2, dördüncütur15) 
    Group11, Group22 = dördüncütur25[:len(dördüncütur25) // 2], dördüncütur25[len(dördüncütur25) // 2:] 

renk_degis(Group11, Group22)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group11,Group22)
Masalar2=(list(zipped))
#print("Group 2:",Masalar2)

#2 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(dördüncütur2) % 2 == 0):   
    Group111, Group222 = dördüncütur2[:len(dördüncütur2) // 2], dördüncütur2[len(dördüncütur2) // 2:] 
else:        
    puan1_dışarıdakalan(dördüncütur2, dördüncütur15, dördüncütur1) 
    Group111, Group222 = dördüncütur2[:len(dördüncütur2) // 2], dördüncütur2[len(dördüncütur2) // 2:] 

renk_degis(Group111, Group222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group111,Group222)
Masalar3=(list(zipped))
#print("Group 3:",Masalar3)     

#1.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(dördüncütur15) % 2 == 0):   
    Group1111, Group2222 = dördüncütur15[:len(dördüncütur15) // 2], dördüncütur15[len(dördüncütur15) // 2:] 
else:        
    puan1_dışarıdakalan(dördüncütur15, dördüncütur1, dördüncütur05) 
    Group1111, Group2222 = dördüncütur15[:len(dördüncütur15) // 2], dördüncütur15[len(dördüncütur15) // 2:] 

renk_degis(Group1111, Group2222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1111,Group2222)
Masalar4=(list(zipped))
#print("Group 4:",Masalar4)

#1 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(dördüncütur1) % 2 == 0):   
    Group11111, Group22222 = dördüncütur1[:len(dördüncütur1) // 2], dördüncütur1[len(dördüncütur1) // 2:] 
else:        
    puan1_dışarıdakalan(dördüncütur1, dördüncütur05, dördüncütur0) 
    Group11111, Group22222 = dördüncütur1[:len(dördüncütur1) // 2], dördüncütur1[len(dördüncütur1) // 2:] 

renk_degis(Group11111, Group22222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group11111,Group22222)
Masalar5=(list(zipped))
#print("Group 5:",Masalar5) 

skoralan=[] #boşta kalanların atıldığı liste
#0.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak  

if (len(dördüncütur05) % 2 == 0):   
    Group111111, Group222222 = dördüncütur05[:len(dördüncütur05) // 2], dördüncütur05[len(dördüncütur05) // 2:] 
else:        
    puan05_dışarıdakalan(dördüncütur05,dördüncütur0)  
    Group111111, Group222222 = dördüncütur05[:len(dördüncütur05) // 2], dördüncütur05[len(dördüncütur05) // 2:] 


renk_degis(Group111111, Group222222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group111111,Group222222)
Masalar6=(list(zipped))
#print("Group 6:",Masalar6)

#0 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak  
if (len(dördüncütur0) % 2 == 0):   
    Group1111111, Group2222222 = dördüncütur0[:len(dördüncütur0) // 2], dördüncütur0[len(dördüncütur0) // 2:] 
else:        
    puan0_dışarıdakalan(dördüncütur0)     
    Group1111111, Group2222222 = dördüncütur0[:len(dördüncütur0) // 2], dördüncütur0[len(dördüncütur0) // 2:] 


renk_degis(Group1111111, Group2222222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1111111,Group2222222)
Masalar7=(list(zipped))
#print("Group 7:",Masalar7)

print(f"\n\nMatch List(Fourth Round):\n\n\nGroup 1 : {Masalar1}\n\n\nGroup 2 : {Masalar2}\n\n\nGroup 3 : {Masalar3}\n\n\nGroup 4 : {Masalar4}\n\n\nGroup 5 : {Masalar5}\n\n\nGroup 6 : {Masalar6}\n\n\nGroup 7 : {Masalar7}")

#Dışarıda kalan oyuncu 1 puan alacağı için gerekli bilgileri yazdım.Bu şekilde daha sonra sıralamada kullanıcağım.
yerlesskor=[]
for line in skoralan:  
    name,score,colour=line[0],line[1],line[2]
    score += float(1)
    yerlesskor.append([name,score,colour]) 

masa_skor(Masalar1)  
masa_skor(Masalar2)
masa_skor(Masalar3)
masa_skor(Masalar4)
masa_skor(Masalar5)
masa_skor(Masalar6)
masa_skor(Masalar7)
#print(f"\nMasalar 1(Skor) : {Masalar1}\n\nMasalar 2(Skor) : {Masalar2}\n\nMasalar 3(Skor) : {Masalar3}\n\nMasalar 4(Skor) : {Masalar4}\n\nMasalar 5(Skor) : {Masalar5}\n\nMasalar 6(Skor) : {Masalar6}\n\nMasalar 7(Skor) : {Masalar7}\n\n")

Masalar12=(Masalar1+Masalar2+Masalar3+Masalar4+Masalar5+Masalar6+Masalar7)
Masalar12= [ item for i in Masalar12 for item in i]  

if (len(skoralan) >= 1):
    Masalar12.append(yerlesskor[0]) #Yukarıda oluşturduğum yerlesskor listesini kullanıyorum bu şekilde açıkta kalan oyuncuya ana listeye atıyorum.
    sort_d1(Masalar12)

elif (len(skoralan) == 0):
    sort_d1(Masalar12)
    
df4 = pd.DataFrame (Masalar12,columns = ["Full Name","Rating","Colour"])
print(f"{df4}\n\nThe fourth round of the competition is over.The results of the fourth round are given above.\nStart of the fifth round...\n")

#5.turun başlangıcında en fazla 4 puan olacağı için ,sırasıyla puan değerlerini içeren boş liste oluşturdum.
besincitur0, besincitur05, besincitur1, besincitur15, besincitur2, besincitur25, besincitur3, besincitur35, besincitur4=[],[],[],[],[],[],[],[],[]  

for line in Masalar12:
    name,score=line[0],line[1]
    colour=(random.choice(["Black","White"])) 
    if score==float(4):
        besincitur4.append([name,score,colour])
    elif score==float(3.5):
        besincitur35.append([name,score,colour])
    elif score==float(3):
        besincitur3.append([name,score,colour])
    elif score==float(2.5) :
        besincitur25.append([name,score,colour])
    elif score==float(1):
        besincitur2.append([name,score,colour])
    elif score==float(1.5):
        besincitur15.append([name,score,colour])
    elif score==float(1):
        besincitur1.append([name,score,colour])
    elif score==float(0.5):
        besincitur05.append([name,score,colour])
    elif score==float(0):
        besincitur0.append([name,score,colour])

#4 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(besincitur4) % 2 == 0):   
    Group1, Group2 = besincitur4[:len(besincitur4) // 2], besincitur4[len(besincitur4) // 2:] 
else:        
    puan1_dışarıdakalan(besincitur4, besincitur35, besincitur3) 
    Group1, Group2 = besincitur4[:len(besincitur4) // 2], besincitur4[len(besincitur4) // 2:] 

renk_degis(Group1, Group2)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1,Group2)
Masalar1=(list(zipped))
print("Group 1:",Masalar1)

#3.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(besincitur35) % 2 == 0):   
    Group11, Group22 = besincitur35[:len(besincitur35) // 2], besincitur35[len(besincitur35) // 2:] 
else:        
    puan1_dışarıdakalan(besincitur35, besincitur3, besincitur25) 
    Group11, Group22 = besincitur35[:len(besincitur35) // 2], besincitur35[len(besincitur35) // 2:] 

renk_degis(Group11, Group22)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group11,Group22)
Masalar2=(list(zipped))
print("Group 2:",Masalar2)

#3 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(besincitur3) % 2 == 0):   
    Group111, Group222 = besincitur3[:len(besincitur3) // 2], besincitur3[len(besincitur3) // 2:] 
else:        
    puan1_dışarıdakalan(besincitur3, besincitur25, besincitur2) 
    Group111, Group222 = besincitur3[:len(besincitur3) // 2], besincitur3[len(besincitur3) // 2:] 

renk_degis(Group111, Group222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group111,Group222)
Masalar3=(list(zipped))
print("Group 3:",Masalar3)

#2.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(besincitur25) % 2 == 0):   
    Group1111, Group2222 = besincitur25[:len(besincitur25) // 2], besincitur25[len(besincitur25) // 2:] 
else:        
    puan1_dışarıdakalan(besincitur25, besincitur2, besincitur15) 
    Group1111, Group2222 = besincitur25[:len(besincitur25) // 2], besincitur25[len(besincitur25) // 2:] 

renk_degis(Group1111, Group2222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1111,Group2222)
Masalar4=(list(zipped))
print("Group 4:",Masalar4)

#2 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(besincitur2) % 2 == 0):   
    Group11111, Group22222 = besincitur2[:len(besincitur2) // 2], besincitur2[len(besincitur2) // 2:] 
else:        
    puan1_dışarıdakalan(besincitur2, besincitur15, besincitur1) 
    Group11111, Group22222 = besincitur2[:len(besincitur2) // 2], besincitur2[len(besincitur2) // 2:] 

renk_degis(Group11111, Group22222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group11111,Group22222)
Masalar5=(list(zipped))
print("Group 5:",Masalar5)

#1.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(besincitur15) % 2 == 0):   
    Group111111, Group222222 = besincitur15[:len(besincitur15) // 2], besincitur15[len(besincitur15) // 2:] 
else:        
    puan1_dışarıdakalan(besincitur15, besincitur1, besincitur05) 
    Group111111, Group222222 = besincitur15[:len(besincitur15) // 2], besincitur15[len(besincitur15) // 2:] 

renk_degis(Group111111, Group222222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group111111,Group222222)
Masalar6=(list(zipped))
print("Group 6:",Masalar6)

#1 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak
if (len(besincitur1) % 2 == 0):   
    Group1111111, Group2222222 = besincitur1[:len(besincitur1) // 2], besincitur1[len(besincitur1) // 2:] 
else:        
    puan1_dışarıdakalan(besincitur1, besincitur05, besincitur0) 
    Group1111111, Group2222222 = besincitur1[:len(besincitur1) // 2], besincitur1[len(besincitur1) // 2:] 

renk_degis(Group1111111, Group2222222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group1111111,Group2222222)
Masalar7=(list(zipped))
print("Group 7:",Masalar7)

skoralan=[] #boşta kalanların atıldığı liste
#0.5 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak  

if (len(besincitur05) % 2 == 0):   
    Group11111111, Group22222222 = besincitur05[:len(besincitur05) // 2], besincitur05[len(besincitur05) // 2:] 
else:        
    puan05_dışarıdakalan(besincitur05,besincitur0)  
    Group11111111, Group22222222 = besincitur05[:len(besincitur05) // 2], besincitur05[len(besincitur05) // 2:] 


renk_degis(Group11111111, Group22222222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group11111111,Group22222222)
Masalar8=(list(zipped))
#print("Group 8:",Masalar8)

#0 puan alanlar eğer dışarıda kalırlarsa 1 alt gruba atılacak onun en yüksek skorlusuyla yarışacak  
if (len(besincitur0) % 2 == 0):   
    Group111111111, Group222222222= besincitur0[:len(besincitur0) // 2], besincitur0[len(besincitur0) // 2:] 
else:        
    puan0_dışarıdakalan(besincitur0)     
    Group111111111, Group222222222 = besincitur0[:len(besincitur0) // 2], besincitur0[len(besincitur0) // 2:] 


renk_degis(Group111111111, Group222222222)  #Eğer aynı renk gelirse karşı rakiple ikinci oyuncunu rengi değiştirmekte.

zipped = zip(Group111111111,Group222222222)
Masalar9=(list(zipped))
#print("Group 9:",Masalar9)

print(f"\n\nMatch List(Fifth Round):\n\n\nGroup 1 : {Masalar1}\n\n\nGroup 2 : {Masalar2}\n\n\nGroup 3 : {Masalar3}\n\n\nGroup 4 : {Masalar4}\n\n\nGroup 5 : {Masalar5}\n\n\nGroup 6 : {Masalar6}\n\n\nGroup 7 : {Masalar7}\n\n\nGroup 8 : {Masalar8}\n\n\nGroup 9 : {Masalar9}")

#Dışarıda kalan oyuncu 1 puan alacağı için gerekli bilgileri yazdım.Bu şekilde daha sonra sıralamada kullanıcağım.
yerlesskor=[]
for line in skoralan:  
    name,score,colour=line[0],line[1],line[2]
    score += float(1)
    yerlesskor.append([name,score,colour]) 

masa_skor(Masalar1)  
masa_skor(Masalar2)
masa_skor(Masalar3)
masa_skor(Masalar4)
masa_skor(Masalar5)
masa_skor(Masalar6)
masa_skor(Masalar7)
masa_skor(Masalar8)
masa_skor(Masalar9)
#print(f"\nMasalar 1(Skor) : {Masalar1}\n\nMasalar 2(Skor) : {Masalar2}\n\nMasalar 3(Skor) : {Masalar3}\n\nMasalar 4(Skor) : {Masalar4}\n\nMasalar 5(Skor) : {Masalar5}\n\nMasalar 6(Skor) : {Masalar6}\n\nMasalar 7(Skor) : {Masalar7}\n\nMasalar 8(Skor) : {Masalar8}\n\nMasalar 9(Skor) : {Masalar9}\n\n"")

Masalar12=(Masalar1+Masalar2+Masalar3+Masalar4+Masalar5+Masalar6+Masalar7+Masalar8+Masalar9)
Masalar12= [ item for i in Masalar12 for item in i]  

if (len(skoralan) >= 1):
    Masalar12.append(yerlesskor[0]) #Yukarıda oluşturduğum yerlesskor listesini kullanıyorum bu şekilde açıkta kalan oyuncuya ana listeye atıyorum.
    sort_d1(Masalar12)

elif (len(skoralan) == 0):
    sort_d1(Masalar12)
    
df5 = pd.DataFrame (Masalar12,columns = ["Full Name","Rating","Colour"])
print(f"{df5}\n\nThe fifth round of the competition is over.The results of the fifth round are given above.\nCongratulations {Masalar12[0][0]} you have won the Tournament ...\n")
