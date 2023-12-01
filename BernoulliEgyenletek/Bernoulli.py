from manim import *

SMALL_WAIT_TIME = 1
STANDARD_WAIT_TIME = 3
LONGER_WAIT_TIME = 5


class SideNoteBubble(VGroup):
    def __init__(self, content, position, **kwargs):
        super().__init__(**kwargs)

        # Create a custom text bubble with an arrow
        self.bubble = RoundedRectangle(
            width=len(content) * 0.2 + 0.5,
            height=0.5,
            corner_radius=0.25,
            fill_color=WHITE,
            fill_opacity=0.7,
            stroke_color=WHITE,
            stroke_width=2,
        )
        self.bubble.next_to(position, DOWN, buff=0.2)

        # Add content to the bubble
        text = Text(content, color=BLACK, font_size=28)
        text.move_to(self.bubble.get_center())
        self.add(self.bubble, text)

    def create_animation(self):
        return FadeIn(self)

    def fade_out_animation(self):
        return FadeOut(self)


class BernoulliEquation(Scene):
    def construct(self):
        # Introduction
        title = MathTex(r"\text{Bernoulli egyenletek megoldása}", font_size=80).to_edge(
            UP, buff=0.5
        )
        subtitle = MathTex(r"\text{Lépések}", font_size=72)

        self.play(Write(title))
        self.wait(SMALL_WAIT_TIME)
        self.play(FadeOut(title))

        self.play(Write(subtitle))
        self.wait(SMALL_WAIT_TIME)

        self.play(FadeOut(subtitle))
        # First step
        first_step_title = MathTex(r"\text{1. Standard forma felírása:}").to_edge(
            UP, buff=0.5
        )
        self.play(Write(first_step_title))

        self.wait(SMALL_WAIT_TIME)

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

        self.wait(SMALL_WAIT_TIME)

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
            arrow_to_0, LEFT, buff=0
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
        self.wait(STANDARD_WAIT_TIME)

        # Second step
        second_step_title = MathTex(
            r"\text{2. Integrál faktor meghatározása:}",
        ).next_to(equation, DOWN, buff=0.5)

        self.play(Write(second_step_title))

        integrating_factor = MathTex(r"I(x) = e^{\int [1-n]P(x)dx}")
        integrating_factor.next_to(second_step_title, DOWN)
        self.play(Write(integrating_factor))

        self.wait(STANDARD_WAIT_TIME)

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

        self.wait(LONGER_WAIT_TIME)

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

        # Example
        example_title = MathTex(r"\text{Példa:}").to_edge(UP, buff=0.5)
        self.play(Write(example_title))

        # y' + \left( \frac{2}{x} \right) y = x^2y^3
        example_equation = MathTex(
            r"y'", r"+", r"\left( \frac{2}{x} \right)", r"y", r"=", r"x^2", r"y^3"
        )

        example_p = MathTex(r"P(x) = \frac{2}{x}")
        example_q = MathTex(r"Q(x) = x^2")
        example_n = MathTex(r"n = 3")

        example_equation.next_to(example_title, DOWN)
        example_p.next_to(example_equation, DOWN, buff=0.5)
        example_q.next_to(example_p, DOWN, buff=0.5)
        example_n.next_to(example_q, DOWN, buff=0.5)

        # Use the custom class for side note bubble
        side_note_bubble = SideNoteBubble(
            content="Látható, hogy alapból standard formában van az egyenlet",
            position=example_equation.get_bottom() + DOWN * 0.5,
        )
        standard_form_reminder = equation.copy().next_to(side_note_bubble, DOWN)

        # Underline the P(x) and Q(x) in the equation and in the example
        underline_p = Underline(example_equation.submobjects[2], color=RED)
        underline_q = Underline(example_equation.submobjects[5], color=BLUE)
        rectangle_around_n = SurroundingRectangle(
            example_equation.submobjects[6], color=PURPLE_B
        )

        underline_p_standard_form = Underline(
            standard_form_reminder.submobjects[2], color=RED
        )
        underline_q_standard_form = Underline(
            standard_form_reminder.submobjects[4], color=BLUE
        )
        rectangle_around_n_standard_form = SurroundingRectangle(
            standard_form_reminder.submobjects[5], color=PURPLE_B
        )

        # Play the animations
        self.play(Write(example_equation))
        self.wait(SMALL_WAIT_TIME)

        # Show the custom side note bubble
        self.play(side_note_bubble.create_animation())
        self.play(Write(standard_form_reminder))

        # Wait for some time
        self.wait(STANDARD_WAIT_TIME)

        self.play(
            Create(underline_p),
            Create(underline_q),
            Create(underline_p_standard_form),
            Create(underline_q_standard_form),
            Create(rectangle_around_n),
            Create(rectangle_around_n_standard_form),
        )

        self.wait(STANDARD_WAIT_TIME)

        # Fade out the custom side note bubble
        self.play(
            side_note_bubble.fade_out_animation(),
            FadeOut(standard_form_reminder),
            FadeOut(underline_p),
            FadeOut(underline_q),
            FadeOut(rectangle_around_n),
            FadeOut(underline_p_standard_form),
            FadeOut(underline_q_standard_form),
            FadeOut(rectangle_around_n_standard_form),
        )

        self.play(Write(example_p))
        self.play(Write(example_q))
        self.play(Write(example_n))

        self.wait(STANDARD_WAIT_TIME)
