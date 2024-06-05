from enum import Enum, IntEnum

def get_from_list(input:list,index:int,default=None):
    """This is a simple function to remove index errors from the group generators"""
    try:
        return input[index]
    except IndexError:
        return default

def SubstituteCharacterAtPosition(string: str, char: str, index: int) -> str:
    """
    This is a helper function that works like 'string[index] = char' in C.

    :param string: String to process
    :param char: The character that is going to be at that position
    :param index: Index of the character
    :return: Modified string with the character at the specified index
    """
    if not isinstance(string, str) or not isinstance(char, str) or not isinstance(index, int):
        raise Exception("Invalid input types")
    if not (0 <= index < len(string)):
        raise IndexError("Index out of range")
    return string[:index] + char + string[index + 1:]

class BitManipulator:
    """
    This is a alternative to bitwising as its too complex to understand for me, so what did i do?
    This class can set/get bits of a number it a specific location using bin() and int(str,2)
    """
    @staticmethod
    def set_bit(value:int, bit:int, bit_value:bool, max_bits:int=16) -> int:
        """
        This function sets a single bit in a value

        :param value: Input int
        :param bit: The bit index to set
        :param bit_value: 0 or 1?
        :param max_bits: If you don't want unexpected indexerrors, then you can use this, this will pad the start of the bin string as 01 and 0000001 are the same thing
        """
        string = ("0"*(max_bits-(value.bit_length())))
        string += bin(value).removeprefix("-").removeprefix("0b")
        
        if bit > len(string): raise IndexError
        string = SubstituteCharacterAtPosition(string,("1" if bit_value else "0"),bit)
        return int(("0b"+string),2)
    @staticmethod
    def get_bit(value:int, bit:int, max_bits:int=16) -> int:
        string = ("0"*(max_bits-(value.bit_length())))
        string += bin(value).removeprefix("-").removeprefix("0b")
        return int(("0b"+string[bit]),2)
    @staticmethod
    def set_bits(value: int, bits: list[int], bit_values: list[int], max_bits: int = 16) -> int:
        print(bit_values)
        out = value
        for i, bit_pos in enumerate(bits):
            out = BitManipulator.set_bit(out, bit_pos, bit_values[i], max_bits)
        return out
    @staticmethod
    def get_bits(value: int, bits: int, index:int=0, max_bits:int=16) -> int:
        out = "0b"
        for i in range(bits):
            out += bin(BitManipulator.get_bit(value, (i+index), max_bits)).removeprefix("0b")
        return int(out,2)

def calculate_mjd(year: int, month: int, day:int):
    """
    :param year: e.x 2024
    :param month: (starts from 0) 0 - Jan, 1 - Feb ...
    :param day: (starts from 1)"""
    l = 1 if (month == 0 or month == 1) else 0
    return (
        14956 + day + 
        int(
            ((year - 1900) - l) * 365.25
        ) +
        int(
            (month + 2 + l * 12) * 30.6001
        )
    )

def calculate_ymd(mjd:int):
    """Returns the same format as calculate_mjd, so you can encode and decode without any conversions"""
    if mjd < 15079.0:
        raise Exception("Invalid MJD")
    jd = mjd + 2_400_001
    ljd = jd + 68569
    
    njd = int((4 * ljd / 146097))
    ljd = ljd - int(((146097 * njd + 3) / 4))
    
    year = int((4000 * (ljd + 1) / 1461001))
    ljd = ljd - int(((1461 * year / 4))) + 31
    
    month = int((80 * ljd / 2447))
    
    day = ljd - int((2447 * month / 80))
    
    ljd = int((month / 11))
    month = int((month + 2 - 12 * ljd))
    year = int((100 * (njd - 49) + year + ljd))
    return year, (month-1), day

def calculate_ctoffset_to_hrmin(offset:int) -> tuple[int,int]:
    """Returns the hour and minute offset of CT"""
    h = int((offset*30)/60)
    return h, int((offset*30)-(h*60))

class Groups(Enum):
    PS = 0
    PS_B = 1
    RT = 2
    RT_B = 3
    PTYN = 4
    ECC = 5
    LIC = 6
    TDC = 7
    TDC_B = 8
    IN_HOUSE = 9
    IN_HOUSE_B = 10
    EON = 11
    EON_B = 12
    ODA = 13
    ODA_AID = 14
    LONG_PS = 15

class GroupSequencer:
    """you can use this code to sequence though anything"""
    def __init__(self, sequence:list[IntEnum]) -> None:
        self.cur_idx = 1
        self.sequence = sequence
    def get_next(self):
        if len(self.sequence) == 0: return
        if self.cur_idx > len(self.sequence): self.cur_idx = 1
        prev = self.sequence[self.cur_idx-1]
        self.cur_idx += 1
        return prev
    def change_sequence(self, sequence:list[IntEnum]):
       self.sequence = sequence
       self.cur_idx = 1
    def __len__(self):
        return len(self.sequence)
    def __iter__(self):
        return self.sequence
