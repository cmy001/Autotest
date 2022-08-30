import requests

url = "http://192.168.159.128/prod-api/getRouters"

canshu = {
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMzNzM5MGQ1LWMzMWYtNGY0Yi04MzNkLTRiYTFjZDAwYmMyMiJ9.QyF_NZGGXoUYZ3uLJHhlmtLXD96gD0Nlko_BmA9RAXuEcV5s5OTViNbFxznZL0rK4qYVIEAo73sLJ8GzJPld4g",
    "Content-Type":"application/json;charset=UTF-8"

}

data ={"roleName":"77","roleKey":"10086","roleSort":6,"status":"0","menuIds":[],"deptIds":[],"menuCheckStrictly":True,"deptCheckStrictly":True}

response = requests.get(url=url,json=data,headers=canshu)
print(response.json())