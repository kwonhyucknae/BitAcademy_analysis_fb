#FaceBook API Wrapper Functions
from urllib.parse import urlencode


BASE_URL_FB_API= "https://graph.facebook.com/v3.0"


# params dictionary 형태로 들어온다
#params{"since":20173221, "until":2018dwqdwq}


def fb_gen_url(base=BASE_URL_FB_API,
               node='',
               **params):
    url='%s/%s/posts/?%s' % (base,node,urlencode(params));
    return url
