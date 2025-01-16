class Solution(object):
    def compress(self, chars):
        N = len(chars)

        r = 0 # reader
        w = 0 # writer
        while r < N:
			# count
            char = chars[r]
            count = 0
            while r < N and chars[r] == char:
                r += 1
                count += 1
			# write
            chars[w] = char
            w += 1
            if count > 1:
                for c in str(count):
                    chars[w] = c
                    w += 1
        print(chars)

        return w
