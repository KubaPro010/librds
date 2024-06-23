class RDSCharsetError(Exception): pass
class RDSCharset:
    """Encoding puposes only: Translates UTF-8 into RDS"""
    @staticmethod
    def translate(character:str) -> int:
        if not type(character) == str: raise RDSCharsetError("Input is not a string")
        elif len(character) != 1: raise RDSCharsetError("This accepts only 1 character.")
        out = 0
        match ord(character):
            case 0xa1: out = 0x8e #INVERTED EXCLAMATION MARK
            case 0xa3: out = 0xaa #POUND SIGN
            case 0xa7: out = 0xbf #SECTION SIGN
            case 0xa9: out = 0xa2 #COPYRIGHT SIGN
            case 0xaa: out = 0xa0 #FEMININE ORDINAL INDICATOR
            case 0xb0: out = 0xbb #DEGREE SIGN
            case 0xb1: out = 0xb4 #PLUS-MINUS SIGN
            case 0xba: out = 0xb0 #MASCULINE ORDINAL INDICATOR
            case 0xb9: out = 0xb1 #SUPERSCRIPT ONE
            case 0xb2: out = 0xb2 #SUPERSCRIPT TWO
            case 0xb3: out = 0xb3 #SUPERSCRIPT THREE
            case 0xb5: out = 0xb8 #MIKRO SIGN
            case 0xbc: out = 0xbc #VULGAR FRACTION ONE QUARTER
            case 0xbd: out = 0xbd #VULGAR FRACTION ONE HALF
            case 0xbe: out = 0xbe #VULGAR FRACTION THREE QUARTERS
            case 0xbf: out = 0xb9 #INVERTED QUESTION MARK
            case 0x80: out = 0xc1 #LATIN CAPITAL LETTER A WITH GRAVE
            case 0x81: out = 0xc0 #LATIN CAPITAL LETTER A WITH ACUTE
            case 0x82: out = 0xd0 #LATIN CAPITAL LETTER A WITH CIRCUMFLEX
            case 0x83: out = 0xe0 #LATIN CAPITAL LETTER A WITH TILDE
            case 0x84: out = 0xd1 #LATIN CAPITAL LETTER A WITH DIAERESIS
            case 0x85: out = 0xe1 #LATIN CAPITAL LETTER A WITH RING ABOVE
            case 0x86: out = 0xe2 #LATIN CAPITAL LETTER AE
            case 0x87: out = 0x8b #LATIN CAPITAL LETTER C WITH CEDILLA
            case 0x88: out = 0xc3 #LATIN CAPITAL LETTER E WITH GRAVE
            case 0x89: out = 0xc2 #LATIN CAPITAL LETTER E WITH ACUTE
            case 0x8a: out = 0xd2 #LATIN CAPITAL LETTER E WITH CIRCUMFLEX
            case 0x8b: out = 0xd3 #LATIN CAPITAL LETTER E WITH DIAERESIS
            case 0x8c: out = 0xc5 #LATIN CAPITAL LETTER I WITH GRAVE
            case 0x8d: out = 0xc4 #LATIN CAPITAL LETTER I WITH ACUTE
            case 0x8e: out = 0xd4 #LATIN CAPITAL LETTER I WITH CIRCUMFLEX
            case 0x8f: out = 0xd5 #LATIN CAPITAL LETTER I WITH DIAERESIS
            case 0x90: out = 0xce #LATIN CAPITAL LETTER ETH
            case 0x91: out = 0x8a #LATIN CAPITAL LETTER N WITH TILDE
            case 0x92: out = 0xc7 #LATIN CAPITAL LETTER O WITH GRAVE
            case 0x93: out = 0xc6 #LATIN CAPITAL LETTER O WITH ACUTE
            case 0x94: out = 0xd6 #LATIN CAPITAL LETTER O WITH CIRCUMFLEX
            case 0x95: out = 0xe6 #LATIN CAPITAL LETTER O WITH TILDE
            case 0x96: out = 0xd7 #LATIN CAPITAL LETTER O WITH DIAERESIS
            case 0x98: out = 0xe7 #LATIN CAPITAL LETTER O WITH STROKE
            case 0x99: out = 0xc9 #LATIN CAPITAL LETTER U WITH GRAVE
            case 0x9a: out = 0xc8 #LATIN CAPITAL LETTER U WITH ACUTE
            case 0x9b: out = 0xd8 #LATIN CAPITAL LETTER U WITH CIRCUMFLEX
            case 0x9c: out = 0xd9 #LATIN CAPITAL LETTER U WITH DIAERESIS
            case 0x9d: out = 0xe5 #LATIN CAPITAL LETTER Y WITH ACUTE
            case 0x9e: out = 0xe8 #LATIN CAPITAL LETTER THORN
            case 0xa0: out = 0x81 #LATIN SMALL LETTER A WITH GRAVE
            case 0xa1: out = 0x80 #LATIN SMALL LETTER A WITH ACUTE
            case 0xa2: out = 0x90 #LATIN SMALL LETTER A WITH CIRCUMFLEX
            case 0xa3: out = 0xf0 #LATIN SMALL LETTER A WITH TILDE
            case 0xa4: out = 0x91 #LATIN SMALL LETTER A WITH DIAERESIS
            case 0xa5: out = 0xf1 #LATIN SMALL LETTER A WITH RING ABOVE
            case 0xa6: out = 0xf2 #LATIN SMALL LETTER AE
            case 0xa7: out = 0x9b #LATIN SMALL LETTER C WITH CEDILLA
            case 0xa8: out = 0x83 #LATIN SMALL LETTER E WITH GRAVE
            case 0xa9: out = 0x82 #LATIN SMALL LETTER E WITH ACUTE
            case 0xaa: out = 0x92 #LATIN SMALL LETTER E WITH CIRCUMFLEX
            case 0xab: out = 0x93 #LATIN SMALL LETTER E WITH DIAERESIS
            case 0xac: out = 0x85 #LATIN SMALL LETTER I WITH GRAVE
            case 0xad: out = 0x84 #LATIN SMALL LETTER I WITH ACUTE
            case 0xae: out = 0x94 #LATIN SMALL LETTER I WITH CIRCUMFLEX
            case 0xaf: out = 0x95 #LATIN SMALL LETTER I WITH DIAERESIS
            case 0xb0: out = 0xef #LATIN SMALL LETTER ETH
            case 0xb1: out = 0x9a #LATIN SMALL LETTER N WITH TILDE
            case 0xb2: out = 0x87 #LATIN SMALL LETTER O WITH GRAVE
            case 0xb3: out = 0x86 #LATIN SMALL LETTER O WITH ACUTE
            case 0xb4: out = 0x96 #LATIN SMALL LETTER O WITH CIRCUMFLEX
            case 0xb5: out = 0xf6 #LATIN SMALL LETTER O WITH TILDE
            case 0xb6: out = 0x97 #LATIN SMALL LETTER O WITH DIAERESIS
            case 0xb7: out = 0xba #DIVISION SIGN
            case 0xb8: out = 0xf7 #LATIN SMALL LETTER O WITH STROKE
            case 0xb9: out = 0x89 #LATIN SMALL LETTER U WITH GRAVE
            case 0xba: out = 0x88 #LATIN SMALL LETTER U WITH ACUTE
            case 0xbb: out = 0x98 #LATIN SMALL LETTER U WITH CIRCUMFLEX
            case 0xbc: out = 0x99 #LATIN SMALL LETTER U WITH DIAERESIS
            case 0xbd: out = 0xf5 #LATIN SMALL LETTER Y WITH ACUTE
            case 0xbe: out = 0xf8 #LATIN SMALL LETTER THORN
            case 0x87: out = 0xfb #LATIN SMALL LETTER C WITH ACUTE
            case 0x8c: out = 0xcb #LATIN CAPITAL LETTER C WITH CARON
            case 0x8d: out = 0xdb #LATIN SMALL LETTER C WITH CARON
            case 0x91: out = 0xde #LATIN SMALL LETTER D WITH STROKE
            case 0x9b: out = 0xa5 #LATIN SMALL LETTER E WITH CARON
            case 0xb0: out = 0xb5 #LATIN CAPITAL LETTER I WITH DOT ABOVE
            case 0xb1: out = 0x9f #LATIN SMALL LETTER DOTLESS I
            case 0xb2: out = 0x8f #LATIN CAPITAL LIGATURE IJ
            case 0xb3: out = 0x9f #LATIN SMALL LIGATURE IJ
            case 0xbf: out = 0xcf #LATIN CAPITAL LETTER L WITH MIDDLE DOT
            case 0x80: out = 0xdf #LATIN SMALL LETTER L WITH MIDDLE DOT
            case 0x84: out = 0xb6 #LATIN SMALL LETTER N WITH ACUTE
            case 0x88: out = 0xa6 #LATIN SMALL LETTER N WITH CARON
            case 0x8a: out = 0xe9 #LATIN CAPITAL LETTER ENG
            case 0x8b: out = 0xf9 #LATIN SMALL LETTER ENG
            case 0x91: out = 0xa7 #LATIN SMALL LETTER O WITH DOUBLE ACUTE
            case 0x92: out = 0xe3 #LATIN CAPITAL LIGATURE OE
            case 0x93: out = 0xf3 #LATIN SMALL LIGATURE OE
            case 0x94: out = 0xea #LATIN CAPITAL LETTER R WITH ACUTE
            case 0x95: out = 0xfa #LATIN SMALL LETTER R WITH ACUTE
            case 0x98: out = 0xca #LATIN CAPITAL LETTER R WITH CARON
            case 0x99: out = 0xda #LATIN SMALL LETTER R WITH CARON
            case 0x9a: out = 0xec #LATIN CAPITAL LETTER S WITH ACUTE
            case 0x9b: out = 0xfc #LATIN SMALL LETTER S WITH ACUTE
            case 0x9e: out = 0x8c #LATIN CAPITAL LETTER S WITH CEDILLA
            case 0x9f: out = 0x9c #LATIN SMALL LETTER S WITH CEDILLA
            case 0xa0: out = 0xcc #LATIN CAPITAL LETTER S WITH CARON
            case 0xa1: out = 0xdc #LATIN SMALL LETTER S WITH CARON
            case 0xa6: out = 0xee #LATIN CAPITAL LETTER T WITH STROKE
            case 0xa7: out = 0xfe #LATIN SMALL LETTER T WITH STROKE
            case 0xb1: out = 0xb7 #LATIN SMALL LETTER U WITH DOUBLE ACUTE
            case 0xb5: out = 0xf4 #LATIN SMALL LETTER W WITH CIRCUMFLEX
            case 0xb7: out = 0xe4 #LATIN SMALL LETTER Y WITH CIRCUMFLEX
            case 0xb9: out = 0xed #LATIN CAPITAL LETTER Z WITH ACUTE
            case 0xba: out = 0xfd #LATIN SMALL LETTER Z WITH ACUTE
            case 0xbd: out = 0xcd #LATIN CAPITAL LETTER Z WITH CARON
            case 0xbe: out = 0xdd #LATIN SMALL LETTER Z WITH CARON
            case 0xa6: out = 0xa4 #LATIN CAPITAL LETTER G WITH CARON
            case 0xa7: out = 0x9d #LATIN SMALL LETTER G WITH CARON
            case 0xb1: out = 0xa1 #GREEK SMALL LETTER ALPHA
            case 0xb2: out = 0x8d #GREEK SMALL LETTER BETA
            case 0x80: out = 0xa8 #GREEK SMALL LETTER PI
            case 0x24: out = 0xab #DOLLAR SIGN
            case _: out = ord(character)
        return out

class RDSCharsetDecode:
    """Decoding puposes only: Translates RDS into UTF-8"""
    @staticmethod
    def translate(value:int) -> str: #thx chatgpt
        if not isinstance(value, int): raise RDSCharsetError("Input is not an integer")
        if value < 0 or value > 255: raise RDSCharsetError("Input must be a byte (0-255).")
        character = None
        match value:
            case 0x8e: character = 0xa1 #INVERTED EXCLAMATION MARK
            case 0xaa: character = 0xa3 #POUND SIGN
            case 0xbf: character = 0xa7 #SECTION SIGN
            case 0xa2: character = 0xa9 #COPYRIGHT SIGN
            case 0xa0: character = 0xaa #FEMININE ORDINAL INDICATOR
            case 0xbb: character = 0xb0 #DEGREE SIGN
            case 0xb4: character = 0xb1 #PLUS-MINUS SIGN
            case 0xb0: character = 0xba #MASCULINE ORDINAL INDICATOR
            case 0xb1: character = 0xb9 #SUPERSCRIPT ONE
            case 0xb2: character = 0xb2 #SUPERSCRIPT TWO
            case 0xb3: character = 0xb3 #SUPERSCRIPT THREE
            case 0xb8: character = 0xb5 #MIKRO SIGN
            case 0xbc: character = 0xbc #VULGAR FRACTION ONE QUARTER
            case 0xbd: character = 0xbd #VULGAR FRACTION ONE HALF
            case 0xbe: character = 0xbe #VULGAR FRACTION THREE QUARTERS
            case 0xb9: character = 0xbf #INVERTED QUESTION MARK
            case 0xc1: character = 0x80 #LATIN CAPITAL LETTER A WITH GRAVE
            case 0xc0: character = 0x81 #LATIN CAPITAL LETTER A WITH ACUTE
            case 0xd0: character = 0x82 #LATIN CAPITAL LETTER A WITH CIRCUMFLEX
            case 0xe0: character = 0x83 #LATIN CAPITAL LETTER A WITH TILDE
            case 0xd1: character = 0x84 #LATIN CAPITAL LETTER A WITH DIAERESIS
            case 0xe1: character = 0x85 #LATIN CAPITAL LETTER A WITH RING ABOVE
            case 0xe2: character = 0x86 #LATIN CAPITAL LETTER AE
            case 0x8b: character = 0x87 #LATIN CAPITAL LETTER C WITH CEDILLA
            case 0xc3: character = 0x88 #LATIN CAPITAL LETTER E WITH GRAVE
            case 0xc2: character = 0x89 #LATIN CAPITAL LETTER E WITH ACUTE
            case 0xd2: character = 0x8a #LATIN CAPITAL LETTER E WITH CIRCUMFLEX
            case 0xd3: character = 0x8b #LATIN CAPITAL LETTER E WITH DIAERESIS
            case 0xc5: character = 0x8c #LATIN CAPITAL LETTER I WITH GRAVE
            case 0xc4: character = 0x8d #LATIN CAPITAL LETTER I WITH ACUTE
            case 0xd4: character = 0x8e #LATIN CAPITAL LETTER I WITH CIRCUMFLEX
            case 0xd5: character = 0x8f #LATIN CAPITAL LETTER I WITH DIAERESIS
            case 0xce: character = 0x90 #LATIN CAPITAL LETTER ETH
            case 0x8a: character = 0x91 #LATIN CAPITAL LETTER N WITH TILDE
            case 0xc7: character = 0x92 #LATIN CAPITAL LETTER O WITH GRAVE
            case 0xc6: character = 0x93 #LATIN CAPITAL LETTER O WITH ACUTE
            case 0xd6: character = 0x94 #LATIN CAPITAL LETTER O WITH CIRCUMFLEX
            case 0xe6: character = 0x95 #LATIN CAPITAL LETTER O WITH TILDE
            case 0xd7: character = 0x96 #LATIN CAPITAL LETTER O WITH DIAERESIS
            case 0xe7: character = 0x98 #LATIN CAPITAL LETTER O WITH STROKE
            case 0xc9: character = 0x99 #LATIN CAPITAL LETTER U WITH GRAVE
            case 0xc8: character = 0x9a #LATIN CAPITAL LETTER U WITH ACUTE
            case 0xd8: character = 0x9b #LATIN CAPITAL LETTER U WITH CIRCUMFLEX
            case 0xd9: character = 0x9c #LATIN CAPITAL LETTER U WITH DIAERESIS
            case 0xe5: character = 0x9d #LATIN CAPITAL LETTER Y WITH ACUTE
            case 0xe8: character = 0x9e #LATIN CAPITAL LETTER THORN
            case 0x81: character = 0xa0 #LATIN SMALL LETTER A WITH GRAVE
            case 0x80: character = 0xa1 #LATIN SMALL LETTER A WITH ACUTE
            case 0x90: character = 0xa2 #LATIN SMALL LETTER A WITH CIRCUMFLEX
            case 0xf0: character = 0xa3 #LATIN SMALL LETTER A WITH TILDE
            case 0x91: character = 0xa4 #LATIN SMALL LETTER A WITH DIAERESIS
            case 0xf1: character = 0xa5 #LATIN SMALL LETTER A WITH RING ABOVE
            case 0xf2: character = 0xa6 #LATIN SMALL LETTER AE
            case 0x9b: character = 0xa7 #LATIN SMALL LETTER C WITH CEDILLA
            case 0x83: character = 0xa8 #LATIN SMALL LETTER E WITH GRAVE
            case 0x82: character = 0xa9 #LATIN SMALL LETTER E WITH ACUTE
            case 0x92: character = 0xaa #LATIN SMALL LETTER E WITH CIRCUMFLEX
            case 0x93: character = 0xab #LATIN SMALL LETTER E WITH DIAERESIS
            case 0x85: character = 0xac #LATIN SMALL LETTER I WITH GRAVE
            case 0x84: character = 0xad #LATIN SMALL LETTER I WITH ACUTE
            case 0x94: character = 0xae #LATIN SMALL LETTER I WITH CIRCUMFLEX
            case 0x95: character = 0xaf #LATIN SMALL LETTER I WITH DIAERESIS
            case 0xef: character = 0xb0 #LATIN SMALL LETTER ETH
            case 0x9a: character = 0xb1 #LATIN SMALL LETTER N WITH TILDE
            case 0x87: character = 0xb2 #LATIN SMALL LETTER O WITH GRAVE
            case 0x86: character = 0xb3 #LATIN SMALL LETTER O WITH ACUTE
            case 0x96: character = 0xb4 #LATIN SMALL LETTER O WITH CIRCUMFLEX
            case 0xf6: character = 0xb5 #LATIN SMALL LETTER O WITH TILDE
            case 0x97: character = 0xb6 #LATIN SMALL LETTER O WITH DIAERESIS
            case 0xba: character = 0xb7 #DIVISION SIGN
            case 0xf7: character = 0xb8 #LATIN SMALL LETTER O WITH STROKE
            case 0x89: character = 0xb9 #LATIN SMALL LETTER U WITH GRAVE
            case 0x88: character = 0xba #LATIN SMALL LETTER U WITH ACUTE
            case 0x98: character = 0xbb #LATIN SMALL LETTER U WITH CIRCUMFLEX
            case 0x99: character = 0xbc #LATIN SMALL LETTER U WITH DIAERESIS
            case 0xf5: character = 0xbd #LATIN SMALL LETTER Y WITH ACUTE
            case 0xf8: character = 0xbe #LATIN SMALL LETTER THORN
            case 0xfb: character = 0x87 #LATIN SMALL LETTER C WITH ACUTE
            case 0xcb: character = 0x8c #LATIN CAPITAL LETTER C WITH CARON
            case 0xdb: character = 0x8d #LATIN SMALL LETTER C WITH CARON
            case 0xde: character = 0x91 #LATIN SMALL LETTER D WITH STROKE
            case 0xa5: character = 0x9b #LATIN SMALL LETTER E WITH CARON
            case 0xb5: character = 0xb0 #LATIN CAPITAL LETTER I WITH DOT ABOVE
            case 0x9f: character = 0xb1 #LATIN SMALL LETTER DOTLESS I
            case 0x8f: character = 0xb2 #LATIN CAPITAL LIGATURE IJ
            case 0x9f: character = 0xb3 #LATIN SMALL LIGATURE IJ
            case 0xcf: character = 0xbf #LATIN CAPITAL LETTER L WITH MIDDLE DOT
            case 0xdf: character = 0x80 #LATIN SMALL LETTER L WITH MIDDLE DOT
            case 0xb6: character = 0x84 #LATIN SMALL LETTER N WITH ACUTE
            case 0xa6: character = 0x88 #LATIN SMALL LETTER N WITH CARON
            case 0xe9: character = 0x8a #LATIN CAPITAL LETTER ENG
            case 0xf9: character = 0x8b #LATIN SMALL LETTER ENG
            case 0xa7: character = 0x91 #LATIN SMALL LETTER O WITH DOUBLE ACUTE
            case 0xe3: character = 0x92 #LATIN CAPITAL LIGATURE OE
            case 0xf3: character = 0x93 #LATIN SMALL LIGATURE OE
            case 0xea: character = 0x94 #LATIN CAPITAL LETTER R WITH ACUTE
            case 0xfa: character = 0x95 #LATIN SMALL LETTER R WITH ACUTE
            case 0xca: character = 0x98 #LATIN CAPITAL LETTER R WITH CARON
            case 0xda: character = 0x99 #LATIN SMALL LETTER R WITH CARON
            case 0xec: character = 0x9a #LATIN CAPITAL LETTER S WITH ACUTE
            case 0xfc: character = 0x9b #LATIN SMALL LETTER S WITH ACUTE
            case 0x8c: character = 0x9e #LATIN CAPITAL LETTER S WITH CEDILLA
            case 0x9c: character = 0x9f #LATIN SMALL LETTER S WITH CEDILLA
            case 0xcc: character = 0xa0 #LATIN CAPITAL LETTER S WITH CARON
            case 0xdc: character = 0xa1 #LATIN SMALL LETTER S WITH CARON
            case 0xee: character = 0xa6 #LATIN CAPITAL LETTER T WITH STROKE
            case 0xfe: character = 0xa7 #LATIN SMALL LETTER T WITH STROKE
            case 0xb7: character = 0xb1 #LATIN SMALL LETTER U WITH DOUBLE ACUTE
            case 0xf4: character = 0xb5 #LATIN SMALL LETTER W WITH CIRCUMFLEX
            case 0xe4: character = 0xb7 #LATIN SMALL LETTER Y WITH CIRCUMFLEX
            case 0xed: character = 0xb9 #LATIN CAPITAL LETTER Z WITH ACUTE
            case 0xfd: character = 0xba #LATIN SMALL LETTER Z WITH ACUTE
            case 0xcd: character = 0xbd #LATIN CAPITAL LETTER Z WITH CARON
            case 0xdd: character = 0xbe #LATIN SMALL LETTER Z WITH CARON
            case 0xa4: character = 0xa6 #LATIN CAPITAL LETTER G WITH CARON
            case 0x9d: character = 0xa7 #LATIN SMALL LETTER G WITH CARON
            case 0xa1: character = 0xb1 #GREEK SMALL LETTER ALPHA
            case 0x8d: character = 0xb2 #GREEK SMALL LETTER BETA
            case 0xa8: character = 0x80 #GREEK SMALL LETTER PI
            case 0xab: character = 0x24 #DOLLAR SIGN
            case _: character = value
        return chr(character) if character is not None else chr(value)
