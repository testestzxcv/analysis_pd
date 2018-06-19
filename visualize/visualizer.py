import matplotlib.pyplot as plt



def graph_scatter(result_analysis):
    fig, subplots = plt.subplots(1, len(result_analysis), sharey=True)  # sharey 는 다른 값과 같은 비율로 조정해줌


    for index, result in enumerate(result_analysis):    # enumerate 는 자동으로 index가 나온다
        subplots[index].set_xlabel('{0}인 입국자수'.format(result['country_name']))
        index == 0 and subplots[index].set_ylabel('관광지 입장객 수')
        subplots[index].set_title('r={:.5f}'.format(result['r']))
        subplots[index].scatter(result['x'], result['y'], c='black', s=6)

    plt.subplots_adjust(wspace=0)
    plt.show()
