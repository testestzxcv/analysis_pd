# PD API Wrapper Functions
from datetime import datetime
from urllib.parse import urlencode
from .web_request import json_request


SERVICE_KEY = '6m9Oq%2F9j8cIEp6w%2F3PmNrbAS1P17y24uk3Q2xloOH0WyDrSXbGHGpnF3Pf%2Bob8J6AW2k2HO%2BygzGcjrnyKNgog%3D%3D'


def pd_gen_url(endpoint, **param):
    url = '%s?%s&serviceKey=%s' % (endpoint, urlencode(param), SERVICE_KEY)
    return url

def pd_fetch_foreign_visitor(country_code, year, month):
    endpoint = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    url = pd_gen_url(
        endpoint,
        YM='{0:04d}{1:02d}'.format(year, month),
        NAT_CD=country_code,
        ED_CD='E',
        _type='json')
    json_result = json_request(url=url)

    # 참고 예제
    # pageno = 1
    # hasnext = True
    #
    # while hasnext:
    #     url = pd_gen_url(......., numofrows=50, pageno=pageno)
    #     json_result = json_request(url=url)
    #
    #     json_body = json_response.get('body')
    #     numofrows = json_body.get('humOfRows')
    #     totalcount = json_body.get('totalCount')
    #
    #     if totalcount == 0:
    #         break
    #
    #     last_page = math.ceil(totalcount/numofrows)
    #     if pageno == last_page:
    #         hasnext = False
    #     else:
    #         pageno += 1

    json_response = json_result.get('response')
    json_header = json_response.get('header')
    result_message = json_header.get('resultMsg')
    if 'OK' != result_message:
        print('%s Error[%s] for request %s' % (datetime.now(), result_message, url))
        return None

    json_body = json_response.get('body')
    json_items = json_body.get('items')

    return json_items.get('item') if isinstance(json_items, dict) else None



def pd_fetch_tourspot_visitor(district1='',district2='', tourspot='', year=0, month=0):
    pass

# BASE_URL_FB_API = 'http://openapi.tour.go.kr/openapi/service'
# def pd_gen_url(endpoint, **params):
#     url = '%s?%s' % (endpoint, urlencode(params));
#     json_result = json_request(url=url)
#     return url
#
# def pd_fetch_tourspot_visitor(district1='', district2='', tourspot='', year=0, month=0):
#     pass


# ACCESS_TOKEN = "EAACEdEose0cBAMqjagSZBoe7s9akBG2vZB3gWkb0w9GZCRdrCOu22BkLkRl4OMos1XUHwbR8F9lh3ViEzZBqErHQ9wFZCZBr0WQ46OctEUJ90uvyTTO2RJ5mABNImmltd8QOryhhN7GSUfFK2lZAeEylIJhZAOZBGiYNuOYXxmQdpJUiXvwNCT7heZAvIMkyrYtyX0lnBCTh0MJr1DTu5DlHiO2zuW3CqgaSUZD"
# BASE_URL_FB_API = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"
# def pd_gen_url(
#         base=BASE_URL_FB_API,
#         node='',
#         **params):
#     url = '%s/%s/?%s' % (base,node, urlencode(params));
#     return url
#
# def fb_name_to_id(pagename):
#     url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
#     json_result = json_request(url=url)
#     return json_result.get("id")
#
#
# def fb_fetch_posts(pagename, since, until):
#     url = fb_gen_url(node=fb_name_to_id(pagename)+"/posts",
#                      fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
#                      since=since,
#                      until=until,
#                      limit=50,
#                      access_token=ACCESS_TOKEN)
#
#     # results = []
#     isnext = True
#     while isnext is True:
#         json_result = json_request(url=url)
#
#         paging = None if json_result is None else json_result.get('paging')
#         posts = None if json_result is None else json_result.get('data')
#
#         # results.append(posts)
#         # results += posts
#
#         url = None if paging is None else paging.get("next")
#         isnext = url is not None
#
#         yield posts
#
#
#
#
#
