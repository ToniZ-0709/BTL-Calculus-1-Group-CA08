# manim -p -r 1920,1080 -q h --fps 120 C:\HCMUT\BTL\Calculus1\FinalWork.py
from manim import *

class CalculusIntroScene(Scene):
    def construct(self):
        # Title Text
        TITLE_FONT = "Times New Roman"
        #------------------------------------------------------------------------------------#
        # 1.Group Introduction
        GroupName = Text("Group CA08 – CC15", font_size=50, color=WHITE, font=TITLE_FONT)
        SubjectName = Text("Calculus 1", font_size=120, color=BLUE_C, font=TITLE_FONT, weight=BOLD).next_to(GroupName, UP, buff = 0.3)
        GroupIntroduction = VGroup(SubjectName, GroupName)
        self.play(Write(GroupIntroduction), run_time = 3)
        self.wait(2)
        self.play(FadeOut(GroupIntroduction))
        #------------------------------------------------------------------------------------#
        # 2.Topic Introduction
        Title_top = Text("Integration and its Application", font_size=48, color=WHITE, font=TITLE_FONT)
        integral_sign1 = MathTex(r"\int", font_size=70, color=WHITE).next_to(Title_top, LEFT, buff=0.2)
        FullTopicTitle = VGroup(Title_top, integral_sign1).to_edge(UP*1.05, buff=0.4)

        # Setup Axes (Graph area)
        axes1 = Axes( x_range=[-2, 9, 1], y_range=[-2, 6, 1], x_length=10, y_length=5, axis_config={"include_numbers": False, "color": GRAY_B})
        axes1.next_to(Title_top, DOWN * 2, buff=0.45)
        
        # Define the Curve (Cubic function as requested: f(x) = 0.04(x-4)(x-8)(x-1) + 3)
        def cubic_func_new(x):
            return 0.04 * (x - 4) * (x - 8) * (x - 1) + 3
            
        # Plot the curve over the range [0, 8]
        curve = axes1.plot(cubic_func_new, x_range=[-1.5, 9], color=BLUE) 
        
        # Riemann Sum (Approximation Rectangles)
        num_rects = 20
        x_min_rect = -0.5
        x_max_rect = 8 
        
        rects = axes1.get_riemann_rectangles(
            graph=curve,
            x_range=[x_min_rect, x_max_rect], 
            dx=(x_max_rect - x_min_rect) / num_rects,
            input_sample_type="right",
            stroke_width=0.1, 
            fill_opacity=0.8).set_color_by_gradient(TEAL_B, BLUE_C) 
        
        #------------------------------------------------------------------------------------#
        # 3. Table of Contents
        Table = Text("Table of Contents", font_size=62, color=WHITE, font=TITLE_FONT, weight="BOLD").to_edge(UP*2, buff=0.8)
        line = Line(Table.get_left() + DOWN * 0.15, Table.get_right() + DOWN * 0.15, color=WHITE, stroke_width=2).next_to(Table, DOWN, buff=0.1)
        TableGroup = VGroup(Table, line).shift(UP * 1.2)

        #Define the list items and colors
        toc_items = [
            ("Definition of Integration", RED_B),
            ("Riemann Sums & Approximating Area", YELLOW_B),
            ("Fundamental Theorem of Calculus", GREEN_B),
            ("Geometric Meaning", BLUE_C),
        ]

        list_mobjects = VGroup()

        start_position = line.get_center() + DOWN * 1.5
        for i, (text, color) in enumerate(toc_items):
            # Text Mobject
            item_text = Text(
                text,
                font_size=42,
                color=color,
                font=TITLE_FONT,
                weight="BOLD"
            )
            
            # Bullet point (Circle)
            bullet = Circle(
                radius=0.15,
                color=color,
                fill_opacity=1
            )
            
            # Group the bullet and text
            item_group = VGroup(bullet, item_text)
            item_text.next_to(bullet, RIGHT, buff=0.5)
            item_group.move_to(start_position + DOWN * i * 1.3)
            item_group.align_to(Table, LEFT).shift(RIGHT * 1.5) 
            list_mobjects.add(item_group)

        #------------------------------------------------------------------------------------#
        # --- ANIMATION --- #
        # Write the title
        self.play(LaggedStart(Write(FullTopicTitle),lag_ratio=0.3))
        self.wait(0.5)
        
        # Create Axes and Draw the Curve
        self.play(Create(axes1), Create(curve), run_time=2)
        self.wait(1)
        
        # Show the Riemann Sum Rectangles
        self.play(FadeIn(rects, shift=UP, lag_ratio=0.05), run_time=2.5)
        self.wait(2)
        
        # Clean up
        self.play(FadeOut(FullTopicTitle, shift=UP), FadeOut(axes1), FadeOut(curve), FadeOut(rects))
        self.wait(1)

        # Write the Title and Line
        self.play(Write(Table), Create(line), run_time = 1.5)
        self.wait(0.8)
        
        # Write the List Items sequentially
        for item in list_mobjects:
            self.play(FadeIn(item[0].shift(LEFT*4), scale=0.5), run_time=0.5) 
            self.play(Write(item[1].shift(LEFT*4)), run_time=1.6)
        self.wait(2)
        
        # Clean up
        self.play(
            FadeOut(Table, shift=UP),
            FadeOut(line, shift=UP),
            FadeOut(list_mobjects, shift=DOWN),
            run_time=1
        )
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        # Part 1: Title and Basic Formula
        global title
        title = Text("What is Integration?", font_size = 48, color=BLUE, font=TITLE_FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time = 2)
        self.wait(1.5)

        formula = MathTex("\\int_{a}^{b} f(x) dx = F(b) - F(a)", font_size = 36)
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula), run_time = 1.5)
        self.wait(1.5)

        # Clear for next part
        self.play(FadeOut(title), FadeOut(formula))
        
        #------------------------------------------------------------------------------------#
        # Part 2: Integral Symbol Explanation
        symbols_title = Text("Integral Symbol Explanation", font_size=48, color=BLUE, font=TITLE_FONT)
        symbols_title.to_edge(UP*1.5, buff=0.8)
        
        DESCRIPTION_FONT = "Times New Roman"
                
        # Integral Sign 
        integral_math = MathTex(r"\int", color=RED_D)
        integral_desc = Text("  -  Integral sign", font=DESCRIPTION_FONT, color=YELLOW).scale(0.8)
        integral_group = VGroup(integral_math, integral_desc).arrange(RIGHT, buff=0.1)
        integral_desc.align_to(integral_math, UP) 
        
        # Lower Limit (a)
        a_math = MathTex(r"a", color=ORANGE).scale(1.1)
        a_desc = Text("  -  Lower limit", font=DESCRIPTION_FONT, color=YELLOW).scale(0.8)
        a_group = VGroup(a_math, a_desc).arrange(RIGHT, buff=0.1)

        # Upper Limit (b)
        b_math = MathTex(r"b", color=ORANGE).scale(1.1)
        b_desc = Text("  -  Upper limit", font=DESCRIPTION_FONT, color=YELLOW).scale(0.8)
        b_group = VGroup(b_math, b_desc).arrange(RIGHT, buff=0.1)

        # Function (f(x))
        fx_math = MathTex(r"f(x)", color=PURPLE_B)
        fx_desc = Text("  -  Function (Integrand)", font=DESCRIPTION_FONT, color=YELLOW).scale(0.8)
        fx_group = VGroup(fx_math, fx_desc).arrange(RIGHT, buff=0.1)

        # Differential (dx)
        dx_math = MathTex(r"dx", color=PURPLE_B)
        dx_desc = Text("  -  Differential (Variable)", font=DESCRIPTION_FONT, color=YELLOW).scale(0.8)
        dx_group = VGroup(dx_math, dx_desc).arrange(RIGHT, buff=0.1)
        
        # Antiderivative (F(x))
        Fx_math = MathTex(r"F(x)", color=GREEN_D)
        Fx_desc = Text("  -  Antiderivative", font=DESCRIPTION_FONT, color=YELLOW).scale(0.8)
        Fx_group = VGroup(Fx_math, Fx_desc).arrange(RIGHT, buff=0.1)

        
        all_symbols = VGroup(
            integral_group,
            a_group,
            b_group,
            fx_group,
            dx_group,
            Fx_group
        ).arrange(DOWN * 0.8, buff=0.6).scale(0.8) 
        all_symbols.next_to(symbols_title, DOWN * 0.2, buff=0.5)


        # --- ANIMATION ---
        symbols_title.shift(UP * 0.8)
        self.play(Write(symbols_title), run_time = 1.5)
        self.wait(0.5)
        
        for item in all_symbols:
            self.play(
                Write(item[0], run_time=1),
                FadeIn(item[1], shift=RIGHT, run_time=0.8),
                run_time = 1.5
            )
            self.wait(1.2)
            
        self.wait(2)
        self.play(
            FadeOut(symbols_title, shift=UP),
            FadeOut(all_symbols, shift=DOWN),
            run_time=1
        )
        #------------------------------------------------------------------------------------#
        # Part 3: Meaning
        meaning_title = Text("Meaning of Integration", font_size=48, color=BLUE, font=TITLE_FONT)
        meaning_title.to_edge(UP)
        self.play(Write(meaning_title), run_time = 1.5)

        meanings = VGroup(
            Text("• Sum of small changes", font_size=32),
            Text("• Reverse of differentiation", font_size=32),
            Text("• Adds infinitesimal parts", font_size=32),
            Text("• Finds accumulated change", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.8)

        meanings.next_to(meaning_title, DOWN, buff=0.5)
        
        for meaning in meanings:
            self.play(Write(meaning), run_time = 1.5)
            self.wait(1)

        self.wait(2)
        self.play(FadeOut(meaning_title), FadeOut(meanings))

        # Part 4: Visual with a straight line function f(x) = 2x, a=1, b=2
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 6, 1],
            x_length=7,
            y_length=4
        ).scale(1.4)
        
        # Define a straight line function f(x) = 2x
        graph = axes.plot(lambda x: 2*x, x_range=[0, 3], color=GREEN)
        
        # Set integration limits
        a, b = 1, 2
        area = axes.get_area(graph, x_range=[a, b], color=BLUE, opacity=0.5)
        
        self.play(Create(axes), Create(graph), run_time = 1)
        self.wait(1)
        self.play(Create(area), run_time = 1)
        self.wait(2)

        # Add labels for a and b
        a_label = MathTex("a=1", font_size=20, color=RED).next_to(axes.c2p(a, 0), DOWN)
        b_label = MathTex("b=2", font_size=20, color=RED).next_to(axes.c2p(b, 0), DOWN)
        
        function_label = MathTex("f(x) = 2x", font_size=36, color=GREEN)
        function_label.next_to(axes, UP * 0.7, buff=0.1)
        
        area_label = Text("The area under the curve = Integration", font = TITLE_FONT, font_size=24, color=WHITE)
        area_label.next_to(axes, DOWN * 0.8, buff=0.4)
        
        self.play(Write(a_label), Write(b_label), Write(function_label), Write(area_label), run_time = 1.5)
        self.wait(3)
        ABCABC = VGroup(a_label, b_label, function_label, area_label, axes, graph, area)
        self.play(FadeOut(ABCABC), run_time = 1)
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        # Title 
        title = Text("Riemann Sums and Area Approximation", font = TITLE_FONT, font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(1.5) 

        text_part1 = MathTex(
            "\\text{Let } f(x) \\text{ be a function defined on the closed interval } [a, b] \\text{ with } a < b.",
            font_size=32,
            color=WHITE
        ).next_to(title, DOWN, buff=0.5)
        
        text_part2 = MathTex(
            "\\text{We subdivide the interval } [a, b] \\text{ into } n \\text{ equal sub-intervals: }",
            font_size=32,
            color=WHITE
        ).next_to(text_part1, DOWN, buff=0.3)

        text_part3 = MathTex(
            "x_0 < x_1 < x_2 < \\dots < x_n = b",
            font_size=32,
            color=WHITE
        ).next_to(text_part2, DOWN, buff=0.3)

        # Formula for xi and delta x
        formula1 = MathTex("x_i = a + i \\cdot \\Delta x", font_size=32, color=WHITE).next_to(text_part3, DOWN, buff=0.5)
        formula2 = MathTex("\\Delta x = \\frac{b - a}{n}", font_size=32, color=WHITE).next_to(formula1, DOWN, buff=0.3)

        # Animation
        self.play(Write(text_part1), run_time=3)
        self.wait(1)
                
        self.play(Write(text_part2), run_time=3)
        self.wait(2)
        
        self.play(Write(text_part3), run_time=3)
        self.wait(2)

        self.play(Write(formula1), run_time=1.5)
        self.wait(1.5)

        self.play(Write(formula2), run_time=1.5)
        self.wait(3)

        elements = VGroup(text_part1, text_part2, text_part3, formula1, formula2)
        self.play(FadeOut(elements))
        
        # Create axes and function f(x) = x^3 - 3x + 5, shift to left - Đã tăng run_time từ 1s lên 2.5s
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 35, 5],
            x_length = 6,
            y_length = 5.2,
            axis_config={"color": WHITE}
        )
        axes.shift(LEFT * 2 + DOWN * 0.5)  # Shift left to make space for text
        
        # Define the function
        def func(x):
            return x**3 - 3*x + 5
        
        graph = axes.plot(func, x_range=[0, 3.6], color=GREEN)
        
        # Set integration limits
        a, b = 1, 3
        
        # Function label
        global func_label1
        func_label1 = MathTex("f(x) = x^3 - 3x + 5", font_size=24, color=GREEN)
        func_label1.next_to(axes, UP, buff = 0.1)
    

        self.play(Create(axes), Create(graph), Write(func_label1), run_time=2.5)
        self.wait(2)
        

        # Show the Riemann sum rectangles with FAST transition
        self.show_smooth_riemann_transition(axes, graph, a, b, func)
        
        # Transition to integral - normal speed
        self.transition_to_integral(axes, graph, a, b, func)
        
    def show_smooth_riemann_transition(self, axes, graph, a, b, func):
        n = 5
        
        # Create initial rectangles
        rectangles = self.create_rectangles(axes, a, b, n, func)
        
        # Create Riemann sum formula - position on the right side
        riemann_sum = MathTex(
            "\\sum_{i=1}^{n} f(x_i) \\Delta x",
            font_size=32
        )
        riemann_sum.shift(UP * 1)  # Position on right side
        riemann_sum.shift(RIGHT * 4)
        # Show n value
        n_text = MathTex(f"n = {n}", font_size=32)
        n_text.next_to(riemann_sum, DOWN, buff=0.3)
        
        self.rectangles = rectangles
        self.riemann_sum_text = VGroup(riemann_sum, n_text)
        
        self.play(Create(rectangles), Write(riemann_sum), Write(n_text), run_time=2)
        self.wait(2) 
        
        # FAST transitions for the graph part only 
        n_values = list(range(6, 15)) + list(range(15, 51, 5)) + list(range(60, 151, 20))
        
        for new_n in n_values:
            self.smooth_update_rectangles(axes, graph, a, b, new_n, func)
    
    def create_rectangles(self, axes, a, b, n, func):
        # Calculate delta x
        dx = (b - a) / n
        
        # Create rectangles
        rectangles = VGroup()
        for i in range(n):
            x_left = a + i * dx
            x_right = x_left + dx
            height = func(x_left)
            
            # Create rectangle
            rect = Polygon(
                axes.c2p(x_left, 0),
                axes.c2p(x_right, 0),
                axes.c2p(x_right, height),
                axes.c2p(x_left, height),
                color=BLUE,
                fill_opacity=0.5,
                stroke_width=0.2
            )
            rectangles.add(rect)
        
        return rectangles
    
    def smooth_update_rectangles(self, axes, graph, a, b, n, func):
        # Create new rectangles
        new_rectangles = self.create_rectangles(axes, a, b, n, func)
        
        # Update n value text
        new_n_text = MathTex(f"n = {n}", font_size=24)
        new_n_text.move_to(self.riemann_sum_text[1].get_center())
        
        # FAST animation for rectangles only 
        self.play(
            ReplacementTransform(self.rectangles, new_rectangles),
            Transform(self.riemann_sum_text[1], new_n_text),
            run_time=0.1
        )
        
        # Update references
        self.rectangles = new_rectangles
    
    def transition_to_integral(self, axes, graph, a, b, func):
        # Clear previous elements
        self.play(
            FadeOut(self.rectangles),
            FadeOut(self.riemann_sum_text),
            run_time=2
        )
        
        # Show the actual area under the curve 
        area = axes.get_area(graph, x_range=[a, b], color=BLUE, opacity=0.3)
        
        # Transition from sum to integral - position on the right side 
        sum_formula = MathTex("\\lim_{n \\to \\infty} \\sum_{i=1}^{n} f(x_i) \\Delta x", font_size=32)
        sum_formula.shift(UP * 1)
        sum_formula.shift(RIGHT * 4)
        
        integral_formula = MathTex("= \\int_{a}^{b} f(x) dx", font_size=32)
        integral_formula.next_to(sum_formula, DOWN, buff=0.3)
        
        self.play(FadeIn(area), Write(sum_formula), run_time=2)
        self.wait(2) 
        self.play(Write(integral_formula), run_time=2)
        self.wait(2) 
        
        # Final conclusion as formula 
        conclusion = MathTex(
            "\\int_{a}^{b} f(x) dx = \\lim_{n \\to \\infty} \\sum_{i=1}^{n} f(x_i) \\Delta x",
            font_size=32,
            color=GREEN
        )
        conclusion.next_to(integral_formula, DOWN, buff=0.5)
        
        self.play(Write(conclusion), run_time=3)
        self.wait(4)

        self.play(
            FadeOut(sum_formula),
            FadeOut(integral_formula),
            FadeOut(conclusion),
            FadeOut(area),
            FadeOut(axes),
            FadeOut(graph),
            FadeOut(func_label1),
            FadeOut(title),
            run_time=2
        )
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        # Title
        TITLE_FONT = "Times New Roman"
        title = Text("Fundamental Theorem of Calculus", font_size=48, color=BLUE, font=TITLE_FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time = 2)
        self.wait(1.5)

        # Part 1: Derivative of the Integral
        part1_title = Text("Part 1: Derivative of the Integral", font_size=36, color=YELLOW, font=TITLE_FONT)
        part1_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(part1_title), run_time = 1.5)
        self.wait(1.5)

        # FTC Part 1 formula
        ftc1_formula = MathTex(
            "\\frac{d}{dx} \\int_a^x f(t) dt = f(x)",
            font_size=40,
            color=GREEN
        )
        ftc1_formula.next_to(part1_title, DOWN, buff=0.8)
        self.play(Write(ftc1_formula), run_time = 1.5)
        self.wait(2)

        # Explanation of Part 1
        explanation1 = VGroup(
            Text("• The derivative 'undoes' the integral", font_size=24),
            Text("• Rate of change of accumulated area = The original function", font_size=24),
            Text("• If F(x) = ∫f(t)dt from a to x, then F'(x) = f(x)", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        explanation1.next_to(ftc1_formula, DOWN, buff=0.8)
        
        for item in explanation1:
            self.play(Write(item), run_time = 2)
            self.wait(1.5)
        
        self.wait(3)

        # Clear for Part 2
        self.play(
            FadeOut(part1_title),
            FadeOut(ftc1_formula),
            FadeOut(explanation1)
        )

        # Part 2: Evaluation of Definite Integrals
        part2_title = Text("Part 2: Evaluation using Antiderivative", font_size=36, color=ORANGE, font=TITLE_FONT)
        part2_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(part2_title), run_time = 1.5)
        self.wait(1.5)

        # FTC Part 2 formula
        ftc2_formula = MathTex(
            "\\int_a^b f(x) dx = F(b) - F(a)",
            font_size=40,
            color=GREEN
        )
        ftc2_formula.next_to(part2_title, DOWN, buff=0.8)
        self.play(Write(ftc2_formula), run_time = 1.5)
        self.wait(2)

        # Where F is antiderivative
        where_F = MathTex(
            "\\text{where } F'(x) = f(x)",
            font_size=30,
            color=WHITE
        )
        where_F.next_to(ftc2_formula, DOWN, buff=0.3)
        self.play(Write(where_F))
        self.wait(1)

        # Explanation of Part 2
        explanation2 = VGroup(
            Text("• To compute definite integral, find the antiderivative F(x)", font_size=24),
            Text("• Evaluate F(x) at upper and lower limits", font_size=24),
            Text("• Subtract: F(b) - F(a)", font_size=24),
            Text("• This gives the exact area under the curve", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)

        explanation2.next_to(where_F, DOWN, buff=0.8)
        
        for item in explanation2:
            self.play(Write(item), run_time=2)
            self.wait(1.5)
        
        self.wait(3)

        # Clear for example
        self.play(
            FadeOut(part2_title),
            FadeOut(ftc2_formula),
            FadeOut(where_F),
            FadeOut(explanation2)
        )

        # Example
        self.show_example(title)
    def show_example(self, main_title):
        # 1. Example Title
        example_title = Text("Example: Compute ∫(2x) dx from 1 to 3", font_size=36, color=PURPLE, font="Times New Roman")
        example_title.next_to(main_title, DOWN, buff=0.5)
        self.play(Write(example_title), run_time = 1.5)
        self.wait(1.5)

        # 2. Step by step solution
        steps = VGroup(
            MathTex("\\text{1. Find antiderivative: } F(x) = x^2 + C", font_size=28),
            MathTex("\\text{2. Apply FTC: } \\int_1^3 2x dx = F(3) - F(1)", font_size=28),
            MathTex("\\text{3. Evaluate: } F(3) - F(1) = (3^2) - (1^2)", font_size=28),
            MathTex("\\text{4. Compute: } (3^2) - (1^2) = 9 - 1 = 8", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        steps.next_to(example_title, DOWN, buff=0.8)

        for step in steps:
            self.play(Write(step), run_time = 1.8)
            self.wait(1.5)

        self.wait(3)

        # 3. Visual demonstration
        self.show_visual_demonstration(main_title, example_title, steps)

    def show_visual_demonstration(self, main_title, example_title, steps):
        # Clear steps for visualization
        self.play(FadeOut(steps))

        # Create axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 8, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE}
        )
        axes.shift(DOWN * 0.5)

        # Function f(x) = 2x
        graph = axes.plot(lambda x: 2*x, x_range=[0, 3.5], color=GREEN)
        
        # Area under curve from 1 to 3
        area = axes.get_area(graph, x_range=[1, 3], color=BLUE, opacity=0.4)

        # Labels
        func_label = MathTex("f(x) = 2x", font_size=24, color=GREEN)
        func_label.next_to(axes, UP, buff=0.1)

        area_label = MathTex("\\text{Area} = 8", font_size=24, color=BLUE)
        area_label.next_to(area, UP, buff=0.2)

        # Vertical lines at x=1 and x=3
        line1 = DashedLine(axes.c2p(1, 0), axes.c2p(1, 6), color=RED)
        line3 = DashedLine(axes.c2p(3, 0), axes.c2p(3, 6), color=RED)

        x1_label = MathTex("x=1", font_size=20, color=RED).next_to(axes.c2p(1, 0), DOWN)
        x3_label = MathTex("x=3", font_size=20, color=RED).next_to(axes.c2p(3, 0), DOWN)

        # Connection formula
        ftc_connection = MathTex(
            "\\int_1^3 2x dx = 3^2 - 1^2 = 8",
            font_size=30,
            color=GREEN
        )
        ftc_connection.next_to(axes, DOWN * 0.5, buff=0.8)
        
        # Presentation of graph
        self.play(
            Create(axes),
            Create(graph),
            Write(func_label),
            run_time = 3
        )
        self.wait(0.5)

        self.play(
            Create(line1),
            Create(line3),
            Write(x1_label),
            Write(x3_label)
        )
        self.wait(1)

        self.play(FadeIn(area), Write(area_label))
        self.wait(2)

        self.play(Write(ftc_connection))
        self.wait(2)
                
        # FadeOut 
        graph_elements = VGroup(
            axes, graph, area, func_label, area_label, line1, line3, x1_label, x3_label, ftc_connection, example_title
        )
        self.play(FadeOut(graph_elements), run_time=2)
        self.wait(0.5)

        # Summary
        summary_title = Text("Summary of FTC:", font_size=36, color=GREEN, font="Times New Roman")
        summary_title.next_to(main_title, DOWN, buff=0.5)
        self.play(Write(summary_title), run_time = 1.5)
        self.wait(1.5)

        summary = VGroup(
            MathTex("\\text{FTC Part 1: } \\frac{d}{dx} \\int_a^x f(t) dt = f(x)", font_size=24),
            MathTex("\\text{FTC Part 2: } \\int_a^b f(x) dx = F(b) - F(a)", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(summary_title, DOWN, buff=1.0) 

        self.play(Write(summary), run_time = 4)
        self.wait(3)

        # FadeOut
        self.play(
            FadeOut(main_title),
            FadeOut(summary_title),
            FadeOut(summary),
            run_time=1.5
        )
        self.wait(1)
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        # Problem 1
        # Title for Exercise section
        TITLE_FONT = "Times New Roman"
        title = Text("Problem 1: Find the Value of m", font_size=48, color=BLUE, font = TITLE_FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time = 2)
        self.wait(1.5)
        
        # Problem statement
        problem = VGroup(
            Text("Find positive m such that:", font_size=32, color=WHITE),
            MathTex("\\text{Area bounded by } y = 2x + 3, y = 0, x = 0, x = m \\text{ equals } 10", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT*0.8, buff=0.3)
        
        problem.next_to(title, DOWN, buff=0.5)
        problem.shift(RIGHT*0.1)
        self.play(Write(problem), run_time = 4)
        self.wait(4)
        
        # Clear for solution
        self.play(FadeOut(problem))
        
        # Mathematical solution
        self.show_solution(title)
        
        # Draw the figure after solution
        self.draw_final_figure(title)
        
        # Final FadeOut for the main scene elements
        self.play(FadeOut(title), run_time=1.5)
        self.wait(0.5)
    
    def show_solution(self, title):
        # Step 1: Set up the integral
        step1 = MathTex("\\text{Area} = \\int_0^m (2x + 3) dx = 10", font_size=36)
        step1.next_to(title, DOWN, buff=0.8)
        self.play(Write(step1))
        self.wait(2)
        
        # Step 2: Find antiderivative
        step2 = MathTex("F(x) = x^2 + 3x", font_size=36)
        step2.next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2), run_time = 2)
        self.wait(2)
        
        # Step 3: Apply FTC
        step3 = MathTex("\\Rightarrow F(m) - F(0) = m^2 + 3m", font_size=36)
        step3.next_to(step2, DOWN, buff=0.5)
        self.play(Write(step3), run_time = 2)
        self.wait(2)
        
        # Step 4: Set up equation
        step4 = MathTex("\iff m^2 + 3m = 10", font_size=36)
        step4.next_to(step3, DOWN, buff=0.5)
        self.play(Write(step4))
        self.wait(2)
        
        # Step 7: Solutions (Implicitly solving m^2 + 3m - 10 = 0)
        step7 = MathTex("\iff m = -5 \\quad \\text{or} \\quad m = 2", font_size=36)
        step7.next_to(step4, DOWN, buff=0.5)
        self.play(Write(step7))
        self.wait(2)
        
        # Step 8: Select positive solution
        step8 = MathTex("m > 0 \\Rightarrow m = 2", font_size=36, color=GREEN)
        step8.next_to(step7, DOWN, buff=0.5)
        self.play(Write(step8), run_time = 2)
        self.wait(2)
        
        # Store steps for later fade out
        self.solution_steps = VGroup(step1, step2, step3, step4, step7, step8)
    
    def draw_final_figure(self, title):
        # Clear the solution steps
        self.play(FadeOut(self.solution_steps))
        
        # Create final figure title
        final_title = Text("Final Solution: m = 2", font_size=24, color=GOLD)
        final_title.next_to(title, DOWN, buff=0.5)
        self.play(Write(final_title))
        self.wait(1)
        
        # Create axes
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 12, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE}
        )
        axes.shift(DOWN * 0.4)
        
        # Function y = 2x + 3
        graph = axes.plot(lambda x: 2*x + 3, x_range=[0, 3.5], color=GREEN)
        
        # Area for m = 2
        area = axes.get_area(graph, x_range=[0, 2], color=BLUE, opacity=0.4)
        
        # Labels
        func_label = MathTex("y = 2x + 3", font_size=24, color=GREEN)
        func_label.next_to(axes, UP, buff=0.1)
        
        m_label = MathTex("m = 2", font_size=20, color=RED)
        m_label.next_to(axes.c2p(2, 0), DOWN)
        
        area_label = MathTex("\\text{Area} = 10", font_size=20, color=BLUE)
        area_label.next_to(area, UP, buff=0.2)
        
        # Vertical line at x = 2
        m_line = DashedLine(axes.c2p(2, 0), axes.c2p(2, 7), color=RED)
        
        # Store all graph elements
        all_graph_elements = VGroup(
            axes, graph, area, func_label, m_label, area_label, m_line, final_title
        )
        
        # Create all elements
        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Write(func_label))
        self.wait(0.5)
        
        self.play(Create(m_line))
        self.play(Write(m_label))
        self.play(FadeIn(area))
        self.play(Write(area_label))
        self.wait(2)
        
        # Show the integral calculation
        calculation = MathTex(
            "\\int_0^2 (2x + 3) dx = [x^2 + 3x]_0^2 = (4 + 6) - 0 = 10",
            font_size=28,
            color=GREEN
        )
        calculation.next_to(axes, DOWN * 0.6 , buff=0.6)
        self.play(Write(calculation))
        self.wait(3)
        
        # FadeOut
        self.play(FadeOut(all_graph_elements, calculation), run_time=2)
        self.wait(0.5)
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        # Problem 2
        TITLE_FONT = "Times New Roman"
        title = Text("Problem 2: Area Calculation", font_size=48, color=BLUE, font = TITLE_FONT)
        title.to_edge(UP)
        self.play(Write(title), run_time = 2)
        self.wait(1.5)
        
        problem = Text("Compute the area of the region (H) using both Integral & Riemann Sum.", font_size=28, color=WHITE).next_to(title, DOWN, buff=0.3)        
        self.play(Write(problem), run_time = 4)
        self.wait(1)
        
        # 1. Setup Axes and Function
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[0, 8, 1],
            x_length=7.5,
            y_length=7.5,
        ).shift(DOWN).scale(0.7)
        
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Create(labels), run_time=2)
        self.wait(1.5)

        # Function and region
        def func(x):
            return x**2
        
        graph = axes.plot(func, x_range=[-2.5, 2.5], color=BLUE)        
        self.play(Create(graph))
        self.wait(0.5)

        # Highlight region H
        region_H = axes.get_area(graph, x_range=[1, 2], color=GREEN, opacity=0.5)
        region_label = MathTex("\\text{Region } H").next_to(axes.c2p(1.5, 2), RIGHT*1.4).scale(0.6)
        
        self.play(FadeIn(region_H), Write(region_label))
        self.wait(3)


        # 3. Transition
        
        # A. Fade Out Problem
        self.play(FadeOut(problem), run_time=1.5)
        
        # B. Move the graph
        graph_group = VGroup(axes, labels, graph, region_H, region_label)
        self.play(
            graph_group.animate.to_edge(LEFT, buff=0.5).shift(UP*0.5).scale(1.05),
            run_time=1.5
        )
        self.wait(1)

        # Riemann Sum
        riemann_rects = axes.get_riemann_rectangles(
            graph,
            x_range=[1, 2],
            dx=0.1,
            input_sample_type="right",
            color=RED,
            fill_opacity=0.6
        )

        riemann_text = VGroup(
            MathTex("\\text{Riemann Sum (n=10):}"),
            MathTex("\\Delta x = 0.1"),
            MathTex("A \\approx 2.185")
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3.5 + UP*1.2).scale(0.7)
        
        self.play(FadeOut(region_H), FadeOut(region_label))
        self.play(Create(riemann_rects), Write(riemann_text), run_time = 3)
        self.wait(2)

        # Integral calculation
        integral_text = VGroup(
            MathTex("\\text{The exact Area:}"),
            MathTex("A = \\int_1^2 x^2 dx"),
            MathTex("A = \\left[\\frac{x^3}{3}\\right]_1^2"),
            MathTex("A = \\frac{8}{3} - \\frac{1}{3}"),
            MathTex("A = \\frac{7}{3} \\approx 2.3333")
        ).arrange(DOWN, aligned_edge=LEFT).shift(RIGHT * 3.5).scale(0.7)
        integral_text.shift(DOWN*0.3)
        self.play(
            FadeOut(riemann_rects),
            FadeOut(riemann_text),
        )
        self.play(Write(integral_text), run_time = 4)
        self.wait(4)

        # Animation: 
        self.play(
            FadeOut(integral_text), 
            run_time=1.5
        )
        self.wait(2)

       # Summary
        summary_title = Text("Summary:", font_size=36, font=TITLE_FONT, color=RED_C)
        summary_riemann = MathTex("+ \\text{Riemann Sum: } A \\approx 2.185", font_size=36)
        summary_integral = MathTex("+ \\text{Integral: } A = \\frac{7}{3} \\approx 2.3333", font_size=36)
        
        summary = VGroup(
            summary_title,
            summary_riemann,
            summary_integral
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.8) 
        
        summary.move_to(integral_text.get_center())
        summary.shift(UP*0.5 + RIGHT*0.4)
        
        # Write Summary
        self.play(Write(summary))
        self.wait(3)
        
        # Clean finish 
        all_final_elements = VGroup(summary, title, graph, axes, labels)
        self.play(FadeOut(all_final_elements), run_time=1.5)
        self.wait(1)
