from manim import *


def create_float(str : str):
    group = VGroup()
    arrayblock = []
    # get infos of Float16 (IEEE)
    infos = (0,5,len(str))
    color = (RED,YELLOW,BLUE)
    #Creates Numbers and Sqaures for Number
    for i, bit in enumerate(str):
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
        
        #Creates Text for 
    sign = Text("sign",color=color[0])
    exponent = Text("exponent",color=color[1])
    mantissa = Text("mantissa",color=color[2])
    group.to_edge(LEFT)
    #arranges sign to right place
    sign.shift(2*UP)
    sign.to_edge(LEFT)
    #arranges exponent to right place
    exponent.shift(2*UP)
    exponent.to_edge(LEFT)
    exponent.shift(RIGHT*2)
    #arranges mantissa to right place
    mantissa.shift(2*UP)
    mantissa.to_edge(LEFT)
    mantissa.shift(RIGHT*12)
    #adds text to VGroup
    group += sign
    group += exponent
    group += mantissa
    #scales to screen size
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    return arrayblock,group




def create_binary_radix(str: str, index: int):
    point = Text(".")
    b1 = Text(str[:index])
    b2 = Text(str[index:])
    b2.next_to(b1,buff=0.15)
    point.next_to(b1,buff=0.05).shift(DOWN*0.2)
    return [b1,point,b2],VGroup(b1,point,b2).center()

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


class Test(Scene):
    def construct(self):
        binary_str = "0100010101001010"
        a = 10
        array,group = create_binary_radix(binary_str,5)
        a1,g1 = create_bin_index_list2(a,3)
        self.play(Create(g1))
        #self.play(Create(group))
        self.wait(2)
        



class BitBlocks(Scene):
    def construct(self):
        binary_str = "0100010101001010"
        posit_block_array,posit_block_group = create_float(binary_str)
        self.play(Create(posit_block_group))
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

        self.wait(2)

        bin_str = "010101010101000001010101010110"
        lastgroup = g1
        tmp_a,tmp_group = create_bin_index_list(30)
        self.play(Uncreate(txt1),Create(tmp_group))
        for i in range(1,30):
            array,group = create_binary_radix(bin_str,i)
            indexl1_array,indexl1_group = create_bin_index_list(30,bias=i)
            self.play(Transform(lastgroup,group,replace_mobject_with_target_in_scene=True,run_time=0.1),
                      Transform(tmp_group,indexl1_group,replace_mobject_with_target_in_scene=True,run_time=0.1)
                      )
            self.wait(0.3)
            lastgroup = group

        
        

        self.wait(2)

