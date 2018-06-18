import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import numpy as np
from numpy.random import randn


def ex1():
    # plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
    plt.plot([10, 20, 30, 40])
    plt.show()


def ex2():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 1, 1)
    sp1.plot([1, 2, 3, 4], [10, 20, 30, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [100, 200, 300, 400])

    plt.show()


def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(1000), bins=20, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * randn(100))


    plt.show()


def ex4():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot([10, 20, 30, 40])
    plt.show()


def ex5():
    fig, subplots=plt.subplots(2,3,sharex=True,sharey=True)
    for i in range(2):
        for j in range(2):
            subplots[i,j].hist(randn(100),bins=20,color='k')

    plt.subplots_adjust(wspace=0,hspace=0)

    plt.show()

def ex6():
    fig,subplots=plt.subplots(1,1)
    subplots.plot([10,20,30,40],[10,20,30,40],'go--')
    plt.show()


def ex7():
    fig,subplots=plt.subplots(1,1)
    subplots.plot([10,20,30,40],[10,20,30,40],'go--',color='g',linestyle='--',marker='o')

    plt.show()

#marker = . 일때, v 일때 화살표 , color 에는 # 값등 넣을수 있음 , linestyle = solid, -- 등 가능


def ex8():
    fig,subplots=plt.subplots(1,1)
    subplots.plot([10,20,30,40],[10,20,30,40],'go--',color='#335599',linestyle='solid',marker='v')

    plt.show()

#같은데이터 그림 2개 그리기
#randn() =
def ex9():
    fig,subplots=plt.subplots(1,1)
    #subplots.plot([10,20,30,40],[10,20,30,40],'go--',color='#335599',linestyle='solid',marker='v')
    data=randn(50).cumsum()
    subplots.plot(data,color='black',linestyle='dashed',label='AAA')
    #AAA 그래프
    subplots.plot(data,color='blue',drawstyle='steps-mid',label='BBB')
    #BBB 그래프 계단형

    #best 그래프 그리기 좋은곳 창 크기 달라졌을때 가장 best 한곳에 위치 됨 그래프가
    plt.legend(loc='best')
    plt.show()


#xticks는 스케일과 연관

def ex10():
    fig,subplots=plt.subplots(1,1)
    subplots.plot(randn(50).cumsum())
    subplots.set_xticks([0,100,200,300,400,500,600,700,800,900])
    plt.show()

#xtickslabels 과의 차이?

def ex11():
    fig,subplots=plt.subplots(1,1)

    #스케일과 관련된놈
    subplots.plot(randn(1000).cumsum())
    subplots.set_xticks([0,100,200,300,400,500,600,700,800,900])



    subplots.set_xticklabels(['pt0','pt1','pt2','pt3','pt4','pt5','pt6','pt7','pt8','pt9'],
                             rotation=30,
                             fontsize='small'
                             )
    subplots.set_xlabel('Points')
    subplots.set_title('Matplotlib Test')

    plt.show()


def ex12():
    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='one')
    subplots.plot(randn(1000).cumsum(), 'k-.', label='two')
    subplots.plot(randn(1000).cumsum(), 'k.', label='three')

    plt.legend(loc='best')
    plt.show()


#한글 깨짐

def ex13():
    #폰트 알아내기?
    #font_filename = 'c:/Windows/fonts/malgun.ttf'
    #font_name = font_manager.FontProperties(fname=font_filename).get_name()
    #print(font_name)

    #폰트 사용? 이거 넣은 후에 한글 제대로 나옴
    font_options = {'family': 'Malgun Gothic'}
    plt.rc('font', **font_options)
    plt.rc('axes', unicode_minus=False)

    fig, subplots = plt.subplots(1, 1)

    subplots.plot(randn(1000).cumsum(), 'k', label='기본')
    subplots.plot(randn(1000).cumsum(), 'k--', label='대시')
    subplots.plot(randn(1000).cumsum(), 'k.', label='점')

    subplots.set_xticklabels(
        ['pt0', 'pt1', 'pt2', 'pt3', 'pt4', 'pt5', 'pt6', 'pt7', 'pt8', 'pt9', 'pt10'],
        rotation=30,
        fontsize='small')
    subplots.set_xlabel('포인트')
    subplots.set_title('예제12 한글처리')
    plt.legend(loc='best')

    plt.show()


if __name__ == '__main__':
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    #ex5()
    #ex6()
    #ex7()
    #ex8()
    #ex9()
    #ex10()
    #ex11()
    #ex12()
    ex13()