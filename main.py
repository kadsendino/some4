from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class BinaryBlocks(Scene):
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
