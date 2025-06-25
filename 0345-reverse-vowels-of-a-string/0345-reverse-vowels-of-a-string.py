class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        lt, rt = 0 , len(s) - 1

        while lt < rt:
            if chars[lt] not in vowels:
                lt += 1
                continue
            if chars[rt] not in vowels:
                rt -= 1
                continue

            chars[lt], chars[rt] = chars[rt], chars[lt]
            lt +=1 
            rt -=1
        
        return ''.join(chars)