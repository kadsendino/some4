from manim import *


def create_float(str : str, sign_bit = True):
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
            for j in range(3):
                if i <= infos[j]:
                    sq.set_fill(color[j], opacity=0.3)
                    break
            sq.shift(RIGHT * 2*i)
            txt = Text(bit).scale(1.5)
            txt.move_to(sq.get_center())
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

def create_arrow(start_point,end_point,color_arc=WHITE):
        # Create a curved arc between points
        arc = ArcBetweenPoints(start_point, end_point, angle=-PI/2, stroke_width=4, color=color_arc)
        arc.add_tip(tip_length=0.1,tip_shape=StealthTip).shift(DOWN*0.1)  # add arrow tip
        return arc


def create_binary_radix(str: str, index: int):
    point = Text(".")
    b1 = Text(str[:index])
    b2 = Text(str[index:])
    b2.next_to(b1,buff=0.15)
    point.next_to(b1,buff=0.05).shift(DOWN*0.2)
    return [b1,point,b2],VGroup(b1,point,b2).center()

# TODO Decide between list and list2
def create_bin_index_list(ind : int,bias=0):
    array = []
    group = VGroup()
    # adds index infront
    sq = Rectangle(width=4,stroke_width=2)
    sq.set_fill(BLUE, opacity=0.3)
    txt = Text("index")
    sq.shift(RIGHT * 2)
    txt.move_to(sq.get_center())
    group += sq 
    group += txt
    array.append((sq,txt))  
    for i in range(ind):
        sq = Square(stroke_width=2)
        sq.set_fill(BLUE, opacity=0.3)
        zahl = i - bias
        if zahl >= 0:
            exp = 2**zahl
            txt = MathTex(f"{exp}")
        else:
            exp = 2**(abs(zahl))
            txt = MathTex(r"\frac{1}{" + str(exp) + "}")
        sq.shift(RIGHT * 2*(i+2.5))
        txt.move_to(sq.get_center())
        group += sq 
        group += txt
        array.append((sq,txt))  
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    group.shift(UP*2)
    return array, group

def create_bin_index_list2(ind : int,bias=0):
    array = []
    group = VGroup()
    # adds index infront
    txt = Text("index")
    txt.shift(RIGHT * 2) 
    group += txt
    array.append(txt)  
    for i in range(ind):
        zahl = i - bias
        if zahl >= 0:
            exp = 2**zahl
            txt = MathTex(f"{exp}")
        else:
            exp = 2**(abs(zahl))
            txt = MathTex(r"\frac{1}{" + str(exp) + "}")
        txt.shift(RIGHT * 2*(i+2.5))
        group += txt
        array.append(txt)  
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    group.shift(UP*2)
    return array, group

def shift_bits(self, bits, num_shifts):
    #TODO Coppied but has to be changed
    # Step 0: Setup
    shifts = [
        MathTex(r"-111.1111100001_2").scale(1.3),
        MathTex(r"-11.11111100001_2").scale(1.3),
        MathTex(r"-1.111111100001_2").scale(1.3),
    ]

    # Get the initial state from the return value of regime
    current_bin = number
    current_dot = current_bin[0][5]  # starting dot index

    # Initial exponent label
    e_val = 0
    e_expr = MathTex("e", "=", str(e_val)).scale(1.3).shift(UP)
    e_expr.set_color_by_tex("e", BLUE)
    self.play(Write(e_expr))
    self.wait(1)

    # Iterate through shifts
    for i, shifted in enumerate(shifts):
        e_val += 1

        # Get new dot for arrow
        new_dot = shifted[0][5-e_val]  # assuming dot stays at same relative index
        arc = create_arrow(current_dot.get_center(), new_dot.get_center(),BLUE)

        # Show arc
        self.play(Create(arc))
        self.wait(0.5)

        # Update binary and e expression
        new_e_expr = MathTex("e", "=", str(e_val)).scale(1.3).shift(UP)
        new_e_expr.set_color_by_tex("e", BLUE)

        self.play(
            ReplacementTransform(current_bin, shifted),
            ReplacementTransform(e_expr, new_e_expr),
            FadeOut(arc)
        )
        self.wait(0.5)

        current_bin = shifted
        current_dot = new_dot
        e_expr = new_e_expr

    # Step 4: Add → exponent bits (e.g. → 011)
    bits_expr = MathTex(r"\rightarrow", "1", "1").scale(1.3).shift(DOWN)
    bits_expr.set_color_by_tex("1", BLUE)
    bits_expr.next_to(e_expr, RIGHT, buff=0.6)

    self.play(FadeIn(bits_expr))
    self.wait(2)

    # Merge into exponent_bits and show label
    self.play(ReplacementTransform(bits_expr, exponent_bits), FadeOut(e_expr), FadeIn(field_labels[2]))
    self.wait(2)

    return current_bin



class Test(Scene):
    def construct(self):
        binary_str = "0100010101001010"
        a = 10
        array,group = create_binary_radix(binary_str,5)
        a1,g1 = create_bin_index_list2(a,3)
        self.play(Create(g1))
        self.play(Create(group))
        self.wait(2)
        



class BitBlocks(Scene):
    def construct(self):
        binary_str = "0100010101001010"
        float_block_array, float_text_array, float_block_group = create_float(binary_str, sign_bit = True)
        self.play(Create(float_block_group))
        self.wait(2)


class FixedPoint(Scene):
    def construct(self):
        txt1 = Text("We need a binary representation!")
        bin_num = Text("010101010101000001010101010110")
        txt1.shift(UP*2)
        self.play(FadeIn(txt1),run_time=0.8)
        self.play(FadeIn(bin_num),run_time=0.8)
        
        self.wait(2)
        
        #radix point
        point = Text(".")
        arrow = Arrow(start= ORIGIN+RIGHT*2,end=ORIGIN+0.5*RIGHT,color=RED)
        arrow_dis = Text("radix point",color=RED).scale(0.5)
        arrow_dis.move_to(arrow.get_center()).shift(UP*0.5)
        g1 = VGroup(point,arrow,arrow_dis).shift(DOWN*2)
        self.play(FadeIn(g1))
        self.play(FadeOut(arrow,arrow_dis))

        self.wait(2)
        
        # Morph Radix into binary number
        bin_num1 = Text("010101010101000")
        p1 = Text(".")
        bin_num2 = Text("001010101010110")
        bin_num2.next_to(bin_num1,buff=0.15)
        p1.next_to(bin_num1,buff=0.05).shift(DOWN*0.2)
        g1 = VGroup(bin_num1,p1,bin_num2).center()
        self.play(Transform(point,g1,replace_mobject_with_target_in_scene=True),FadeOut(bin_num))
        #arrow = always_redraw(lambda : Arrow(start= p1.get_center()+DOWN*2,end=p1.get_center()+0.5*DOWN,color=RED))
        self.play(Uncreate(txt1))
        self.wait(2)

        bin_str = "010101010101000001010101010110"
        num = Text("10920.16668...")
        num.shift(DOWN*2)
        self.play(Create(num))
        self.wait(2)
        # Transform to front radix point
        lastgroup = g1
        lastnum = num
        num = Text("10.66422...")
        num.shift(DOWN*2)
        array,group = create_binary_radix(bin_str,5)
        self.play(Transform(lastgroup,group,replace_mobject_with_target_in_scene=True,run_time=1),
                  Transform(lastnum,num,replace_mobject_with_target_in_scene=True,run_time=1)
                 )
        self.wait(2.5)
        # Transform to back radix point
        lastgroup = group
        lastnum = num
        num = Text("11182250.6875")
        num.shift(DOWN*2)
        array,group = create_binary_radix(bin_str,25)
        self.play(Transform(lastgroup,group,replace_mobject_with_target_in_scene=True,run_time=1),
                  Transform(lastnum,num,replace_mobject_with_target_in_scene=True,run_time=1)
                 )
        self.wait(2.5)


        self.wait(2)

class Float_Concept(Scene):
    def construct(self):
        # Explain exponent bits
        """
        Floats use this basic idea of the scientific notation. For that you have 2 major components, the exponent and mantissa, where the mantissa is just like in fixed point. 
        To safe as many bits as possible we have actually no bits in front of the floating point. This is known as the concept of “implicit one”, where we always set the point to match the format 1.x. Remember that the number is in binary.    
        """
        color = (RED,YELLOW,BLUE)
        group = VGroup()
        
        fe = MathTex("f = ")
        exp = MathTex("2 ^ x", color=color[1])
        star = MathTex("\cdot")
        man = MathTex("1.y", color=color[2])

        exp.shift(RIGHT)
        star.shift(RIGHT * 2)
        man.shift(RIGHT * 3)

        group.add(fe, exp, star, man)
        group.center()

        self.play(FadeIn(group),run_time=0.8)
        self.wait(2)
        self.remove(group)

        fe_new = MathTex("float = ")
        exp_new = MathTex("Exponent", color=color[1])
        star_new = MathTex("\cdot")
        man_new = MathTex("Mantissa", color=color[2])
        exp_new.shift(RIGHT * 2)
        star_new.shift(RIGHT * 4)
        man_new.shift(RIGHT * 6)

        group_new = VGroup()
        group_new.add(fe_new, exp_new, star_new, man_new)
        group_new.center()

        self.play(ReplacementTransform(group, group_new, run_time=1))
        self.wait(2)

        binary_str = "0100010101001010"
        float_block_array, float_text_array, float_block_group = create_float(binary_str, sign_bit = False)
        group_transform = VGroup()
        group_transform.add(float_text_array[1].copy(), float_text_array[0].copy())

        self.remove(fe_new)
        group_new.remove(fe_new)
        #self.play(ReplacementTransform(group_new, group_transform, run_time=1))
        self.play(ReplacementTransform(exp_new, float_text_array[0].copy(), run_time=1))
        self.remove(star_new)
        group_new.remove(star_new)
        self.play(ReplacementTransform(man_new, float_text_array[1].copy(), run_time=1))
        float_block_group.remove(float_text_array[1], float_text_array[0])
        self.play(Create(float_block_group))
        self.wait(2)

        self.remove(group_transform)
        float_block_group.add(float_text_array[1], float_text_array[0])
        exp = 1

        # Explain mantissa bits
        """
        Our Exponent Bits are quite similar to the exponent in the scientific notation, where they just give the exponent or where to place the point. 
        """

