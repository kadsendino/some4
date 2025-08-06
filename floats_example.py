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
        self.wait(2)
        # Binary representation
        binary = MathTex("1010.11")
        self.play(Transform(num, binary))
        self.wait(2)
        # Normalized form
        num_new, count = self.shifting_num(num)
        self.wait(2)
        # Explain 1.x
        implicit = MathTex("1.X")
        implicit.set_color(RED)
        implicit.next_to(num_new, DOWN*1.5)
        num_new.set_color(RED)
        #num_new[2:].set_color(BLUE)
        self.play(Write(implicit))
        self.wait(2)
        self.play(FadeOut(implicit))
        # filling mantissa with bits TODO
        num_filled = MathTex("0101100000")
        self.play(Transform(num_new, num_filled))
        self.wait(2)
        # Transform mantissa into mantissa bits
        mantissatext = VGroup(*[txt for sq, txt in mantissa])
        mantissatext.set_opacity(1)
        self.play(ReplacementTransform(num_new, mantissatext))
        self.wait(2)
        # number of shifts + bias
        characteristic = MathTex("3 + 15 = 18",substrings_to_isolate=["3","15","18"]) 
        characteristic.set_color_by_tex("3", BLUE) 
        characteristic.set_color_by_tex("15", GREEN)
        characteristic.set_color_by_tex("18",YELLOW)
        self.play(Write(characteristic))
        self.wait(2)
        self.play(Uncreate(count))
        self.wait(2)
        # Convert to binary
        bin_char = MathTex("10010")
        self.play(Transform(characteristic, bin_char, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        # move exponent to right place
        exponent_group = VGroup(*[txt for sq, txt in exponent])
        exponent_group.set_opacity(1)
        self.play(ReplacementTransform(bin_char, exponent_group))
        self.wait(2)
        # show result
        array_block_r, array_text_r, group_block_r = create_float("0100100101100000")
        self.play(ReplacementTransform(group_block, group_block_r))
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
            new_count_expr += Text(" shifts").scale(1).shift(UP*1.4).next_to(new_count_expr[0], RIGHT)
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
        sign = [array_block[0]]
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
        self.wait(2)
        # Binary representation
        binary = MathTex("11111111.00001")
        self.play(Transform(num, binary))
        self.wait(2)
        # Normalized form
        num_new, count = self.shifting_num(num)
        self.wait(2)
        # Explain 1.x
        implicit = MathTex("1.X")
        implicit.set_color(RED)
        implicit.next_to(num_new, DOWN*1.5)
        num_new.set_color(RED)
        #num_new[2:].set_color(BLUE)
        self.play(Write(implicit))
        self.wait(2)
        self.play(FadeOut(implicit))
        # convertion to Binary
        num_filled = MathTex("111111100001",substrings_to_isolate=["01"])
        self.play(Transform(num_new, num_filled,replace_mobject_with_target_in_scene=True))
        self.play(Uncreate(count))
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
        # Remove bitstring and brace
        self.play(FadeOut(brace2), FadeOut(brace_text2), run_time=1)
        self.wait()
        # Transform mantissa into mantissa bits 
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
        self.wait(2)
        # Convert to binary
        bin_char = MathTex("10110").set_color(YELLOW)
        self.play(Transform(characteristic, bin_char, replace_mobject_with_target_in_scene=True))
        self.wait(2)
        # move exponent to right place
        exponent_group = VGroup(*[txt for sq, txt in exponent])
        exponent_group.set_opacity(1)
        self.play(ReplacementTransform(bin_char, exponent_group))
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
            time = 0.1
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
    