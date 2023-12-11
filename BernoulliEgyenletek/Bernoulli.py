from manim import *

SMALL_WAIT_TIME = 1
STANDARD_WAIT_TIME = 3
LONGER_WAIT_TIME = 5

global equation, integrating_factor, solution_equation
equation = MathTex(r"y'", r"+", r"P(x)", r"y", r"=", r" Q(x)", r"y", r"^n")
integrating_factor = MathTex(r"I(x) = e^{\int [1-n]P(x)dx}")
solution_equation = MathTex(
    r"y^{1-n} =  \frac{1}{I(x)} \left[\int [1-n]Q(x)I(x)dx +c\right]"
)


class SideNoteBubble(VGroup):
    def __init__(self, content, position, **kwargs):
        super().__init__(**kwargs)

        # Create a custom text bubble with an arrow
        self.bubble = RoundedRectangle(
            width=len(content) * 0.15,
            height=0.5,
            corner_radius=0.25,
            fill_color=WHITE,
            fill_opacity=0.7,
            stroke_color=WHITE,
            stroke_width=2,
        )
        self.bubble.next_to(position, DOWN, buff=0.2)

        # Add content to the bubble
        text = MathTex(r"\text{" + content + "}", color=BLACK, font_size=28)
        text.move_to(self.bubble.get_center())
        self.add(self.bubble, text)

    def create_animation(self):
        return FadeIn(self)

    def fade_out_animation(self):
        return FadeOut(self)


class Introduction(Scene):
    def construct(self):
        # Variables
        title = MathTex(r"\text{Bernoulli egyenletek megoldása}", font_size=80)

        # Animations
        self.play(Write(title))
        self.wait(SMALL_WAIT_TIME)
        self.play(FadeOut(title))


class Steps(Scene):
    def construct(self):
        # First step
        # Variables
        subtitle = MathTex(r"\text{Lépések:}", font_size=72).to_edge(UP, buff=0.5)

        self.play(Write(subtitle))

        first_step_title = MathTex(r"\text{1. Standard forma felírása:}").next_to(
            subtitle, DOWN, buff=0.5
        )

        equation = MathTex(r"y'", r"+", r"P(x)", r"y", r"=", r" Q(x)", r"y", r"^n")
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

        underline_p = Underline(equation.submobjects[2], color=RED)
        underline_q = Underline(equation.submobjects[5], color=BLUE)

        rect_around_n = SurroundingRectangle(equation.submobjects[7], color=PURPLE_B)

        arrow_to_0 = Arrow(
            n_value.submobjects[1].get_right() + UP,
            n_value.submobjects[1].get_top(),
            color=PURPLE,
        )
        text_0 = Text("lineáris egyenlet", color=PURPLE, font_size=15).next_to(
            arrow_to_0, LEFT, buff=0
        )

        arrow_to_1 = Arrow(
            n_value.submobjects[3].get_right() + UP * 2,
            n_value.submobjects[3].get_top(),
            color=PURPLE_C,
        )
        text_1 = Text(
            "szétválasztható változójú egyenlet", color=PURPLE_C, font_size=15
        ).next_to(arrow_to_1, LEFT)

        # Animations
        self.play(Write(first_step_title))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(equation))
        self.play(Write(n_value))

        # Underline P(x) and Q(x)
        self.play(Create(underline_p), Create(underline_q))
        self.wait(SMALL_WAIT_TIME)

        # Draw a rectangle around y^n
        self.play(Create(rect_around_n))

        # Draw an arrow to 0 and write a text "lineáris egyenlet"
        self.play(Create(arrow_to_0), Write(text_0))

        # Draw an arrow to 1 and write a text "szétválasztható változójú egyenlet"
        self.play(Create(arrow_to_1), Write(text_1))
        self.wait(STANDARD_WAIT_TIME)

        # Second step
        # Variables
        second_step_title = MathTex(
            r"\text{2. Integrál faktor meghatározása:}",
        ).next_to(equation, DOWN, buff=0.5)

        integrating_factor = MathTex(r"I(x) = e^{\int [1-n]P(x)dx}")
        integrating_factor.next_to(second_step_title, DOWN)

        # Animations
        self.play(Write(second_step_title))
        self.play(Write(integrating_factor))

        self.wait(STANDARD_WAIT_TIME)

        # Third step
        # Variables
        third_step_title = MathTex(r"\text{3. Az egyenlet megoldása }").next_to(
            integrating_factor, DOWN, buff=0.5
        )

        solution_equation = MathTex(
            r"y^{1-n} =  \frac{1}{I(x)} \left[\int [1-n]Q(x)I(x)dx +c\right]"
        )
        solution_equation.next_to(third_step_title, DOWN)

        # Animations
        self.play(Write(third_step_title))
        self.play(Write(solution_equation))

        self.wait(LONGER_WAIT_TIME)

        # Fade out
        self.play(
            FadeOut(subtitle),
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


class FirstExample:
    def construct(self):
        # Variables
        example_title = MathTex(r"\text{1. Példa:}").to_edge(UP, buff=0.5)

        # y' + \left( \frac{2}{x} \right) y = x^2y^3
        example_equation = MathTex(
            r"y'", r"+", r"\left( \frac{2}{x} \right)", r"y", r"=", r"x^2", r"y", r"^3"
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
            example_equation.submobjects[7], color=PURPLE_B
        )

        underline_p_standard_form = Underline(
            standard_form_reminder.submobjects[2], color=RED
        )
        underline_q_standard_form = Underline(
            standard_form_reminder.submobjects[5], color=BLUE
        )
        rectangle_around_n_standard_form = SurroundingRectangle(
            standard_form_reminder.submobjects[7], color=PURPLE_B
        )

        # Play the animations
        self.play(Write(example_title))
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

        # Calculate the integrating factor
        # Move the example_p, example_q and example_n to the top
        example_p.generate_target()
        example_q.generate_target()
        example_n.generate_target()
        example_p.target.to_edge(UP)
        example_q.target.next_to(example_p.target, DOWN, buff=0.5)
        example_n.target.next_to(example_q.target, DOWN, buff=0.5)

        # Side note bubble
        side_note_bubble = SideNoteBubble(
            content="Ki kell számolni az integrál faktort a képlet alapján",
            position=example_n.target.get_bottom(),
        )

        # Integrating factor reminder
        integrating_factor_reminder = integrating_factor.copy().next_to(
            side_note_bubble, DOWN
        )

        ex_integrating_factor = MathTex(r"= e^{\int [1-3]\frac{2}{x}dx}")
        ex_integrating_factor.next_to(
            integrating_factor_reminder, DOWN + LEFT + 0.25, buff=0.5
        )

        ex_integrating_factor_s2 = MathTex(r"= e^{\int \left(-2\right)\frac{2}{x}dx}")
        ex_integrating_factor_s2.next_to(ex_integrating_factor, RIGHT, buff=0.5)

        ex_integrating_factor_s3 = MathTex(r"= e^{-4 \int \frac{1}{x}dx}")
        ex_integrating_factor_s3.next_to(ex_integrating_factor_s2, RIGHT, buff=0.5)

        ex_integrating_factor_s4 = MathTex(r"= e^{", r"-4", r" \cdot", r"\ln x}")
        ex_integrating_factor_s4.next_to(ex_integrating_factor_s3, RIGHT, buff=0.5)

        # curved arrow from the top -4 to ln x
        curved_arrow = CurvedArrow(
            ex_integrating_factor_s4.submobjects[1].get_center() + 0.25 * UP,
            ex_integrating_factor_s4.submobjects[3].get_center() + 0.25 * UP,
            radius=-0.75,
            color=RED,
        )

        ex_integrating_factor_s5 = MathTex(r"= e^{\ln x^{-4}}")
        ex_integrating_factor_s5.next_to(ex_integrating_factor, DOWN, buff=0.5)

        ex_integrating_factor_s6 = MathTex(r"= x^{-4}")
        ex_integrating_factor_s6.next_to(ex_integrating_factor_s5, RIGHT, buff=0.5)

        ex_integrating_factor_s7 = MathTex(r"= \frac{1}{x^4}")
        ex_integrating_factor_s7.next_to(ex_integrating_factor_s6, RIGHT, buff=0.5)

        # Animations
        self.play(FadeOut(example_equation), FadeOut(example_title))
        self.play(
            MoveToTarget(example_p), MoveToTarget(example_q), MoveToTarget(example_n)
        )

        self.play(side_note_bubble.create_animation())
        self.play(Write(integrating_factor_reminder))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_integrating_factor))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_integrating_factor_s2))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_integrating_factor_s3))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_integrating_factor_s4))
        self.play(Create(curved_arrow))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_integrating_factor_s5))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_integrating_factor_s6))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_integrating_factor_s7))
        self.wait(STANDARD_WAIT_TIME)

        self.play(
            side_note_bubble.fade_out_animation(),
            FadeOut(integrating_factor_reminder),
            FadeOut(ex_integrating_factor),
            FadeOut(ex_integrating_factor_s2),
            FadeOut(ex_integrating_factor_s3),
            FadeOut(ex_integrating_factor_s4),
            FadeOut(curved_arrow),
            FadeOut(ex_integrating_factor_s5),
            FadeOut(ex_integrating_factor_s6),
            FadeOut(ex_integrating_factor_s7),
        )
        # Rearranging the position of the example_p, example_q
        # and example_n with the addition of I(x) = 1/x^4 in a 2x2 matrix style
        example_p.generate_target()
        example_q.generate_target()
        example_n.generate_target()
        example_int_factor = MathTex(r"I(x) = \frac{1}{x^4}").next_to(
            example_q.target, DOWN, buff=0.5
        )

        # Group them into a 2x2 matrix style
        example_group = VGroup(
            example_p.target, example_q.target, example_n.target, example_int_factor
        )
        example_group.arrange_in_grid(rows=2, cols=2, buff=0.5)
        example_group.move_to(UP * 2)

        # Animations
        self.play(
            MoveToTarget(example_p),
            MoveToTarget(example_q),
            MoveToTarget(example_n),
            Write(example_int_factor),
        )
        self.wait(SMALL_WAIT_TIME)

        # Side note bubble
        side_note_bubble = SideNoteBubble(
            content="Használva a megoldási képletet, felírhatjuk az egyenlet megoldását",
            position=example_group.get_bottom(),
        )

        ex_solution_equation = solution_equation.copy().next_to(side_note_bubble, DOWN)
        ex_solution_eq_s2 = MathTex(
            r"y^{1-3} = \frac{1}{\frac{1}{x^4}} \left[\int [1-3]x^2 \frac{1}{x^4}dx +c\right]"
        ).next_to(ex_solution_equation, DOWN, buff=0.5)

        # Move the ex solution equations to the top
        ex_solution_equation.generate_target()
        ex_solution_eq_s2.generate_target()
        ex_solution_equation.target.to_edge(UP)
        ex_solution_eq_s2.target.next_to(ex_solution_equation.target, DOWN, buff=0.5)

        ex_solution_eq_s3 = MathTex(
            r"y^{-2} = x^4 \left[\int -2 \frac{1}{x^2}dx +c\right]"
        ).next_to(ex_solution_eq_s2.target, DOWN, buff=0.5)
        ex_solution_eq_s3.shift(LEFT * 2)
        ex_solution_eq_s4 = MathTex(r"= x^4 \left[\int -2 x^{-2} dx +c\right]").next_to(
            ex_solution_eq_s3, RIGHT, buff=0.5
        )

        ex_solution_eq_s5 = MathTex(
            r"y^{-2} = x^4 \left[\frac{-2 x^{-1}}{-1} +c\right]"
        ).next_to(ex_solution_eq_s3, DOWN, buff=0.5)

        left_right_arrow = MathTex(r"\Leftrightarrow").next_to(
            ex_solution_eq_s5, RIGHT, buff=0.5
        )

        ex_solution_eq_s6 = MathTex(
            r"y^{-2}",
            r" =",
            r" x^4",
            r" \left[\frac{2}{x}",
            r" +",
            r"c\right]",
        ).next_to(ex_solution_eq_s4, DOWN, buff=0.5)
        curved_arrow2 = CurvedArrow(
            ex_solution_eq_s6.submobjects[2].get_center() + 0.25 * UP,
            ex_solution_eq_s6.submobjects[3].get_center() + 0.25 * UP,
            radius=-1,
            color=BLUE,
        )
        curved_arrow3 = CurvedArrow(
            ex_solution_eq_s6.submobjects[2].get_center() + 0.25 * UP,
            ex_solution_eq_s6.submobjects[5].get_center() + 0.25 * UP,
            radius=-2,
            color=BLUE,
        )

        # Move the ex_solution_eq_s6 to the top
        ex_solution_eq_s6.generate_target()
        ex_solution_eq_s6.target.move_to(ORIGIN).to_edge(UP)

        ex_solution_eq_s7 = MathTex(r"y^{-2} = 2 \cdot x^{3} + c \cdot x^4").next_to(
            ex_solution_eq_s6.target, DOWN, buff=0.5
        )

        side_note_bubble2 = SideNoteBubble(
            content="A megoldás tehát:",
            position=ex_solution_eq_s7.get_bottom(),
        )

        ex_solution_eq_s8 = MathTex(
            r"\frac{1}{y^2} = 2 \cdot x^{3} + c \cdot x^4"
        ).next_to(side_note_bubble2, DOWN, buff=0.5)

        # Surrounding rectangle around the ex_solution_eq_s8
        rect_around_ex_solution_eq_s8 = SurroundingRectangle(
            ex_solution_eq_s8, color=RED
        )

        # Animations
        self.play(side_note_bubble.create_animation())
        self.play(Write(ex_solution_equation))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_solution_eq_s2))
        self.play(
            FadeOut(example_p),
            FadeOut(example_q),
            FadeOut(example_n),
            FadeOut(example_int_factor),
            FadeOut(side_note_bubble),
        )
        self.play(MoveToTarget(ex_solution_equation), MoveToTarget(ex_solution_eq_s2))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_solution_eq_s3))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_solution_eq_s4))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_solution_eq_s5))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(left_right_arrow))
        self.play(Write(ex_solution_eq_s6))
        self.play(Create(curved_arrow2), Create(curved_arrow3))
        self.wait(SMALL_WAIT_TIME)

        self.play(
            FadeOut(ex_solution_equation),
            FadeOut(ex_solution_eq_s2),
            FadeOut(ex_solution_eq_s3),
            FadeOut(ex_solution_eq_s4),
            FadeOut(ex_solution_eq_s5),
            FadeOut(left_right_arrow),
            FadeOut(curved_arrow2),
            FadeOut(curved_arrow3),
        )

        self.play(MoveToTarget(ex_solution_eq_s6))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(ex_solution_eq_s7))
        self.wait(SMALL_WAIT_TIME)
        self.play(side_note_bubble2.create_animation())
        self.play(Write(ex_solution_eq_s8), Create(rect_around_ex_solution_eq_s8))
        self.wait(STANDARD_WAIT_TIME)

        self.play(
            side_note_bubble2.fade_out_animation(),
            FadeOut(ex_solution_eq_s7),
            FadeOut(ex_solution_eq_s6),
            FadeOut(ex_solution_eq_s8),
            FadeOut(rect_around_ex_solution_eq_s8),
        )

        self.wait(SMALL_WAIT_TIME)


class SecondExample:
    def construct(self):
        # Variables
        second_example_title = MathTex(r"\text{2. Példa:}").to_edge(UP, buff=0.5)
        second_example_equation = MathTex(
            r"y'", r"+", r"3x^{2}", r"y", r"=", r"4x^{2}", r"y", r"^{2}"
        ).next_to(second_example_title, DOWN, buff=0.5)
        rectangle_around_px = SurroundingRectangle(
            second_example_equation.submobjects[2], color=RED
        )
        rectangle_around_qx = SurroundingRectangle(
            second_example_equation.submobjects[5], color=BLUE
        )
        rect_around_n_2 = SurroundingRectangle(
            second_example_equation.submobjects[7], color=PURPLE_B
        )

        second_example_px = MathTex(r"P(x) = 3x^2").next_to(
            second_example_equation, DOWN, buff=0.5
        )
        second_example_qx = MathTex(r"Q(x) = 4x^2").next_to(
            second_example_px, DOWN, buff=0.5
        )
        second_example_n = MathTex(r"n = 2").next_to(second_example_qx, DOWN, buff=0.5)

        # Move px, qx and n to the top
        second_example_px.generate_target()
        second_example_qx.generate_target()
        second_example_n.generate_target()

        second_example_group = VGroup(
            second_example_px.target,
            second_example_qx.target,
            second_example_n.target,
        )

        second_example_group.arrange_in_grid(rows=2, cols=2, buff=0.5).to_edge(UP)

        side_note_bubble3 = SideNoteBubble(
            content="Ki kell számolni az integrál faktort", position=ORIGIN
        )

        side_note_bubble3.shift(UP * 0.5)

        integrating_factor_reminder2 = integrating_factor.copy().next_to(
            side_note_bubble3, DOWN, buff=0.5
        )

        integrating_factor_reminder2.to_edge(LEFT, buff=2)

        int_fact_s1 = MathTex(r"= e^{\int [1-2]3x^2dx}").next_to(
            integrating_factor_reminder2, RIGHT, buff=0.5
        )
        int_fact_s2 = MathTex(r"= e^{-3 \int x^2dx}").next_to(int_fact_s1, RIGHT)
        int_fact_s3 = MathTex(r"= e^{-3 \cdot \frac{x^3}{3}}").next_to(
            integrating_factor_reminder2, DOWN, buff=0.5
        )
        int_fact_s4 = MathTex(r"= e^{-x^3}").next_to(int_fact_s3, RIGHT, buff=0.5)

        # Put the int_fact_s4 into the vgroup and move it to the top
        final_int_fact = MathTex(r"I(x) = e^{-x^3}")
        second_example_group.add(final_int_fact)
        second_example_group.arrange_in_grid(rows=2, cols=2, buff=0.5)

        side_note_bubble4 = SideNoteBubble(
            content="Használva a megoldási képletet, felírhatjuk az egyenlet megoldását",
            position=second_example_group.get_bottom(),
        )

        solution_equation_reminder = solution_equation.copy().next_to(
            side_note_bubble4, DOWN, buff=0.5
        )

        sol_eq_s1 = MathTex(
            r"y^{1-2} = \frac{1}{e^{-x^3}} \left[",
            r"\int [1-2]4x^2e^{-x^3}dx",
            r" +c\right]",
        ).next_to(solution_equation_reminder, DOWN, buff=0.5)

        # Move sol_eq_s1 to the top
        sol_eq_s1.generate_target()
        sol_eq_s1.target.move_to(ORIGIN).to_edge(UP)

        sol_eq_sub_eq = MathTex(r"\int -4x^2e^{-x^3}dx").next_to(sol_eq_s1.target, DOWN)
        sol_eq_sub_eq.shift(LEFT * 2)

        currved_arrow_int = CurvedArrow(
            sol_eq_s1.target.submobjects[1].get_center(),
            sol_eq_sub_eq.get_center(),
            radius=-2,
            color=RED,
        )

        sol_eq_sub_eq2 = MathTex(r"u = -x^3").next_to(sol_eq_sub_eq, RIGHT, buff=1)
        sol_eq_sub_eq3 = MathTex(r"du = -3x^2dx").next_to(sol_eq_sub_eq, DOWN, buff=0.5)
        sol_eq_sub_eq4 = MathTex(r"dx = \frac{du}{-3x^2}").next_to(
            sol_eq_sub_eq2, DOWN, buff=0.5
        )

        sol_eq_sub_eq5 = MathTex(r"\int -4x^2e^u \frac{du}{-3x^2}")
        sol_eq_sub_eq5.next_to(sol_eq_sub_eq4, DOWN, buff=0.5)
        sol_eq_sub_eq5.shift(LEFT * 4)

        sol_eq_sub_eq6 = MathTex(r"=\frac{4}{3} \int e^u du")
        sol_eq_sub_eq6.next_to(sol_eq_sub_eq5, RIGHT, buff=0.5)

        sol_eq_sub_eq7 = MathTex(r"= \frac{4}{3} e", r"^u")
        sol_eq_sub_eq7.next_to(sol_eq_sub_eq6, RIGHT, buff=0.5)

        sol_eq_sub_eq8 = MathTex(r"= \frac{4}{3} e^{-x^3}")
        sol_eq_sub_eq8.next_to(sol_eq_sub_eq7, DOWN, buff=0.5)

        currved_arrow4 = CurvedArrow(
            sol_eq_sub_eq2.get_center(),
            sol_eq_sub_eq7.submobjects[1].get_center(),
            radius=-6,
            color=RED,
        )

        rectangle_around_eq8 = SurroundingRectangle(sol_eq_sub_eq8, color=RED)
        rectangle_around_qx_integral = SurroundingRectangle(
            sol_eq_s1.target.submobjects[1], color=RED
        )

        side_note_bubble5 = SideNoteBubble(
            content="Ezután behelyettesítjük az kiszámolt integrált...",
            position=sol_eq_sub_eq5.get_bottom() + DOWN * 0.5,
        )

        sol_eq_s2 = MathTex(
            r"y^{-1} = \frac{1}{e^{-x^3}} \left[",
            r"\frac{4}{3} e^{-x^3}",
            r" +c\right]",
        ).next_to(sol_eq_s1.target, DOWN, buff=0.5)

        sol_eq_s3 = MathTex(
            r"y^{-1} = \frac{4}{3} + c \cdot e^{x^3}",
        ).next_to(sol_eq_s2, DOWN, buff=0.5)

        sol_eq_s4 = MathTex(
            r"\frac{1}{y} = \frac{4}{3} + c \cdot e^{x^3}",
        ).next_to(sol_eq_s3, DOWN, buff=0.5)

        # Move sol_eq_s4 to the top
        sol_eq_s4.generate_target()
        sol_eq_s4.target.move_to(ORIGIN).to_edge(UP)

        sol_eq_s5 = MathTex(
            r"y = \frac{1}{\frac{4}{3} + c \cdot e^{x^3}}",
        ).next_to(sol_eq_s4.target, DOWN, buff=0.5)

        side_note_bubble6 = SideNoteBubble(
            content="Beszorozzuk a számlálót és a nevezőt is 3-mal",
            position=sol_eq_s5.get_bottom(),
        )

        sol_eq_s6 = MathTex(
            r"y = \frac{3}{4 + 3c \cdot e^{x^3}}",
        ).next_to(side_note_bubble6, DOWN, buff=0.5)

        rectangle_final = SurroundingRectangle(sol_eq_s6, color=RED)
        side_note_bubble7 = SideNoteBubble(
            content="Ez lesz a végső megoldás", position=rectangle_final.get_bottom()
        )

        # Animations
        self.play(Write(second_example_title))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(second_example_equation))
        self.wait(SMALL_WAIT_TIME)
        self.play(Create(rectangle_around_px))
        self.play(Write(second_example_px))
        self.wait(SMALL_WAIT_TIME)
        self.play(Create(rectangle_around_qx))
        self.play(Write(second_example_qx))
        self.wait(SMALL_WAIT_TIME)
        self.play(Create(rect_around_n_2))
        self.play(Write(second_example_n))
        self.wait(STANDARD_WAIT_TIME)

        self.play(
            FadeOut(second_example_equation),
            FadeOut(second_example_title),
            FadeOut(rectangle_around_px),
            FadeOut(rectangle_around_qx),
            FadeOut(rect_around_n_2),
        )

        # Put the example equation, px, qx and n into a group
        # and move them to the top
        self.play(
            MoveToTarget(second_example_px),
            MoveToTarget(second_example_qx),
            MoveToTarget(second_example_n),
        )
        self.wait(SMALL_WAIT_TIME)
        self.play(side_note_bubble3.create_animation())
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(integrating_factor_reminder2))
        self.play(Write(int_fact_s1))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(int_fact_s2))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(int_fact_s3))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(int_fact_s4))
        self.wait(STANDARD_WAIT_TIME)
        self.play(
            FadeOut(integrating_factor_reminder2),
            FadeOut(int_fact_s1),
            FadeOut(int_fact_s2),
            FadeOut(int_fact_s3),
            FadeOut(int_fact_s4),
            Write(final_int_fact),
        )
        self.wait(SMALL_WAIT_TIME)
        self.play(side_note_bubble3.fade_out_animation())
        self.play(side_note_bubble4.create_animation())
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(solution_equation_reminder))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_s1))
        self.wait(STANDARD_WAIT_TIME)

        self.play(
            FadeOut(second_example_px),
            FadeOut(second_example_qx),
            FadeOut(second_example_n),
            FadeOut(final_int_fact),
            FadeOut(side_note_bubble4),
            FadeOut(solution_equation_reminder),
            MoveToTarget(sol_eq_s1),
        )
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_sub_eq))
        self.play(Create(currved_arrow_int))
        self.wait(SMALL_WAIT_TIME)
        self.play(FadeOut(currved_arrow_int))
        self.play(Write(sol_eq_sub_eq2))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_sub_eq3))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_sub_eq4))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_sub_eq5))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_sub_eq6))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_sub_eq7))
        self.wait(SMALL_WAIT_TIME)
        self.play(Create(currved_arrow4))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_sub_eq8))
        self.wait(SMALL_WAIT_TIME)
        self.play(FadeOut(currved_arrow4))

        self.play(side_note_bubble5.create_animation())
        self.play(Create(rectangle_around_eq8))
        self.wait(SMALL_WAIT_TIME)
        self.play(Create(rectangle_around_qx_integral))
        self.wait(STANDARD_WAIT_TIME)
        self.play(
            FadeOut(sol_eq_sub_eq),
            FadeOut(sol_eq_sub_eq2),
            FadeOut(sol_eq_sub_eq3),
            FadeOut(sol_eq_sub_eq4),
            FadeOut(sol_eq_sub_eq5),
            FadeOut(sol_eq_sub_eq6),
            FadeOut(sol_eq_sub_eq7),
            FadeOut(sol_eq_sub_eq8),
            FadeOut(rectangle_around_eq8),
            FadeOut(rectangle_around_qx_integral),
            FadeOut(side_note_bubble5),
        )
        self.play(Write(sol_eq_s2))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_s3))
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_s4))
        self.wait(SMALL_WAIT_TIME)

        self.play(
            FadeOut(sol_eq_s1),
            FadeOut(sol_eq_s2),
            FadeOut(sol_eq_s3),
            MoveToTarget(sol_eq_s4),
        )
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_s5))
        self.wait(STANDARD_WAIT_TIME)
        self.play(side_note_bubble6.create_animation())
        self.wait(SMALL_WAIT_TIME)
        self.play(Write(sol_eq_s6))
        self.play(Create(rectangle_final))
        self.wait(SMALL_WAIT_TIME)
        self.play(side_note_bubble7.create_animation())
        self.wait(STANDARD_WAIT_TIME)

        self.play(
            FadeOut(sol_eq_s4),
            FadeOut(sol_eq_s5),
            FadeOut(sol_eq_s6),
            FadeOut(rectangle_final),
            FadeOut(side_note_bubble6),
            FadeOut(side_note_bubble7),
        )


class Goodbye(Scene):
    def construct(self):
        thanks = MathTex(r"\text{Köszönöm a figyelmet!}", font_size=80)
        self.play(Write(thanks))
        self.wait(STANDARD_WAIT_TIME)
        self.play(FadeOut(thanks))


class BernoulliEquation(Scene):
    def construct(self):
        # Introduction
        Introduction.construct(self)

        # Steps
        Steps.construct(self)

        # First Example
        FirstExample.construct(self)

        # Second example
        SecondExample.construct(self)

        # Goodbye
        Goodbye.construct(self)
