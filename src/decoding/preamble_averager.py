#!/usr/bin/env python3
"""Module string"""

BARKER = "1111100110101"

def main():
    """Doc string"""
    with open('binaryoutput.txt', 'r') as infile:
        data = ''.join(infile.read().split())
    likely_packets = []
    average_packet = []
    for idx in range(len(data) - len(BARKER)):
        section = data[idx:idx+len(BARKER)]
        if section == BARKER:
            likely_packets.append(data[idx:idx+269])
    for bit in range(269):
        running_sum = 0
        for packet in likely_packets:
            running_sum += int(packet[bit])
        if running_sum >= 135:
            average_packet.append('1')
        else:
            average_packet.append('0')
    print(''.join(average_packet))
    return

if __name__ == "__main__":
    main()
