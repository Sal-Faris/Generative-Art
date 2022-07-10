from manim import *
import numpy as np

config.pixel_height = 1080
config.pixel_width = 1080


class Derivation(Scene):

    def construct(self):

        # What is e^{itheta}?

        eitheta = Tex(r"$\text{What is } e^{i\theta}\text{?}$").scale(2)

        self.wait()
        self.play(Write(eitheta))
        self.wait(2)
        self.play(FadeOut(eitheta))
        self.wait()

        # Writing out the sums

        Etheta = Tex(r"$e^{\theta}$").scale(2)
        Esum = Tex(r"$ = \sum_{n=0}^{\infty} \frac{\theta^n}{n!}$").scale(2)
        Etaylor = Tex(
            r"$ = \frac{\theta^0}{0!} + \frac{\theta^1}{1!} + \frac{\theta^2}{2!} + ...$").scale(2).shift(0.4*UP + 0.4*RIGHT)

        self.play(Write(Etheta))
        self.wait()
        self.play(Etheta.animate.shift(2*UP+4.5*LEFT))
        self.wait()
        self.play(Write(Esum.next_to(Etheta, RIGHT)))
        self.wait()
        self.play(Write(Etaylor))
        self.wait()

        # The derivation

        Eitheta = Tex(r"$e^{i\theta}$").scale(2).shift(2*UP+4.5*LEFT)
        Eisum = Tex(
            r"$ = \sum_{n=0}^{\infty} \frac{(i\theta)^n}{n!}$").scale(2).next_to(Eitheta, RIGHT)
        Eitaylor = Tex(
            r"$ = \frac{(i\theta)^0}{0!} + \frac{(i\theta)^1}{1!} + \frac{(i\theta)^2}{2!} + ...$").scale(1.5).shift(0.4*UP + 0.5*RIGHT)

        self.play(Transform(Etheta, Eitheta))
        self.wait()
        self.play(Transform(Esum, Eisum), Transform(Etaylor, Eitaylor))
        self.wait()

        EitaylorLong = Tex(
            r"$\frac{(i\theta)^0}{0!} + \frac{(i\theta)^1}{1!} + \frac{(i\theta)^2}{2!} + \frac{(i\theta)^3}{3!}+ \frac{(i\theta)^4}{4!} + ...$").scale(1.5)
        EitaylorLongSimp = Tex(
            r"$1 + i\theta + \frac{-\theta^2}{2!} + \frac{-i\theta^3}{3!} + \frac{\theta^4}{4!} + \frac{i\theta^5}{5!} + ...$").scale(1.5)

        self.play(FadeOut(Etheta), FadeOut(Esum))
        self.wait()
        self.play(Etaylor.animate.shift(-(0.4*UP + 0.5*RIGHT)))
        self.play(Transform(Etaylor, EitaylorLong))
        self.wait(2)
        self.play(Transform(Etaylor, EitaylorLongSimp))
        self.wait(2)

        EitaylorLongSimp2 = Tex(
            r"$\left( 1 - \frac{\theta^2}{2!} + \frac{\theta^4}{4!} + ... \right) + i \left( \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} + ... \right)$").scale(1.5)
        cosisin = Tex(r"$\cos(\theta) + i \cdot \sin(\theta)$").scale(2)
        Eitheta2 = Tex(r"$e^{i\theta} = $").scale(2).shift(4*LEFT+0.1*UP)

        self.play(Transform(Etaylor, EitaylorLongSimp2))
        self.wait(2)
        self.play(ReplacementTransform(Etaylor, cosisin))
        self.wait()
        self.play(cosisin.animate.shift(1.1*RIGHT), FadeIn(
            Eitheta2, shift=LEFT))
        self.wait()

        # Generating the grid and moving the eqn to the top

        EqGroup = VGroup(Eitheta2, cosisin)

        plane = ComplexPlane(
            axis_config={
                "unit_size": 4
            }
        ).add_coordinates()
        plane.z_index = EqGroup.z_index - 1

        self.play(EqGroup.animate.scale(0.75).shift(
            5*UP), Write(plane, run_time=2))
        self.wait(2)

        ang = PI/3
        r = 4
        vec = Vector([r, 0])
        angarc = Arc(angle=ang, radius=1)
        angarc.set_color(RED)
        theta = Tex(r"$\theta$").scale(1).next_to(angarc, 0.5*RIGHT)

        self.play(Write(vec))
        self.play(
            Rotate(
                vec,
                angle=ang,
                about_point=ORIGIN,
                rate_func=smooth
            ))
        self.wait()
        self.play(Write(angarc, rate_func=smooth), Write(theta))

        dashed_vert = DashedLine(
            r*np.cos(ang)*RIGHT + r*np.sin(ang)*UP, r*np.cos(ang)*RIGHT)
        isin = Tex(r"$i \cdot \sin(\theta)$").scale(
            1).next_to(dashed_vert, 0.5*RIGHT)

        dashed_horiz = DashedLine(0*RIGHT, r*np.cos(ang)*RIGHT)
        cos = Tex(r"$\cos(\theta)$").scale(1).next_to(dashed_horiz, 0.5*DOWN)

        self.play(Write(dashed_vert), Write(isin))
        self.wait()
        self.play(Write(dashed_horiz), Write(cos))
        self.wait(4)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait()
