# it is one of the standart data exchange formats
# also often used as data storage format
# looks very similar to Python dictionaries

# JSON - JavaScript Object Notation

# json data is a string, so it must be converted to dict

import json

json_string = '{"id": 12, "brand":"ABIBAS", "in_stock": true}'

# when i tried to replicate json file i used 'True' and it gave me an error. In json it is 'true/false'.

# reading json file as dict for python
sneakers = json.loads(json_string)

print(type(sneakers))

key = []
value = []

for k, v in sneakers.items():
    key.append(k)
    value.append(v)

print(key)
print(value)
print(sneakers['brand'])


# converting dict to json file/format
js = json.dumps(sneakers)
print(js)
print('')
# or like this, it will add formatting
js2 = json.dumps(sneakers, indent=1)
print(js2)

print(type(js))  # is now string because json files are string
