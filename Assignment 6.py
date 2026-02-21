"تکه برنامه ای بنویسید که دارای تابع پیچیدگی زمانی زیر باشد"
n=8
#F(n) = 1.3 n**2 + 6 n + 2
#      4/3 n**2 + 6 n + 2
a=b=c=d=e=f=g=h=1
for i in range(n):
    for j in range(0,n,3):
        a=b
        b=c
        c=d
        d=e

    e=f 
    f=g
    g=h
    h=a
    a=c
    b=d

c=e
d=f   
print(a,b,c,d,e,f,g,h)

#هر کدوم از نقطه چین ها یک دستور هستند
#for i in range(0,n,3):
#    for i in range(-1,n,3):
#         ...
#         ...
#    ...
#    ...
#    ...
#    ...

#F(n) = 1/3 (n-0) * (n+1) * 2 + 4/3 n 
#     = 2/9 n**2 + 14/9 n       
# ***مثال دانشجو بود***  
      
            
              