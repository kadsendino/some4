from manim import *
from numpy import number

def create_arrow(start_point,end_point,color_arc=WHITE):
        # Create a curved arc between points
        arc = ArcBetweenPoints(start_point, end_point, angle=-(PI/4)*3, stroke_width=4, color=color_arc)
        arc.add_tip(tip_length=0.05,tip_shape=StealthTip).shift(DOWN*0.1)  # add arrow tip
        return arc

def create_float(str : str, sign_bit = True, Placeholder = False):
    group = VGroup()
    arrayblock = []
    arraytext = []
    # get infos of Float16 (IEEE)
    infos = (0,5,len(str))
    color = (RED,YELLOW,BLUE)
    #Creates Numbers and Sqaures for Number
    for i, bit in enumerate(str):
        if (sign_bit == True or i != 0):
            sq = Square(stroke_width=2)
            sq.shift(RIGHT * 2 * i)
            txt = Text(bit).scale(1.5)
            txt.move_to(sq.get_center())
            for j in range(3):
                if i <= infos[j]:
                    txt.set_color(color[j])
                    break
            if Placeholder:
                txt.set_opacity(0) 
            group += sq
            group += txt
            arrayblock.append((sq,txt))
        
    group.to_edge(LEFT)
    #Creates Text for 
    if sign_bit == True:
        sign = Text("sign",color=color[0])
        #arranges sign to right place
        sign.shift(2*UP)
        sign.to_edge(LEFT)
        group += sign
        arraytext.append(sign)
    #arranges exponent to right place
    exponent = Text("exponent",color=color[1])
    exponent.shift(2*UP)
    exponent.to_edge(LEFT)
    if sign_bit == True:
        exponent.shift(RIGHT*2)
    #arranges mantissa to right place
    mantissa = Text("mantissa",color=color[2])
    mantissa.shift(2*UP)
    mantissa.to_edge(LEFT)
    if sign_bit == True:
        mantissa.shift(RIGHT*12)
    else:
        mantissa.shift(RIGHT*10)
    #adds text to VGroup
    
    group += exponent
    group += mantissa
    arraytext.append(exponent)
    arraytext.append(mantissa)
    #scales to screen size
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    
    return arrayblock, arraytext, group


class Float_Example1(Scene):
    def construct(self):
        # Example 
        """ 
        10.75 -> Visualisierung 2^4 - 2^3 - 2^2 - 2^1 - 2^0 - 2^(-1) -  2^(-2) (1010.11)
        1010.11 -> 1.01011 shifts
        Char = Exp + Bias (Bias = 15)
        Sign Bit
        """
        headding = Text("Lets start with Float16", font_size=48, color=WHITE).to_edge(UP)
        self.play(Write(headding))
        self.wait(1)
        #0 10010 0101100000 without sign bit
        array_block, array_text, group_block = create_float("0100100101100000", sign_bit = False, Placeholder=True)
        # Split Exponent and Mantissa
        exponent = []
        mantissa = []
        for i,(sq, txt) in enumerate(array_block):
            if i < 5:
                exponent.append((sq, txt))
            else:
                mantissa.append((sq, txt))
        group_block.to_corner(DOWN+LEFT).scale(0.8)
        self.play(Write(group_block))
        self.wait(1)
        self.play(FadeOut(headding))
        # 10.75 in binary
        num = MathTex("10.75")
        self.play(Write(num))
        self.wait(5)
        # Binary representation
        binary = MathTex("1010.11")
        self.play(Transform(num, binary))
        self.wait(2)
        # Normalized form
        num_new, count = self.shifting_num(num)
        self.wait(2)

        # Explain 1.x
        self.remove(num_new)
        shifted_text = "01011"
        one_dot_X = MathTex("1.").set_color(RED)
        one_dot_shift = MathTex("1.").set_color(RED)
        implicit = MathTex("X").next_to(one_dot_X, RIGHT, buff=0.05)
        num_ohne_one = MathTex(shifted_text).next_to(one_dot_shift, RIGHT, buff=0.05)
        group_one_dot = VGroup().add(one_dot_shift, num_ohne_one).center()
        self.add(group_one_dot)
        group_one_X = VGroup().add(one_dot_X, implicit).center().shift(DOWN * 0.7)
        self.play(Write(group_one_X))
        self.wait(10)
        self.play(FadeOut(group_one_X))

        # remove 1.
        self.wait(2)
        self.play(FadeOut(one_dot_shift))
        self.wait(2)

        # fill up with zeros
        group_filled_up = VGroup().add(num_ohne_one)
        brace = Brace(group_filled_up, direction=DOWN)
        brace_text = Text(str(len(shifted_text)) + " bits", font_size=50).next_to(brace, DOWN)
        self.play(GrowFromCenter(brace), FadeIn(brace_text), run_time=1)
        for i in range(10 - len(shifted_text)):
            zero = MathTex("0").next_to(group_filled_up, RIGHT, buff=0.05)
            group_filled_up.add(zero)
            self.play(Create(zero))

            new_brace = Brace(group_filled_up, direction=DOWN)
            new_bit_count = len(shifted_text) + i + 1
            new_brace_text = Text(f"{new_bit_count} bits", font_size=50).next_to(new_brace, DOWN)
            self.play(
                ReplacementTransform(brace, new_brace),
                ReplacementTransform(brace_text, new_brace_text),
            )
            brace = new_brace
            brace_text = new_brace_text
        self.wait(2)

        # Transform mantissa into mantissa bits
        self.remove(brace, brace_text)
        mantissatext = VGroup(*[txt for sq, txt in mantissa])
        mantissatext.set_opacity(1)
        self.play(ReplacementTransform(group_filled_up, mantissatext))
        self.wait(2)
        # number of shifts + bias
        characteristic = MathTex("3 + 15 = 18",substrings_to_isolate=["3","15","18"]) 
        characteristic.set_color_by_tex("3", BLUE) 
        characteristic.set_color_by_tex("15", GREEN)
        characteristic.set_color_by_tex("18",YELLOW)
        self.play(Write(characteristic))
        bias = characteristic.get_parts_by_tex("15")
        arrow = Arrow(start=UP, end=DOWN, color=GREEN).scale(0.5).next_to(bias, UP)
        text_bias = MathTex("bias").set_color(GREEN).next_to(arrow, UP)
        group_bias = VGroup().add(arrow, text_bias)
        self.play(Create(group_bias))
        self.wait(10)
        self.play(Uncreate(group_bias))
        self.play(Uncreate(count))
        self.wait(2)
        # Convert to binary
        bin_char = MathTex("10010").set_color(YELLOW)
        self.play(Transform(characteristic, bin_char, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        # move exponent to right place
        exponent_group = VGroup(*[txt for sq, txt in exponent])
        exponent_group.set_opacity(1)
        self.play(ReplacementTransform(bin_char, exponent_group))
        self.wait(5)
        # show result
        array_block_r, array_text_r, group_block_r = create_float("0100100101100000")
        group_block_r.remove(array_block_r[0][0], array_block_r[0][1], array_text_r[0])
        self.play(ReplacementTransform(group_block, group_block_r))
        self.wait(2)
        self.play(Create(array_block_r[0][0]), Create(array_block_r[0][1]), Create(array_text_r[0]))
        self.wait(2)


    def shifting_num(self,num):
        shifts = [
            MathTex(r"101.011"),
            MathTex(r"10.1011"),
            MathTex(r"1.01011"),
        ]
        # Get the initial state from the return value of regime
        current_bin = num
        current_dot = current_bin[0][4]  # starting dot index

        count = 0
        count_expr = VGroup()
        count_expr += MathTex(str(count)).set_color_by_tex(str(count),BLUE).scale(1.5).shift(UP)
        count_expr += Text(" shifts").scale(1).shift(UP*1.4).next_to(count_expr[0], RIGHT)
        count_expr.scale(0.8).center().shift(UP*3)
        self.play(Write(count_expr))
        self.wait(1)

        for i, shifted in enumerate(shifts):
            count += 1

            # Get new dot for arrow
            new_dot = shifted[0][4-count]  # assuming dot stays at same relative index
            arc = create_arrow(current_dot.get_center(), new_dot.get_center(),BLUE)

            # Show arc
            self.play(Create(arc))
            self.wait(0.5)

            # Update binary and count expression
            new_count_expr = VGroup()
            new_count_expr += MathTex(str(count)).set_color_by_tex(str(count),BLUE).scale(1.5).shift(UP)
            new_count_expr += Text(" shifts").scale(1).shift(UP * 1.4).next_to(new_count_expr[0], RIGHT)
            new_count_expr.scale(0.8).center().shift(UP*3)
            self.play(
                ReplacementTransform(current_bin, shifted),
                ReplacementTransform(count_expr, new_count_expr),
                FadeOut(arc)
            )
            self.wait(0.5)

            current_bin = shifted
            current_dot = new_dot
            count_expr = new_count_expr
        return current_bin, count_expr


class Float_Example2(Scene):
    def construct(self):
        # Example 2
        """
        -255.03125 -> 11111111.00001
        11111111.00001  ⇒ 1.111111100001 (7 shifts needed)
        7 + 15 = 22 = 10110
        1 10110 1111111000
        """
        # Rest + Special Cases
        #1 10110 1111111000 without sign bit
        array_block, array_text, group_block = create_float("1101101111111000", Placeholder=True)
        # Split Exponent and Mantissa
        sign = array_block[0]
        exponent = []
        mantissa = []
        for i,(sq, txt) in enumerate(array_block[1:]):
            if i < 5:
                exponent.append((sq, txt))
            else:
                mantissa.append((sq, txt))
        group_block.to_corner(DOWN+LEFT).scale(0.8)
        self.play(Write(group_block))
        self.wait(1)
        # -255.03125 in binary
        num = MathTex("-255.03125")
        self.play(Write(num))
        self.wait(5)
        # Binary representation
        binary = MathTex("11111111.00001")
        self.play(Transform(num, binary))
        self.wait(2)
        # Normalized form
        num_new, count = self.shifting_num(num)
        self.wait(2)

        # Explain 1.x
        self.remove(num_new)
        shifted_text = num_new.tex_string[2:]
        one_dot_X = MathTex("1.").set_color(RED)
        one_dot_shift = MathTex("1.").set_color(RED)
        implicit = MathTex("X").next_to(one_dot_X, RIGHT, buff=0.05)
        num_ohne_one = MathTex(shifted_text).next_to(one_dot_shift, RIGHT, buff=0.05)
        group_one_dot = VGroup().add(one_dot_shift, num_ohne_one).center()
        self.add(group_one_dot)
        group_one_X = VGroup().add(one_dot_X, implicit).center().shift(DOWN * 0.7)
        self.play(Write(group_one_X))
        self.wait(2)
        self.play(FadeOut(group_one_X))

        # remove 1.
        self.wait(2)
        self.play(FadeOut(one_dot_shift))
        self.wait(2)

        # convertion to Binary
        num_filled = MathTex("111111100001",substrings_to_isolate=["01"])
        self.play(Uncreate(count))
        self.play(num_ohne_one.animate.shift(LEFT * 0.175)) # trail and error wert
        self.remove(num_ohne_one)
        self.add(num_filled)
        self.wait(2)
        # show current bit size
        brace = Brace(num_filled, direction=DOWN)
        brace_text = Text("12 bits", font_size=50).next_to(brace, DOWN)
        self.play(GrowFromCenter(brace), FadeIn(brace_text), run_time=1)
        self.wait(2)
        # Cutoff 2 Bits
        last_bits = num_filled.get_part_by_tex("01").set_color(RED)
        self.wait(0.5)
        self.play(Uncreate(last_bits),run_time=1)
        # show updated bit size
        brace2 = Brace(MathTex("1111111000").shift(LEFT*0.2), direction=DOWN)
        brace_text2 = Text("10 bits", font_size=50).next_to(brace2, DOWN)
        self.play(Transform(brace,brace2,replace_mobject_with_target_in_scene=True),Transform(brace_text,brace_text2,replace_mobject_with_target_in_scene=True))
        self.wait(1)
        self.play(num_filled.animate.set_color(BLUE),run_time=0.5)
        # Remove bitstring and brace
        self.play(FadeOut(brace2), FadeOut(brace_text2), run_time=1)
        self.wait()
        # Transform mantissa into mantissa bits  TODO smoothering animation?
        mantissatext = VGroup(*[txt for sq, txt in mantissa])
        mantissatext.set_opacity(1)
        self.play(ReplacementTransform(num_filled, mantissatext))
        self.wait(2)
        # number of shifts + bias
        characteristic = MathTex("7 + 15 = 22",substrings_to_isolate=["7","15","22"]) 
        characteristic.set_color_by_tex("7", BLUE) 
        characteristic.set_color_by_tex("15", GREEN)
        characteristic.set_color_by_tex("22",YELLOW)
        self.play(Write(characteristic))
        bias = characteristic.get_parts_by_tex("15")
        arrow = Arrow(start=UP, end=DOWN, color=GREEN).scale(0.5).next_to(bias, UP)
        text_bias = MathTex("bias").set_color(GREEN).next_to(arrow, UP)
        group_bias = VGroup().add(arrow, text_bias)
        self.play(Create(group_bias))
        self.wait(2)
        self.play(Uncreate(group_bias))
        # Convert to binary
        bin_char = MathTex("10110").set_color(YELLOW)
        self.play(Transform(characteristic, bin_char, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        # move exponent to right place
        exponent_group = VGroup(*[txt for sq, txt in exponent])
        exponent_group.set_opacity(1)
        self.play(ReplacementTransform(bin_char, exponent_group))
        self.wait(2)
        # explain sign bit
        txt_num = MathTex("-255.03125",substrings_to_isolate=["-"])
        txt_bit = MathTex(r"\rightarrow 1",substrings_to_isolate=["1"])
        txt_min = txt_num.get_parts_by_tex("-")
        txt_1 = txt_bit.get_parts_by_tex("1")
        txt_bit.next_to(txt_num,DOWN,buff=1)
        txt_group = VGroup(txt_num,txt_bit)
        self.play(Create(txt_num))
        self.wait(1)
        self.play(Create(txt_bit))
        self.wait(2)
        txt_min.set_color(RED)
        txt_1.set_color(RED)
        self.wait(1)
        # Replace Sign
        sign[1].set_opacity(1)
        self.play(ReplacementTransform(txt_group, VGroup(sign[1])))
        self.wait(2)
        # show result
        array_block_r, array_text_r, group_block_r = create_float("1101101111111000")
        self.play(ReplacementTransform(group_block, group_block_r))
        self.wait(2)
    def shifting_num(self,num):
        shifts = [
            MathTex(r"1111111.100001"),
            MathTex(r"111111.1100001"),
            MathTex(r"11111.11100001"),
            MathTex(r"1111.111100001"),
            MathTex(r"111.1111100001"),
            MathTex(r"11.11111100001"),
            MathTex(r"1.111111100001"),
        ]
        # Get the initial state from the return value of regime
        current_bin = num
        current_dot = current_bin[0][8]  # starting dot index

        count = 0
        count_expr = VGroup()
        count_expr += MathTex(str(count)).set_color_by_tex(str(count),BLUE).scale(1.5).shift(UP)
        count_expr += Text(" shifts").scale(1).shift(UP*1.4).next_to(count_expr[0], RIGHT)
        count_expr.scale(0.8).center().shift(UP*3)
        self.play(Write(count_expr))
        self.wait(0.5)

        for i, shifted in enumerate(shifts):
            count += 1

            #set time
            time = 0.05
            # Get new dot for arrow
            new_dot = shifted[0][8-count]  # assuming dot stays at same relative index
            arc = create_arrow(current_dot.get_center(), new_dot.get_center(),BLUE)

            # Show arc
            self.play(Create(arc),run_time=time)
            

            # Update binary and count expression
            new_count_expr = VGroup()
            new_count_expr += MathTex(str(count)).set_color_by_tex(str(count),BLUE).scale(1.5).shift(UP)
            new_count_expr += Text(" shifts").scale(1).shift(UP*1.4).next_to(new_count_expr[0], RIGHT)
            new_count_expr.scale(0.8).center().shift(UP*3)
            self.play(
                ReplacementTransform(current_bin, shifted),
                ReplacementTransform(count_expr, new_count_expr),
                FadeOut(arc)
            )
            self.wait(time)

            current_bin = shifted
            current_dot = new_dot
            count_expr = new_count_expr
        return current_bin, count_expr


class Float_Special_Cases(Scene):
    def construct(self):
        text = MathTex("special \; case: ")
        text_zero = MathTex("\pm0").next_to(text)
        group_text = VGroup().add(text, text_zero).center().shift(UP)
        self.play(Create(group_text))
        array_block_r, array_text_r, group_block_r = create_float("X000000000000000")
        group_block_r.shift(DOWN)
        self.play(Create(group_block_r))
        self.wait(15)

        self.play(Uncreate(text_zero))
        group_text.remove(text_zero)
        text_inf = MathTex("\pm\infty").next_to(text)
        self.play(Create(text_inf))
        array_block_inf, array_text_inf, group_block_inf = create_float("X111110000000000")
        group_block_inf.shift(DOWN)
        self.play(ReplacementTransform(group_block_r, group_block_inf))
        self.wait(10)


        self.play(Uncreate(text_inf))
        text_unequal = MathTex(r"\neq0").next_to(array_text_inf[2], buff = 0.02).set_color(BLUE).scale(0.8)
        text_NaN = MathTex("NaN").next_to(text)
        self.play(Create(text_NaN))
        array_block_NaN, array_text_NaN, group_block_NaN = create_float("X11111XXXXXXXXXX")
        group_block_NaN.shift(DOWN)
        self.add(text_unequal)
        self.play(ReplacementTransform(group_block_inf, group_block_NaN))
        self.wait(5)



class Float_03(Scene):
    def construct(self):
        text_start = Text("How would we represent 0.3 in float16?").shift(UP * 2).scale(0.6)
        self.add(text_start)
        self.wait(2)
        array_block_r, array_text_r, group_block_r = create_float("0011010011001101")
        self.play(Create(group_block_r))
        text_03 = Text("0.300048828125").shift(UP * 2).scale(0.6)
        self.play(Uncreate(text_start))
        self.play(Create(text_03))
        self.wait(2)
