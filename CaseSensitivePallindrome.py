def is_palindrome(s):
    rs= s[::-1]
    i=0
    while i < len(rs):
        if rs[i] == s[i]:
            i+=1
        else :
          break
        
    if i == len(s):
        return True
    else:
        return False 
t= is_palindrome('malayAlam')
print(t)


