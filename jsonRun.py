import  json
jsonstr = '{"name":"qiyue", "age": 18}'
data=json.loads(jsonstr)
print(data)
print(type(data))
json_string=json.dumps(data)
print(json_string)
print(type(json_string))
