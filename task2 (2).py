a = 4*25*50*100
mb = a/1024**2
c = 1
while mb <= 1.44:
    mb+=mb
    c+=1
print("Количество книг, помещающихся на дискету:", c)
