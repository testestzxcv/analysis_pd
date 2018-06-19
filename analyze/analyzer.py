import json
import pandas as pd
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import math


def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except ZeroDivisionError:
        r = 0.0

    return r


def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())   # 서울특별시 파일에서 읽어온 데이터를 json 형식으로 저장
        print("json_data ===", json_data)

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())   # date와 외국 방문자수 데이터 폼

    results = []
    for filename in resultfiles['foreign_visitor']: # 외국 데이터 문서 전체 순환
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())   # 외국 데이터 파일을 읽어서 변수에 저장

        foreignvisitor_table = pd.DataFrame(json_data, columns = ['country_name', 'date', 'visit_count'])
        print("fore table ===", foreignvisitor_table)##
        foreignvisitor_table = foreignvisitor_table.set_index('date')
        print("fore table.index date ===", foreignvisitor_table)##
        merge_table = pd.merge(temp_tourspotvisitor_table, foreignvisitor_table, left_index=True, right_index=True) # 테이블 병합
        print("merge === ", merge_table)##

        x = list(merge_table['visit_count'])    # visit_count 데이터 리스트로 저장
        y = list(merge_table['count_foreigner'])    # count_foreigner 데이터 리스트로 저장
        print("x list visit count ===", x)##
        print("y list foreigner count ===", y)##
        country_name = (foreignvisitor_table['country_name'].unique()).item(0)  # unique는 중복되는 값을 줄여준다. 나라이름 저장
        print("count name === ",country_name)##
        r = ss.pearsonr(x, y)[0]    # 상관계수 뽑기
        print("상관계수 === ",r ) ##
        # r = np.corrcoef(x, y)[0]
        data = {'x': x, 'y': y, 'country_name':country_name, 'r':r} # 데이터 dict형식으로 저장
        print("data === ",data)##
        results.append(data)    # 전체 데이터 변수에 저장

        print("results === " , results) ##

        merge_table['visit_count'].plot(kind='bar') # Pandas의 시각화 기능
        plt.show()

    return results


def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data = json.loads(infile.read())   # 서울특별시 파일에서 읽어온 데이터를 json 형식으로 저장
        # print("json_data ===", json_data)

    tourspot_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner', 'date'])
    print("fore====",tourspot_table)

    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
            # print("json data infile === ", json_data)

        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        print("foreignvisitor_table === ", foreignvisitor_table)
        # foreignvisitor_table = foreignvisitor_table.set_index('date')
        # print("fore table.index date 222 ===", foreignvisitor_table)  ##
        merge_table = pd.merge(tourspot_table, foreignvisitor_table, left_index=True,
                               right_index=True)  # 테이블 병합
        print("merge_table === ",merge_table)

        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])
        print("x list visit count 222===", x)##
        print("y list foreigner count 222===", y)##

        tourist_spot = (tourspot_table['tourist_spot'].unique())
        print("tour spot unique === ",tourist_spot)
        r = ss.pearsonr(x, y)[0]  # 상관계수 뽑기
        print("상관계수 === 222", r)  ##

        data = {'x': x, 'y': y, 'tourist_spot': tourist_spot, 'r': r}  # 데이터 dict형식으로 저장
        print("data 222=== ", data)  ##
        results.append(data)
        # foreignvisitor_table = tourspot_table.set_index('date')
    # print("fore table index date ====", foreignvisitor_table)

    # test = pd.DataFrame(json_data, columns=['tourist_spot'])
    # print(test)



        temp_table = tourspot_table[tourspot_table['tourist_spot']=='경복궁']
        print(temp_table)


    return results