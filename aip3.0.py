import csv
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
    'Referer': 'http://fundf10.eastmoney.com/jjjz_160706.html'
}


def get_html(url):
    html = requests.get(url, headers=headers)
    html_text = html.text
    # print(html_text)
    start = html_text.find('{"Data":{"LSJZList"')
    json_data = json.loads(html_text[start:-1])
    netvalues = json_data['Data']['LSJZList']
    with open('aip.csv', mode='a', encoding='utf-8', newline='') as ff:
        for data in netvalues:
            fsrq = data['FSRQ']
            dwjz = data['DWJZ']
            ljjz = data['LJJZ']
            jzzzl = data['JZZZL']
            print(fsrq, dwjz, ljjz, jzzzl)
            writer = csv.writer(ff)
            writer.writerow([fsrq, dwjz, ljjz, jzzzl])
    pass


if __name__ == '__main__':
    csvfile = 'aip.csv'
    with open(csvfile, mode='w', encoding='utf-8', newline='') as f:
        f.write('发售日期,单位净值,累计净值,净值增长率\n')
    # str = 'jQuery183015088915834593553_1586246635664('
    # print(len(str))
    for i in range(1, 11):
        url = 'http://api.fund.eastmoney.com/f10/lsjz?' \
              'callback=jQuery183015088915834593553_1586246635664&' \
              'fundCode=160706&pageIndex={}&pageSize=20&' \
              'startDate=&endDate=&_=1586246635678'.format(i)
        print('当前输出地{}页'.format(i))
        get_html(url)

# import csv
# with open('aip.csv', 'r')as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#
# with open('aip.csv', 'a', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(['7', 'hu', '18', '100', '90', '85'])
#     writer.writerow(['8', 'zahng', '19', '87', '97', '77'])
