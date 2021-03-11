'''Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]'''

#solution:
import math
def letterCombinations(n):
    dict={1:"",2:['a','b','c'],3:['d','e','f'],4:['g','h','k'],5:['j','k','l'],
          6:['m','n','o'], 7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
    result=[]
    m=n%10
    n=math.floor(n/10) #if n=23 then 
     #n = 2 & m= 3
    print(m)
    print(n)
    if n!=0 and (m!=1 or m!=0):
        for i in dict[int(n)]:
            print("for1")
                
            for j in dict[m]:
                print("for2")
                print("i,j ",i,j)
                print(result.append(i+j))
    else:
        for i in dict[m]:
            result.append(i)

    return result

s=letterCombinations(2)
print(s)