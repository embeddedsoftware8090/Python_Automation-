import  re
conut = 0
pattern =re.compile("ab")
matcher =pattern.finditer("abaababa")
for i in matcher:
    conut+=1
    print(i.start(),"...",i.end(),"..",i.group())
print("The number of occurences:",conut)