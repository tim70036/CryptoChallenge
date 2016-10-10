#Fixed XOR : Write a function that takes two equal-length buffers and produces their XOR combination.
while 1 : 
    s = raw_input("Input a hex string:\n")
    key = raw_input("Input a key:\n")
    
    s = int(s,16)
    key = int(key,16)
    ans = format(s ^ key , 'x')
    print("XOR combination is : \n" + ans + "\n\n")
