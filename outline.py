from manim import *

class PaperFadeInFromBottom(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("data/beatingfloatspaper.png")
        image.scale(0.7)
        image.rotate(PI / 64)
        image.move_to(DOWN * 4)
        image.set_opacity(0)

        # Step 1: Animate image fading in from below
        self.play(
            image.animate.move_to(ORIGIN).set_opacity(1),
            run_time=2,
            rate_func=smooth
        )
        self.wait(3)

        # Step 2: Create multi-line text (initially invisible)
        text = MarkupText("+ other resources\nlinked in the description", font_size=28, line_spacing=0.5)
        text.set_opacity(0)

        # Step 3: Compute positions to center the group
        image_target_x = -text.width / 2 - 0.25  # shift image left
        text_target_x = image_target_x + image.width + 0.5  # position text to the right

        # Animate image shift left and text fade-in + position
        self.play(
            image.animate.move_to([image_target_x, 0, 0]),
            text.animate.set_opacity(1).move_to([text_target_x, 0, 0]),
            run_time=1.5,
            rate_func=smooth
        )

        self.wait(5)

        image_x = image.get_x()
        text_x = text.get_x()

        self.play(
            image.animate.move_to([image_x, -4, 0]).set_opacity(0),
            text.animate.move_to([text_x, -4, 0]).set_opacity(0),
            run_time=2,
            rate_func=smooth
        )


        self.wait(0.5)


class CreditsScene(Scene):
    def construct(self):
        # Top text
        top_text = Text("Created by").to_edge(UP)
        self.play(Write(top_text),run_time=1.5)

        # Middle names
        names = VGroup(
            Text("Vorname1 Nachname1"),
            Text("Vorname2 Nachname2"),
            Text("Vorname3 Nachname3"),
            Text("Vorname4 Nachname4"),
        ).arrange(DOWN, buff=0.3).scale(0.5)
        names.next_to(top_text,DOWN).shift(DOWN)
        

        self.wait(1)
        self.play(FadeIn(names, shift=UP),run_time=2)

        self.wait(3)

        # Bottom text
        bottom_text = Text("Made with").scale(0.7).next_to(ORIGIN, DOWN*2.5)

        # Manim Banner animation
        banner = ManimBanner().scale(0.4)
        banner.to_edge(DOWN)

        bottom_text.next_to(banner,UP)

        self.play(Write(bottom_text),run_time=1)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait(20)
        self.play(Unwrite(banner), FadeOut(top_text), FadeOut(names), FadeOut(bottom_text))

class ThankYouWriting(Scene):
    def construct(self):
        text = Text("Thank you for watching!",font_size=72)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))
        self.wait(2)

