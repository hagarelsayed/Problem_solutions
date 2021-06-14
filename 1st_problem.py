
n,h =map(int,input().split())   # first input
a=list(map(int,input().split())) # second input


width = 0
for i in a:             # take care this is L not (len(L)) nor (range(L))
  if i <h or i ==h:     # take care it is "i" for the value not (L[i])
    width = width + 1
  else:
    width = width + 2
print(width)




