import json
from json import JSONEncoder

"""
Exercise 1: Convert the following dictionary into JSON format
"""


def convert_into_json(dict):
    return json.dumps(dict)


"""
Exercise 2: Access the value of key2 from the following JSON
"""


def extract_key(f):
    data = json.loads(f)
    return data["key2"]


"""
Exercise 3: PrettyPrint following JSON data
"""


def prettyprint_json(dict):
    return json.dumps(dict, indent=2, separators=(",", " = "))


"""
Exercise 4: Sort JSON keys in and write them into a file
"""
sampleJson = {"id": 1, "name": "value2", "age": 29}
with open("exercises/files/exo4.json", "w+") as f:
    json.dump(sampleJson, f, indent=4, sort_keys=True)


"""
Exercise 5: Access the nested key ‘salary’ from the following JSON
"""


def nested_key(dict):
    return dict["company"]["employee"]["payble"]["salary"]


"""
Exercise 6: Convert the following Vehicle Object into JSON
"""


def convert_object_into_json(classe):
    class object_encoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

    return json.dumps(classe, indent=2, cls=object_encoder)


"""
Exercise 7: Convert the following JSON into Vehicle Object
"""


def convert_json_into_object(class_constructor, fp):
    def decoder(obj):
        return class_constructor(obj["name"], obj["engine"], obj["price"])

    class_obj = json.loads(fp, object_hook=decoder)
    return class_obj.name, class_obj.engine, class_obj.price


"""
Exercise 8: Check whether following json is valid or invalid. If Invalid correct it

{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}

Réponse avec bash : echo { "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } } | python -m json.tool
"""
def is_valid_json(data):
    try:
        json.loads(data)
    except:
        return False
    
    return True