sum=0
n=str(input())
for i in range(len(n)):#len関数は文字列じゃないとダメだからstr型でinput
    i+=n[i]
print(sum)

