import analysis_pd.collect.api.api as pdapi
for items in pdapi.pd_fetch_tourspot_visitor(district1="서울특별시",year=2012,month=7):
    print(items)