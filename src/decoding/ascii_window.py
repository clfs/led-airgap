#!/usr/bin/env python3
"""Module string"""

import reedsolo
RS_CODEC_128 = reedsolo.RSCodec(16)

def main():
    """Docstring"""
    with open('binaryoutput.txt', 'r') as infile:
        data = "".join(infile.read().split())
    datalen = len(data)
    windowlen = 256
    with open('parsed.txt', 'w') as outfile:
        for startbit in range(datalen-windowlen):
            endbit = startbit + windowlen
            windowstr = data[startbit:endbit]
            windowbytes = bitstring_to_bytes(windowstr)
            outfile.write(str(startbit)+'\t')
            outfile.write(str(windowbytes)+'\n')
            outfile.write(str(startbit)+'\t')
            for idx in range(windowlen//8):
                outfile.write(windowstr[8*idx:8*(idx+1)]+' ')
            outfile.write('\n')
            #try:
            #    print(RS_CODEC_128.decode(windowbytes))
            #except:
            #    pass
    return

def bitstring_to_bytes(bitstr):
    """Convert bitstring "011010101....." to bytes"""
    return int(bitstr, 2).to_bytes((len(bitstr)+7) // 8, byteorder='big')

if __name__ == "__main__":
    main()
