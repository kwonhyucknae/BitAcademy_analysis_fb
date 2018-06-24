# BitAcademy_analysis_fb
Facebook API analysis

사용 라이브러리 :konlypy , matplotlib


수집


분석 


시각화

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


	{
        "name": "Malgun",
        
        "ttf": "malgun.ttf",
        
        "web": "http://fonts.googleapis.com/css?family=Malgun"
        
    }


    추가


# 주의
