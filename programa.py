import json
from pprint import pprint

#with open('data.json') as data_file:
#    data = json.load(data_file)
#data["maps"][0]["id"]  # will return 'blabla'
#pprint(data)


#with open('receitas.json', encoding='utf-8') as data_file:
#    data = json.loads(data_file.read())

#import json
#    from pprint import pprint
    with open('data.json') as data_file:
        data_item = json.load(data_file)
    pprint(data_item)

    print(data_item['parameters'][0]['id'])
