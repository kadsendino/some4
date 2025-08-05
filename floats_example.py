class Float_Example(Scene):
    def construct(self):
        # Example 
        """ 
        10.75 -> Visualisierung 2^4 - 2^3 - 2^2 - 2^1 - 2^0 - 2^(-1) -  2^(-2) (1010.11)
        1010.11 -> 1.01011 shifts
        Char = Exp + Bias (Bias = 15)
        Sign Bit
        """
        exp = 1
        # Example 2
        """
        -255.03125 -> 11111111.00001
        11111111.00001  ⇒ 1.111111100001 (7 shifts needed)
        7 + 15 = 22 = 10110
        1 10110 1111111000
        """
        # Rest + Special Cases