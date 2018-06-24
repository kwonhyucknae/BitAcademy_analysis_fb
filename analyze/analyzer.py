import json
import re
from konlpy.tag import Twitter
from collections import Counter

'''
형태소 분석
- 어떤 대상 어절의 모든 가능한 분석 결과 추출
- 문장의 주요 단어 추출

예) 논밭-> 논+밭,논밭
-----konlpy 패키지 사용
'''


#수집된 포스트 데이터에서 단어 추출 및 빈도 카운팅

def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    jsonfile.close()

    data = ''
    json_data = json.loads(json_string)
    for item in json_data:
        value = item.get(key)
        if value is None:
            continue

        data += re.sub(r'[^\w]', '', value)

    return data

#입력 받은 문자열에서 단어를 추출하고 빈도수를 세서 dict 타입으로 리턴
def count_wordfreq(data):
    twitter = Twitter()
    nouns = twitter.nouns(data)

    count = Counter(nouns)
    return count
