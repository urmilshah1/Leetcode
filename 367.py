class Solution:
    def isPerfectSquare(self, num: int) -> bool:   
        square_root = num ** 0.5
        modulus_1 = square_root % 1
        is_perfect_square = modulus_1
        if (is_perfect_square == 0):
            return True
        else:
            return False
            
        