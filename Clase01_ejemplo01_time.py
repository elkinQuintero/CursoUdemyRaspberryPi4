import time

t1 = time.time()
t2 = time.time()
while True:
    if (t2-t1)<1:
        t2=time.time()
        
    else:
        t1=time.time()
        print("ya paso 1 segundo")
        

