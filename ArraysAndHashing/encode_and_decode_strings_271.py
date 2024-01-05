"""
659. Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode

Example 1
Input: ["lint","code","love","you"]
output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
"""

def decode(strs):
    res = []
    while ":" in strs:
        pos = strs.find(":")
        length = int(strs[:pos])
        strs = strs[pos+1:]
        word = strs[:length]
        strs = strs[length:]
        #strs += word  
        res.append(word)
    return res

def encode(strs):
 
    res = ""
    for word in strs:
        length = len(word)
        res += str(length) + ":" + word
    return res 

encoded = encode(["lint","code","love","you"])
print(encoded)

decoded = decode(encoded)
print(decoded)

