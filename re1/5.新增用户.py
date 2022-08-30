
import requests


url = "http://192.168.159.128/prod-api/system/user"

bb = {
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMzNzM5MGQ1LWMzMWYtNGY0Yi04MzNkLTRiYTFjZDAwYmMyMiJ9.QyF_NZGGXoUYZ3uLJHhlmtLXD96gD0Nlko_BmA9RAXuEcV5s5OTViNbFxznZL0rK4qYVIEAo73sLJ8GzJPld4g",
    "Content-Type":"application/json;charset=UTF-8"
}

data = {"userName":"55","nickName":"55","password":"123456","status":"000","postIds":[],"roleIds":[]}

res = requests.get(url=url,json=data,headers=bb)
print(res.json())