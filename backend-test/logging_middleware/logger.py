import requests
TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzZzk0OTVAc3JtaXN0LmVkdS5pbiIsImV4cCI6MTc3NzY5OTM0MCwiaWF0IjoxNzc3Njk4NDQwLCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiNmQ0NzQwMzktNzI4Yy00NjQ5LTllNDQtMDA0NTBjZmJlMDM5IiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoic2FuamFpIGd1cnUiLCJzdWIiOiJiMDE3MzkzMC1lNDhlLTRkNmYtYjQ5Yy1hNzZhYzFhMTU2NWEifSwiZW1haWwiOiJzZzk0OTVAc3JtaXN0LmVkdS5pbiIsIm5hbWUiOiJzYW5qYWkgZ3VydSIsInJvbGxObyI6InJhMjMxMTAyNjAxMDY5OCIsImFjY2Vzc0NvZGUiOiJRa2JweEgiLCJjbGllbnRJRCI6ImIwMTczOTMwLWU0OGUtNGQ2Zi1iNDljLWE3NmFjMWExNTY1YSIsImNsaWVudFNlY3JldCI6ImtOcmVqQXRkU0taVXJXYUQifQ.QVS7L_oow6vBbc0dcF4AoS0zFYtIv1ilKh0maFPg968"

def Log(stack,level,message,package):
    url="http://20.207.122.201/evaluation-service/logs"
    payload={
        "stack":stack,
        "level":level,
        "package":package,
        "message":message
    }
    headers={
        "Authorization":f"Bearer {TOKEN}",
        "Content-Type":"application/json"
    }

    try:
        response=requests.post(url,json=payload,headers=headers)
        print(response.json())
    except Exception as e:
        print("failed!",str(e))