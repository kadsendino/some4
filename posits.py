from manim import *

def create_label_list():
    binary_strings = [
        "0000", "0001", "001x", "01xx", "10xx", "110x", "1110", "1111"
    ]

    list = []
    for binary in binary_strings:
        bin_group = VGroup()
        for i, char in enumerate(binary):
            if char == "x":
                t = MathTex(r"\times", font_size=16).set_color(GRAY)
                bin_group.add(t)
            else:
                t = MathTex(char, font_size=16)
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

class Formula(Scene):
    def construct(self):
        number = MathTex(
            r"(-1)^{sign} \cdot useed^k \cdot 2^{exponent} \cdot (1+fraction)",
            substrings_to_isolate=[r"(-1)", r"^{sign}" ,r"useed", r"^k" , r"2", r"^{exponent}", r"(1+",  r"fraction" , r")"]
        )

        number.set_color_by_tex("^{sign}", RED)
        number.set_color_by_tex("^k", YELLOW)  # same color as useed for exponent
        number.set_color_by_tex("^{exponent}", BLUE)
        number.set_color_by_tex("fraction",GREEN)

        self.play(Write(number))
        self.wait()

        print("(-1):", number.get_parts_by_tex("(-1)"))
        print("(1+):", number.get_parts_by_tex("(1+"))
        print("fraction:", number.get_parts_by_tex("fraction"))
        print("):", number.get_parts_by_tex(")"))


        parts =  []
        parts.append(VGroup(*number.get_parts_by_tex("useed"), *number.get_parts_by_tex("^k")))
        parts.append(VGroup(*number.get_parts_by_tex("2"), *number.get_parts_by_tex("^{exponent}")))
        parts.append(VGroup(
            *number.get_parts_by_tex("(1+"),
            *number.get_parts_by_tex("fraction"),
            *number.get_parts_by_tex(")")[1],
        ))
        parts.append(VGroup(*number.get_parts_by_tex("(-1)"), *number.get_parts_by_tex("^{sign}")))

        for part in parts:
            part_center = part.get_center()

            others = VGroup(*[p for p in number if p != part])
            self.play(
                others.animate.set_opacity(0),
                part.animate.set_opacity(1),
                run_time=0.5
            )

            # Zoom in: scale up & move part to center
            self.play(
                part.animate.scale(2).move_to(ORIGIN),
                run_time=1
            )
            self.wait(0.7)

            #Here start of anim in between
            if(parts.index(part)==0):
                self.regime(part)
            #Here end of anim in between

            # Zoom out: back to original scale and position
            self.play(
                part.animate.scale(0.5).move_to(number.get_center() + part_center - number.get_center()),
                run_time=1
            )

            # Restore opacity of all parts
            self.play(
                others.animate.set_opacity(1),
                run_time=0.5
            )
            self.wait(0.3)

    def regime(self,useed_k):
        # Titel "Regime"
        title = Text("Regime", font_size=72, color=YELLOW).to_edge(UP)
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
        es_group = VGroup(es_tex, useed_full)
        self.play(
            es_group.animate.scale(0.7).to_corner(UR).shift(DOWN * 0.5),
            run_time=1
        )
        self.wait()

        self.play(FadeIn(useed_k), run_time=0.8)
        self.wait(1)

        self.play(FadeOut(useed_k), run_time=0.8)
        self.wait()

        #Start von Tabelle
        binary_strings = [
            "0000", "0001", "001x", "01xx", "10xx", "110x", "1110", "1111"
        ]
        k_values = ["-4", "-3", "-2", "-1", "0", "1", "2", "3"]

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
        header_bin = Text("Binary", font_size=32)
        header_k = Text("Value of k", font_size=32)
        headers = VGroup(header_bin, header_k).arrange(DOWN, buff=0.6)
        headers.next_to(table_body, LEFT, buff=0.8)
        # Komplettgruppe
        table = VGroup(headers, table_body).move_to(ORIGIN)
        table.shift(DOWN*0.5)

        self.play(Write(header_bin), Write(header_k))
        self.play(LaggedStart(*[FadeIn(col) for col in columns], lag_ratio=0.1))
        self.wait()

        self.play(FadeOut(table))
        self.wait()
        # Ende von Tabelle

        self.smartlabeledarc()

        self.play(FadeOut(es_group), run_time=0.8)
        self.wait()

        self.play(FadeIn(useed_k), run_time=0.8)
        self.wait()

        return es_group

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
            r"1", r"16", r"256" ]

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
            label2 = MathTex(label2_list[i], font_size=15)
            label2.move_to(point - 0.3 * direction_normalized)

            visual_elements.add(dot, label, label2)
            self.add(dot, label, label2)

            self.add(label)
            self.add(label2)

        self.wait(1)

        # Alles auf einmal verschwinden lassen
        self.play(FadeOut(visual_elements), run_time=1)
        self.wait()

