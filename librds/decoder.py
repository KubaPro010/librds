from enum import IntEnum
from .charset import RDSCharset
from .group import Group, dataclass

@dataclass
class Details:
    details=True

@dataclass
class PSDetails(Details):
    segment: int
    di: int
    ms: bool
    ta: bool
    text: str
@dataclass
class RTDetails(Details):
    segment: int
    ab: int
    text: str
@dataclass
class PTYNDetails(Details):
    segment: int
    ab: int
    text: str
    
@dataclass
class ECCLICDetails(Details):
    data:int
    is_lic:bool

@dataclass
class DecodedGroup:
    raw_group:Group
    pi: int
    tp: bool
    pty: int
    group: IntEnum
    details:Details

class GroupDecoder:
    def decode_0(self, group: Group, dgroup: DecodedGroup):
        segment = group.b & 3
        ta = (group.b >> 4) & 1
        ms = (group.b >> 3) & 1
        if segment == 3:
            di = (group.b >> 2) & 9
        else:
            di = 0
        details = PSDetails(segment,di,bool(ms),bool(ta),"")
        
        char_1 = (group.d >> 8) & 0xFF
        char_2 = group.d & 0xFF
        details.text += chr(char_1) #TODO: add charset decoding
        details.text += chr(char_2) #TODO: add charset decoding
        
        dgroup.details = details
        return group, dgroup
    def decode_2(self, group: Group, dgroup: DecodedGroup):
        dgroup.group = 2
        segment = group.b & 15
        ab = (group.b >> 4) & 1
        details = RTDetails(segment,ab,"")
        
        if not group.is_version_b:
            char_1 = (group.c >> 8) & 0xFF
            char_2 = group.c & 0xFF
            char_3 = (group.d >> 8) & 0xFF
            char_4 = group.d & 0xFF
            details.text += chr(char_1) #TODO: add charset decoding
            details.text += chr(char_2) #TODO: add charset decoding
            details.text += chr(char_3) #TODO: add charset decoding
            details.text += chr(char_4) #TODO: add charset decoding
        else:
            char_1 = (group.d >> 8) & 0xFF
            char_2 = group.d & 0xFF
            details.text += chr(char_1) #TODO: add charset decoding
            details.text += chr(char_2) #TODO: add charset decoding
        
        dgroup.details = details
        return group, dgroup
    def decode_1(self, group:Group, dgroup:DecodedGroup):
        dgroup.group = 1
        tmp = (group.c & 0xFF)
        details = ECCLICDetails(0,False)
        if ((tmp >> 4) & 0xF) != 14: 
            details.is_lic = True
            tmp = tmp & 0xFF
        details.data = tmp
        dgroup.details = details
        return group, dgroup
    def decode_10(self, group:Group, dgroup:DecodedGroup):
        dgroup.group = 10
        segment = group.b & 3
        ab = (group.b >> 4) & 1
        details = PTYNDetails(segment,ab,"")
        char_1 = (group.c >> 8) & 0xFF
        char_2 = group.c & 0xFF
        char_3 = (group.d >> 8) & 0xFF
        char_4 = group.d & 0xFF
        details.text += chr(char_1) #TODO: add charset decoding
        details.text += chr(char_2) #TODO: add charset decoding
        details.text += chr(char_3) #TODO: add charset decoding
        details.text += chr(char_4) #TODO: add charset decoding
        dgroup.details = details
        return group, dgroup
        
        
    def decode(self, group: Group):
        out = DecodedGroup(group,group.a,False,0,0,None)
        out.pty = ((group.b >> 5) & 31)
        out.tp = bool((group.b >> 10) & 1)
        gr = (group.b >> 12) & ((1 << 12) - 1)
        if group.is_version_b and gr != 0: gr -= 1
        match gr:
            case 0:
                group, out = self.decode_0(group, out)
            case 2:
                group, out = self.decode_2(group, out)
            case 1:
                group, out = self.decode_1(group, out)
            case 10:
                group, out = self.decode_10(group, out)
            case _:
                print(gr)
        return out
def test_decoder():
    dec = GroupDecoder()
    from .generator import GroupGenerator
    basic = GroupGenerator.basic(0x3000, tp=True, pty=10)
    ps = GroupGenerator.ps(basic, "radio95 ", 3,ta=True)
    psb = GroupGenerator.ps_b(basic, "radio95 ", 3,ta=True)
    rt = GroupGenerator.rt(basic,"hello!\r ",0)
    rtb = GroupGenerator.rt_b(basic,"hello!\r ",0)
    ecc = GroupGenerator.ecc(basic,0xe2)
    lic = GroupGenerator.lic(basic,0x20)
    ptyn = GroupGenerator.ptyn(basic, "Test".ljust(8), 0,ab=True)
    print("ps", dec.decode(ps))
    print("psb", dec.decode(psb))
    print("rt", dec.decode(rt))
    print("rtb", dec.decode(rtb))
    print("ecc", dec.decode(ecc))
    print("lic", dec.decode(lic))
    print("ptyn", dec.decode(ptyn))