from manim import *
import numpy as np
import random
from pynverse import inversefunc

YELLOW_Z = "#e2e1a4"

A_AQUA = "#8dd3c7"
A_YELLOW = "#ffffb3"
A_LAVENDER = "#bebada"
A_RED = "#fb8072"
A_BLUE = "#80b1d3"
A_ORANGE = "#fdb462"
A_GREEN = "#b3de69"
A_PINK = "#fccde5"
A_GREY = "#d9d9d9"
A_VIOLET = "#bc80bd"
A_UNKA = "#ccebc5"
A_UNKB = "#ffed6f"




class QuoteScene(Scene):

    def __init__(self,quote="", author="(Unknown)", **kwargs):
        self.quote = quote
        self.author = author
        super().__init__(**kwargs)

    def construct(self):
        
        quotetext = Paragraph(self.quote, height=config.frame_height*0.3, width=config.frame_width*0.3)
        author = Text(f"--{self.author}", height=config.frame_height*0.3, width=config.frame_width*0.3, slant=ITALIC)

        self.play(Write(quotetext))
        self.wait()
        self.play(Write(author.next_to(quotetext, DOWN)))
        self.wait()

class OpeningQuote(QuoteScene):
    def __init__(self):
        quote = ""
        super().__init__(quote=quote, author="=")

class PartScene(Scene):
    def __init__(self, n=1, title="", question="", title_color=RED, **kwargs):
        self.n = n
        self.title = title
        self.title_color = title_color
        self.question = question
        super().__init__(**kwargs)

    def construct(self):
        part = Tex(f"Part {self.n}: {self.title}")
        part.scale(2)
        part.shift(UP)

        #title = Tex(self.title, color=self.title_color)
        #title.scale(2)
        question = Text(self.question, slant=ITALIC)
        question.next_to(part, DOWN)

        self.play(Write(part))
        #self.play(Write(title))
        self.play(Write(question))

        self.play(FadeOut(part), FadeOut(question))
        #self.play(FadeOut(title))
        #self.play(FadeOut(question))

        self.wait()

class PartOneFunctions(PartScene):
    def __init__(self):
        self.n = 1
        self.title = "Functions"
        self.question = "What exactly is a function?"
        self.title_color = DARK_BLUE

        super().__init__(n=1, title=self.title, question=self.question, title_color=self.title_color)

class PartTwoInjections(PartScene):
    def __init__(self):
        self.n = 2
        self.title = "Injections"
        self.question = "What exactly is an Injection?"
        self.title_color = DARK_BLUE

        super().__init__(n=1, title=self.title, question=self.question, title_color=self.title_color)

class PartThreeSurjections(PartScene):
    def __init__(self):
        self.n = 3
        self.title = "Surjections"
        self.question = "What exactly is a Surjection?"
        self.title_color = DARK_BLUE

        super().__init__(n=1, title=self.title, question=self.question, title_color=self.title_color)

class PartFourBijections(PartScene):
    def __init__(self):
        self.n = 1
        self.title = "Bijections"
        self.question = "What exactly is a Bijection?"
        self.title_color = DARK_BLUE

        super().__init__(n=1, title=self.title, question=self.question, title_color=self.title_color)

#FUNCTIONS
class FunctionDiagram(Scene):
    def construct(self):
        diagram = VGroup()

        #Creation of Domain
        dellipse = Ellipse(width=3.0, height=6.0, color=A_BLUE).shift(LEFT*3)
        self.play(Write(dellipse))
        x_s = [MathTex(f"x_{i}").shift(UP*3 + i * DOWN + LEFT*3) for i in range(1, 5)]
        for var in x_s:
            self.play(Write(var))
            diagram.add(var)
        self.wait()

        #Creation of Codomain
        cellipse = Ellipse(width=3.0, height=6.0, color=A_RED).shift(RIGHT*3)
        self.play(Write(cellipse))
        y_s = [MathTex(f"y_{i}").shift(UP*3 + i * DOWN + RIGHT*3) for i in range(1, 6)]
        for var in y_s:
            self.play(Write(var))
            diagram.add(var)

        #f(x) mapping
        f_x = MathTex(r"f: X \to Y").shift(UP*3)
        self.play(Write(f_x))
        self.wait()

        for i in range(2):
            arrow = Arrow(x_s[i].get_center(), y_s[i].get_center())
            diagram.add(arrow)

            self.play(Write(arrow))

        #Manually Cross Arrows 3 & 4
        arrow_tf = Arrow(x_s[2].get_center(), y_s[3].get_center())
        arrow_ft = Arrow(x_s[3].get_center(), y_s[2].get_center())
        diagram.add(arrow)

        self.play(Write(arrow_tf), Write(arrow_ft))

        self.wait()

        #Denotation of Domain & Codomain
        dbrace = Brace(dellipse, direction=UP).get_text("Domain").next_to(dellipse, UP)
        cbrace = Brace(cellipse, direction=UP).get_text("Codomain").next_to(cellipse, UP)
        self.add(dbrace, cbrace)
        self.wait()
        #Introduction of range

        rellipse = Ellipse(width=3.0, height=6.0, color=RED_B, fill_color=RED_B, fill_opacity=0.6).scale(0.8).align_to(cellipse, UP).shift(RIGHT*3)
        rbrace = Brace(rellipse, direction=RIGHT).get_text("Range")

        self.play(Write(rellipse), Write(rbrace))
        self.wait()

class VerticalLineTest(Scene):

    def construct(self):
        axes = Axes(x_range = [-5, 5.01, 1], y_range = [-5, 5.01, 1],
        x_length = 10, y_length = 10,
        axis_config = {"include_tip": True, "numbers_to_include": np.arange(-5, 5, 2)}).add_coordinates()
        #graph = axes.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 10])

        self.play(DrawBorderThenFill(axes.scale(0.75)))
        #self.play(Write(graph))

        self.wait()
        graphs = [lambda x: np.sin(x), lambda x: np.cos(x)]


        def test_graph(func):
            t = ValueTracker(-4.9)

            initial_point = [axes.coords_to_point(t.get_value(), func(t.get_value()))]
            dot = Dot(point=initial_point)
            vertical_line = Line(start=axes.get_bottom(), end=axes.get_top()).move_to([axes.coords_to_point(t.get_value(), 0)])

            dot.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), func(t.get_value()))))
            vertical_line.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), 0)))
                
            x_space = np.linspace(*axes.x_range[:1], 5)
            minimum_index = func(x_space).argmin()

            plot = axes.plot(func, color=BLUE, x_range=[-5, 5])

            self.play(Write(plot))
            self.add(dot, vertical_line)
            self.wait()

            self.play(t.animate.increment_value(10), run_time=5)

            checkmark = MathTex(r"\checkmark")
            self.play(Write(checkmark.shift(2*RIGHT + 2*UP)))
            self.play(FadeOut(checkmark, dot, vertical_line, plot))

            self.wait()

        for func in graphs:
            test_graph(func)

        fgraphs = [([0, 2, 0], [0, -2, 0], 3)]


        #Draws a line between two faulty points
        def fslice(loc1, loc2, fadeout=1):

            inter_1 = Dot(point=[axes.coords_to_point(loc1[0], loc1[1])], color=YELLOW)
            inter_2 = Dot(point=[axes.coords_to_point(loc2[0], loc2[1])], color=YELLOW)

            vertical_line = Line(start=axes.get_bottom(), end=axes.get_top(), color=YELLOW).move_to((inter_1.get_center() + inter_2.get_center())/2)

            self.play(Write(inter_1), Write(inter_2))

            self.play(FadeIn(vertical_line))

            checkmark = Tex(r"x", font_size=30)
            self.play(Write(checkmark.shift(2*RIGHT + 2*UP)))
            return (checkmark, inter_1, inter_2, vertical_line)

            
        
        #Faulty Circle
        cslice = fslice(fgraphs[0][0], fgraphs[0][1], 2)

        circle = Circle(radius=1).move_to((cslice[1].get_center() + cslice[2].get_center())/2)
        self.play(Write(circle))
        
        for ret in cslice:
            self.play(FadeOut(ret))
        self.play(FadeOut(circle))

        self.wait()

class FunctionNotations(Scene):

    def construct(self):
        Tex.set_default(font_size=30)

        introduction = Tex("A function satisfies Two Definitions")

        self.play(Write(introduction.to_edge(UP)))
        self.wait()

        fdef_one = Tex(r"$\cdot$ For any $x \in X$ there exists $y \in Y$ such that $(x, y) \in G$, where $G$ is the Number Plane. Symbolically: ").next_to(introduction, DOWN, buff=2)
        sfdef_one = Tex(r"$\forall x \in X, \exists y \in Y : (x, y) \in G$").next_to(fdef_one, DOWN).align_to(fdef_one, LEFT).shift(RIGHT)

        fdef_two = Tex(r"$\cdot$ For any $x \in X$ and any $y_1, y_2 \in Y$, if $(x, y_1), (x, y_2) \in G$, then $y_1 = y_2$. Symbolically: ").next_to(sfdef_one, DOWN).align_to(fdef_one, LEFT)
        sfdef_two = Tex(r"$\forall x \in X, \forall y_1, y_2 \in Y, ((x, y_1) \in G \land (x, y_2) \in G)) \implies (y_1 = y_2)$").next_to(fdef_two, DOWN).align_to(fdef_two, LEFT).shift(RIGHT)


        self.play(Write(fdef_one), Write(fdef_two))
        
        self.wait()

        self.play(Write(sfdef_one), Write(sfdef_two))

        self.wait()

#INJECTIONS

class InjectionDiagram(Scene):
        def construct(self):
            diagram = VGroup()

            #Creation of Domain
            dellipse = Ellipse(width=3.0, height=6.0, color=A_BLUE).shift(LEFT*3)
            diagram.add(dellipse)
            x_s = [MathTex(f"x_{i}").shift(UP*3 + i * DOWN + LEFT*3) for i in range(1, 5)]
            for var in x_s:
                diagram.add(var)
            self.wait()

            #Creation of Codomain
            cellipse = Ellipse(width=3.0, height=6.0, color=A_RED).shift(RIGHT*3)
            diagram.add(cellipse)
            y_s = [MathTex(f"y_{i}").shift(UP*3 + i * DOWN + RIGHT*3) for i in range(1, 6)]
            for var in y_s:
                diagram.add(var)

            #f(x) mapping
            f_x = MathTex(r"f: X \to Y").shift(UP*3)
            diagram.add(f_x)

            #Manually Cross Arrows 3 & 4

            #Denotation of Domain & Codomain
            dbrace = Brace(dellipse, direction=UP).get_text("Domain").next_to(dellipse, UP)
            #cbrace = Brace(cellipse, direction=UP).get_text("Codomain")
            diagram.add(dbrace)
            #Introduction of range

            rellipse = Ellipse(width=3.0, height=6.0, color=RED_B, fill_color=RED_B, fill_opacity=0.6).scale(0.8).align_to(cellipse, UP).shift(RIGHT*3)
            rbrace = Brace(rellipse, direction=RIGHT).get_text("Range")
            diagram.add(rellipse, rbrace)

            self.play(Write(diagram))

            points_to_test = [[0, 1, 2, 3], [0, 0, 1, 2], [0, 1, 1, 2], [3, 3, 3, 3]]

            def test_injective(mapping):
                """Given a list of y relations, color the arrows that destroy injection"""
                arrows = []
                seen = []

                i = 0

                for destination in mapping:
                    if destination in seen:
                        arrows.append(Arrow(x_s[i].get_center(), y_s[destination].get_center(), color=YELLOW))
                        inj = False
                        i += 1
                    else:
                        arrows.append(Arrow(x_s[i].get_center(), y_s[destination].get_center()))
                        seen.append(destination)
                        i += 1
                    
                inj = len(set(seen)) == len(mapping)#Returns whether the function is injective

                return (inj, arrows)

            for mapping in points_to_test:
                inj_test, returned_arrows = test_injective(mapping)
                not_inj = Tex("IS NOT AN INJECTION").scale(0.5)
                is_inj = Tex("IS AN INJECTION").scale(0.5)
                arrow_group = VGroup()

                for arrow in returned_arrows:
                    self.play(Write(arrow))

                if inj_test == False:
                    self.play(Write(not_inj.next_to(f_x, DOWN)))
                else:
                    self.play(Write(is_inj.next_to(f_x, DOWN)))
                    
                self.wait()
                for arrow in returned_arrows:
                    arrow_group.add(arrow)
                self.play(FadeOut(arrow_group))
                self.remove(not_inj, is_inj)

            self.wait()

class HorizontalLineTest(Scene):
    def construct(self):
        axes = Axes(x_range = [-5, 5.1, 1], y_range = [-5, 5.1, 1],
        x_length = 10, y_length = 10,
        x_axis_config = {"include_tip": True, "numbers_to_include": np.arange(-5, 5.01, 1)},
        y_axis_config={"include_tip": True, "numbers_to_include": np.arange(-5, 5.01, 1)}).add_coordinates()

        

        self.play(DrawBorderThenFill(axes.scale(0.5)))
        #self.play(Write(graph))

        self.wait()
        graphs = [lambda x: x**3, lambda x: np.exp(x), lambda x: np.sinh(x)]


        def approve_graph(func, min_y=-5):
            t = ValueTracker(inversefunc(func, y_values=-5))

            initial_point = [axes.coords_to_point(t.get_value(), func(t.get_value()))]
            
            dot = Dot(point=initial_point)
            horizontal_line = Line(start=axes.get_left(), end=axes.get_right()).move_to([0, min_y, 0])

            dot.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), func(t.get_value()))))
            horizontal_line.add_updater(lambda x: x.move_to(axes.c2p(0, func(t.get_value()))))
                
            x_space = np.linspace(*axes.x_range[:1], 5)
            minimum_index = func(x_space).argmin()
            

            plot = axes.plot(func, color=BLUE, x_range=[max(-5, inversefunc(func, y_values=-5)), inversefunc(func, y_values=5)])

            self.play(Write(plot))
            self.add(dot, horizontal_line)
            self.wait()

            self.play(t.animate.increment_value(inversefunc(func, y_values=5) - inversefunc(func, y_values=-5)), run_time=5)

            checkmark = MathTex(r"\checkmark")
            self.play(Write(checkmark.shift(2*RIGHT + 2*UP)))
            self.play(FadeOut(checkmark, dot, horizontal_line, plot))

            self.wait()

        for func in graphs:
            approve_graph(func, -5)

        #Draws a line between two faulty points
        def fslice(func, loc1, loc2, fadeout=1):
            graph = axes.plot(func, color=BLUE, x_range=[-4, 4])

            inter_1 = Dot(point=[axes.coords_to_point(loc1[0], loc1[1])], color=YELLOW)
            inter_2 = Dot(point=[axes.coords_to_point(loc2[0], loc2[1])], color=YELLOW)

            self.play(FadeIn(graph))

            horizontal_line = Line(start=axes.get_left(), end=axes.get_right(), color=YELLOW).move_to((inter_1.get_center() + inter_2.get_center())/2)

            self.play(Write(inter_1), Write(inter_2), Write(horizontal_line))
            
            self.wait()
            checkmark = Tex(r"x", font_size=30)
            self.play(Write(checkmark.shift(2*RIGHT + 2*UP)))
            self.wait()

            self.play(FadeOut(graph), FadeOut(inter_1), FadeOut(inter_2), FadeOut(horizontal_line), FadeOut(checkmark))
            self.wait(fadeout)


            return (checkmark, inter_1, inter_2, horizontal_line)

        ffuncs = [(lambda x: x**2, [-1, 1], [1, 1]), (lambda x: 0.3*((x-1)**5 + (x-1)**4 - 3*(x-1)**3 + 2), [-0.8, 3.329], [2.732, 3.329])]

        for func in ffuncs:
            fslice(func[0], func[1], func[2])

            


        self.wait()
    
class InjectionNotation(Scene):

    def construct(self):
        Tex.set_default(font_size=30)

        introduction = Tex("A function is injective if:")

        self.play(Write(introduction.to_edge(UP)))
        self.wait()

        fdef_one = Tex(r"$\forall x_1, x_2 \in X : x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$").next_to(introduction, DOWN)

        fdef_two = Tex(r"This is equivalent to saying the following: ").next_to(fdef_one, DOWN).align_to(fdef_one, LEFT)
        sfdef_two = Tex(r"$\forall x_1, x_2 \in X : f(x_1) = f(x_2) \implies x_1 = x_2$").next_to(fdef_two, DOWN).align_to(fdef_two, LEFT).shift(RIGHT)

        self.play(Write(fdef_one), Write(fdef_two), Write(sfdef_two))

        self.wait()

#SURJECTIONS

class SurjectiveFunctionDiagram(Scene):
    def construct(self):
        diagram = VGroup()

        #Creation of Domain
        dellipse = Ellipse(width=3.0, height=6.0, color=A_BLUE).shift(LEFT*3)
        self.play(Write(dellipse))
        x_s = [MathTex(f"x_{i}").shift(UP*3 + i * DOWN + LEFT*3) for i in range(1, 6)]
        for var in x_s:
            self.play(Write(var))
            diagram.add(var)
        self.wait()

        #Creation of Codomain
        cellipse = Ellipse(width=3.0, height=6.0, color=A_RED).shift(RIGHT*3)
        self.play(Write(cellipse))
        y_s = [MathTex(f"y_{i}").shift(UP*3 + i * DOWN + RIGHT*3) for i in range(1, 6)]
        for var in y_s:
            self.play(Write(var))
            diagram.add(var)

        #Denotation of Domain & Codomain
        dbrace = Brace(dellipse, direction=UP).get_text("Domain").next_to(dellipse, UP)
        cbrace = Brace(cellipse, direction=UP).get_text("Codomain").next_to(cellipse, UP)
        rcbrace = Brace(cellipse, direction=UP).get_text("Range = Codomain!").next_to(cellipse, UP)

        self.play(Write(dbrace), Write(cbrace))
        self.wait()
        #Introduction of range

        rellipse = Ellipse(width=3.0, height=6.0, color=RED_B, fill_color=RED_B, fill_opacity=0.6).scale(0.8).align_to(cellipse, UP).shift(RIGHT*3)
        rcellipse = Ellipse(width=3.0, height=6.0, color=A_RED, fill_color = RED_B, fill_opacity=0.6).shift(RIGHT*3)
        rcellipse.z_index = y_s[0].z_index - 1#Sends to back so there is no overlap

        rbrace = Brace(rellipse, direction=RIGHT).get_text("Range")
        self.play(Write(rellipse), Write(rbrace))

        #f(x) mapping
        f_x = MathTex(r"f: X \to Y").shift(UP*3)
        self.play(Write(f_x))
        self.wait()

        for i in range(2):
            arrow = Arrow(x_s[i].get_center(), y_s[i].get_center())
            diagram.add(arrow)

            self.play(Write(arrow))

        #Manually Cross Arrows 3 & 4
        arrow_tf = Arrow(x_s[2].get_center(), y_s[3].get_center())
        arrow_ft = Arrow(x_s[3].get_center(), y_s[2].get_center())
        arrow_ff = Arrow(x_s[4].get_center(), y_s[4].get_center())
        diagram.add(arrow_tf, arrow_ft, arrow_ff)

        self.play(Write(arrow_tf), Write(arrow_ft), Write(arrow_ff))

        #Transformation of Range is the Codomain
        self.wait()
        self.play(ReplacementTransform(rbrace, rcbrace), ReplacementTransform(cbrace, rcbrace))
        self.play(ReplacementTransform(rellipse, rcellipse))


        self.wait()
    
class SurjectiveNotation(Scene):
    def construct(self):
        Tex.set_default(font_size=30)

        introduction = Tex("A function is surjective if:")

        self.play(Write(introduction.to_edge(UP)))
        self.wait()

        fdef_one = Tex(r"$\forall y \in Y, \exists x \in X : y = f(x)$").next_to(introduction, DOWN)

        self.play(Write(fdef_one))

        self.wait()

#BIJECTIONS

class BijectionNotation(Scene):
        def construct(self):
            Tex.set_default(font_size=30)

            introduction = Tex("A function is bijective if it is both injective and surjective, i.e.: ")

            self.play(Write(introduction.to_edge(UP)))
            self.wait()

            fdef_one = Tex(r"$\forall y \in Y, \exists ! x \in X : y = f(x)$").next_to(introduction, DOWN)

            self.play(Write(fdef_one))

            self.wait()

class Conclusion(Scene): 
    def construct(self):
        text = Text("Thanks for Watching!").scale(2)
        self.play(Write(text))
        self.wait()




            

        




        




        

    


