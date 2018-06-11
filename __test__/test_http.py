#http test

import sys
from urllib.request import Request , urlopen
from datetime import *

try:
    url='http://www.naverwqeqwe.com'
#클래스다 리퀘스트 객체 생성
#요청하는 객체 생성
    request=Request(url)
    resp=urlopen(request)

#데이터는 동영상 , 이미지 전부 바이트
#
    resp_body=resp.read().decode("utf-8")
    print(resp_body)
except Exception as e:
    print('%s %s' % (e, datetime.now()) , file=sys.stderr)



'''



'''




