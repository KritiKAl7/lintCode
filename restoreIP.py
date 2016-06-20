def restoreIP(s):
    if len(s) > 12 or not s:
        return []
    res = []
    generate(s, 0, 0, "", res)
    return res

#length: current segments of solution
def generate(s, index, length, solution, res):
    if index >= len(s):
        return
    if length == 3:
        #there are already 4 segments of numbers
        #see if the remaining is valid
        #if so, the solution is valid
        if isValid(s[index:]):
            res.append(solution + "." + s[index:])
        return
    i = 1
    while i <= 4 and i+index < len(s):
        #for each segment of s[index:index+i]
        #see if its valid if valid, append to solution
        tstring = s[index:i+index]
        if isValid(tstring):
            if length == 0:
                generate(s, index+i, length+1, tstring, res)
            else:
                generate(s, index+i, length+1, solution+"."+tstring, res)
        i += 1


def isValid(s):
    if s == "0":
        return True
    return int(s) < 256 and s[0] != "0"

print restoreIP("25525511135")