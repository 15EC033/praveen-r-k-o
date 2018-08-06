a=12345
check= 123466
n=str(a)
m=str(check)
for i in n:
  count = m.count(i)
  if (count>1):
   print (i,count)
