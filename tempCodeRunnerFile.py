response = requests.post(url=pixela_endpoint, json=user_parms)
print(response.text)