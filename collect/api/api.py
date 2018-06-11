#FaceBook API Wrapper Functions
from urllib.parse import urlencode
from .web_request import json_request

ACCESS_TOKEN="EAACEdEose0cBAIGaj4s1l7GsC8I0r3M9W5x80jlSFVyBYt5USDjIJop7ZAICZBo6MWUmWx2BJzqC3eJirb8Bp3riTHKtZBRIk0EEyJDe8J3brVyIoygjjKXZAayktZAGcx1tqHt9nvyZCEohPIXzjdZAMmZBjNBdLJmdOX5gFcQZBHwoKuAk7EJv5A3soFM7BXCcEHHG7ZAmjQVgZDZD"
BASE_URL_FB_API= "https://graph.facebook.com/v3.0"


# params dictionary 형태로 들어온다
#params{"since":20173221, "until":2018dwqdwq}


def fb_gen_url(base=BASE_URL_FB_API,
               node='',
               **params):
    url='%s/%s/?%s' % (base,node,urlencode(params))
    return url


def fb_name_to_id(pagename):
    url=fb_gen_url(node=pagename,access_token=ACCESS_TOKEN)

    json_result=json_request(url=url)
    return json_result.get("id")



def fb_fetch_posts(pagename,since,until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename) + "/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN
    )

    print("url======"+url)
    json_result = json_request(url=url)
    print(json_result)
    return json_result

