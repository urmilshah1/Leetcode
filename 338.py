class Solution:
    def countBits(self, num: int) -> List[int]:
        lis = []
        counter = 0
        for i in range(0, num+1):
            a = bin(i)[2:]
            if a.count("1"):
                lis.append(a.count("1"))
            else:
                lis.append(0)
        return lis