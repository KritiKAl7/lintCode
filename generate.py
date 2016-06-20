def generateParenthesis(n):
    # Write your code here
    if n == 0:
        return []
    if n == 1:
        return ["()"]
    else:
        return generateN(n-1, ["()"])

def generateN(n, solution):
    if n == 0:
        return solution
    res = []
    for i in solution:
        for posa in range(len(i)):
            temp = i[:posa]+"("+i[posa:]
            btemp = temp
            for posb in range(posa+1, len(i)+1):
                result = temp[:posb] + ")" + temp[posb:]
                res.append(result)
                temp = btemp
    res = list(set(res))
    return generateN(n-1, res)

print generateParenthesis(4)

