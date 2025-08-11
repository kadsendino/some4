from manim import *

class ExponentialGraph(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 260, 26],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4
        )

        # Labels
        labels = axes.get_axis_labels(x_label=r"\text{time}", y_label=r"\text{computing power}")

        # Exponential function y = 2^x
        graph = axes.plot(lambda x: 2**x, color=PINK)

        # Graph label
        graph_label = axes.get_graph_label(graph, label=r"\text{moore's law}")

        # Animate
        self.play(Create(axes), Write(labels))
        self.wait(1.5)
        self.play(Create(graph), Write(graph_label))
        self.wait(3.5)

        # Fade out all elements
        self.play(
            FadeOut(axes),
            FadeOut(labels),
            FadeOut(graph),
            FadeOut(graph_label)
        )
