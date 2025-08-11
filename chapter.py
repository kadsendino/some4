from typing_extensions import runtime
from manim import *


CHAPTER_COLOR = WHITE

chapters = [
    "1. What were Floats again?",
    "2. How do Posits work?",
    "3. Comparison Floats vs. Posits"
]

class TableOfContents(Scene):
    def construct(self):
        group = VGroup()
        for i,text in enumerate(chapters):
            chapter = Text(text, font_size=48, color=CHAPTER_COLOR).to_edge(UP).to_edge(LEFT)
            chapter.shift(DOWN * 2).shift(DOWN * i)
            group.add(chapter)

            self.play(Write(chapter),run_time=1)
            self.wait(1)

        self.play(FadeOut(group))
        self.wait(1)

class ChapterTitle(Scene):
    def construct(self):
        for i,text in enumerate(chapters):
            chapter = Text(text, font_size=48, color=CHAPTER_COLOR)

            self.play(Write(chapter),run_time=1)
            self.wait(2)

            self.play(FadeOut(chapter))
            self.wait(1)

class ImageTest(Scene):
    def construct(self):
        img  = ImageMobject("data/floats.png").scale_to_fit_height(config.frame_height).scale(0.28).to_edge(LEFT)
        img2 = ImageMobject("data/posits.png").scale_to_fit_height(config.frame_height).scale(0.28)
        img3 = ImageMobject("data/posits.png").scale_to_fit_height(config.frame_height).scale(0.28).to_edge(RIGHT)


        padding = 0.075
        img_rect = RoundedRectangle(width=img.width+padding,height=img.height+padding,corner_radius=0.2,color=CHAPTER_COLOR,stroke_width=3)
        img_rect.move_to(img)
        img_rect2 = RoundedRectangle(width=img.width+padding,height=img.height+padding,corner_radius=0.2,color=CHAPTER_COLOR,stroke_width=3)
        img_rect2.move_to(img2)
        img_rect3 = RoundedRectangle(width=img.width+padding,height=img.height+padding,corner_radius=0.2,color=CHAPTER_COLOR,stroke_width=3)
        img_rect3.move_to(img3)

        img_text = Text("floats",font_size=32,color=CHAPTER_COLOR).next_to(img,UP)
        img_text2 = Text("posits",font_size=32,color=CHAPTER_COLOR).next_to(img2,UP)
        img_text3 = Text("comparison",font_size=32,color=CHAPTER_COLOR).next_to(img3,UP)


        self.play(FadeIn(img),FadeIn(img_rect),FadeIn(img_text),run_time=1)
        self.wait(5)
        self.play(FadeIn(img2),FadeIn(img_rect2),FadeIn(img_text2),run_time=1)
        self.wait(5)
        self.play(FadeIn(img3),FadeIn(img_rect3),FadeIn(img_text3),run_time=1)
        self.wait(13)
        self.play(FadeOut(img),FadeOut(img_rect),FadeOut(img_text),FadeOut(img2),FadeOut(img_rect2),FadeOut(img_text2),FadeOut(img3),FadeOut(img_rect3),FadeOut(img_text3))
        # self.play(FadeOut(img2),FadeOut(img_rect2),FadeOut(img_text2))
        # self.play(FadeOut(img3),FadeOut(img_rect3),FadeOut(img_text3))
        self.wait(1)

class ImageFadeInFromBottom(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("data/beatingfloatspaper.png")

        # Set image size and angle
        image.scale(0.7)  # You can adjust size here
        image.rotate(PI / 64)  # Rotate by 22.5 degrees (adjust as needed)

        # Set the starting position (below screen) and zero opacity
        image.move_to(DOWN * 4)  # Start from below
        image.set_opacity(0)    # Fully transparent

        # Target position (center or adjusted)
        target_position = ORIGIN  # Final position slightly above center

        # Animate moving up and fading in
        self.play(
            image.animate.move_to(target_position).set_opacity(1),
            run_time=2,
            rate_func=smooth
        )

        self.wait(12)

        # Animate: fade out (and optionally move down again)
        self.play(
            image.animate.move_to(DOWN * 4).set_opacity(0),
            run_time=2,
            rate_func=smooth
        )

        self.wait(0.5)

class AtariBlendInOut(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("data/Atari_1040STf_v2.jpg")
        
        # Set the initial scale of the image
        image.scale(0.3)
        
        # Position the image in the center
        image.move_to(ORIGIN)
        
        # Start the image fully transparent
        image.set_opacity(0)
        
        # Animate the image blending in (opacity from 0 to 1)
        self.play(image.animate.set_opacity(1),run_time=1)
        
        # Wait for a moment to show the image fully visible
        self.wait(8)
        
        # Animate the image fading out (opacity from 1 to 0)
        self.play(image.animate.set_opacity(0),run_time=1)

class AtariIEEE(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("data/Atari_1040STf_v2.jpg")
        image.scale(0.3)
        image.move_to(ORIGIN)

        # IEEE-Logo-Style Text
        ieee_color = "#31709e"  # IEEE-Blau
        # Alternativ könntest du eine systemseitige Schrift verwenden, z. B. "Helvetica Bold"
        ieee_text = Text(
            "IEEE",
            font="Helvetica Bold",
            weight=BOLD,
            color=ieee_color,
            font_size=64
        )

        # Move text to the *center* of the image
        ieee_text.move_to(image.get_center())
        ieee_text.shift(LEFT * 0.5).shift(UP * 0.5)

        # Rotate text 45 degrees (pi/4 radians)
        ieee_text.rotate(- PI / 32)


        # Start mit 0 Transparenz
        image.set_opacity(0)
        ieee_text.set_opacity(0)

        # Einblenden
        self.play(
            image.animate.set_opacity(1),
            run_time=1
        )

        self.wait(6)
        self.play(ieee_text.animate.set_opacity(1),run_time=0.1)

        self.wait(3)

        # Ausblenden
        self.play(
            image.animate.set_opacity(0),
            ieee_text.animate.set_opacity(0),
            run_time=1
        )

