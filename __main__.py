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
        collect.crawling(**item)
        resultfile=collect.crawling(**item,fetch=False)
        item['resultfile']=resultfile
        #item['resultfile']=resultfile
    #collect.crawling(
    ##    'jtbcnews',
     #   '2017-01-01',
     #   '2017-12-31'
    #)
    #데이터 분석(analyze)
    for item in items:
        data=analyze.json_to_str(item['resultfile'], 'message')
        print(data)
        #item['count_word_freq']=analyze.count_wordfreq(data)

    #데이터 시각화(visualize)

print('run analysis_fb...')

