x,y,z = map(int,input().split())
a=0
if x==1:
    a+=1
if y==1:
    a+=1
if z==1:
    a+=1
print(a)

#これだと1 0 1とかはいいけど空白の無い101とかはできない