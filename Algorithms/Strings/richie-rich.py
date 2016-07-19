'''
Given  and an -digit number, help Sandy determine the largest possible number she can make by changing  digits.

Note: Treat the integers as numeric strings. Leading zeros are permitted and can't be ignored (So 0011 is not a palindrome, 0110 is a valid palindrome). A digit can be modified more than once.

Input Format
The first line contains two space-separated integers,  (the number of digits in the number) and  (the maximum number of digits that can be altered), respectively. 
The second line contains an -digit string of numbers that Sandy must attempt to make palindromic.
'''
def richie_rich():
  len_s, tries = map(int, input().split(" "))
  number = list(input())
  change = 0
  for i in range(int(len_s/2)):
    if number[i] != number[len_s-1-i]:
      change += 1
  
  if change > tries:
    print("-1")
    
  else:
    change = 0
    ret = []
    for i in range(int(len_s/2)):
      if number[i] != number[len_s-1-i]:
        ret.append(i)
        if int(number[i]) > int(number[len_s-1-i]):
          number[len_s-1-i]=number[i]
        else:
          number[i] = number[len_s-1-i]
        change += 1

    i = 0

    while(tries-change > 0):
      if i <= len_s/2:
        if number[i] != '9':
          number[i] = '9'
          number[len_s-1 -i] = '9'
          if i in ret:
            change += 1
          else:
            change += 2
        i += 1
      else:
        break
          
    if len_s % 2 == 1 and tries-change > 0:
        number[len_s/2 + 1] = '9'
        change += 1
          
    print ("".join(str(num) for num in number))
      
richie_rich()