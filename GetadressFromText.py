
#Turhan ÇETİN(2018123047)#
#İsmail IŞIK(2018123037)#

import re



dosya = open("emailler_ve_urller.txt")

def email(line):
    email = re.findall('\S+@\S+com', line) 
    if email != []:
        print("Email" , email)
        

def edu(line):
    edu = re.findall('\S+@\S+edu.tr', line) 
    if edu != []:
        print("Edu" , edu)
        
    

def bonus(line):
    bonus = re.findall('\S+@\S+com|\S+@\S+edu.tr', line)
    if bonus != []:
        print("Bonus" ,bonus)
        
   

def www(line):
    www = re.findall("w{3}\S+",line)
    if www != []:
        print("WWW",www)
        

def avesis(line):
    avesis = re.findall("avesis\S+",line)
    if avesis != []:
        print("AVESİS",avesis)
    


for line in dosya:#düzenli ifadeler yardımıyla aldığımız email,www,edu.tr,avesisve bonusları sıralı yazılması karışıklılığın ortadan kalkması için her fonksiyon için dosyayı ayrı ayrı tekrardan açarak fonksiyonların içine gönderdik#
    email(line)

dosya = open("emailler_ve_urller.txt")
for line in dosya :
    edu(line)

dosya = open("emailler_ve_urller.txt")
for line in dosya :
    bonus(line)
    

dosya = open("emailler_ve_urller.txt")
for line in dosya :
    www(line)
    
dosya = open("emailler_ve_urller.txt")
for line in dosya :
    avesis(line)
    

    















    
    
