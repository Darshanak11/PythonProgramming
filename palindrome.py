def is_palindrome(s):
        s=s.lower().replace('','')
        return s==s[::-1]
test_string="A man a plan a canal panama"
if is_palindrome(test_string):
        print(f'"{test_string}"is a palindrome.')
else:
        print(f'"{test_string}"is not a palindrome.')