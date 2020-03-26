import socket
from tkinter import *
from tkinter import messagebox
import info
import model
from model import domain

model.connect("project")
def search():
    try:
        info.myresolver = info.dns.resolver.Resolver()
        nameserver = info.getns(request.get())
        info.myresolver.nameservers=[socket.gethostbyname(nameserver)]
        d = domain()
        d.name = request.get()
        d.ip = info.getip(request.get())
        d.ttl= info.getttl(request.get())
        d.mx = info.getmx(request.get())
        d.txt = info.gettxt(request.get())
        d.ptr=info.getptr(request.get())
        d.cname=info.getcname(request.get())
        d.ttl = info.getttl(request.get())
        d.city = info.getLocation(request.get()).city
        d.country = info.getLocation(request.get()).country
        d.state = info.getLocation(request.get()).region
        d.longitude = info.getLocation(request.get()).longitude
        d.latitude = info.getLocation(request.get()).latitude
        d.save()
        messagebox.showinfo("search status","search done")
    except Exception as e:
        messagebox.showerror("error message",e)

def SearchResult():
    try:
        show = domain.objects().first()
        namee.insert(0,show.name)
        ipe.insert(0,show.ip)
        txte.insert(0,show.txt)
        mxe.insert(0,show.mx)
        ttle.insert(0,str(show.ttl))
        ptre.insert(0,show.ptr)
        cnamee.insert(0,show.cname)
        countrye.insert(0,show.country)
        citye.insert(0,show.city)
        statee.insert(0,show.state)
        latitudee.insert(0,show.latitude)
        longitudee.insert(0,show.longitude)
    except :
        messagebox.showerror("erro","try again")

root = Tk()
root.title("domain info ")
width = root.winfo_screenwidth()
height = root.winfo_screenmmheight()
root.geometry("1280x720")
frame = Frame(root)
requestl = Label(frame,text = "domain:")
request = Entry(frame,width=35)
searchb = Button(frame,text ="search",command=search)
resultb = Button(frame,text="show result",command=SearchResult)
requestl.grid(row=0,column=0)
request.grid(row=0,column=1)
searchb.grid(row=0,column=2)
resultb.grid(row=2,columnspan=2)
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
frame.pack()
root.mainloop()
