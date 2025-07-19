from typing import Text
from typing_extensions import runtime
from manim import *

def create_label_list():
    binary_strings = [
        "0001", "001x", "01xx", "10xx", "110x", "1110"   
    ]

    list = []
    for binary in binary_strings:
        bin_group = VGroup()
        for i, char in enumerate(binary):
            if char == "x":
                t = MathTex(r"\times", font_size=24).set_color(GRAY)
                bin_group.add(t)
            else:
                t = MathTex(char, font_size=24)
                if binary.startswith("0") and char == "1":
                    t.set_color(DARK_BROWN)  # DARK_BROWN = terminierendes 1 (negativ)
                elif binary.startswith("1") and char == "0" and i >= 1:
                    t.set_color(DARK_BROWN)  # terminierendes 0 (positiv)
                else:
                    t.set_color(YELLOW)
                bin_group.add(t)
        bin_group.arrange(RIGHT, buff=0.02)
        list.append(bin_group)
    return list

def create_label_list_exponent():
    # binary_strings = [
    #     "0001", "001x", "01xx", "10xx", "110x", "1110"   
    #
    binary_strings = [format(i, "04b") for i in range(1,16)]


    list = []
    for binary in binary_strings:
        bin_group = VGroup()
        after_terminate = False
        for i, char in enumerate(binary):
            if after_terminate:
                t = MathTex(char, font_size=24).set_color(BLUE)
                bin_group.add(t)
            else:
                t = MathTex(char, font_size=24)
                if binary.startswith("0") and char == "1":
                    t.set_color(DARK_BROWN)  # DARK_BROWN = terminierendes 1 (negativ)
                    after_terminate = True
                elif binary.startswith("1") and char == "0" and i >= 1:
                    t.set_color(DARK_BROWN)  # terminierendes 0 (positiv)
                    after_terminate = True
                else:
                    t.set_color(YELLOW)
                bin_group.add(t)
        bin_group.arrange(RIGHT, buff=0.02)
        list.append(bin_group)
    return list


def get_positinf(bits: str, es_value: int):
    starting_index = 0
    # Regime: starts at bit 1, runs until the first bit flip
    regime_sign = bits[1]
    i = 1
    while i < len(bits) and bits[i] == regime_sign:
        i += 1
    regime_index = i  # index after regime
    exponent_index = regime_index + es_value
    if exponent_index > len(bits):
        exponent_index = len(bits)
    fraction_index = len(bits)
    return (starting_index, regime_index, exponent_index, fraction_index)




def create_posit(str : str,es_value : int):
    group = VGroup()
    arrayblock = []
    # get infos of Posit
    infos = get_positinf(str,es_value)
    color = (RED,YELLOW,DARK_BROWN,BLUE)
    # Creates Numbers and Sqaures for Number
    for i, bit in enumerate(str):
        sq = Square(stroke_width=2)
        for j in range(4):
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
    regime = Text("regime",color=color[1])
    exponent = Text("exponent",color=color[2])
    frac = Text("fraction",color=color[3])
    group.to_edge(LEFT)
    #arranges sign to right place
    sign.shift(2*UP)
    sign.to_edge(LEFT)
    #arranges regime to right place
    regime.shift(2*UP)
    regime.to_edge(LEFT)
    regime.shift(RIGHT*infos[1])
    #arranges exponent to right place
    exponent.shift(2*UP)
    exponent.to_edge(LEFT)
    exponent.shift(RIGHT*infos[2])
    #arranges frac to right place
    frac.shift(2*UP)
    frac.to_edge(LEFT)
    frac.shift(RIGHT*(infos[3]-2))
    #adds text to VGroup
    group += sign
    group += regime
    group += exponent
    group += frac
    #scales to screen size
    group.width = 13
    group.scale_to_fit_width
    group.to_edge(LEFT)
    return arrayblock,group



class BitBlocks(Scene):
    def construct(self):
        binary_str =  "0100101100010100"
        posit_block_array,posit_block_group = create_posit(binary_str,4)
        intro = Text("Floats vs. Posits")
        intro.scale(2)
        intro.to_edge(UP)
        self.play(Create(posit_block_group),Create(intro))
        self.wait(2)


        """
        #Scene 2 with Arrow moving allong
        self.play(Uncreate(intro))
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
        l1 = Line(start=arrow.get_center(),end=arrow.get_center()+RIGHT*12.5)
        self.play(MoveAlongPath(arrow, l1), rate_func=linear,run_time=5)
        self.wait
        """




class Formula(Scene):
    def construct(self):
        formula = MathTex(
            r"(-1)^{s} \cdot useed^k \cdot 2^{e} \cdot (1.f)", font_size=64,
            substrings_to_isolate=[r"(-1)", r"^{s}" ,r"useed", r"^k" , r"2", r"^{e}", r"(1.",  r"f" ,r")"]
        )

        formula.set_color_by_tex("^{s}", RED)
        formula.set_color_by_tex("^k", YELLOW)  # same color as useed for exponent
        formula.set_color_by_tex("^{e}", BLUE)
        formula.set_color_by_tex("f",GREEN)

        self.play(Write(formula))
        self.wait()

        parts =  []
        parts.append(VGroup(*formula.get_parts_by_tex("useed"), *formula.get_parts_by_tex("^k")))
        parts.append(VGroup(*formula.get_parts_by_tex("2"), *formula.get_parts_by_tex("^{e}")))
        parts.append(VGroup(
            *formula.get_parts_by_tex("(1."),
            *formula.get_parts_by_tex("f"),
            *formula.get_parts_by_tex(")")[1]
        ))
        parts.append(VGroup(*formula.get_parts_by_tex("(-1)"), *formula.get_parts_by_tex("^{s}")))

        for part in parts:
            part_center = part.get_center()

            others = VGroup(*[p for p in formula if p != part])
            self.play(
                others.animate.set_opacity(0),
                part.animate.set_opacity(1),
                run_time=0.8
            )

            # Zoom in: scale up & move part to center
            self.play(
                part.animate.scale(1.6).move_to(ORIGIN),
                run_time=1
            )
            self.wait(0.7)

            #Here start of anim in between
            if(parts.index(part)==0):
                self.regime(part)
            elif(parts.index(part)==1):
                self.exponent(part)
            elif(parts.index(part)==2):
                self.fraction(part)
            elif(parts.index(part)==3):
                self.sign(part)
            #Here end of anim in between

            # Zoom out: back to original scale and position
            self.play(
                part.animate.scale(0.625).move_to(formula.get_center() + part_center - formula.get_center()),
                run_time=1
            )

            # Restore opacity of all parts
            self.play(
                others.animate.set_opacity(1),
                run_time=0.8
            )
            self.wait(0.3)

        self.play(FadeOut(formula), run_time=0.8)
        self.wait()

    def regime(self,useed_k):
        # Titel "Regime"
        title = Text("regime", font_size=72, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait()

        # === useed^k verschwindet ===
        self.play(FadeOut(useed_k),FadeOut(title), run_time=0.8)

        # === es und useed Definition mit Gleichheitszeichen zentriert ===
        es_tex = MathTex("es", "=", "2").scale(1.2)
        es_eq_index = 1  # Index vom "=" im es_tex

        # Platziere es_tex so, dass das Gleichheitszeichen im Zentrum liegt
        es_tex.move_to(ORIGIN - es_tex[es_eq_index].get_center())

        # useed mit vollständiger Definition
        useed_full = MathTex(r"useed", "=", r"es^{2^2}", "=", r"2^{2^2}", "=", "16").scale(1.2)
        # Gleiche Ausrichtung: Gleichheitszeichen von useed_full auf Gleichheitszeichen von es_tex
        useed_eq_index = 1  # Erstes "="
        useed_full.move_to(es_tex).align_to(es_tex[es_eq_index], LEFT).next_to(es_tex, DOWN, buff=0.4).shift(LEFT*0.45)

        self.play(Write(es_tex))
        self.wait()
        self.play(Write(useed_full))
        self.wait()

        # === Kürzen auf useed = 16, ebenfalls am Gleichheitszeichen zentriert ===
        useed_simple = MathTex("useed", "=", "16").scale(1.2)
        useed_simple.move_to(useed_full).align_to(useed_full[useed_eq_index], LEFT).shift(RIGHT*0.2)

        self.play(Transform(useed_full, useed_simple), run_time=1)
        self.wait()

        # === Oben rechts platzieren, sauber skaliert ===
        self.es_group = VGroup(es_tex, useed_full)
        self.play(
            self.es_group.animate.scale(0.7).to_corner(UR).shift(DOWN * 0.5),
            run_time=1
        )
        self.wait()

        self.play(FadeIn(useed_k), run_time=0.8)
        self.wait(1)

        self.play(FadeOut(useed_k), run_time=0.8)
        self.wait()

        self.k_vlauetable()

        self.smartlabeledarc()

        self.play(FadeOut(self.es_group), run_time=0.8)
        self.wait()

        self.play(FadeIn(useed_k), run_time=0.8)
        self.wait()

        return self.es_group

    def k_vlauetable(self):
        #Start von Tabelle
        binary_strings = [
            "0001", "001x", "01xx", "10xx", "110x", "1110"
        ]
        k_values = ["-3", "-2", "-1", "0", "1", "2"]

        # Eine Liste von VGroups für jede Spalte
        columns = []
        for binary, k_val in zip(binary_strings, k_values):
            bin_group = VGroup()
            for i, char in enumerate(binary):
                if char == "x":
                    t = MathTex(r"\times", font_size=38).set_color(GRAY)
                else:
                    t = MathTex(char, font_size=38)
                    if binary.startswith("0") and char == "1":
                        t.set_color(DARK_BROWN)  # DARK_BROWN = terminierendes 1 (negativ)
                    elif binary.startswith("1") and char == "0" and i >= 1:
                        t.set_color(DARK_BROWN)  # terminierendes 0 (positiv)
                    else:
                        t.set_color(YELLOW)
                bin_group.add(t)

            bin_group.arrange(RIGHT, buff=0.05)
            k_text = Text(k_val, font_size=32)

            col = VGroup(bin_group, k_text).arrange(DOWN, buff=0.65)
            columns.append(col)

        # Komplette Tabelle horizontal anordnen
        table_body = VGroup(*columns).arrange(RIGHT, buff=0.6)

        # Überschriften
        header_bin = Text("binary", font_size=32)
        header_k = Text("value of k", font_size=32)
        headers = VGroup(header_bin, header_k).arrange(DOWN, buff=0.6)
        headers.next_to(table_body, LEFT, buff=0.8)
        # Komplettgruppe
        table = VGroup(headers, table_body).move_to(ORIGIN)
        table.shift(DOWN*0.5)

        self.play(Write(header_bin), Write(header_k))
        self.play(LaggedStart(*[FadeIn(col) for col in columns], lag_ratio=0.1))
        self.wait(3)

        self.play(FadeOut(table))
        self.wait()
        # Ende von Tabelle


    def smartlabeledarc(self):
        radius = 2.5
        start_angle = 3 * PI / 2
        arc_angle = PI
        arc = Arc(radius=radius, angle=arc_angle, start_angle=start_angle,color=DARK_BLUE)
        arc.shift(LEFT)
        self.play(Create(arc))

        center = arc.get_center()

        label_list = create_label_list()

        label2_list = [
            r"\frac{1}{4096}", r"\frac{1}{256}", 
            r"\frac{1}{16}",
            r"1", r"16", r"256"]

        visual_elements = VGroup(arc)
        num_points = len(label2_list)
        for i in range(num_points):
            alpha = i / (num_points - 1)
            point = arc.point_from_proportion(alpha)

            dot = Dot(point,radius=0.05)
            self.add(dot)

            direction = (point - center)
            direction_normalized = direction / np.linalg.norm(direction)

            label = label_list[i]

            label.move_to(point + 0.3 * direction_normalized + RIGHT * 0.1)
            label2 = MathTex(label2_list[i], font_size=20)
            label2.move_to(point - 0.4 * direction_normalized)

            visual_elements.add(dot, label, label2)
            self.add(dot, label, label2)

            self.add(label)
            self.add(label2)

        self.wait(1)

        # Alles auf einmal verschwinden lassen
        self.play(FadeOut(visual_elements), run_time=1)
        self.wait()


    def exponent(self, two_e):
        # Title "Exponent"
        title = Text("exponent", font_size=72, color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Fade out the title
        self.play(FadeOut(title),FadeOut(two_e), run_time=0.8)
        self.wait()

        self.play(FadeIn(self.es_group), run_time=0.8)
        self.wait()

        # Add brace under just the exponent (index 1 is the exponent part "0\\cdots0")
        bits = MathTex("e = 11011\cdots" , font_size=50, substrings_to_isolate=[r"e",r"1011\cdots"])
        bits.set_color_by_tex("e", BLUE)
        bits_part = bits[2]
        self.play(Create(bits), run_time=1)
        self.wait()
        brace = Brace(bits_part, direction=DOWN)
        brace_text = MathTex("\le es", font_size=50).next_to(brace, DOWN)
        self.play(GrowFromCenter(brace), FadeIn(brace_text), run_time=1)
        self.wait(1)        # Remove bitstring and brace

        example_bits = MathTex("e = 10" , font_size=50, substrings_to_isolate=[r"e",r"10" ])
        example_bits.set_color_by_tex("e", BLUE)
        example_brace = Brace(example_bits[2], direction=DOWN)

        brace_text_example = MathTex("\le 2", font_size=50).next_to(brace, DOWN)

        self.play(Transform(bits,example_bits), Transform(brace_text,brace_text_example),Transform(brace,example_brace),run_time=1)
        self.wait(1)

        self.play(FadeOut(brace), FadeOut(brace_text), FadeOut(bits), run_time=0.8)
        self.wait()

        self.smartlabeledarc_exponent()
        self.play(FadeOut(self.es_group), run_time=0.8)
        self.wait()

        self.play(FadeIn(two_e), run_time=0.8)
        self.wait()

    def smartlabeledarc_exponent(self):
        radius = 2.5
        start_angle = 3 * PI / 2
        arc_angle = PI
        arc = Arc(radius=radius, angle=arc_angle, start_angle=start_angle,color=DARK_BLUE)
        arc.shift(LEFT)
        self.play(Create(arc))

        center = arc.get_center()

        label_list = create_label_list_exponent()

        label2_list = [
            r"\frac{1}{4096}", r"\frac{1}{256}", r"\frac{1}{64}",
            r"\frac{1}{16}", r"\frac{1}{8}", r"\frac{1}{4}", r"\frac{1}{2}",
            r"1", r"2", r"4", r"8", r"16", r"64", r"256"
        ]

        visual_elements = VGroup(arc)
        num_points = len(label2_list)
        for i in range(num_points):
            alpha = i / (num_points - 1)
            point = arc.point_from_proportion(alpha)

            dot = Dot(point,radius=0.05)
            self.add(dot)

            direction = (point - center)
            direction_normalized = direction / np.linalg.norm(direction)

            label = label_list[i]

            label.move_to(point + 0.3 * direction_normalized + RIGHT * 0.1)
            label2 = MathTex(label2_list[i], font_size=18)
            label2.move_to(point - 0.35 * direction_normalized)

            visual_elements.add(dot, label, label2)
            self.add(dot, label, label2)

            self.add(label)
            self.add(label2)

        self.wait(3)

        # Alles auf einmal verschwinden lassen
        self.play(FadeOut(visual_elements), run_time=1)
        self.wait()

    def fraction(self,one_p_f):
        # Titel "Fraction"
        
        self.play(FadeOut(one_p_f), run_time=0.8)
        self.wait()

        bits_point = MathTex("1.11011100001" , font_size=70, substrings_to_isolate=[r"1.",r"11011100", r"001" ])

        bits_point.set_color_by_tex("11011100", GREEN)
        bits_point.set_color_by_tex("001", GREEN)

        self.play(Create(bits_point), run_time=0.8)
        self.wait()

        title = Text("fraction", font_size=72, color=GREEN).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        self.play(FadeOut(title), run_time=0.8)
        self.wait()

        # Briefly highlight the implicit '1'
        bits_point_one = bits_point.get_part_by_tex("1.")
        self.play(Indicate(bits_point_one,color="WHITE"),run_time=1)
        self.wait()

        self.play(FadeOut(bits_point_one),run_time=0.8)
        self.wait()

        bits_over = bits_point.get_part_by_tex("001")
        print(bits_over)
        self.play(bits_over.animate.set_color(RED_E), run_time=1)
        self.play(Uncreate(bits_over))
        self.wait(1)

        bits_leftover = bits_point.get_part_by_tex("11011100")
        self.play(FadeOut(bits_leftover),run_time=0.8)
        self.wait()

        self.play(FadeIn(one_p_f), run_time=0.8)
        self.wait()

    def sign(self,mone_s):
        # Titel "Sign-Bit"
        title = Text("sign bit", font_size=72, color=RED).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        self.play(FadeOut(title), run_time=0.8)
        self.wait()


class SpecialCases(Scene):
    def construct(self):
        title = Text("special cases", font_size=72, color=WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # First expression: 000... = 0
        zero_expr = MathTex(r"000\dots = 0", font_size=64)
        zero_expr.to_edge(LEFT)

        # Second expression: 100... = ±∞
        inf_expr = MathTex(r"100\dots = \pm \infty", font_size=64)
        inf_expr.next_to(zero_expr, DOWN, buff=0.5).to_edge(LEFT)

        group = VGroup(zero_expr, inf_expr).move_to(ORIGIN)
        inf_expr.shift(0.04*RIGHT)

        # Animate in
        self.play(Write(zero_expr))
        self.wait(0.5)
        self.play(Write(inf_expr))
        self.wait()

        self.play(FadeOut(title), run_time=0.8)
        self.wait()
