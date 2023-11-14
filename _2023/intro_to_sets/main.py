from manim import *

        
class Introduction(Scene):
    def construct(self):
        question = Tex("So... what exactly is a set?").shift(UP)
        self.play(FadeIn(question))
        self.wait(2)

        #Remove question, shift tex up, gives examples
        self.play(FadeOut(question))

        text1 = Tex("A set is simply a collection of things, and we define a set using a ':=' symbol. For example$\dots$", font_size=35).shift(UP)
        
        self.play(FadeIn(text1))
        examples = Tex("E:= \{2, 4, 6, 8, \dots \}, ","$\mathbb{N}:= \{1, 2, 3, \dots\}, $",r"$ D:= \{x \text{ }|\text{ } x \text{ is a dog}\} = \{\text{Bulldog}, \text{Rottweiler}, \text{Labrador}\}, $", r" P:= $\{$George Washington, Abraham Lincoln, Thomas Jefferson,$\dots\}$", font_size=15).scale(2)
        animations = [FadeIn(examples[i]) for i in range(len(examples))]
        self.play(AnimationGroup(*animations, lag_ratio=0.1))
        self.wait(10)
        #
        self.play(FadeOut(text1), FadeOut(examples))

        self.wait(3)

class Examples(Scene):
    def construct(self):

        fruits = Tex(r"$F:= \{$apple$,$ ", r"banana, ", r"orange\}")
        
        x_in_X = Tex(r"We say banana is in the set $F$ by writing: banana $\in$ $F$")
        framebox1 = SurroundingRectangle(fruits[1], color=PURPLE_A, buff = 0.1)

        x_not_in_X = Tex(r"We say rice is in not the set $F$ by writing: rice $\not \in$ $F$")
        framebox2 = SurroundingRectangle(fruits[1], color=PURPLE_A, buff = 0.1)

                #joined_text = VGroup(fruits, x_in_X, framebox1)
        #self.wait(2)
        #self.play(Transform(joined_text, joined_text.to_corner(UP)))
        #self.wsait(1)


        self.play(Write(fruits))
        
        self.wait(3)
        self.play(Write(x_in_X.next_to(fruits, DOWN)))
        self.play(Write(framebox1))
        self.wait(3)
        self.play(Uncreate(framebox1))
        self.wait(2)
        self.play(Write(x_not_in_X.next_to(x_in_X, DOWN)))
        self.wait(4)

class Digression(Scene):
    def construct(self):

        empty_set = Tex(r"$1.\text{ } \varnothing := \{\}$")
        self.play(Write(empty_set.to_corner(UP)))
        self.wait(5)
        intervals = Tex(r"$2. \text{ }(0, 1) \cap (2, 3) = \varnothing$")
        self.play(Write(intervals.next_to(empty_set, DOWN)))

        power_set = Tex(r"$\frak{P}$", "$(\{x, y, z\})$" "$:= \{\{\}$ ", "$, \{x\}, \{y\}, \{z\}, \{x, y\}, \{x, z\}, \{y, z\}, \{x, y, z\}\}$")
        framebox2 = SurroundingRectangle(power_set[0], color=PURPLE_A, buff = 0.1)

        self.play(Write(power_set.shift(DOWN)))
        self.wait()
        self.play(Write(framebox2.shift(DOWN)))
        self.wait()
        self.play(Unwrite(framebox2))
        self.wait(3)

class Statements(Scene):
    def construct(self):
        introtext = Text("We can now make a few statements...", font_size=DEFAULT_FONT_SIZE*0.5)
        self.play(Write(introtext.to_corner(LEFT+UP)))
        self.wait(1)
        self.play(Unwrite(introtext))

        self.wait(2)

        title = Tex(R"Example Sets: $A:= \{1, 2, 3, 4, 5\}, B:= \{1, 2, 3, 4, 5\}, C:= \{1, 2, 3\}, D:= \{4, 5\}$", font_size=40,color=PURPLE_B)
        self.play(Write(title.to_edge(UP)))

        self.wait(4)

        terms = [
        Tex(R"Equivalent: $A = B$"),
        Tex(R"Subset: $C \subset A$"),
        Tex(R"Intersection: $A \cap C = \{1, 2, 3\}$"),
        Tex(R"Difference: $A \setminus C = D$"),
        Tex(R"Union: $C \cup D = \{1, 2, 3, 4, 5\}$"),
        Tex(R"Disjoint: $C \cap D = \varnothing$")]
        animations = [Write(terms[i].to_corner(LEFT + DOWN).shift(UP*i)) for i in range(len(terms))]
        print(animations)

        self.play(AnimationGroup(*animations))
        self.wait(5)

class Conclusion(Scene): 
    def construct(self):
        text = Text("Thanks for Watching!").scale(2)
        self.play(Write(text))
        self.wait(10)