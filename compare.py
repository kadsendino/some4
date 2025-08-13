from manim import *


class ComparePart1(Scene):
    def construct(self):
        # slide 1
        head_1 = Text("Are Posits really better?").scale(1.5)
        self.play(Write(head_1))
        self.wait(5)
        # slide 2
        head_2 = Text("How do we compare them?").scale(1.5)
        self.play(ReplacementTransform(head_1, head_2))
        self.wait(5)
        self.play(Uncreate(head_2))
        # slide 3
        txt_speed = Text("Speed?").scale(1.5)
        txt_precision = Text("Precision?").scale(1.5)
        txt_speed.shift(LEFT*2.5).shift(UP).rotate(PI/8)
        txt_precision.shift(RIGHT*2.5).shift(UP).rotate(-PI/8)
        self.play(Write(txt_speed), Write(txt_precision))
        self.wait(5)
        txt_lets = Text("Let's see!").shift(DOWN)
        self.play(Write(txt_lets))
        self.wait(2)
        self.play(Uncreate(txt_speed), Uncreate(txt_precision), Uncreate(txt_lets))
        self.wait(2)
        # slide 4
        img  = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.6).shift(DOWN*1.5)
        self.add(img)
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
        img2 = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.6).shift(DOWN*2)
        self.add(img2)
        self.wait(10)
        # slide 8
        brace = Brace(img2, stroke_width=7, direction=UP).scale(0.15).shift(RIGHT*4)
        txt_float_a = Text("Floats are more accurate!").set_color(PURPLE).next_to(brace, UP)
        self.play(Write(brace), Write(txt_float_a))
        self.wait(5)
        self.play(Uncreate(brace), Uncreate(txt_float_a))
        self.wait(2)
        # slide 9
        brace2 = Brace(img2, stroke_width=7,direction=UP).scale(0.15).shift(UP)
        txt_posits_a = Text("Posits are more accurate!").set_color(GREEN).next_to(brace2, UP)
        self.play(Write(brace2), Write(txt_posits_a))
        self.wait(5)
        # slide 10
        txt_intention = Text("This is intentional").shift(LEFT*3).shift(UP*2)
        arrow = CurvedArrow(
            txt_intention.get_right(), 
            img2.get_top(), 
            angle=-PI/2, 
            color=YELLOW
        )
        self.play(Write(txt_intention), Write(arrow))
        self.wait(5)
        self.play(Uncreate(brace2), Uncreate(txt_posits_a), Uncreate(txt_intention), Uncreate(arrow))
        self.wait(2)
        # slide 11
        line_left = Line(LEFT*3, LEFT*3+DOWN*4, color=RED, stroke_width=4).shift(UP*2)
        line_right = Line(RIGHT*3, RIGHT*3+DOWN*4, color=RED, stroke_width=4).shift(UP*2)
        self.play(Write(line_left), Write(line_right))
        self.wait(5)
        self.play(Uncreate(line_left), Uncreate(line_right),FadeOut(img2))
        self.wait(2)
        # slide 12
        first_line = MathTex(r"2\% error \times 20 operations", substrings_to_isolate=["2\%", "20"])
        first_line.get_parts_by_tex("2\%").set_color(BLUE)
        first_line.get_part_by_tex("20").set_color(ORANGE)
        second_line = MathTex(r"0.98 \cdot 0.98 \cdot ... \cdot 0.98", substrings_to_isolate=["0.98"])
        second_line_2 = MathTex(r"\approx 0.66 ").next_to(second_line, RIGHT) 
        second_line_4 = MathTex(r"\implies 33 \% error",substrings_to_isolate=["error"]).shift(DOWN*2)
        second_line_4.get_part_by_tex("error").set_color(RED)
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
        self.play(Write(second_line_4))
        self.wait(10)
        self.play(Uncreate(brace), Uncreate(times), Uncreate(second_line_2), Uncreate(second_line_4),Uncreate(first_line),Uncreate(second_line))
        self.wait(2)
class ClosurePlots(Scene):
    def construct(self):
        #2d Plots
        #1/x
        opp = Text("Operation: ")
        opp2 = MathTex(r"\frac{1}{x}").set_color(RED)
        Closure_2d_1 = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.7).shift(DOWN*0.1)
        txt_2d_1 = VGroup(opp, opp2)
        opp.next_to(Closure_2d_1, UP)
        opp2.next_to(opp, RIGHT)
        self.play(Write(txt_2d_1), FadeIn(Closure_2d_1))
        self.wait(5)
        self.play(Uncreate(txt_2d_1), FadeOut(Closure_2d_1))
        self.wait(2)
        #sqrt(x)
        txt_2d_2 = MathTex(r"\sqrt{x}")
        Closure_2d_2 = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.7).shift(DOWN*0.1)
        txt_2d_2.next_to(Closure_2d_2, UP)
        self.play(Write(txt_2d_2), FadeIn(Closure_2d_2))
        self.wait(5)
        self.play(Uncreate(txt_2d_2), FadeOut(Closure_2d_2))
        self.wait(2)
        #x^2
        txt_2d_3 = MathTex(r"x^{2}")
        Closure_2d_3 = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.7).shift(DOWN*0.1)
        txt_2d_3.next_to(Closure_2d_3, UP)
        self.play(Write(txt_2d_3), FadeIn(Closure_2d_3))
        self.wait(5)
        self.play(Uncreate(txt_2d_3), FadeOut(Closure_2d_3))
        self.wait(2)
        #log(x)
        txt_2d_4 = MathTex(r"\log{x}")
        Closure_2d_4 = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.7).shift(DOWN*0.1)
        txt_2d_4.next_to(Closure_2d_4, UP)
        self.play(Write(txt_2d_4), FadeIn(Closure_2d_4))
        self.wait(5)
        self.play(Uncreate(txt_2d_4), FadeOut(Closure_2d_4))
        self.wait(2)
        #3d Plots
        # x+y
        txt_3d_1 = MathTex(r"x+y")
        Closure_3d_1 = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.7).shift(DOWN*0.1)
        txt_3d_1.next_to(Closure_3d_1, UP)
        self.play(Write(txt_3d_1), FadeIn(Closure_3d_1))
        self.wait(5)
        self.play(Uncreate(txt_3d_1), FadeOut(Closure_3d_1))
        self.wait(2)
        #x*y
        txt_3d_2 = MathTex(r"x \cdot y")

        img_left = ImageMobject("data/multiplication_f16.png").scale_to_fit_height(config.frame_height).scale(0.7)
        img_right = ImageMobject("data/multiplication_p16.png").scale_to_fit_height(config.frame_height).scale(0.7)

        gap_size = 1  # adjust this to increase/decrease space
        img_left.shift(LEFT * (img_left.width/2 + gap_size/2))
        img_right.shift(RIGHT * (img_right.width/2 + gap_size/2))

        images_group = Group(img_left, img_right).shift(DOWN * 0.1)

        txt_3d_2.next_to(images_group, UP)

        self.play(Write(txt_3d_2), FadeIn(images_group))
        self.wait(5)
        self.play(Uncreate(txt_3d_2), FadeOut(images_group))
        self.wait(2)
        # x/y
        txt_3d_3 = MathTex(r"\frac{x}{y}")
        Closure_3d_3 = ImageMobject("data/placeholder.png").scale_to_fit_height(config.frame_height).scale(0.7).shift(DOWN*0.1)
        txt_3d_3.next_to(Closure_3d_3, UP)
        self.play(Write(txt_3d_3), FadeIn(Closure_3d_3))
        self.wait(5)
        self.play(Uncreate(txt_3d_3), FadeOut(Closure_3d_3))
        self.wait(2)

class ComparePart2(Scene):
    def construct(self):
         # slide 21
        head_1 = Text("How do we measure speed?").scale(1.5)
        self.play(Write(head_1))
        self.wait(5)
        self.play(Uncreate(head_1))
        # slide 22
        img_fpga = ImageMobject("data/FPGA.jpg").scale_to_fit_height(config.frame_height).scale(0.6)
        txt_fpga = Text("Field Programmable Gate Array").scale(0.5).next_to(img_fpga, DOWN)
        self.play(FadeIn(img_fpga), Write(txt_fpga))
        self.wait(20)
        self.play(FadeOut(img_fpga), Unwrite(txt_fpga))
        self.wait(2)
        # slide 23a with Table Adder
        table_adder_posit = Table(
            [[str(312), str(1.33), "11.1 ns", str(1.27)],
             [str(647), str(1.49), "15.8 ns", str(1.33)],
             [str(1550), str(1.59), "21.6 ns", str(1.35)]],
            row_labels=[Text("16"), Text("32"), Text("64")],
            col_labels=[Text("LUT"), Text("(ratio)"), Text("delay"), Text("(ratio)")],
            top_left_entry=Text("Adder Posit")
        )
        """
         ["234", "1", "8.8 ns", "1"],
            ["434", "1", "11.9 ns", "1"],
            ["976", "1", "16.0 ns", "1"],
            """
        table_adder_floats = Table(
            [[str(234), str(1), "8.8 ns", str(1)],
             [str(434), str(1), "11.9 ns", str(1)],
             [str(976), str(1), "16.0 ns", str(1)]],
            row_labels=[Text("16"), Text("32"), Text("64")],
            col_labels=[Text("LUT"), Text("(ratio)"), Text("delay"), Text("(ratio)")],
            top_left_entry=Text("Adder Float")
        )
        table_adder_posit.scale(0.4).shift(UP*1.2)
        table_adder_floats.scale(0.4).shift(DOWN*1.2)

        self.play(FadeIn(table_adder_posit), FadeIn(table_adder_floats))
        self.wait(10)
        self.play(FadeOut(table_adder_posit), FadeOut(table_adder_floats))
        self.wait(2)
        # slide 23b with Table Mult
        """
        posit_data = [
            [182, 1.03, 1, "11.3 ns", 1.39],
            [466, 1.37, 4, "15.8 ns", 1.62],
            [1213, 1.58, 16, "21.1 ns", 1.48]
        ]

        # IEEE → IEEE
        ieee_data = [
            [176, 1.00, 1, "8.1 ns", 1.00],
            [340, 1.00, 2, "9.8 ns", 1.00],
            [768, 1.00, 9, "14.3 ns", 1.00]
        ]
        """
        table_mult_posit = Table(
            [[str(182), str(1.03), "11.3 ns", str(1.39)],
             [str(466), str(1.37), "15.8 ns", str(1.62)],
             [str(1213), str(1.58), "21.1 ns", str(1.48)]
            ],
            row_labels=[Text("16"), Text("32"), Text("64")],
            col_labels=[Text("LUT"), Text("(ratio)"), Text("delay"), Text("(ratio)")],
            top_left_entry=Text("Mult Posit")
        )
        table_mult_floats = Table(
            [[str(176), str(1), "8.1 ns", str(1)],
             [str(340), str(1), "9.8 ns", str(1)],
             [str(768), str(1), "14.3 ns", str(1)]
            ],
            row_labels=[Text("16"), Text("32"), Text("64")],
            col_labels=[Text("LUT"), Text("(ratio)"), Text("delay"), Text("(ratio)")],
            top_left_entry=Text("Mult Float")
        )
        table_mult_posit.scale(0.4).shift(UP*1.2)
        table_mult_floats.scale(0.4).shift(DOWN*1.2)

        self.play(FadeIn(table_mult_posit), FadeIn(table_mult_floats))
        self.wait(10)
        self.play(FadeOut(table_mult_posit), FadeOut(table_mult_floats))
        self.wait(2)
        # slide 24
        head_2 = Text("Will we use Posits in the future?").scale(1.3)
        self.play(Write(head_2))
        self.wait(5)
        self.play(Uncreate(head_2))
        # slide 25
        head_3 = Text("well...")
        head_4 = Text("probably not.")
        head_4.next_to(head_3, RIGHT)
        VGroup(head_3, head_4).center()
        self.play(Write(head_3))
        self.wait(0.5)
        self.play(Write(head_4))
        self.wait(5)
        self.play(Uncreate(head_3), Uncreate(head_4))
        # slide 26
        comp1 = Text("Intel")
        comp2 = Text("AMD").rotate(PI/8).shift(LEFT).shift(UP)
        comp3 = Text("Apple").rotate(-PI/10).shift(RIGHT).shift(UP)
        group = VGroup(comp1, comp2, comp3).center().shift(LEFT*3)
        self.play(Write(comp1))
        self.wait(2)
        self.play(Write(comp2))
        self.wait(1)
        self.play(Write(comp3))
        self.wait(2)
        questionmark = Text("?").scale(2).set_color(BLUE)
        self.play(Write(questionmark))
        self.wait(5)
        self.play(Uncreate(questionmark))
        self.wait(2)
        # Load the image
        image = ImageMobject("data/beatingfloatspaper.png")

        # Set image size and angle
        image.scale(0.7)  # You can adjust size here
        image.rotate(PI / 64)  # Rotate by 22.5 degrees (adjust as needed)

        # Set the starting position (below screen) and zero opacity
        image.move_to(DOWN * 4 + RIGHT * 2.2)  # Start from below
        image.set_opacity(0)    # Fully transparent

        # Target position (center or adjusted)
        target_position = ORIGIN + RIGHT * 2.2  # Final position slightly above center

        # Animate moving up and fading in
        self.play(
            image.animate.move_to(target_position).set_opacity(1),
            run_time=2,
            rate_func=smooth
        )
        self.wait(2)
        self.play(FadeOut(image), Uncreate(group))
        self.wait(5)
