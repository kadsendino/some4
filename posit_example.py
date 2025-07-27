from manim import *
from posits import create_posit,get_positinf

def create_arrow(start_point,end_point,color_arc=WHITE):
        # Create a curved arc between points
        arc = ArcBetweenPoints(start_point, end_point, angle=-PI/2, stroke_width=4, color=color_arc)
        arc.add_tip(tip_length=0.1,tip_shape=StealthTip).shift(DOWN*0.1)  # add arrow tip
        return arc

def split_posit_parts(binary_str: str, es_value: int):
    posit_block_array, posit_group = create_posit(binary_str, es_value)

    # Info: [sign_index, last_regime_index, last_exponent_index, last_fraction_index]
    infos = get_positinf(binary_str, es_value)

    # Extract parts
    squares = VGroup()
    sign_bits = VGroup()
    regime_bits = VGroup()
    exponent_bits = VGroup()
    fraction_bits = VGroup()
    field_labels = VGroup()

    for i, (sq, txt) in enumerate(posit_block_array):
        squares.add(sq)
        if i == infos[0]:  # sign
            sign_bits.add(txt)
        elif infos[0] < i <= infos[1]:  # regime
            regime_bits.add(txt)
        elif infos[1] < i <= infos[2]:  # exponent
            exponent_bits.add(txt)
        elif infos[2] < i <= infos[3]:  # fraction
            fraction_bits.add(txt)

    # Extract the text labels ("sign", "regime", etc.) from posit_group
    for mobj in posit_group:
        if isinstance(mobj, Text) and mobj not in sign_bits and mobj not in regime_bits and mobj not in exponent_bits and mobj not in fraction_bits:
            field_labels.add(mobj)

    return posit_block_array, posit_group, squares, sign_bits, regime_bits, exponent_bits, fraction_bits, field_labels

class Example(Scene):
    def construct(self):
        self.enable_es_useed()

        binary_str = "0110111111111000"
        posit_block_array, posit_block_group, squares, sign_bits, regime_bits, exponent_bits, fraction_bits, field_labels = split_posit_parts(binary_str,2)
        posit_block_group.move_to(ORIGIN)


        sign_bits.set_opacity(0)
        regime_bits.set_opacity(0)
        # regime_bits.set_color(opacity=0)
        exponent_bits.set_opacity(0)
        fraction_bits.set_opacity(0)
        field_labels.set_opacity(0)

        self.play(Create(squares))
        self.wait(1)

        brace = Brace(squares, direction=DOWN)
        brace_text = Text("16 bits", font_size=50).next_to(brace, DOWN)
        self.play(GrowFromCenter(brace), FadeIn(brace_text), run_time=1)
        self.wait(2)        # Remove bitstring and brace

        self.play(FadeOut(brace), FadeOut(brace_text), run_time=1)
        self.wait()

        self.play(posit_block_group.animate.scale(0.625).to_edge(DL, buff=0.6))

        sign_bits = sign_bits.copy().set_opacity(1)
        regime_bits = regime_bits.copy().set_opacity(1)
        exponent_bits = exponent_bits.copy().set_opacity(1)
        fraction_bits = fraction_bits.copy().set_opacity(1)
        field_labels = field_labels.copy().set_opacity(1)

        number = self.create_regime_bits(regime_bits,field_labels)
        number = self.create_exponent_bits(exponent_bits,field_labels,number)
        self.create_fraction_bits(fraction_bits,field_labels,number)
        self.create_sign_bits(sign_bits,field_labels)

        posit_block_group.add(regime_bits)
        posit_block_group.add(exponent_bits)
        posit_block_group.add(fraction_bits)
        posit_block_group.add(sign_bits)

        for field_label in field_labels:
            posit_block_group.add(field_label)

        self.play(posit_block_group.animate.scale(1.6).move_to(ORIGIN))
        self.wait(2)

        posit_block_array2,posit_block_group2 = create_posit(binary_str,2)
        posit_block_group2.move_to(ORIGIN)
        self.play(FadeIn(posit_block_group2))
        posit_block_group.set_opacity(0)

        self.twos_complement(posit_block_array2,posit_block_group2)

        self.play(FadeOut(posit_block_group2),FadeOut(self.es_group))
        self.wait(1)

    def twos_complement(self,posit_block_array, posit_block_group):
        # First flip
        for i, (square, bit_text) in enumerate(posit_block_array):
            current_char = bit_text.text
            flipped_char = "1" if current_char == "0" else "0"

            new_bit = Text(flipped_char).scale(0.625)
            new_bit.move_to(bit_text.get_center())
            new_bit.set_fill(bit_text.get_color())

            self.play(ReplacementTransform(bit_text, new_bit), run_time=0.2)
            posit_block_array[i] = (square, new_bit)

        self.wait(4)

        # Second flip with "+1"
        for i in reversed(range(len(posit_block_array))):
            square, bit_text = posit_block_array[i]

            plus_one = Text("+1", font_size=24).next_to(square, DOWN)
            self.play(FadeIn(plus_one), run_time=0.3)
            self.play(plus_one.animate.move_to(bit_text), run_time=0.3)

            current_char = bit_text.text
            flipped_char = "1" if current_char == "0" else "0"

            new_bit = Text(flipped_char).scale(0.625)
            new_bit.move_to(bit_text.get_center())
            new_bit.set_fill(bit_text.get_color())

            self.play(ReplacementTransform(bit_text, new_bit), FadeOut(plus_one), run_time=0.3)
            posit_block_array[i] = (square, new_bit)

            if(bit_text.text=="0"):
                break

        self.wait(2)


    def create_sign_bits(self,sign_bits,field_labels):
        dec = MathTex(r"-255.03125_{10}",substrings_to_isolate=[r"-"]).scale(1.5)
        dec.set_color_by_tex("-",RED)

        self.play(Write(dec))
        self.wait(1)

        self.play(ReplacementTransform(dec, sign_bits), FadeIn(field_labels[0]))
        self.wait(2)

    def create_fraction_bits(self, fraction_bits, field_labels, number):
        number2 = MathTex(r"-1.111111100001_2",substrings_to_isolate=["-1.","111111100001","01","_2"]).scale(1.3)

        self.play(number2.animate.set_color_by_tex("111111100001", GREEN),number2.animate.set_color_by_tex("01", GREEN))
        number.set_opacity(0)
        self.wait(2)

        bits_point_one = number2.get_part_by_tex("-1.")
        base_two = number2.get_part_by_tex("_2")
        self.play(FadeOut(base_two),FadeOut(bits_point_one),run_time=0.8)
        self.wait(1)

        bits_over = VGroup()

        bits_over.add(number2.get_part_by_tex("01")[-1])
        bits_over.add(number2.get_part_by_tex("01")[-2])
        self.play(bits_over.animate.set_color(RED_E), run_time=1)
        self.play(Uncreate(bits_over))
        self.wait(1)

        frac_bits = number2.get_part_by_tex("1111111000")

        # Add "f = " to the left
        f_expr = MathTex("f", "=").scale(1.3)
        f_expr.set_color_by_tex("f", GREEN)
        f_expr.next_to(frac_bits, LEFT, buff=0.5)

        self.play(Write(f_expr))
        self.wait(1)

        self.play(FadeOut(f_expr),ReplacementTransform(frac_bits, fraction_bits), FadeIn(field_labels[3]))
        self.wait(2)

    def create_exponent_bits(self, exponent_bits, field_labels, number):
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

    def create_regime_bits(self,regime_bits,field_labels):
        dec = MathTex(r"-255.03125_{10}").scale(1.5)
        bin_val = MathTex(r"-11111111.00001_2").scale(1.3)
        dot = bin_val[0][9]  # the dot in '11111111.00001'

        bin_val_shifted = MathTex(r"-1111.111100001_2").scale(1.3)
        dot_shifted = bin_val_shifted[0][5]  # the dot in '11111111.00001'

        self.play(Write(dec))
        self.wait(1)
        self.play(ReplacementTransform(dec, bin_val))
        self.wait(2)

        # Step 1: Start with "k = 0"
        k_expr = MathTex("k", "=", "0").scale(1.3).shift(UP)
        k_expr.set_color_by_tex("k", YELLOW)
        self.play(Write(k_expr))
        self.wait(1)

        # Step 2: Transform "k = 0" -> "k = 1"
        k_expr_target = MathTex("k", "=", "1").scale(1.3).shift(UP)
        k_expr_target.set_color_by_tex("k", YELLOW)

        start_point = dot.get_center()
        end_point = dot_shifted.get_center()

        arc = create_arrow(start_point,end_point,YELLOW)

        self.play(Create(arc))
        self.wait(0.7)

        log = MathTex(r"\log_2 useed = 4").scale(0.5).next_to(arc,DOWN,buff=0.1)
        self.play(Create(log))
        self.wait(1)


        self.play(ReplacementTransform(bin_val, bin_val_shifted),ReplacementTransform(k_expr, k_expr_target), FadeOut(arc),FadeOut(log))
        self.wait(2)

        # Step 3: Add "→ 110" next to it
        bits_expr = MathTex(r"\rightarrow", "1", "1", "0").scale(1.3).shift(DOWN)
        bits_expr.set_color_by_tex("1", YELLOW)
        bits_expr.set_color_by_tex("0", DARK_BROWN)
        bits_expr.next_to(k_expr, RIGHT, buff=0.6)

        self.play(FadeIn(bits_expr))
        self.wait(2)

        self.play(ReplacementTransform(bits_expr,regime_bits),FadeOut(k_expr_target),FadeIn(field_labels[1]))
        self.wait(2)

        return bin_val_shifted

    def enable_es_useed(self):
        es_tex = MathTex("es", "=", "2").scale(1.2)
        es_eq_index = 1  # Index vom "=" im es_tex

        # Platziere es_tex so, dass das Gleichheitszeichen im Zentrum liegt
        es_tex.move_to(ORIGIN - es_tex[es_eq_index].get_center())

        # useed mit vollständiger Definition
        useed_full = MathTex(r"useed", "=", r"es^{2^2}", "=", r"2^{2^2}", "=", "16").scale(1.2)
        # Gleiche Ausrichtung: Gleichheitszeichen von useed_full auf Gleichheitszeichen von es_tex
        useed_eq_index = 1  # Erstes "="
        useed_full.move_to(es_tex).align_to(es_tex[es_eq_index], LEFT).next_to(es_tex, DOWN, buff=0.4).shift(LEFT*0.45)

        # === Kürzen auf useed = 16, ebenfalls am Gleichheitszeichen zentriert ===
        useed_simple = MathTex("useed", "=", "16").scale(1.2)
        useed_simple.move_to(useed_full).align_to(useed_full[useed_eq_index], LEFT).shift(RIGHT*0.2)

        self.play(Write(es_tex),run_time=1)
        self.play(Write(useed_simple),run_time=1)
        self.wait(2)

        # === Oben rechts platzieren, sauber skaliert ===
        self.es_group = VGroup(es_tex, useed_simple)
        self.play(
            self.es_group.animate.scale(0.7).to_corner(UR).shift(DOWN * 0.5),
            run_time=1
        )
        self.wait(2)





