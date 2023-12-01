#!/usr/bin/env python
from manim import *
import numpy as np
from threeBodyProblem import ThreeBodyProblem


# Main driver class
class ButterflyEffect(ThreeDScene):
    def construct(self):
        Introduction.construct(self)
        self.wait(1)
        QuestioningPredictibility.construct(self)


# 1. Introduction
class Introduction(Scene):
    def construct(self):
        # The butterfly effect
        butterfly_effect = Tex("A pillangó effektus")
        butterfly_effect.scale(1.5)

        # Displaying the text, waiting 2 seconds, then fading out
        self.play(Write(butterfly_effect, run_time=2))
        self.wait(2)
        self.play(FadeOut(butterfly_effect, run_time=1))

        # Displaying the images from assets folder
        # waiting 3 seconds, then fading out
        movies = ImageMobject("./assets/movies.png")
        meme1 = ImageMobject("./assets/meme1.jpg")
        meme2 = ImageMobject("./assets/meme2.jpg")
        meme3 = ImageMobject("./assets/meme3.jpg")

        # Positioning the images to fit all on the screen in a grid
        movies.scale(0.7)
        movies.move_to(UP * 1.9 + LEFT * 3)
        meme1.scale(1.2)
        meme1.move_to(UP * 1.9 + RIGHT * 3)
        meme2.move_to(DOWN * 2.1 + LEFT * 3)
        meme3.scale(1.5)
        meme3.move_to(DOWN * 2.1 + RIGHT * 3)

        # Displaying the images, waiting 3 seconds, then fade out
        self.play(FadeIn(movies))
        self.play(FadeIn(meme1))
        self.play(FadeIn(meme2))
        self.play(FadeIn(meme3))
        self.wait(2)
        self.play(FadeOut(movies, run_time=0.7))
        self.play(FadeOut(meme1), run_time=0.7)
        self.play(FadeOut(meme2), run_time=0.7)
        self.play(FadeOut(meme3), run_time=0.7)

        quote = Tex(
            '"A pillangóhatás elmélet szerint (...) ha egy pillangó meglebbenti a szárnyát Hongkongban, az tíz évvel később hurrikánt okozhat Floridában, vagy megakadályozhat egy tornádót tíz évvel később Texasban, az ember választhat, mert kiszámíthatatlan."'
        )
        quote.scale(0.8)

        author = Tex("- Jennifer Crusiez")
        author.next_to(quote, DOWN)
        author.shift(RIGHT * 3)
        author.scale(0.7)
        self.play(FadeIn(quote, run_time=1), FadeIn(author, run_time=1))
        self.wait(5)
        self.play(FadeOut(quote, run_time=1), FadeOut(author, run_time=1))

        Wait(2)

        interesting_question = Tex("Mennyire jól megjósolható a jövő?")
        self.play(Write(interesting_question, run_time=2))
        Wait(3)
        self.play(FadeOut(interesting_question, run_time=1.5))


# 2. Questioning predictibility
class Pendulum(Scene):
    def construct(self):
        time = ValueTracker(0)
        theta_max = 30 / 180 * PI
        l = 3
        g = 9.8
        w = np.sqrt(g / l)
        T = 2 * PI / w

        p_x = -2.5
        p_y = 3

        shift_req = p_x * RIGHT + p_y * UP

        theta = DecimalNumber().set_color(BLACK).move_to(10 * RIGHT)
        theta.add_updater(
            lambda m: m.set_value((theta_max) * np.sin(w * time.get_value()))
        )

        self.add(theta)

        def get_line(x, y):
            line_here = Line(
                start=ORIGIN + shift_req, end=x * RIGHT + y * UP + shift_req, color=GRAY
            )
            global line_vertical
            line_vertical = DashedLine(
                start=line_here.get_start(),
                end=line_here.get_start() + 3 * DOWN,
                color=GRAY,
            )
            return line_here

        line = always_redraw(
            lambda: get_line(
                l * np.sin(theta.get_value()), -l * np.cos(theta.get_value())
            )
        )

        self.add(line)
        self.add(line_vertical)

        def angle_arc(theta):
            if theta == 0:
                angle = VectorizedPoint().move_to(10 * RIGHT)
                arc_text = VectorizedPoint().move_to(10 * RIGHT)
            else:
                if theta > 0:
                    angle = Angle(
                        line,
                        line_vertical,
                        quadrant=(1, 1),
                        other_angle=True,
                        color=YELLOW,
                        fill_opacity=0.5,
                    )
                if theta < 0:
                    angle = Angle(
                        line,
                        line_vertical,
                        quadrant=(1, 1),
                        other_angle=False,
                        color=YELLOW,
                        fill_opacity=0.5,
                    )
            return angle

        angle = always_redraw(lambda: angle_arc(theta.get_value()))
        self.add(angle)

        arc_text = Tex(r"$\theta$").scale(0.5)

        def get_ball(x, y):
            ball = Dot(radius=0.5, color=BLUE)
            ball.move_to(x * RIGHT + y * UP + shift_req).scale(1)
            return ball

        ball = always_redraw(
            lambda: get_ball(
                l * np.sin(theta.get_value()), -l * np.cos(theta.get_value())
            )
        )

        self.add(ball)

        explanation_text_1 = (
            Tex(
                "Az inga mozgásegyenlete előállítható Newton második törvényének alkalmazásával a következő képpen:"
            )
            .scale(0.5)
            .to_edge(UP, buff=0.5)
            .shift(RIGHT * 3)
        )

        explanation_text_2 = (
            MathTex(
                r"\tau = I \alpha \quad \Rightarrow \quad -mg \sin\theta\; L = mL^2 \; \frac{d^2\theta}{dt^2}"
            )
            .scale(0.5)
            .next_to(explanation_text_1, DOWN)
        )

        explanation_text_3 = (
            Tex("Az egyenlet átrendezésével megkapjuk:")
            .scale(0.5)
            .next_to(explanation_text_2, DOWN)
        )

        explanation_text_4 = (
            MathTex(r"\frac{d^2\theta}{dt^2} + \frac{g}{L}\sin\theta = 0")
            .scale(0.5)
            .next_to(explanation_text_3, DOWN)
        )

        explanation_text_5 = (
            Tex("Ha a lengés amplitúdója elég kicsi, ")
            .scale(0.5)
            .next_to(explanation_text_4, DOWN)
        )

        explanation_text_5_1 = (
            Tex("akkor közelíthetjük a szinuszfüggvényt annak az argumentumával:")
            .scale(0.5)
            .next_to(explanation_text_5, DOWN)
        )

        explanation_text_6 = (
            MathTex(r"\frac{d^2\theta}{dt^2} + \frac{g}{L}\theta = 0")
            .scale(0.5)
            .next_to(explanation_text_5_1, DOWN)
        )

        explanation_text_7 = (
            Tex("Az egyszerű harmonikus mozgás egyenlete:")
            .scale(0.5)
            .next_to(explanation_text_6, DOWN)
        )

        explanation_text_8 = (
            MathTex(r"\theta(t) = \theta_o \cos(\omega t),")
            .scale(0.5)
            .next_to(explanation_text_7, DOWN)
        )

        explanation_text_9 = (
            MathTex(
                r"\text{ahol } \theta_o \text{ az kezdeti szögelfordulás és } \omega \text{az mozgás természetes frekvenciája.}"
            )
            .scale(0.5)
            .next_to(explanation_text_8, DOWN)
        )

        explanation_text_10 = (
            Tex("Ennek a rendszernek a periódusa:")
            .scale(0.5)
            .next_to(explanation_text_9, DOWN)
        )

        explanation_text_11 = (
            MathTex(r"T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{L}{g}}")
            .scale(0.5)
            .next_to(explanation_text_10, DOWN)
        )

        explanations_group = VGroup(
            explanation_text_1,
            explanation_text_2,
            explanation_text_3,
            explanation_text_4,
            explanation_text_5,
            explanation_text_5_1,
            explanation_text_6,
            explanation_text_7,
            explanation_text_8,
            explanation_text_9,
            explanation_text_10,
            explanation_text_11,
        )

        self.play(FadeIn(explanations_group))
        self.play(time.animate.set_value(T), run_time=T, rate_func=linear)


class QuestioningPredictibility(Scene):
    def construct(self):
        questioning_predictibility = Tex("A megjósolhatóság megkérdőjelezése")
        questioning_predictibility.scale(1.5)

        # Displaying the text, waiting 2 seconds, then fading out
        self.play(Write(questioning_predictibility, run_time=2))
        self.wait(2)
        self.play(FadeOut(questioning_predictibility, run_time=1))

        # Animation to represent the predictability of a Newtonian system (Pendulum example)
        Pendulum.construct(self)
        # Clearing the screen
        self.clear()

        Wait(5)
        ThreeBodyProblem.construct(self)
