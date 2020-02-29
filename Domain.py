from mongoengine import *
connect("project")
import json
import dns.resolver
import dns.reversename
from tkinter import *
import socket
from tkinter import messagebox
# initilize the resolver
myresolver =dns.resolver.Resolver()
# define the document
class domain(Document):
    name = StringField(unique=True,required=True)
    ip = StringField(unique=True)
    mx = StringField(unique=True)
    txt = StringField()
    ns = StringField()
    ptr = StringField()
    cname = StringField()
    ttl = IntField()
    def json(self):
        name_dict = {
            "name":self.name,
            "ip":self.ip,
            "mx:":self.mx,
            "txt":self.txt,
            "ns":self.ns,
            "ptr":self.ptr,
            "cname":self.cname,
            "ttl":self.ttl
        }
        return json.dumps(name_dict)
    meta = {
        "indexes":["name"],
        "ordering":["-id"]
    }
#getting the records info
def getip(url):
    ar = myresolver.query(url,"A")
    for a in ar :
        return a.to_text()
def getmx(url):
    mxr = myresolver.query(url,"MX")
    for m in mxr:
        return m.to_text()
def getns(url):
    nsr = myresolver.query(url,"NS")
    for n in nsr:
        return n.to_text()
def gettxt(url):
    txtr = myresolver.query(url,"TXT")
    for t in txtr:
        return t.to_text()
def getttl(url):
    ttlr = myresolver.query(url,"NS")
    return ttlr.rrset.ttl
def getptr(url):
    res = str(getip(url))
    name,alias,adress = socket.gethostbyaddr(res)
    return name
def getcname(url):
    cnr = myresolver.query(url,"A")
    return str(cnr.canonical_name)
#cereating the document
def search():
    try:
        d = domain()
        d.name = request.get()
        d.ip = getip(request.get())
        d.ns = getns(request.get())
        d.ttl= getttl(request.get())
        d.mx = getmx(request.get())
        d.txt = gettxt(request.get())
        d.ptr=getptr(request.get())
        d.cname=getcname(request.get())
        d.ttl = getttl(request.get())
        d.save()
        messagebox.showinfo("search status","search done")
    except :
        messagebox.showerror("error message","try again")

# setting the resolver
def setresolver():
    myresolver.nameservers = [resolve.get()]
    messagebox.showinfo("reslover settings","resolver succsefuly seted")
def result():
    try:
        window = Tk()
        window.title("result")
        window.geometry("400x400")
        frame = Frame(window)
        ipl = Label(frame,text="IP:")
        ipe = Entry(frame)
        nsl = Label(frame,text="NS:")
        nse = Entry(frame)
        mxl = Label(frame,text="MX:")
        mxe = Entry(frame)
        txtl = Label(frame,text="TXT:")
        txte = Entry(frame)
        ptrl = Label(frame,text="PTR:")
        ptre = Entry(frame)
        cnamel = Label(frame,text="Cname:")
        cnamee = Entry(frame)
        namel = Label(frame,text="domain name:")
        namee = Entry(frame)
        ttll = Label(frame,text="TTL:")
        ttle = Entry(frame)
        namel.grid(row=0,column=0)
        namee.grid(row=0,column=1)
        ipl.grid(row=1,column=0)
        ipe.grid(row=1,column=1)
        mxl.grid(row=2,column=0)
        mxe.grid(row=2,column=1)
        txtl.grid(row=3,column=0)
        txte.grid(row=3,column=1)
        nsl.grid(row=4,column=0)
        nse.grid(row=4,column=1)
        ttll.grid(row=5,column=0)
        ttle.grid(row=5,column=1)
        ptrl.grid(row=6,column=0)
        ptre.grid(row=6,column=1)
        cnamel.grid(row=7,column=0)
        cnamee.grid(row=7,column=1)
        show = domain.objects().first()
        namee.insert(0,show.name)
        ipe.insert(0,show.ip)
        txte.insert(0,show.txt)
        nse.insert(0,show.ns)
        mxe.insert(0,show.mx)
        ttle.insert(0,str(show.ttl))
        ptre.insert(0,show.ptr)
        cnamee.insert(0,show.cname)
        frame.pack()
    except :
        messagebox.showerror("error message","could not display the result")

#creating thr window
root = Tk()
root.title("domain info ")
root.geometry("400x400")
frame = Frame(root)
requestl = Label(frame,text = "domain:")
request = Entry(frame,width=35)
resolvel= Label(frame,text="resolver:")
resolve = Entry(frame,width=35)
searchb = Button(frame,text ="search",command=search)
resolveb = Button(frame,text="setresolver",command=setresolver)
resultb = Button(frame,text="show result",command=result)
requestl.grid(row=0,column=0)
request.grid(row=0,column=1)
resolve.grid(row=1,column=1)
resolvel.grid(row=1,column=0)
searchb.grid(row=3,columnspan=2)
resolveb.grid(row=2,columnspan=2)
resultb.grid(row=4,columnspan=2)
frame.pack()
root.mainloop()