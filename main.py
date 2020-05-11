import socket
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import info
import model
import pandas
import numpy
from model import domain
global pointer
pointer = 0
model.connect("project")
def search():
    i = 0
    root.filename = filedialog.askopenfilename(title="select a file")
    data_csv = pandas.read_csv(root.filename)
    data = numpy.array(data_csv["domain"])
    while i <100:
        try:
            info.myresolver = info.dns.resolver.Resolver()
            nameserver = info.getns(data[i])
            info.myresolver.nameservers=[socket.gethostbyname(nameserver)]
            d = domain()
            d.name = data[i]
            d.ip = info.getip(data[i])
            d.ttl= info.getttl(data[i])
            d.mx = info.getmx(data[i])
            d.txt = info.gettxt(data[i])
            d.ptr=info.getptr(data[i])
            d.cname=info.getcname(data[i])
            d.ttl = info.getttl(data[i])
            location = info.getLocation(data[i])
            d.city = location.city
            d.country = location.country
            d.state = location.region
            d.longitude = location.longitude
            d.latitude = location.latitude
            d.registrar = info.getwhois(data[i]).registrar
            d.tld = info.gettld(data[i])
            res, res2 = info.getAS(data[i])
            d.asn = res
            d.ipplage = res2 
            d.save()
            i = i + 1
            progress['value']=i
            progress.update()
        except Exception as e:
            i = i+1
            progress['value']=i
            progress.update()
            continue
    messagebox.showinfo("srearch status","search done")


def next():
    global pointer
    pointer = pointer + 1
    try:
        res = domain.objects()
        show = res[pointer]
        namee.delete(0,END)
        namee.insert(0,show.name)
        ipe.delete(0,END)
        ipe.insert(0,show.ip)
        txte.delete(0,END)
        txte.insert(0,show.txt)
        mxe.delete(0,END)
        mxe.insert(0,show.mx)
        ttle.delete(0,END)
        ttle.insert(0,str(show.ttl))
        ptre.delete(0,END)
        ptre.insert(0,show.ptr)
        cnamee.delete(0,END)
        cnamee.insert(0,show.cname)
        countrye.delete(0,END)
        countrye.insert(0,show.country)
        citye.delete(0,END)
        citye.insert(0,show.city)
        statee.delete(0,END)
        statee.insert(0,show.state)
        latitudee.delete(0,END)
        latitudee.insert(0,show.latitude)
        longitudee.delete(0,END)
        longitudee.insert(0,show.longitude)
        registrare.delete(0,END)
        registrare.insert(0,show.registrar)
        tlde.delete(0,END)
        tlde.insert(0,show.tld)
        ase.delete(0,END)
        ase.insert(0,str(show.asn))
        resaue.delete(0,END)
        resaue.insert(0,show.ipplage)
    except Exception as e:
        messagebox.showerror("error message","something is wrong")


def SearchResult():
    try:
        show = domain.objects().first()
        namee.delete(0,END)
        namee.insert(0,show.name)
        ipe.delete(0,END)
        ipe.insert(0,show.ip)
        txte.delete(0,END)
        txte.insert(0,show.txt)
        mxe.delete(0,END)
        mxe.insert(0,show.mx)
        ttle.delete(0,END)
        ttle.insert(0,str(show.ttl))
        ptre.delete(0)
        ptre.insert(0,show.ptr)
        cnamee.delete(0,END)
        cnamee.insert(0,show.cname)
        countrye.delete(0,END)
        countrye.insert(0,show.country)
        citye.delete(0,END)
        citye.insert(0,show.city)
        statee.delete(0,END)
        statee.insert(0,show.state)
        latitudee.delete(0,END)
        latitudee.insert(0,show.latitude)
        longitudee.delete(0,END)
        longitudee.insert(0,show.longitude)
        registrare.delete(0,END)
        registrare.insert(0,show.registrar)
        tlde.delete(0,END)
        tlde.insert(0,show.tld)
        ase.delete(0,END)
        ase.insert(0,str(show.asn))
        resaue.delete(0,END)
        resaue.insert(0,show.ipplage)
    except :
        messagebox.showerror("erro","try again")

root = Tk()
root.title("domain info ")
frame = Frame(root)
requestl = Label(frame,text = "domain:")
request = Entry(frame,width=35)
searchb = Button(frame,text ="search",command=search)
resultb = Button(frame,text="show result",command=SearchResult)
nextb = Button(frame,text="next",command=next)
progress = ttk.Progressbar(frame,length=200,orient=HORIZONTAL,maximum=100,mode = "determinate")
progress.grid(row=0,column=5)
requestl.grid(row=0,column=0)
request.grid(row=0,column=1)
searchb.grid(row=0,column=2)
resultb.grid(row=2,columnspan=2)
nextb.grid(row=2,column=3)
ipl = Label(frame,text="IP:")
ipe = Entry(frame)
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
countryl =Label(frame,text="Country:")
countrye =Entry(frame)
cityl =Label(frame,text="City:")
citye = Entry(frame)
statel = Label(frame,text="Region:")
statee =Entry(frame)
latitudel = Label(frame,text ="Latitude:")
latitudee = Entry(frame)
longitudel = Label(frame,text="Longitude:")
longitudee =Entry(frame)
registrarl = Label(frame,text="registrar:")
registrare = Entry(frame)
tldl = Label(frame,text="TLD:")
tlde =Entry(frame)
asl = Label(frame,text="AS:")
ase = Entry(frame)
resaul = Label(frame,text="sous-resau:")
resaue = Entry(frame)
namel.grid(row=3,column=0,pady="10px")
namee.grid(row=3,column=1)
ipl.grid(row=4,column=0,pady="10px")
ipe.grid(row=4,column=1)
mxl.grid(row=5,column=0,pady="10px")
mxe.grid(row=5,column=1)
txtl.grid(row=6,column=0,pady="10px")
txte.grid(row=6,column=1)
ttll.grid(row=7,column=0,pady="10px")
ttle.grid(row=7,column=1)
ptrl.grid(row=8,column=0,pady="10px")
ptre.grid(row=8,column=1)
cnamel.grid(row=9,column=0,pady="10px")
cnamee.grid(row=9,column=1)
cityl.grid(row=3,column=3)
citye.grid(row=3,column=4)
statel.grid(row=4,column=3)
statee.grid(row=4,column=4)
countryl.grid(row=5,column=3)
countrye.grid(row=5,column=4)
latitudel.grid(row=6,column=3)
latitudee.grid(row=6,column=4)
longitudel.grid(row=7,column=3)
longitudee.grid(row=7,column=4)
registrarl.grid(row=8,column=3)
registrare.grid(row=8,column=4)
tldl.grid(row=9,column=3)
tlde.grid(row=9,column=4)
asl.grid(row=3,column=5)
ase.grid(row=3,column=6)
resaul.grid(row=4,column=5)
resaue.grid(row=4,column=6)
frame.pack()
root.mainloop()
