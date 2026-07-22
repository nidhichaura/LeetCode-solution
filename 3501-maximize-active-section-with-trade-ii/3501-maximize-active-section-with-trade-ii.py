class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * max(1, self.n))
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        self._build(data, 2 * node + 1, start, mid)
        self._build(data, 2 * node + 2, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, start, end, l, r):
        if r < start or end < l or l > r:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(2 * node + 1, start, mid, l, r)
        p2 = self.query(2 * node + 2, mid + 1, end, l, r)
        return max(p1, p2)


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones_all = s.count('1')
        
        pref_ones = [0] * (n + 1)
        for i in range(n):
            pref_ones[i + 1] = pref_ones[i] + (1 if s[i] == '1' else 0)
            
        def count_ones(l, r):
            return pref_ones[r + 1] - pref_ones[l]

 
        segments = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segments.append((s[i], i, j - 1))
            i = j
            
        m = len(segments)
        seg_idx = [0] * n
        for idx, (_, st_i, en_i) in enumerate(segments):
            for k in range(st_i, en_i + 1):
                seg_idx[k] = idx


        V = [0] * m
        for idx in range(1, m - 1):
            char, st_i, en_i = segments[idx]
            if char == '1' and segments[idx - 1][0] == '0' and segments[idx + 1][0] == '0':
                L = segments[idx - 1][2] - segments[idx - 1][1] + 1
                R = segments[idx + 1][2] - segments[idx + 1][1] + 1
                V[idx] = L + R

        st = SegmentTree(V)
        ans = []

        def check_candidate(idx, l, r, s_l, s_r):
            if idx < s_l or idx > s_r:
                return 0
            char, st_i, en_i = segments[idx]
            if char != '1' or st_i < l or en_i > r:
                return 0
            
            L = (st_i - max(l, segments[idx - 1][1])) if (idx - 1 >= s_l and segments[idx - 1][0] == '0') else 0
            R = (min(r, segments[idx + 1][2]) - en_i) if (idx + 1 <= s_r and segments[idx + 1][0] == '0') else 0
            
            return (L + R) if (L > 0 and R > 0) else 0

        for l, r in queries:
            ones_in_query = count_ones(l, r)
            ones_outside = total_ones_all - ones_in_query
            
            s_l = seg_idx[l]
            s_r = seg_idx[r]
            
            max_delta = 0
            

            if s_l + 2 <= s_r - 2:
                max_delta = max(max_delta, st.query(0, 0, m - 1, s_l + 2, s_r - 2))

   
            cand1 = s_l if segments[s_l][0] == '1' else s_l + 1
            max_delta = max(max_delta, check_candidate(cand1, l, r, s_l, s_r))
            
  
            cand2 = s_r if segments[s_r][0] == '1' else s_r - 1
            max_delta = max(max_delta, check_candidate(cand2, l, r, s_l, s_r))

            ans.append(ones_outside + ones_in_query + max_delta)

        return ans