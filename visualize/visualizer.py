import matplotlib.pyplot as plt



def graph_scatter(result_analysis):
    # plt.subplots 은 (몇 행, 몇 열) 의 값으로 그래프를 그려준다.
    fig, subplots = plt.subplots(1, len(result_analysis), sharey=True)  # sharey 는 다른 값과 같은 비율로 조정해줌
    # print("plt.subplots === //",plt.subplots(1, len(result_analysis), sharey=True))
    # print("fig === ", fig)
    # print("subplots === ", subplots)


    for index, result in enumerate(result_analysis):    # enumerate 는 자동으로 index가 나온다
        subplots[index].set_xlabel('{0}인 입국자수'.format(result['country_name']))    # x축 라벨
        index == 0 and subplots[index].set_ylabel('관광지 입장객 수')   # y축 라벨
        subplots[index].set_title('r={:.5f}'.format(result['r']))   # 그래프 이름 출력
        subplots[index].scatter(result['x'], result['y'], c='black', s=6) # 내부 데이터 출력형식 지정

    plt.subplots_adjust(wspace=0)
    plt.show()
