import os
# configuration
CONFIG = {
    'district':'서울특별시',
    'countries': [('중국', 112),('일본', 130),('미국',275)],
    'common':{
        'start_year': 2017,
        'end_year': 2017,
        'fetch': False,
        'result_directory': '__results__/crawling',
        'service_key': '6m9Oq%2F9j8cIEp6w%2F3PmNrbAS1P17y24uk3Q2xloOH0WyDrSXbGHGpnF3Pf%2Bob8J6AW2k2HO%2BygzGcjrnyKNgog%3D%3D',
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])