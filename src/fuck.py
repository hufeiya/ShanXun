import socket,time
from SNHeartBeat import SNThunderProtocol
def sendPack(ip):
    while True:
        sendSiglePack(ip,int(time.time()))
        time.sleep(20)
def sendSiglePack(ip,timeStamp):
    fuck = SNThunderProtocol("15384037961@GDPF.XY",ip,timeStamp)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    data = fuck.digest()
    sock.sendto(data,("115.239.134.167",8080))
    sock.close()
if __name__ == '__main__':
    sendPack("115.200.29.82")
