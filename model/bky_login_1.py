import requests
import urllib3
urllib3.disable_warnings()

s = requests.session()
s.verify=False


url = "https://www.cnblogs.com/"

c = requests.cookies.RequestsCookieJar()
c.set(".Cnblogs.AspNetCore.Cookies","CfDJ8D8Q4oM3DPZMgpKI1MnYlrntZQZgzcYrfe4AefenTz3QdPCNxa7wT6Ws7f4gVEzoA1bjO_py-JV8cicE929WESLe1KdozvNrmyhfC53b1HJ53Ys5hpU2UiGi2KpwmFS5m-KRzRYYVMJPWZiGYKWoh7sBcG7OG9IRerp6DGEL6tMO7xaHG895ag26BAgpbQMh3_pH1so7AuIqUvWtdj3_gZ8K177pF6Gk4h2iHVRzQpIkDflhdITSqpq8Vcsilh_38VaQg4Rz2rjPbOwHSupWbGmlortv_G0ElxOLCcLzVeWcm7ARRwCIXVQ7FEbYTEp0LEfvK5RsVDt-FFWqLYtrsajpumCZf2pDHJwDWIkibmkDFAO1MrY2XBNPjgHgMOeZXdv0M7-72myesmZtI37eaun-W3FuQ39cLaO3lRkzZU_mPeLn2WVGXWV72hdI7Gdq-nWZ4XqlaBtsr6ovB865M2o")
c.set(".CNBlogsCookie","1C471FCB3DBD9760AF2B961873F3DA2F1185FA4F30601E92CDFF1B31B750B818AF4577342983A15C90B02834594E5AD1431AC3845BDF7697AD5938BF48292E6283772F1076052113E1F38B35A7A387F939C4346A917245B4BE70BE31CB11007761D72E93")
s.cookies.update(c)

r = s.get(url)
# print(r.text)
if "开发者的网上家园" in r.text:
    print("博客园登录成功！")
else:
    print("博客园登录失败！")