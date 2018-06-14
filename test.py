import analysis_pd.collect.api.api as pdapi

url = pdapi.pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList',
    YM = '{0:04d}{1:02d}'.format(2017, 1),
    SIDO = '서울특별시',
    GUNGU='',
    RES_NM='',
    numOfRows=10,
    _type='json',
    pageNo=1
)

print(url)

# import urllib.request
# import urllib.parse
# import analysis_pd.collect.api.api as pdapi
# # test for pd_gen_url
# sido = urllib.parse.urlencode('부산광역시')
# gungu = urllib.parse.urlencode('해운대구')
# res_nm = urllib.parse.urlencode('부산시립미술관')
# servicekey = urllib.parse.urlencode('6m9Oq%2F9j8cIEp6w%2F3PmNrbAS1P17y24uk3Q2xloOH0WyDrSXbGHGpnF3Pf%2Bob8J6AW2k2HO%2BygzGcjrnyKNgog%3D%3D')
# url = pdapi.pd_gen_url(
#     'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
#     YM='201201',
#     SIDO=urllib.parse.urlencode(sido),
#     GUNGU=urllib.parse.urlencode(gungu),
#     RES_NM=urllib.parse.urlencode(res_nm),
#     serviceKey=urllib.parse.urlencode(servicekey)
# )
#
# print(url)
