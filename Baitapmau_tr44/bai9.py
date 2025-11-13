a,b,c=eval(input('Nhập vào 3 số cách nhau bởi dấu phẩy: '))
if (a>b):
    if( a>c):
        if(b>c):
          print(c,b,a)
        else:
         print(b,c,a)
    else:
        print(b,a,c)
else:
    if(b>c):
        if(a>c):
            print(a,a,b)
        else:
            print(a,c,b)
    else:
        print(a,b,c)
