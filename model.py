from mongoengine import *
import json
class domain(Document):
    name = StringField(unique=True,required=True)
    ip = StringField()
    mx = StringField()
    txt = StringField()
    ptr = StringField()
    cname = StringField()
    ttl = IntField()
    def json(self):
        name_dict = {
            "name":self.name,
            "ip":self.ip,
            "mx:":self.mx,
            "txt":self.txt,
            "ptr":self.ptr,
            "cname":self.cname,
            "ttl":self.ttl
        }
        return json.dumps(name_dict)
    meta = {
        "indexes":["name"],
        "ordering":["-id"]
    }