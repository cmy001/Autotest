import requests


url = "http://192.168.159.128/prod-api/system/user/list"

cc = {
"Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMzNzM5MGQ1LWMzMWYtNGY0Yi04MzNkLTRiYTFjZDAwYmMyMiJ9.QyF_NZGGXoUYZ3uLJHhlmtLXD96gD0Nlko_BmA9RAXuEcV5s5OTViNbFxznZL0rK4qYVIEAo73sLJ8GzJPld4g",
    "Accept":"application/json, text/plain, */*",
    "Cookie":"username=admin; rememberMe=true; password=XYRZck83ULMQkCYH87PXuW0m8w8UzXvz59OCZri4cNoY77bkPxcR2WD48n3mJUEWfFhpGoF4dqirvo835Zy/5g==; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjMzNzM5MGQ1LWMzMWYtNGY0Yi04MzNkLTRiYTFjZDAwYmMyMiJ9.QyF_NZGGXoUYZ3uLJHhlmtLXD96gD0Nlko_BmA9RAXuEcV5s5OTViNbFxznZL0rK4qYVIEAo73sLJ8GzJPld4g; sidebarStatus=0"
}


response =requests.get(url=url,headers=cc)
print(response.json())