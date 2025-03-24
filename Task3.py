s=input()
a=0
lst = list(map(int, s.split()))
lst.sort(reverse=True)
for i in range(len(lst)-2):
    if lst[i]<lst[i+1]+lst[i+2]:
        a+=1
        print(f'{lst[i+2]}, {lst[i+1]}, {lst[i]}')
        break
if a==0: print(-1)