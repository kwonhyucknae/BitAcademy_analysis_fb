import json
import re
#분석을 위한 전처리


#[a-zA-Z1-9]+ 1부터 Z까지 하나의 문자열?

def json_to_str(filename,key):
    jsonfile = open(filename,'r',encoding='utf-8')
    json_string=jsonfile.read()

    jsonfile.close()
    #객체기 때문에 리스트가 표시
    data=''

    json_data=json.loads(json_string)


    for item in json_data:
        value=item.get(key)
        if value is None:
            continue

        data+=re.sub('[^\w]]','',value)

    return data

    print(json_data)
