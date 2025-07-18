from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class Formula(Scene):
    def construct(self):
        square = Square()
        square.set_fill(BLUE, opacity=0.3)
        number = MathTex(
            r"(-1)^{sign} \cdot useed^k \cdot 2^{exponent} \cdot (1+fraction)"
        )
        # self.play(Create(square))
        self.play(Create(number))
        square.shift(RIGHT)
        self.wait()


def BinarySequence(str :str):
    group = VGroup()
    for i, bit in enumerate(str):
        sq = Square()
        sq.set_fill(BLUE, opacity=0.3)
        sq.shift(RIGHT * 2*i)
        txt = Text(bit).scale(0.5)
        txt.move_to(sq.get_center())
        group += sq 
        group += txt
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    return group

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



def CreatePosit(str : str,es_value : int):
    group = VGroup()
    #TODO correct es_value to fit posit standart
    #Creates Numbers and Sqaures for Number
    for i, bit in enumerate(str):
        sq = Square(stroke_width=2)
        if i == 0:
            sq.set_fill(RED, opacity=0.3)
        elif 1 <= i < 1+es_value :
            sq.set_fill(GREEN, opacity=0.3)
        elif 1+es_value <= i <  1+es_value+2:
            sq.set_fill(YELLOW, opacity=0.3)
        elif 1+es_value+2 <= i:
            sq.set_fill(BLUE, opacity=0.3)
        sq.shift(RIGHT * 2*i)
        txt = Text(bit).scale(1.5)
        txt.move_to(sq.get_center())
        group += sq 
        group += txt
    #Creates Text for 
    sign = Text("sign-Bit",color=RED)
    regime = Text("regime-Bits",color=GREEN)
    exponent = Text("exponent-Bits",color=YELLOW)
    frac = Text("fraction-Bits",color=BLUE)
    group.to_edge(LEFT)
    #arranges sign to right place
    sign.shift(2*UP)
    sign.to_edge(LEFT)
    #arranges regime to right place
    regime.shift(2*UP)
    regime.to_edge(LEFT)
    regime.shift(RIGHT*3.5)
    #arranges exponent to right place
    exponent.shift(2*UP)
    exponent.to_edge(LEFT)
    exponent.shift(RIGHT*10.5)
    #arranges frac to right place
    frac.shift(2*UP)
    frac.to_edge(LEFT)
    frac.shift(RIGHT*1.2*len(str))
    #adds text to VGroup
    group += sign
    group += regime
    group += exponent
    group += frac
    #scales to screen size
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    return group



class NewScene(Scene):
    def construct(self):
        #float vs. posits
        binary_str =  "0100101100010100"
        binary_str2 = "0100010101001010"
        float_bin = CreateFloat(binary_str)
        float_bin.shift(DOWN*2)
        float_bin2 = CreatePosit(binary_str2,4)
        intro = Text("Floats vs. Posits")
        intro.scale(2)
        intro.to_edge(UP)
        self.play(
            Create(float_bin),Create(float_bin2),Create(intro)
            )
        self.wait
        #Scene 2 with Arrow moving allong
        self.play(Uncreate(float_bin),Uncreate(intro))
        first_text = Text("Lets look into posits first!")
        first_text.scale(1.5)
        first_text.to_edge(UP)
        self.play(
            Create(first_text)
        )
        arrow = Arrow(start=DOWN*2, end=ORIGIN, color=RED)
        arrow.to_edge(LEFT)
        arrow.shift(RIGHT*0.2)
        self.add(arrow)
        self.wait(6)
        # step by step, hard 
        for i in range (15):
            arrow.shift(RIGHT*0.815)
            arrow.update
            self.wait(0.5)
        # allong a line, smooth
        #l1 = Line(start=arrow.get_center(),end=arrow.get_center()+RIGHT*12.5)
        #self.play(MoveAlongPath(arrow, l1), rate_func=linear,run_time=5)
        self.wait




