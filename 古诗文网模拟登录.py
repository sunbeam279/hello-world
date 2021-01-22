from CodeApi import FateadmApi
import requests
from lxml import etree
def Imgsb(Codeaddr,Codetype):
    pd_id = "127973"  # 用户中心页可以查询到pd信息
    pd_key = "GiPEvCxxL5bRziGNpvTPIQkx6eLfIC0B"
    app_id = "327973"  # 开发者分成用的账号，在开发者中心可以查询到
    app_key = "ba+Wr4rnMvMhQdu9tn1u4k86fF+/TeNI"
    pred_type = Codetype
    api = FateadmApi(app_id, app_key, pd_id, pd_key)
    file_name = Codeaddr
    result = api.PredictFromFileExtend(pred_type, file_name)  # 直接返回识别结果
    return result
url="https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx"
headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
session=requests.Session()
page_text=session.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
img_url="https://so.gushiwen.org"+tree.xpath('//div[@class="mainreg2"]/div[4]/img[@id="imgCode"]/@src')[0]
data_1=tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
data_2=tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
print('图片地址：',img_url,end='.....')
img=requests.get(url=img_url,headers=headers).content
open('CodeImg.jpg','wb').write(img)
print("下载成功")
yzm=Imgsb("CodeImg.jpg","30400")
print("验证码识别成功",yzm)
'''
###登录
url_dl="https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
data={
    '__VIEWSTATE': data_1,
    '__VIEWSTATEGENERATOR': data_2,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '3394872737@qq.com',
    'pwd': '1qaz2wsx3ed',
    'code': yzm,
    'denglu': '登录'
}
response=requests.post(url=url_dl,data=data,headers=headers)
print(response.text)
print(response.status_code)
'''

