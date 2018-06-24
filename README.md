# Facebook_analysis_fb
Facebook API analysis

페이스북의 포스트를 수집후

전처리 과정을 통해 원하는 데이터를 얻은 후 

형태소 분석을 통해 단어의 빈도 수를 센 후

시각화 시켜주는 프로젝트

사용 라이브러리 :konlypy , matplotlib ,jpype1 , pygame , pytagcloud


# 결과물

![capture1](https://user-images.githubusercontent.com/18182656/41819964-fbb2f3d8-7804-11e8-97ea-5c83996d7d33.JPG)


![capture2](https://user-images.githubusercontent.com/18182656/41819983-23d2b70e-7805-11e8-8370-37a457856b85.JPG)




# 개발 환경 설정 방법
(windows)

python 설치

pycharm IDE 사용

개발 및 디버깅을 위한 환경 설정

virtualenv

File -> Project Interpreter -> Show all -> Python 설치 위치 등록

라이브러리 설정

File -> settings -> Project Interpreter -> + 버튼 클릭 (패키지 추가)


<li>(한글 형태소 분석 오픈소스) konlypy 패키지 인스톨</li>

<li>jpype1 패키지</li> 

<li>(시각화) matplotlib 패키지 인스톨</li>

<li>pygame 설치</li>

<li>pytagcloud 설치</li>


pytagcloud 한글처리

   1) python 설치 디렉토리/Lib/site-packages/pytagcloud/fonts
   
      에 한글 폰트 복사(malgun.ttf)
      
   2) python 설치 디렉토리/Lib/site-packages/pytagcloud/fonts/font.json 수정

<pre><code>
	{
        "name": "Malgun",
        
        "ttf": "malgun.ttf",
        
        "web": "http://fonts.googleapis.com/css?family=Malgun"
        
    }
</pre></code>

    추가
    
# 코드 사용 예제

원하는 데이터 설정

<pre><code>
    items = [
        {'pagename':'jtbcnews','since':'2017-01-01','until':'2017-12-31'},
        {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}
    ]
</pre></code>


데이터 수집(collection)

<pre><code>
 for item in items:
        resultfile = collect.crawling(**item, fetch=True)
        item['resultfile'] = resultfile
</pre></code>


데이터 분석(analyze)

<pre><code>
    for item in items:
        data = analyze.json_to_str(item['resultfile'], 'message')
        item['count_wordfreq'] = analyze.count_wordfreq(data)

        print(item['count_wordfreq'])
	
</pre></code>

<pre><code>
데이터 시각화(visualize)
    for item in items:
        count= item['count_wordfreq']
        count_m50=dict(count.most_common(50))

        filename="%s_%s_%s" %(item['pagename'],item['since'],item['until'])
	
        visualize.wordcloud(filename,count_m50)
	
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
</pre></code>


# 라이센스


# 주의

파이썬이 32비트 jdk가 62비트 일 경우 konlypy 패키지 사용시 에러 발생 
