# import analysis_pd.collect.api.api as pdapi
#
# url = pdapi.pd_gen_url(
#     'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList',
#     YM = '{0:04d}{1:02d}'.format(2017, 1),
#     SIDO = '서울특별시',
#     GUNGU='',
#     RES_NM='',
#     numOfRows=10,
#     _type='json',
#     pageNo=1
# )
#
# print(url)


import analysis_pd.collect.api.api as pdapi
# test for pd_gen_url
url = pdapi.pd_gen_url(
    'http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList',
    YM='201201',
    SIDO='부산광역시',
    GUNGU='해운대구',
    RES_NM='부산시립미술관',
    serviceKey='6m9Oq%2F9j8cIEp6w%2F3PmNrbAS1P17y24uk3Q2xloOH0WyDrSXbGHGpnF3Pf%2Bob8J6AW2k2HO%2BygzGcjrnyKNgog%3D%3D')

print(url)
