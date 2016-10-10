#Convert hex to base64
import base64

while 1 :
    s = raw_input("Enter a hex string:\n").decode('hex')
    print("The base64 encoded of this string is : \n" + base64.b64encode(s) + "\n\n")