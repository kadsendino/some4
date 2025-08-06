from manim import *

class PaperFadeInFromBottom(Scene):
    def construct(self):
        # Load the image
        image = ImageMobject("beatingfloatspaper.png")
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
        self.wait(1)

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

        self.wait(1.5)

        image_x = image.get_x()
        text_x = text.get_x()

        self.play(
            image.animate.move_to([image_x, -4, 0]).set_opacity(0),
            text.animate.move_to([text_x, -4, 0]).set_opacity(0),
            run_time=2,
            rate_func=smooth
        )


        self.wait(0.5)

class ThankYouWriting(Scene):
    def construct(self):
        text = Text("Thank you for watching!",font_size=72)
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))
        self.wait(2)

