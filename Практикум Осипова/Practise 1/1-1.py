def kalc(k,z,r,x,i,summ):
    k=k*(-1)
    z=z*x**2
    r=(2*i+1)
    t=k/(r*z)
    summ+=t
    print(k)
    print(z)
    print(r)
    print(t)
    return k,z,r,summ

def main():
    x=int(input("Введите x"))
    n=int(input('Введите количество элементов для нахождения суммы'))
    summ=1
    z=x
    r=1
    k=-1
    for i in range(1,n):
        k,z,r,summ=kalc(k,z,r,x,i,summ)
    print('pi/2 + (',summ,')')
main()