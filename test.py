import requests
url="http://localhost:8080/customer/currentCustomer"

token = 'iN7aWXUhA5i2OI0qacxWeWRhl4tRW3QCj1uTr5hVMLjo1DiL8VhdD3cIqFQvlUyI3ceC8CUS9gbQ3lyKFqzVd5ImJsxrOBco6bQ9glDHVd+7QOLL+75DACVtH3ngNuEf24BosvRkZLLMVwGoLqctx+QTVYCFmcBCdB2BeS//Zd4='
headers={
    'Authentication':token
}
r=requests.get(url,headers=headers)
print(r.content)
