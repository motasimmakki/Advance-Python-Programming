def isValid(s):
    if s.count('.') != 3:
        return 0
    s1 = s.split('.')
    # print(s1)
    for i in s1:
        if (not i.isdigit()) or (int(i) < 0) or (int(i) > 255):
            return 0
        if (i[0] == '0') and (len(i) == 1):
            return 1
        if (i[0] == '0') and (len(i) != 1):
            return 0
    return 1

# Test Cases:
ip = "222.111.111.111"
# ip = "5555..555"
# ip = "x.0.0.0"

if isValid(ip):
    print(ip, "is a valid IPv4 address.")
else:
    print(ip, "is Invalid IPv4 address.")
