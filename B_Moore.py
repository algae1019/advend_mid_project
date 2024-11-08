### B_M_Algorithm ###
class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.shift_BadChar = self.build_BadChar()
        self.shift_GoodSfx = self.build_GoodSfx()

    def build_BadChar(self):
        bad_chars = {}
        for i in range(len(self.pattern) - 1):
            bad_chars[self.pattern[i]] = len(self.pattern) - 1 - i
        return bad_chars
    
    def build_GoodSfx(self):
        m = len(self.pattern)
        good_suffixs = [m] * m
        z = [0] * (m + 1)

        l, r, z[m] = m, m, m
        for i in range(m - 1, 0, -1):
            if i > r:
                l, r = i, i
                while r > 0 and self.pattern[r - 1] == self.pattern[m - (l - r + 1)]:
                    r -= 1
                z[i] = l - r
            else:
                k = i - l
                if z[k] < i - r:
                    z[i] = z[k]
                else:
                    l = i
                    #print(f"r: {r}, l: {l}, m: {m}, r - 1: {r - 1}, index: {m - (l - r + 1)}")
                    while r > 0 and (m - (l - r + 1)) >= 0 and (m - (l - r + 1)) < m and self.pattern[r - 1] == self.pattern[m - (l - r + 1)]:
                        r -= 1
                    z[i] = l - r

        for j in range(m - 1, -1, -1):
            if z[j] == j:
                for i in range(m - j):
                    if i < m and good_suffixs[i] == m:
                        good_suffixs[i] = m - j

        for j in range(m - 1):
            if 0 <= m - z[j] < m:
                good_suffixs[m - z[j]] = m - j - 1

        return good_suffixs
    

    def search(self, text):
        m, n = len(self.pattern), len(text)
        i, j = 0, m - 1
        results = []

        while i <= n - m:
            while j >= 0 and self.pattern[j] == text[i + j]:
                j -= 1

            if j < 0:
                results.append(i)
                i += self.shift_GoodSfx[0] if i + m < n else 1
            else:
                bc_shift = self.shift_BadChar.get(text[i + j], m)
                if j + 1 < len(self.shift_GoodSfx):
                    gs_shift = self.shift_GoodSfx[j + 1]
                else:
                    gs_shift = 1
                i += max(bc_shift, gs_shift)
            j = m - 1

        return results