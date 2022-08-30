import requests

url = "http://192.168.159.128/prod-api/system/user/list"

Request= {

    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMzNzM5MGQ1LWMzMWYtNGY0Yi04MzNkLTRiYTFjZDAwYmMyMiJ9.QyF_NZGGXoUYZ3uLJHhlmtLXD96gD0Nlko_BmA9RAXuEcV5s5OTViNbFxznZL0rK4qYVIEAo73sLJ8GzJPld4g"
}

res=requests.get(url=url,headers=Request)
print(res.json)


res_json = res.json()
uid = res_json["rows"][5]["userId"]   #row[5].userId
url1 = "/system/user/uid"
Request= {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMzNzM5MGQ1LWMzMWYtNGY0Yi04MzNkLTRiYTFjZDAwYmMyMiJ9.QyF_NZGGXoUYZ3uLJHhlmtLXD96gD0Nlko_BmA9RAXuEcV5s5OTViNbFxznZL0rK4qYVIEAo73sLJ8GzJPld4g"}
response2 = requests.delete(url=url,headers=Request)
print(response2.json())