class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        dic1={}
        for i in range(len(s)):
            if s[i] not in dic :
                dic[s[i]]=1
               
            else:
                dic[s[i]]+=1
        
        for i in range(len(t)):
            if t[i] not in dic1 :
                dic1[t[i]]=1
               
            else:
                dic1[t[i]]+=1        
                
        if dic==dic1:
            return True
        else:
            return False            

        