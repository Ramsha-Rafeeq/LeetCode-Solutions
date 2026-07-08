class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"

        d1 = {}
        d2 = {}
        final = []

        for ch in text:
            d1[ch] = d1.get(ch, 0) + 1

        for ch in target:
            d2[ch] = d2.get(ch, 0) + 1

        for ch in d2:
            final.append(d1.get(ch, 0) // d2[ch])

        return min(final)
        