class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        ones = []
        zeros = []
        n = len(t)
        i = 0
        while i < n:
            start = i
            while i < n and t[i] == '1':
                i +=1
            ones.append(i - start)

            if i < n:
                start = i
                while i < n and t[i] == '0':
                    i += 1
                zeros.append(i - start)

        total_ones= sum(ones) - 2
        k = len(zeros)

        if k < 2:
            return total_ones  

        pref = [0] * k
        pref[0] = zeros[0]
        for j in range(1, k):
            pref[j] = max(pref[j - 1], zeros[j])
            
        suff = [0] * k
        suff[-1] = zeros[-1]
        for j in range(k - 2, -1, -1):
            suff[j] = max(suff[j + 1], zeros[j])
            
        max_delta = 0
        
       
        for idx in range(1, k):
            L_i = ones[idx]
            z_left = zeros[idx - 1]
            z_right = zeros[idx]
            
            
            other_max = 0
            if idx - 2 >= 0:
                other_max = max(other_max, pref[idx - 2])
            if idx + 1 < k:
                other_max = max(other_max, suff[idx + 1])
                
            delta = max(z_left + z_right, other_max - L_i)
            max_delta = max(max_delta, delta)
            
        return total_ones + max(0, max_delta)       

             
