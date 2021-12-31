import sys
import math

class IpMaskCalculator(object):
    def GetIpMask(self, lengthMask):
        mask=0
        for i in range(lengthMask):
            mask=mask*2+1
        for i in range(lengthMask,32):
            mask=mask*2
        return mask
    
    def GetNetworkAddress(self, ip, mask):
        return ip&mask
    
    def GetBroadcastAddress(self, ip, mask):
        return ip|(mask^0xffffffff)
    
    def IpToVaule(self, strIp):
        tmp=list(map(int,strIp.split('.')))
        IpInteger=tmp[0]*2**24+tmp[1]*2**16+tmp[2]*2**8+tmp[3]
        return IpInteger
    
    def ToNumber(self,n,offset):
        n10=(n>>(offset+4))&0xf
        n1=(n>>(offset))&0xf
        return n10 * 16 + n1

    def VauleToIp(self, address):
        return f"{self.ToNumber(address,24)}.{self.ToNumber(address,16)}.{self.ToNumber(address,8)}.{self.ToNumber(address,0)}"
        
    def Calculate(self,formatCIDR):
        tmp1,tmp2=formatCIDR.split('/')
        ip=self.IpToVaule(tmp1)
        mask=sln.GetIpMask(int(tmp2))
        return self.GetNetworkAddress(ip,mask), self.GetBroadcastAddress(ip,mask)
 
ip = input()
sln=IpMaskCalculator()  
networkAddress,broadcastAddress=sln.Calculate(ip)   
print(sln.ShowIpAddress(networkAddress))
print(sln.ShowIpAddress(broadcastAddress)) 
        
        
sln=IpMaskCalculator()    
assert 255==sln.ToNumber(0b11111111,0)     
assert 127==sln.ToNumber(0b01111111,0) 
assert 7==sln.ToNumber(0b000001111111,4) 
assert 5==sln.ToNumber(0b000101111111,6)          
assert 0xff000000==sln.GetIpMask(8)            
assert 0xffffff00==sln.GetIpMask(24)  
assert 0b11000000101010000000000000000000==sln.GetNetworkAddress(0b11000000101010000000000000001111,0b11111111111111111111111100000000)  
assert 0b11000000101010000000000011111111==sln.GetBroadcastAddress(0b11000000101010000000000000001111,0b11111111111111111111111100000000)  
assert 0x000000ff==sln.IpToVaule("0.0.0.255")  
assert 0xffff0110==sln.IpToVaule("255.255.1.16") 
assert "192.168.0.15"==sln.VauleToIp(0b11000000101010000000000000001111) 
assert "192.168.0.0"==sln.VauleToIp(sln.IpToVaule("192.168.0.0")) 
assert "10.0.1.0"==sln.VauleToIp(sln.GetNetworkAddress(sln.IpToVaule("10.0.1.34"),sln.GetIpMask(24)))