from manim import *

class SymbolCreature(VGroup):
    def __init__(self, symbol_tex, **kwargs):
        super().__init__(**kwargs)

        # Base symbol
        symbol = MathTex(symbol_tex, font_size=200,color=BLUE)
        
        # Eyes positions
        eye_y = symbol.get_top()[1] - 0.3
        left_eye_x = symbol.get_center()[0] - 0.4
        right_eye_x = symbol.get_center()[0] + 0.4

        #left eye
        left_eye_white = Circle(radius=1, color=WHITE, fill_opacity=1).move_to([left_eye_x, eye_y, 0])
        left_pupil = Circle(radius=0.5, color=BLACK, fill_opacity=1).move_to(left_eye_white.get_center())
        l_eye = VGroup(left_eye_white, left_pupil).scale(0.15)
        
        #right eye
        right_eye_white = Circle(radius=1, color=WHITE, fill_opacity=1).move_to([right_eye_x, eye_y, 0])
        right_pupil = Circle(radius=0.5, color=BLACK, fill_opacity=1).move_to(right_eye_white.get_center())
        r_eye = VGroup(right_eye_white, right_pupil).scale(0.15)

        # add to VGroup
        self.add(symbol, l_eye, r_eye)
    def move_eyes(self, direction):
        self[1][1].shift(direction)
        self[2][1].shift(direction)
    def think_bubble(self):
        pos_list = [[-2, -1, 0], [0, -0.5, 0], [-1.5, 0.5, 0]]
        tri = Polygon(*pos_list,color=GRAY, fill_opacity=1, stroke_width=0)
        ell = Ellipse(width=4, height=2, color=GRAY, fill_opacity=1, stroke_width=0)
        group = VGroup(ell, tri).next_to(self[0], UP, buff=0.5).shift(RIGHT*2)
        return group

class Test(Scene):
    def construct(self):
        symbol = SymbolCreature(r"\varphi")
        self.add(symbol)
        self.wait(1)
        self.play(Create(symbol.think()))