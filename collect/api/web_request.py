
import sys
from urllib.request import Request , urlopen
from datetime import *
import json

def print_html(html):
    print(html)

def print_error(e):
    print('%s %s' % (e, datetime.now()), file=sys.stderr)


#람브다 익명 함수  error=lambda e:print('%s %s' % (e, datetime.now()), file=sys.stderr) 에러 부분을 람브다로 할 수 있음
def html_request(url='',encoding='utf-8',success=None,error=lambda e:print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        # 클래스다 리퀘스트 객체 생성
        # 요청하는 객체 생성
        request = Request(url)
        resp = urlopen(request)
        # 데이터는 동영상 , 이미지 전부 바이트
        #
        html = resp.read().decode("utf-8")
        #print(html)

        print('%s: success for request[%s]' %(datetime.now(),url))


        if callable(success) is False:
            return html

        success(html)

    except Exception as e:
        if callable(error) is True:
            error(e)

#html_request(url='http://www.naver.com')

#html_request(url='http://www.naver.com',success=print_html)


def json_request(url='',encoding='utf-8',success=None,error=lambda e:print('%s %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        # 클래스다 리퀘스트 객체 생성
        # 요청하는 객체 생성
        request = Request(url)
        resp = urlopen(request)
        # 데이터는 동영상 , 이미지 전부 바이트
        #

        resp_body = resp.read().decode("utf-8")
        # print(html)
        json_result = json.loads(resp_body)
        data = json_result['data']
        print(type(data), ":", data)

        print('%s: success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return resp_body

        success(resp_body)

    except Exception as e:
        if callable(error) is True:
            error(e)



json_request(url='http://kickscar.cafe24.com:8080/myapp-api/api/user/list')

