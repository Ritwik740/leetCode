class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        move = {'L':0, 'R':0, '_':0}
        for c in moves:
            move[c] += 1
        return abs(move['L'] - move['R']) + move['_']