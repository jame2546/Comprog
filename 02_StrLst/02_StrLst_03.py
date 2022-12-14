months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
a,b,c = input().split("/")
a = str(a)
b = int(b)
c = str(c)
print(months[b-1]+' '+a+', '+c)