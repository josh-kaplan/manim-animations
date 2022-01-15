from typing_extensions import runtime
from manim import *


class Azimuths(Scene):
    def construct(self):

        dot = Dot(ORIGIN)
        rotation_center = ORIGIN
        clockwise = True
        theta_tracker = ValueTracker(0.0001)

        # Some lines
        north = Line(ORIGIN, 2*UP, color=RED)
        line_moving = Line(ORIGIN, 2*UP)
        line_ref = line_moving.copy()

        # Rotate the line and create the angle arc
        line_moving.rotate(
            -1*theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )

        # Angle measure
        theta = Angle(north, line_moving, radius=0.5, other_angle=clockwise)

        # Angle label
        tex = MathTex(r"\theta").move_to(
            Angle(
                north, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=clockwise
            ).point_from_proportion(0.5)
        )


        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                -1*theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        tex.add_updater(
            lambda x: x.become(MathTex(str(round(theta_tracker.get_value())) + '^\\circ'))
        )

        theta.add_updater(
            lambda x: x.become(Angle(north, line_moving, radius=0.5, other_angle=clockwise))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    north, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=clockwise
                ).point_from_proportion(0.5)
            )
        )

        self.play(GrowFromCenter(dot))
        self.wait(2)
        self.play(GrowFromPoint(north, ORIGIN))
        self.play(GrowFromPoint(line_moving, ORIGIN), theta_tracker.animate.set_value(30), FadeIn(theta), FadeIn(tex))
        self.wait(2)
        self.play(theta_tracker.animate.set_value(90))
        self.play(tex.animate.set_color(RED), run_time=0.5)
        self.wait(2)
        self.play(theta_tracker.animate.set_value(170))
        self.wait(2)
        self.play(theta_tracker.animate.set_value(270))
        self.wait(4)
