class Solution(object):
    def imageSmoother(self, img):
        m = len(img)
        n = len(img[0])

        result = [[0]*n for _ in range(m)]

        directions = [-1, 0, 1]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                for dx in directions:
                    for dy in directions:
                        ni = i + dx
                        nj = j + dy

                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1

                result[i][j] = total // count

        return result
