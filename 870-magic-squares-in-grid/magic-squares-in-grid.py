class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        if rows < 3 or cols < 3:return 0

        for k in range((rows - 2) * (cols - 2)):
            i = k // (cols - 2)
            j = k % (cols - 2)

            one   = grid[i][j]
            two   = grid[i][j+1]
            three = grid[i][j+2]
            four  = grid[i+1][j]
            five  = grid[i+1][j+1]
            six   = grid[i+1][j+2]
            seven = grid[i+2][j]
            eight = grid[i+2][j+1]
            nine  = grid[i+2][j+2]

            if 1 <= one <= 9 and 1 <= two <= 9 and 1 <= three <= 9 and \
               1 <= four <= 9 and 1 <= five <= 9 and 1 <= six <= 9 and \
               1 <= seven <= 9 and 1 <= eight <= 9 and 1 <= nine <= 9 and \
               len({one,two,three,four,five,six,seven,eight,nine}) == 9 and \
               one + two + three == four + five + six == seven + eight + nine == \
               one + four + seven == two + five + eight == three + six + nine == \
               one + five + nine == three + five + seven:
                count += 1

        return count
