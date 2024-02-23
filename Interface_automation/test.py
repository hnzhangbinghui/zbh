
res_data={
    'loginName':'ab',
    'password':'Ysstech123!@#',
    'validType':0}
url='http://192.168.99.158:9080/acp-custody/rest/login/extend/userForLogin'

a= "{'loginName':'ab','password':'Ysstech123!@#','validType':0}"
print(type(url))
print(type(eval(a)))