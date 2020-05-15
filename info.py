import model
import dns.resolver
import dns.reversename
import socket
import whois
from ip2geotools.databases.noncommercial import DbIpCity
import tldextract
import pyasn
import os
global myresolver
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
    ttlr = myresolver.query(url,"A")
    return ttlr.rrset.ttl

def getptr(url):
    try:
        ip = myresolver.query(url,"A")
        revers = dns.reversename.from_address(str(ip[0]))
        name = str(myresolver.query(revers,"PTR")[0])
    except:
        name = "no data"
    return name

def getcname(url):
    cnr = myresolver.query(url,"A")
    return str(cnr.canonical_name)
def getLocation(url):
    ip = getip(url)
    result = DbIpCity.get(ip,api_key='free')
    return result
def getwhois(url):
    result = whois.whois(url)
    return result
def gettld(url):
    result = tldextract.extract(url)
    return result.suffix
def getAS(url):
    if not(os.path.isfile("rib.20200330.1400")):
        os.system("pyasn_util_download.py --latest")
        
    ip = getip(url)
    asn = pyasn.pyasn("rib.20200330.1400")
    result = asn.lookup(ip)
    return result