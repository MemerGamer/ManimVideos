from manim import *


class BernoulliEquation(Scene):
    def construct(self):
        # Introduction
        self.wait(5)
        # First step
        first_step_title = MathTex(r"\text{1. Standard forma:}").to_edge(UP, buff=0.5)
        self.play(Write(first_step_title))

        self.wait(4)

        equation = MathTex(r"y'", r"+", r"P(x)y", r"=", r" Q(x)", r"y^n")
        equation.next_to(first_step_title, DOWN)
        n_value = MathTex(
            r"\forall n \in \mathbb{R} \backslash \{",
            r"0",
            r",",
            r"1",
            r"\}",
            font_size=40,
        )
        n_value.next_to(equation, RIGHT, buff=0.5)
        self.play(Write(equation))
        self.play(Write(n_value))

        # Underline P(x) and Q(x)
        underline_p = Underline(equation.submobjects[2], color=BLUE)
        underline_q = Underline(equation.submobjects[4], color=BLUE)
        self.play(Create(underline_p), Create(underline_q))

        self.wait(20)

        # Draw a rectangle around y^n
        rect_around_n = SurroundingRectangle(equation.submobjects[5], color=PURPLE_B)
        self.play(Create(rect_around_n))

        # Draw an arrow to 0 and write a text "lineáris egyenlet"
        arrow_to_0 = Arrow(
            n_value.submobjects[1].get_right() + UP,
            n_value.submobjects[1].get_top(),
            color=PURPLE,
        )
        text_0 = Text("lineáris egyenlet", color=PURPLE, font_size=15).next_to(
            arrow_to_0, LEFT
        )
        self.play(Create(arrow_to_0), Write(text_0))

        # Draw an arrow to 1 and write a text "szétválasztható változójú egyenlet"
        arrow_to_1 = Arrow(
            n_value.submobjects[3].get_right() + UP * 2,
            n_value.submobjects[3].get_top(),
            color=PURPLE_C,
        )
        text_1 = Text(
            "szétválasztható változójú egyenlet", color=PURPLE_C, font_size=15
        ).next_to(arrow_to_1, LEFT)
        self.play(Create(arrow_to_1), Write(text_1))
        self.wait(2)

        # Second step
        second_step_title = MathTex(
            r"\text{2. Integrál faktor meghatározása:}",
        ).next_to(equation, DOWN, buff=0.5)

        self.play(Write(second_step_title))

        integrating_factor = MathTex(r"I(x) = e^{\int [1-n]P(x)dx}")
        integrating_factor.next_to(second_step_title, DOWN)
        self.play(Write(integrating_factor))

        self.wait(10)

        # Third step
        third_step_title = MathTex(r"\text{3. Az egyenlet megoldása }").next_to(
            integrating_factor, DOWN, buff=0.5
        )
        self.play(Write(third_step_title))

        solution_equation = MathTex(
            r"y^{1-n} = \left[ \frac{1}{I(x)} \int [1-n]Q(x)I(x)dx +c\right]"
        )
        solution_equation.next_to(third_step_title, DOWN)
        self.play(Write(solution_equation))

        self.wait(10)

        # Fade out
        self.play(
            FadeOut(first_step_title),
            FadeOut(equation),
            FadeOut(n_value),
            FadeOut(underline_p),
            FadeOut(underline_q),
            FadeOut(rect_around_n),
            FadeOut(arrow_to_0),
            FadeOut(text_0),
            FadeOut(arrow_to_1),
            FadeOut(text_1),
            FadeOut(second_step_title),
            FadeOut(integrating_factor),
            FadeOut(third_step_title),
            FadeOut(solution_equation),
        )
        self.wait(1)

        # Example
        example_title = MathTex(r"\text{Példa:}").to_edge(UP, buff=0.5)
        self.play(Write(example_title))

        # y' + \left( \frac{2}{x} \right) y = x^2y^3
        example_equation = MathTex(
            r"y'", r"+", r"\left( \frac{2}{x} \right) y", r"=", r"x^2y^3"
        )

        example_p = MathTex(r"P(x) = \frac{2}{x}")
        example_q = MathTex(r"Q(x) = x^2")
        example_n = MathTex(r"n = 3")

        example_equation.next_to(example_title, DOWN)
        example_p.next_to(example_equation, DOWN, buff=0.5)
        example_q.next_to(example_p, DOWN, buff=0.5)
        example_n.next_to(example_q, DOWN, buff=0.5)

        self.play(Write(example_equation))
        self.wait(5)
        self.play(Write(example_p))
        self.wait(2)
        self.play(Write(example_q))
        self.wait(2)
        self.play(Write(example_n))
