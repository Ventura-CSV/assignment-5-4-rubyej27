isspace = lambda v: True if v == " " or v == "\t" or v == "\n" else False

def mystrip(strval):
   strip = ''
   for v in strval:
       if not isspace(v):
           strip += v
   return strip


strval = 'Python Programming\t Section 1\n'
ret = mystrip(strval)
print(ret)
