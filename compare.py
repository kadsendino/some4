from manim import *


class ComparePart1(Scene):
    def construct(self):
        # slide 1
        head_1 = Text("Are Posits really better?").scale(2)
        self.play(Write(head_1))
        self.wait(5)
        # slide 2
        head_2 = Text("How do we compare them?").scale(2)
        self.play(ReplacementTransform(head_1, head_2))
        self.wait(5)
        self.play(Uncreate(head_2))
        # slide 3
        txt_speed = Text("Speed?").scale(1.5)
        txt_precision = Text("Precision?").scale(1.5)
        txt_speed.shift(LEFT*2).shift(UP).rotate(PI/8)
        txt_precision.shift(RIGHT*2).shift(UP).rotate(-PI/8)
        self.play(Write(txt_speed), Write(txt_precision))
        self.wait(5)
        txt_lets = Text("Let's see!").shift(DOWN)
        self.play(Write(txt_lets))
        self.wait(2)
        self.play(Uncreate(txt_speed), Uncreate(txt_precision), Uncreate(txt_lets))
        self.wait(2)
        # slide 4
        img  = ImageMobject("./src/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.6).shift(DOWN*2)
        self.play(Write(img))
        self.wait(10)
        # slide 5
        txt_two = MathTex("2?",substrings_to_isolate=["2"])
        txt_two.get_part_by_tex("2").set_color(BLUE)
        txt_two.scale(2).shift(UP*2)
        self.play(Write(txt_two))
        self.wait(5)
        self.play(Uncreate(txt_two), FadeOut(img))
        self.wait(2)
        # slide 6
        txt_float = Text("Floating points").set_color(BLUE).scale(1.5).shift(UP)
        txt_acr_size = Text("accuracy vs. size")
        self.play(Write(txt_float), Write(txt_acr_size))
        self.wait(5)
        self.play(Uncreate(txt_float), Uncreate(txt_acr_size))
        self.wait(2)
        # slide 7
        img2 = ImageMobject("./src/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.6).shift(DOWN*2)
        self.play(Write(img2))
        self.wait(10)
        # slide 8
        brace = Brace(img2, UP).scale(0.15).shift(RIGHT*4)
        txt_float_a = Text("Floats are more accurate!").set_color(PURPLE).next_to(brace, UP)
        self.play(Write(brace), Write(txt_float_a))
        self.wait(5)
        self.play(Uncreate(brace), Uncreate(txt_float_a))
        self.wait(2)
        # slide 9
        brace2 = Brace(img2, UP).scale(0.15).shift(UP)
        txt_posits_a = Text("Posits are more accurate!").set_color(GREEN).next_to(brace2, UP)
        self.play(Write(brace2), Write(txt_posits_a))
        self.wait(5)
        # slide 10
        txt_intention = Text("This is intentional").shift(LEFT*3).shift(UP*2)
        arc = Arc(
            start_angle=PI/2, angle=-PI/2, radius=1.5,
            color=YELLOW, stroke_width=4
        ).next_to(txt_intention, RIGHT)
        self.play(Write(txt_intention), Write(arc))
        self.wait(5)
        self.play(Uncreate(brace2), Uncreate(txt_posits_a), Uncreate(txt_intention), Uncreate(arc))
        self.wait(2)
        # slide 11
        line_left = Line(LEFT*3, DOWN*4, color=RED, stroke_width=4).shift(UP*2)
        line_right = Line(RIGHT*3, DOWN*4, color=RED, stroke_width=4).shift(UP*2)
        self.play(Write(line_left), Write(line_right))
        self.wait(5)
        self.play(Uncreate(line_left), Uncreate(line_right),Uncreate(img2))
        self.wait(2)
        # slide 12
        first_line = MathTex("2% error \times 20 operations",substrings_to_isolate=["2%", "20"])
        first_line.get_part_by_tex("2%").set_color(BLUE)
        first_line.get_part_by_tex("20").set_color(ORANGE)
        second_line = MathTex("0.98 \cdot 0.98 \cdot \dots \cdot 0.98",substrings_to_isolate=["0.98"])
        second_line_2 = MathTex("\approx 0.66 ").next_to(second_line, RIGHT)
        second_line_3 = MathTex("\implies 33% error",substrings_to_isolate=["error"]).next_to(second_line_2, RIGHT)
        second_line_3.get_part_by_tex("error").set_color(RED)
        second_line.get_parts_by_tex("0.98").set_color(BLUE)
        first_line.shift(UP)
        second_line.next_to(first_line, DOWN)
        brace = Brace(second_line, DOWN)
        times = MathTex("20 times",substrings_to_isolate=["20"]).next_to(brace, DOWN)
        times.get_part_by_tex("20").set_color(ORANGE)
        self.play(Write(first_line))
        self.wait(5)
        self.play(Write(second_line))
        self.wait(5)
        self.play(Write(brace), Write(times))
        self.wait(2)
        self.play(Write(second_line_2))
        self.wait(2)
        self.play(Write(second_line_3))
        self.wait(2)
        self.play(Uncreate(brace), Uncreate(times), Uncreate(second_line_2), Uncreate(second_line_3))
        self.wait(2)
class ClosurePlots(Scene):
    def construct(self):
        
