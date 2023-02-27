a = input()
b = input()

str1 = a.split(':')
str2 = b.split(':')

h1 = int(str1[0])
m1 = int(str1[1])

h2 = int(str2[0])
m2 = int(str2[1])


sum = 0
if(h2-h1==1):
    if(m1>m2):
        m2+=60
        sum+=m2-m1
    else:
        sum+=m2-m1
else:
    if(h1>h2):
        h2+=24
        sum+=h2-h1
    else:
        sum+=m2-m1
    if(m1>m2):
            m2+=60
            sum+=m2-m1
    else:
        sum+=m2-m1




print(sum)