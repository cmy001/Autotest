import requests

url = "http://192.168.159.128/prod-api/system/user/list"

a = {

    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjY2MjJlODY4LTgyODgtNDRmMS04NGJlLTFkMGY5YjE5MTQzZSJ9.iZjWl7__fOj9Dg68xd3VeeOoAyHIt_tkpfzYIjaAUKciutYVMKhOBOdgwRbylMkl601XYc4SHzH6bSo6kZgPJA"
}
res=requests.get(url=url,headers=a)

print(res.json())