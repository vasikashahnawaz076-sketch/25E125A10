s="Data privacy is quite important"
count=0
for i in s:
    if i in "aeiou":
        count+=1
print("Number of vowel characters:", count)

s="Data privacy is quite important"
count=0
for i in s:
    if i in "aeiou":
        count+=1
print("Number of vowel characters:", count)

s="Data privacy is quite important"
count=0
ecount=0
for i in s:
    if i in "e":
        ecount+=1
print("Number of 'e' characters:", ecount)

s="Data privacy is quite important"
count=0
acount=0
for i in s:
    if i in "a":
        acount+=1
print("Number of 'a' characters:", acount)

s="Data privacy is quite important"
count=0
ocount=0
for i in s:
    if i in "o":
        ocount+=1
print("Number of 'o' characters:", ocount)

s="Data privacy is quite important"
count=0
ucount=0
for i in s:
    if i in "u":
        ucount+=1
print("Number of 'u' characters:", ucount)

v="aeiou"
for i in v:
    count=0
    for j in s:
        if i==j:
            count+=1
    print("Number of",i,"characters:",count)