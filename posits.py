from manim import *

def color_posit(text,es=2):
    textlen = len(text.text)
    if text.text == "1" + "0" * (textlen - 1) or text.text == "0" * textlen:
        return text

    text[0].set_color(RED)

    bs = text.text[1]
    i = 1
    while(bs == text.text[i] and i<textlen):
        text[i].set_color(YELLOW)
        i+=1
        if(i>=textlen):
            return text

    text[i].set_color(DARK_BROWN)

    for j in range(es):
        i+=1
        if(i<textlen):
            text[i].set_color(BLUE)

    return text

class SmartLabeledArc(Scene):
    def construct(self):
        radius = 2.5
        start_angle = 3 * PI / 2
        arc_angle = PI
        arc = Arc(radius=radius, angle=arc_angle, start_angle=start_angle,color=DARK_BLUE)
        arc.shift(LEFT)
        self.play(Create(arc))

        center = arc.get_center()

        label_list = [format(i, "05b") for i in range(17)]

        label2_list = [
            r"0", r"\frac{1}{4096}", r"\frac{1}{256}", r"\frac{1}{64}",
            r"\frac{1}{16}", r"\frac{1}{8}", r"\frac{1}{4}", r"\frac{1}{2}",
            r"1", r"2", r"4", r"8", r"16", r"64", r"256", r"4096", r"\pm \infty"
        ]

        num_points = len(label_list)
        for i in range(num_points):
            alpha = i / (num_points - 1)
            point = arc.point_from_proportion(alpha)

            dot = Dot(point,radius=0.05)
            self.add(dot)

            direction = (point - center)
            direction_normalized = direction / np.linalg.norm(direction)

            label = Text(label_list[i], font_size=12)
            color_posit(label)

            label.move_to(point + 0.3 * direction_normalized + RIGHT * 0.1)
            label2 = MathTex(label2_list[i], font_size=15)
            label2.move_to(point - 0.3 * direction_normalized)

            self.add(dot, label, label2)

            self.add(label)
            self.add(label2)

        self.wait(1)

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
        parts.append(VGroup(*number.get_parts_by_tex("(-1)"), *number.get_parts_by_tex("^{sign}")))
        parts.append(VGroup(*number.get_parts_by_tex("useed"), *number.get_parts_by_tex("^k")))
        parts.append(VGroup(*number.get_parts_by_tex("2"), *number.get_parts_by_tex("^{exponent}")))
        parts.append(VGroup(
            *number.get_parts_by_tex("(1+"),
            *number.get_parts_by_tex("fraction"),
            *number.get_parts_by_tex(")")[1],
        ))

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

