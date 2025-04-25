# s değeri bize verilen bir stringdir. Bu string {[(])} bu parantez türlerini
# içeriyor amacımız bu parantezler düzgün sırada mı veriliyor onu kontrol etmek
# Örneğin () bu şekil veriliyorsa True döndürcek ya da ()[] bu şekil veriliyosa
# yine True döndürcek ya da ([{}]) bu şekilde veriliyorsa yine True döndürcek
# ancak (], ([]} bunun gibi bir ifade veriliyorsa False döndürcek
def isValid(s):
    stack = []
    pairs = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False
    return len(stack) == 0

print(isValid("({})"))
print(isValid("{[])"))