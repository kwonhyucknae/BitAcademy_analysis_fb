import os
import pytagcloud

import collections
#matplot을 plt로 쓴다
import matplotlib.pyplot as plt

RESULT_DIRECTORY = "__result__/visualization"
#result 뒤에 s 하나 더 붙였다가 계속 오류 났엇음


def wordcloud(filename, wordfreq):
    taglist = pytagcloud.make_tags(wordfreq.items(), maxsize=80)
    # print(taglist)
    save_filename = '%s/wordcloud_%s.jpg' % (RESULT_DIRECTORY, filename)
    pytagcloud.create_tag_image(
        taglist,
        save_filename,
        size=(900, 600),
        fontname='Malgun',
        rectangular=False,
        background=(0, 0, 0))


#바 그래프 그릴때 이 함수만 사용하면 된다

def graph_bar(title=None,xlabel=None,ylabel=None,
              showgrid=False,values=None,ticks=None,filename=None,
              showgraph=True
              ):
    #그래프 그리기?
    fig, subplots = plt.subplots(1,1)
    subplots.bar(range(len(values)),values,align='center')

    # show grid , True로 주면 그리고 False 로 주면 안그림
    #격자 생성??
    subplots.grid(showgrid)


    #파일네임이 None이 아니고 string 이어야한다
    #파일로 그래프바 저장하기
    if filename is not None and isinstance(filename,str):
        save_filename =  '%s/bar_%s.png' % (RESULT_DIRECTORY,filename)
        plt.savefig(save_filename,dpi=400,bbox_inches='tight')


    #ticks 카운트 수 셀때 썻던 collections
    if ticks is not None and isinstance(ticks ,collections.Sequence):
        #
        subplots.set_xticks(range(len(ticks)))
        #라벨링?
        subplots.set_xticklabels(ticks)

    #show graph 그릴거냐 말거냐 , 어떤 기능인지 잘 모르겟음

    if showgraph:
        plt.show()



if os.path.exists(RESULT_DIRECTORY) is False:
    print("test")
    os.mkdir(RESULT_DIRECTORY)