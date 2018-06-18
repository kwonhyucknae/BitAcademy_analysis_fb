import collect
import analyze
import visualize


if __name__=='__main__':
    items = [
        {'pagename':'jtbcnews','since':'2017-01-01','until':'2017-12-31'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}

    ]

    #데이터 수집 (collection)
    for item in items:
        resultfile = collect.crawling(**item, fetch=False)
        item['resultfile'] = resultfile
        #item['resultfile']=resultfile


    #데이터 분석(analyze)

    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)

        print(item['count_wordfreq'])
        #item['count_word_freq']=analyze.count_wordfreq(data)

    #데이터 시각화(visualize)
    for item in items:
        count= item['count_wordfreq']
        count_m50=dict(count.most_common(50))

        filename="%s_%s_%s" %(item['pagename'],item['since'],item['until'])
        visualize.wordcloud(filename,count_m50)

        # 6주차 그래프를 파일로 저장
        #count_m50 =
        # {"뉴스룸"=120,
        #"앵커":50,
        # } 식으로 되어있음 여기서 120,50 등을 y로 쓰겟다.
        # ticks = 뉴스룸, 앵커 등을 쓰고
        visualize.graph_bar(
            title='%s 빈도 분석' % (item['pagename']),
            xlabel='단어',
            ylabel='빈도',
            values=list(count_m50.values()),
            #ticks 그래프의 x 축의 값들의 문자?
            ticks=list(count_m50.keys()),
            #그리드는 격자를 그릴거냐 말거냐 옵션
            showgrid=False,
            filename=filename,
            showgraph=False
        )
        #filename 이 있고 showgraph false 이므로 저장된다
print('run analysis_fb...')

