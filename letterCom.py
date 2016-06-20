from collections import defaultdict
def letterCombination(digits):
    d = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"],
         "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"],
         "8":["t","u","v"], "9":["w","x","y","z"]}

    def combo(digits):
        if not digits:
            return [""]
        if len(digits) == 1:
            return d[digits]
        else:
            res = []
            solution = combo(digits[1:])
            for i in solution:
                for j in d[digits[0]]:
                    res.append(j + i)
            return res

    return sorted(combo(digits))

print letterCombination("2245")