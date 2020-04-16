class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        ml=0
        for direction,amount in shift:
            if direction==0:
                ml+=amount
            else:
                ml-=amount
        ml=ml%len(s)
        return s[ml:]+s[:ml]
