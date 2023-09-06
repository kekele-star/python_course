''' Create a program that takes an IP address entered at the keyboard
 and prints out the number of segmenets it contains, and the length of each segment.
 
 An IP address consists of 4 numbers, separated from each other with a full stop. But
 your program should just count however many are entered
 Examples of the input you may get are:
 127.0.0.1
 .192.0.123456.255
 172.16
 255
 
 So your program should work even with invalid IP Addresses. We're just interested in the 
 number of segments and how long each one is.
 
 Once you have a working program, here are some more suggestions for invalid input to test:
 .123.45.679.91
 123.4567.8.9
 123.156.289,10123456
 10.10t.10.10
 12.9.34.6.12.90

 '' - that is, press enter without typing anything

 This challenge is intended to practice for loops and if/else statements, so although
 you could use other techniques(such as splitting the string up), that's not the 
 approach we're looking for here.
 '''

ip_address = input(" An IP address consists of 4 numbers, separated from each other with a full stop: ")
if ip_address[-1] != ".":
    ip_address += "."

segment = 1
segment_length = 0

for character in ip_address:
    if character == ".":
        print(f"segment {segment} contains {segment_length} characters")
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

#unless the final character in the string was a dot, then we haven't printed the last segment
# if character != ".":
#     print(f"segment {segment} contains {segment_length} characters")
