class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and keep only alphanumeric characters
        s = ''.join(char.lower() for char in s if char.isalnum())

        is_palindrome = True

        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                is_palindrome = False
                break
        
        return is_palindrome