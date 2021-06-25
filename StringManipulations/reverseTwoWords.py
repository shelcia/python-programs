# REVERSE TWO WORDS
N = str(input(""))
str0 = ""
str1 = ""
breakIndex = 0
for i in range(0, len(N)):
    if(N[i] != ' '):
        str0 = str0+N[i]
        breakIndex = i
    else:
        break
for j in range(breakIndex+2, len(N)):
    str1 = str1+N[j]
# print(str0)
# print(str1)
# print(breakIndex)
print(str1, str0)
