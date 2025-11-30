# manim -p -r 1920,1080 -q h --fps 120 C:\HCMUT\BTL\Calculus1\Test.py
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
        self.play(Write(GroupIntroduction), runtime = 3)
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
        self.play(Write(Table), Create(line), runtime = 1.5)
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
        title = Text("What is Integration?", font_size = 48, color=BLUE, font=TITLE_FONT)
        title.to_edge(UP)
        self.play(Write(title), runtime = 1.5)
        self.wait(1.5)

        formula = MathTex("\\int_{a}^{b} f(x) dx = F(b) - F(a)", font_size = 36)
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula), runtime = 1.5)
        self.wait(2)

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
        self.play(Write(symbols_title), runtime = 1.5)
        self.wait(0.5)
        
        for item in all_symbols:
            self.play(
                Write(item[0], run_time=1),
                FadeIn(item[1], shift=RIGHT, run_time=1.2),
                runtime = 2
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
        self.play(Write(meaning_title), runtime = 1.5)

        meanings = VGroup(
            Text("• Sum of small changes", font_size=32),
            Text("• Reverse of differentiation", font_size=32),
            Text("• Adds infinitesimal parts", font_size=32),
            Text("• Finds accumulated change", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.8)

        meanings.next_to(meaning_title, DOWN, buff=0.5)
        
        for meaning in meanings:
            self.play(Write(meaning), runtime = 1.5)
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
        
        self.play(Create(axes), Create(graph), runtime = 1)
        self.wait(1)
        self.play(Create(area), runtime = 1)
        self.wait(2)

        # Add labels for a and b
        a_label = MathTex("a=1", font_size=20, color=RED).next_to(axes.c2p(a, 0), DOWN)
        b_label = MathTex("b=2", font_size=20, color=RED).next_to(axes.c2p(b, 0), DOWN)
        
        function_label = MathTex("f(x) = 2x", font_size=36, color=GREEN)
        function_label.next_to(axes, UP * 0.7, buff=0.1)
        
        area_label = Text("The area under the curve = Integration", font = TITLE_FONT, font_size=24, color=WHITE)
        area_label.next_to(axes, DOWN * 0.8, buff=0.4)
        
        self.play(Write(a_label), Write(b_label), Write(function_label), Write(area_label), runtime = 1.5)
        self.wait(3)
        ABCABC = VGroup(a_label, b_label, function_label, area_label, axes, graph, area)
        self.play(FadeOut(ABCABC), runtime = 1)
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        #------------------------------------------------------------------------------------#
        # Title 
        title = Text("Riemann Sums and Area Approximation", font = TITLE_FONT, font_size=48, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(2) 
        
        # Formula for xi and delta x
        formulas = VGroup(
            MathTex("x_i = a + i \\cdot \\Delta x"),
            MathTex("\\Delta x = \\frac{b - a}{n}")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        
        formulas.next_to(title, DOWN, buff=0.8)
        self.play(Write(formulas), run_time=3.5)
        self.wait(4)
        
        # Clear for visualization
        self.play(FadeOut(title), FadeOut(formulas), run_time=2)
        
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
            run_time=2
        )
