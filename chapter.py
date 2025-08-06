from manim import *


CHAPTER_COLOR = WHITE

chapters = [
    "1. What where Floats again?",
    "2. How does Posits work?",
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
            self.wait(1)

            self.play(FadeOut(chapter))
            self.wait(1)

class ImageTest(Scene):
    def construct(self):
        img  = ImageMobject("floats.png").scale_to_fit_height(config.frame_height).scale(0.28).to_edge(LEFT)
        img2 = ImageMobject("posits.png").scale_to_fit_height(config.frame_height).scale(0.28)
        img3 = ImageMobject("posits.png").scale_to_fit_height(config.frame_height).scale(0.28).to_edge(RIGHT)


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


        self.play(FadeIn(img),FadeIn(img_rect),FadeIn(img_text))
        self.play(FadeIn(img2),FadeIn(img_rect2),FadeIn(img_text2))
        self.play(FadeIn(img3),FadeIn(img_rect3),FadeIn(img_text3))
        self.wait(1)
        self.play(FadeOut(img),FadeOut(img_rect),FadeOut(img_text),FadeOut(img2),FadeOut(img_rect2),FadeOut(img_text2),FadeOut(img3),FadeOut(img_rect3),FadeOut(img_text3))
        # self.play(FadeOut(img2),FadeOut(img_rect2),FadeOut(img_text2))
        # self.play(FadeOut(img3),FadeOut(img_rect3),FadeOut(img_text3))
        self.wait(1)

class ImageFadeInFromBottom(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("beatingfloatspaper.png")

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

        self.wait(1)

        # Animate: fade out (and optionally move down again)
        self.play(
            image.animate.move_to(DOWN * 4).set_opacity(0),
            run_time=2,
            rate_func=smooth
        )

        self.wait(0.5)
