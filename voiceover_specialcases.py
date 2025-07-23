from manim import *
from pydub.utils import mediainfo

class SpecialCases(Scene):
    def play_voiceover(self, filename: str):
        """Play the voiceover and wait exactly for its duration"""
        self.add_sound(filename)
        duration = float(mediainfo(filename)['duration'])
        self.wait(duration)

    def construct(self):
        # Title
        title = Text("special cases", font_size=72, color=WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # === Part 1: Introduction ===
        # TTS: "There are two special cases for posits."
        self.play_voiceover("part1_intro.mp3")

        # === Part 2: First case: 000... = 0 ===
        zero_expr = MathTex(r"000\dots = 0", font_size=64).to_edge(LEFT)

        # === Part 3: Second case: 100... = ±∞ ===
        inf_expr = MathTex(r"100\dots = \pm \infty", font_size=64)
        inf_expr.next_to(zero_expr, DOWN, buff=0.5).to_edge(LEFT)

        group = VGroup(zero_expr, inf_expr).move_to(ORIGIN)
        inf_expr.shift(0.04 * RIGHT)

        # TTS: "Only zeros equal zero."
        self.play(Write(zero_expr))
        self.play_voiceover("part2_zero_case.mp3")

        # TTS: "A single one following only zeros equals plus or minus infinity."
        self.play(Write(inf_expr))
        self.play_voiceover("part3_inf_case.mp3")

        # Fade out
        self.play(FadeOut(title), run_time=0.8)
        self.wait(0.5)

