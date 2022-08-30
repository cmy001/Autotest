import requests

url = "http://192.168.159.128/prod-api/getInfo"

a = {

    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6ImJlOTg4YmJiLWE1NGQtNGY4Yy1hZWZiLTIyY2I4MjIwZTdmYSJ9.4lVcDQqoZ51MAg17doXoq86EeUb4UARET2HL4daWeLjecPJtaaDUq__FM1gIeFl9xbEUVwpKa9P13fkVOIrDfA"
}
res=requests.get(url=url,headers=a)

print(res.json())