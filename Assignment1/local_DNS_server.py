import socket
import dnslib
def qnameReverse(qnamelist):
    n = len(qnamelist)
    for i in range(n): qnamelist[i] = qnamelist[i] + "."
    qnamelist.reverse()
    return qnamelist
def checkRes(dnslist, qnamelist):
    root = '198.41.0.4'
    ip_tmp = root
    domain = ""
    for i in qnamelist:
        domain = i + domain
        print(ip_tmp)
        r = dnslib.DNSRecord.question(domain)
        rr = r.send(root)
        res = dnslib.DNSRecord.parse(rr)
        if res.auth != []:
            root = res.auth[0].rdata.__str__()
            ip_tmp = res.ar[0].rdata.__str__() if (res.ar != []) else query(res.auth[0].rdata, dnslist)
        if res.auth == [] and res.rr != []:
            if (str(res.rr[0].rdata)[0].isdigit() == True): continue
            else:
                for RR in res.rr: dnslist.add_answer(RR)
                res = query(res.rr[0].rdata, dnslist)
    return res
            
def query(qin, dnslist):
    qname = str(qin)
    qnamelist = qname.split(".")
    qnamelist.pop(len(qnamelist) - 1) 
    qnamelist = qnameReverse(qnamelist)
    return checkRes(dnslist, qnamelist)

def local_DNS_Server(flag):
    # maintain a cache to store the IP address client has required.
    cache = {}
    while True:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSocket.bind(('127.0.0.1', 1234))
        message, clientAddress = serverSocket.recvfrom(2048)
        message_parse = dnslib.DNSRecord.parse(message)
        message_parse.header.set_rd(0)
        message = dnslib.DNSRecord.pack(message_parse)
        qname = str(message_parse.q.qname)

        if message_parse.q.qname in cache:
            rr = cache[qname]
            response = message_parse.reply()
            for RR in rr: response.add_answer(RR)
        else: 
            if flag == 0:
                request = message_parse.send("8.8.8.8") # public server IP '8.8.8.8'
                response = dnslib.DNSRecord.parse(request)
            else:
                response = message_parse.reply()
                res = query(message_parse.q.qname, response)
                for RR in res.rr: response.add_answer(RR)
            response.header.rd = 1
            cache[qname] = response.rr
            serverSocket.sendto(response.pack(),clientAddress)
        print("==============================")

def main():
    flag = int(input("Enter flag 0 or 1: "))
    local_DNS_Server(flag)
    return
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
