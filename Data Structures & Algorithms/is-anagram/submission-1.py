class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_s={}
        char_t={}

        if len(s)!=len(t):
            return False

        for char in s:
            char_s[char]=char_s.get(char,0)

        for char in t:
            char_t[char]=char_t.get(char,0)
        
        is_anagram=(char_s==char_t)
        return is_anagram

        