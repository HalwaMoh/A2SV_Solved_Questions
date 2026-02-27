class Solution(object):
    def characterReplacement(self, s, k):

        from collections import Counter
        left = 0
        freq = Counter()
        maxFreq = 0
        ans = 0

        for right in range(len(s)):

            freq[s[right]] += 1
            maxFreq = max(maxFreq, freq[s[right]])

            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
