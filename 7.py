print('Введите первую сторону')
try:
    x = int(input())
    if x<=0:
        print('ошибка')
except ValueError:
        print('ошибка')
else:
        if x>0:
            print('Введите вторую сторону')
        
            try:
                y = int(input())
                if y<=0:
                    print('ошибка')
            except ValueError:
                    print('ошибка')
            else:
                if y>0:
            
       
                    print('Введите третью сторону')
                
                    try:
                        z = int(input())
                        if z<=0:
                            print('ошибка')
                    except ValueError:
                            print('ошибка')
                    else:
                        if z>0:
                  


                            t= "False"
                            if (x<z+y) and (y<x+z) and (z<y+x) :
                                print ('Suchestvuet')
                                t= "True"
                            else:
                                print ('Ne suchestvuet')
                            if t=="True":
                                if (x**2==z**2+y**2) or (y**2==z**2+x**2) or (z**2==x**2+y**2):
                                    print ('Treugolnik pryamougolnuy')
                                else:
                                    print('Treugolnik nepryamougolnuy')
                  
                
    

