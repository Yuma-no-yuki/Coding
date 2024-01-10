class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        TOP=0
        TOP_product = 0
        for i in dimensions:
            s1=i[0]
            s2=i[1]
            Diagonal=(s1**2+s2**2)**0.5
            if Diagonal>TOP:
                TOP=Diagonal
                TOP_product = i[0]*i[1]
            if Diagonal==TOP and TOP_product < i[0]*i[1]:
                TOP_product = i[0]*i[1]
        return TOP_product
