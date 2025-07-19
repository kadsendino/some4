from manim import *


def CreateFloat(str : str):
    group = VGroup()

    #Creates Numbers and Sqaures for Number
    for i, bit in enumerate(str):
        sq = Square()
        if i == 0:
            sq.set_fill(RED, opacity=0.3)
        elif 1 <= i < 6:
            sq.set_fill(YELLOW, opacity=0.3)
        elif 6 <= i:
            sq.set_fill(BLUE, opacity=0.3)
        sq.shift(RIGHT * 2*i)
        txt = Text(bit).scale(0.5)
        txt.move_to(sq.get_center())
        group += sq 
        group += txt
    #Creates Text for 
    sign = Text("sign-Bit",color=RED)
    exponent = Text("exponent-Bits",color=YELLOW)
    mantissa = Text("mantissa-Bits",color=BLUE)
    group.to_edge(LEFT)
    #arranges sign to right place
    sign.shift(2*UP)
    sign.to_edge(LEFT)
    #arranges exponent to right place
    exponent.shift(2*UP)
    exponent.to_edge(LEFT)
    exponent.shift(RIGHT*4.5)
    #arranges mantissa to right place
    mantissa.shift(2*UP)
    mantissa.to_edge(LEFT)
    mantissa.shift(RIGHT*1.2*len(str))
    #adds text to VGroup
    group += sign
    group += exponent
    group += mantissa
    #scales to screen size
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    return group


class BitBlocks(Scene):
    def construct(self):
        binary_str = "0100010101001010"
        float_bin = CreateFloat(binary_str)
        float_bin.shift(DOWN*2)

        self.play(
            Create(float_bin))