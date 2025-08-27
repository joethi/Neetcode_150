class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1count, s2count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1   
            s2count[ord(s2[i]) - ord('a')] += 1
        print('s1:',s1)
        print('s2:',s2)    
        print("s1count:", s1count)
        print("s2count:", s2count)
        matches = 0    
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1
        print("matches:", matches)
        if matches == 26:
            return True
        for i in range(0,len(s2)-len(s1)):
            ind_sb = ord(s2[i]) - ord('a')
            s2count[ind_sb] -= 1
            if s2count[ind_sb] == s1count[ind_sb]:
                matches += 1
            else:
                matches -= 1        
            ind_ad = ord(s2[i+3]) - ord('a')
            s2count[ind_ad] += 1
            if s2count[ind_ad] == s1count[ind_ad]:
                matches += 1
            else:
                matches -= 1
            if matches == 26:
                return True
        return False


s1="abc"
s2="bbbca"
sol_obj = Solution()
print(sol_obj.checkInclusion(s1,s2))



