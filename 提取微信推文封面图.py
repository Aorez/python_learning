import requests
import re

# acticleurl = input("请输入想要提取封面文章的链接")
acticleurl = "https://mp.weixin.qq.com/s/O4WTkB-bTAJp9nLGCe-0-A"
htmltext = requests.get(acticleurl).text
imgurl = re.findall(r"var msg_cdn_url = \"(.*?)\";",htmltext)[0]
imgtitle = re.findall(r"var msg_title = \'(.*?)\'",htmltext)[0]
response = requests.get(imgurl)
with open('./图/'+"微信封面："+imgtitle+".jpg","wb") as f:
    f.write(response.content)
    print("保存完毕！！")