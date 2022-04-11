import requests
from lxml import etree
def dearoutsider_url():
    url = "https://clearoutside.com/forecast/31.03/121.23"
    headers = {

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response = requests.get(url,headers=headers)

    xpath_response = etree.HTML(response.text)
    list = []
    day_0 = xpath_response.xpath('//*[@id="day_0"]/div[3]/div/span/text()')[0]
    list.append(day_0)
    #日期
    timemes = xpath_response.xpath('/html/body/div[2]/h2/text()')[0]
    list.append(timemes)
    day_list = []
    #当天日期
    day_now = xpath_response.xpath('//*[@id="day_0"]/div[3]/ul/li/text()')
    for days in day_now:
        day_list.append(days)
    list.append(day_now)
    #TotalClouds
    TotalClouds = xpath_response.xpath('/html/body/div[2]/div[2]/div[1]/div[4]/div[1]/div/ul/li')
    TotalCloudsList = []
    for total_clouds in TotalClouds:
        TotalCloudsList.append(total_clouds.text)
    list.append(TotalCloudsList)


    #LowClouds

    LowClouds = xpath_response.xpath('/html/body/div[2]/div[2]/div[1]/div[4]/div[2]/div/ul/li')
    LowCloudsList = []
    for low_clouds in LowClouds:
        LowCloudsList.append(low_clouds.text)
    list.append(LowCloudsList)

    return list
if __name__ == '__main__':
    print(dearoutsider_url())