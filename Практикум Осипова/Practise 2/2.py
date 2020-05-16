import matplotlib.pyplot as plt
import math
def dots_graph():
    data=[]
    x=-8
    while x<=x_1:
        y=(x/4-1)**3
        data.append([x,y])
        x+=h
    x-=h
    if x - 1 != (x/4-1)**3:
        data.append([x,(x/4-1)**3])
        x += h
    else:
        x+=h
    while x<=x_2:
        data.append([x, x - 1])
        x += h
    x -= h
    if x-1!=2*abs(x+7)**0.5:
        data.append([x, 2 * (abs(x + 7)) ** 0.5])
        x += h
    else:
        x += h
    while x<=x_max:
        data.append([x,2*(abs(x+7))**0.5])
        x += h
    return data
def display():
    plt.plot(list_x,list_y)
    plt.plot(data_trend_1_x, data_trend_1_y)
    #plt.plot(data_trend_2_x, data_trend_2_y)
    plt.show()
def answer(x):
    if x_min<=x<=x_1:
        y=(x/4-1)**3
        check=1
    elif x_1<=x<=x_2:
        y = x - 1
        check=1
    elif x_2<=x<=x_max:
        check=1
        y=2 * (abs(x + 7)) ** 0.5
    else:
        return 'Не в области определения'
    if check==1:
        return y

def line_trend():
    global x_middle
    global y_middle
    global nakl
    global ugl
    a_up=0
    a_down=0
    x=-8
    summ=0
    n=0
    while x<=16:
        summ+=x
        n+=1
        x+=0.25
    x_middle=summ/n
    x=-8
    summ=0
    while x<=16:
        summ+=answer(x)
        n+=1
        x+=0.25
    y_middle=summ/n
    x=-8
    while x<=16:
        a_up+=(x-x_middle)*(answer(x)-y_middle)
        x+=0.25
    x=-8
    while x <= 16:
        a_down += (x - x_middle)**2
        x +=0.25
    a=a_up/a_down
    b=y_middle-a*x_middle
    x=-8
    data_trend_1_x=[]
    data_trend_1_y=[]
    while x<=16:
        data_trend_1_x.append(x)
        data_trend_1_y.append(a*x+b)
        x+=0.25
    x = -8
    data_trend_2_y = []
    data_trend_2_x = []
    while x <= 16:
        data_trend_2_x.append(x)
        if x == 0:
            data_trend_2_y.append(a*1**b)
        else:
            data_trend_2_y.append(a * x ** b)
        x += 0.25
    nakl=a
    ugl=b
    return  data_trend_1_x,data_trend_1_y,data_trend_2_x,data_trend_2_y
def mat_wait():
    x = -8
    a = 0
    while x <= 16:
        a += x * answer(x)
        x += h
    print('Математическое ожидание =', a)
def sredn_otkl():
    x=-8
    a_up=0
    while x<=16:
        a_up+=(x-x_middle)**2
        x+=h
    return(math.sqrt(a_up/len(data)-1))

def table():
    for i in data:
        print(f'При х = {i[0]}, y = {i[1]}')

def det():
    x=-8
    a=0
    b=0
    while x<=16:
        a+=((nakl*x+ugl)-y_middle)**2
        b+=(answer(x)-y_middle)**2
        x+=h
    print('коэффициент детерминации = ',a/b)



x_min=-8
x_max=16
x_1=0.00
x_2=9.00
h=0.25
data=dots_graph()
print(len(data))
args = ([y for y in x] for x in data)
list_x, list_y = zip(*args)
data_trend_1_x,data_trend_1_y,data_trend_2_x,data_trend_2_y=line_trend()
table()
print('Cреднеквадратическое отклонение =',sredn_otkl())
mat_wait()
det()
display()
