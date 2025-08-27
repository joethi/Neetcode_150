class recursion:
    def sum_upto_n(self,n: int) -> int:

        return n + self.sum_upto_n(n-1)


