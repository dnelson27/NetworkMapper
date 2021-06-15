from neomodel import StructuredNode, RelationshipTo
from neomodel.properties import StringProperty, ArrayProperty, IntegerProperty, uuid

class Ipv4Address:
    def __init__(self, ipAddress: str) -> None:
        self.address = ipAddress.split("/")[0]
        self.cidr = ipAddress.split("/")[1]
        self.mask = self.getSubnetMask(self.cidr)
        self.addressBits = list(self.binaryConvert(int(i)) for i in self.address.split("."))
        self.subnetMaskBits = list(self.binaryConvert(int(i)) for i in self.mask.split("."))
        # self.networkId = self.getNetworkId()

    def binaryConvert(self, num):
        binaryNumbers = [128, 64, 32, 16, 8, 4, 2, 1]
        resultNumber = ""
        for i in binaryNumbers:
            if num >= i:
                resultNumber += "1"
                num -= i
            else:
                resultNumber += "0"
        return resultNumber

    def getSubnetMask(self, cidr):
        bits = [0, 128, 192, 224, 240, 248, 252, 254, 255]
        cidr = int(cidr)
        mask = ""
        if cidr >= 8 and cidr < 16:
            cidr -= 8
            mask = "255." + str(bits[cidr]) + ".0.0"
        elif cidr >= 16 and cidr < 24:
            cidr -= 16
            mask = "255.255." + str(bits[cidr]) + ".0"
        elif cidr >= 16 and cidr <= 32:
            cidr -= 24
            mask = "255.255.255." + str(bits[cidr])
        else:
            print("Invalid Cidr")
        return mask

class NetworkHop(StructuredNode):
    sysId = StringProperty(unqiue_index=True, default=uuid)
    ipv4Address = StringProperty()
    dnsName = StringProperty()



