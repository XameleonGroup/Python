import math
def kalc(z,r,x,i,summ):
    z=z*x**2
    r=r*(2*i+1)*2*i
    t=z/r
    summ+=t
    print('-------------------------------------------')
    return z,r,summ,t

def main():
    x=int(input("Введите x"))
    summ=x
    t=x
    z=x
    r=1
    j=1
    check=input('Выберете e:\n1 - e = 10^(-3)\n2 - e = 10^(-5)\n')
    if check=='1':
        e=10**(-3)
    elif check=='2':
        e=10**(-5)
    while abs(t)>e:
       z,r,summ,t=kalc(z,r,x,j,summ)
       print(j)
       print(t)
       print(e)
       print(summ)
       j+=1
    print(summ)
    print('&&&',math.sinh(x))
main()