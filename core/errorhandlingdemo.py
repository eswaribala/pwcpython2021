#read ctc

try:
    ctc = int(input("Enter CTC"))
    print("CTC=%d" %(ctc))
except ValueError as err:
    print("CTC should be number",err)