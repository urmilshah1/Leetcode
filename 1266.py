class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        counter = 0
        for i in range(length -1):
            j = i+1
            point1X = points[i][0]
            point1Y = points[i][1]
            point2X = points[j][0]
            point2Y = points[j][1]
            X = abs(point2X-point1X)
            Y = abs(point2Y-point1Y)
            counter += max(X, Y)
        return counter