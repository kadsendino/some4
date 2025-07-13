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

            label.move_to(point + 0.3 * direction_normalized + RIGHT * 0.1)  # Abstand von Punkt

            label2 = MathTex(label2_list[i], font_size=15)
            label2.move_to(point - 0.3 * direction_normalized)  # Abstand von Punkt

            self.add(dot, label, label2)

            self.add(label)
            self.add(label2)

        self.wait()

