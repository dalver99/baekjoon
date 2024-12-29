while True:
    palindrome = input()
    ispalindrome = True
    if palindrome == '0':
        break
    for i in range (int(len(palindrome)/2)):
        if palindrome[i] != palindrome[-(i+1)]:
            ispalindrome = False
    
    if ispalindrome == True:
        print('yes')
    else:
        print('no')
            