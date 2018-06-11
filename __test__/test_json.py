# test json

import sys
from urllib.request import Request , urlopen
from datetime import *
import json

try:
    url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
#클래스다 리퀘스트 객체 생성
#요청하는 객체 생성
    request=Request(url)
    resp=urlopen(request)
#데이터는 동영상 , 이미지 전부 바이트
    resp_body=resp.read().decode("utf-8")
    print(type(resp_body)," : ",resp_body)
# 파이썬 json 라이브러리를 통해 파싱
    json_result=json.loads(resp_body)
    print(type(json_result), ":", json_result)
#화면은 똑같지만 타입 다르다 . json 객체로 바꿔서 다루기 쉽게 해준다
    data=json_result['data']
    print(type(data),":",data)
    
    
    #print(json)
except Exception as e:
    print('%s %s' % (e, datetime.now()) , file=sys.stderr)

