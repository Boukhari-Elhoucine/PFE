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
    city = StringField()
    country = StringField()
    state = StringField()
    latitude = FloatField()
    longitude = FloatField()
    registration_date = StringField()
    registrar = StringField()
    def json(self):
        name_dict = {
            "name":self.name,
            "ip":self.ip,
            "mx:":self.mx,
            "txt":self.txt,
            "ptr":self.ptr,
            "cname":self.cname,
            "ttl":self.ttl,
            "country":self.country,
            "city":self.city,
            "state":self.state,
            "latitude":self.latitude,
            "longitude":self.longitude,
            "registration_date":self.registration_date,
            "registrar":self.registrar
        }
        return json.dumps(name_dict)
    meta = {
        "indexes":["name"],
        "ordering":["-id"]
    }