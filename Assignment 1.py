"تابع پیچیدگی زمانی الگوریتم زیر را محاسبه کنید"
a = 10
n = 5
t = 0
l = 1
p = 0
for i in range (n):
    p=t
    t=l+6
l = 2 + l
print(a, p, t, l)
#F(n) = 2 n + 2