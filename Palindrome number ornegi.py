#Palindrome sayı bir sayının normal bir şekilde yazılışı ile
#tersten yazılışının aynı sayıya eşit olmasıdır.
#Örneğin 121 sayısını tersten yazılışı yine 121'dir
#ama -121'in tersten yazılışı 121-'dir yani palindrome değildir.
def isPalindrome(x):
    num = str(x)

    if len(num) == 1:
        return True

    z = 0

    x = len(num) - 1
    for i in range(len(num)):
        if x == i or x < i:
            break
        if num[i] == num[x]:
            x -= 1
            z += 1
        else:
            return False
    if len(num) / z == 2 or len(num) / z == 2.5 or len(num) / z == 3:
        return True

print(isPalindrome(121))
print(isPalindrome(123))
print(isPalindrome(1001))
print(isPalindrome(5))