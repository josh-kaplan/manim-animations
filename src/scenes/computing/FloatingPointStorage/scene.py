
import numpy as np
from manim import *


class FloatingPointStorage(Scene):

    def construct(self):

        # 32 bit label
        label = Text('32-bit Floating Point Number').scale(1)
        label.set_color(WHITE)
        label.shift(2.65*UP)

        # Initial table
        block = FloatBlock()
        t1 = block.table
        bit_labels = block.get_bit_labels()

        # Sign bit
        t2 = block.highlight_range(31, 32, color=BLUE)
        l2 = block.get_segment_label('Sign', 31, 32, color=BLUE)

        # Exponent bit
        t3 = block.highlight_range(23, 31, color=GREEN)
        l3 = block.get_segment_label('Exponent', 23, 31, color=GREEN)

        # Fraction bit
        t4 = block.highlight_range(0, 23, color=RED)
        l4 = block.get_segment_label('Fraction', 0, 23, color=RED)


        # 64 bit label
        label_64 = Text('64-bit Floating Point Number').scale(1)
        label_64.set_color(WHITE)
        label_64.shift(2.65*UP)

        # Initial table
        block64 = FloatBlock(bits=64, scale=0.125)
        t1_64 = block64.table
        bit_labels_64 = block64.get_bit_labels()

        # Sign bit
        t2_64 = block64.highlight_range(63, 64, color=BLUE)
        l2_64 = block64.get_segment_label('Sign', 63, 64, color=BLUE)

        # Exponent bit
        t3_64 = block64.highlight_range(52, 63, color=GREEN)
        l3_64 = block64.get_segment_label('Exponent', 52, 63, color=GREEN)

        # Fraction bit
        t4_64 = block64.highlight_range(0, 52, color=RED)
        l4_64 = block64.get_segment_label('Fraction', 0, 52, color=RED)


        ### Animate ###


        # Add the block
        self.play(GrowFromCenter(t1), GrowFromCenter(label))

        # Add the bit labels
        for i in bit_labels[::-8]:
            self.play(GrowFromCenter(i), run_time=0.4)
        self.play(GrowFromCenter(bit_labels[0]))

        # Add highlights and labels
        self.play(FadeTransform(t1,t2), FadeIn(l2))
        self.wait(1)
        self.play(FadeTransform(t2,t3), FadeIn(l3))
        self.wait(1)
        self.play(FadeTransform(t3,t4), FadeIn(l4))
        self.wait(1)

        # Add the bit labels
        fade_out = [ i for i in bit_labels[::-8] ]
        fade_out.append(bit_labels[0])
        fade_out.append(l2)
        fade_out.append(l3)
        fade_out.append(l4)
        fade_out = [ FadeOut(i) for i in fade_out ]
        self.play(*fade_out)

        self.play(FadeTransform(t4, t1_64), Transform(label, label_64))

        # Add the bit labels
        for i in bit_labels_64[::-8]:
            self.play(GrowFromCenter(i), run_time=0.4)
        self.play(GrowFromCenter(bit_labels_64[0]))

        self.play(FadeTransform(t1_64,t2_64), FadeIn(l2_64))
        self.wait(1)
        self.play(FadeTransform(t2_64,t3_64), FadeIn(l3_64))
        self.wait(1)
        self.play(FadeTransform(t3_64,t4_64), FadeIn(l4_64))
        self.wait(1)


class FloatBlock:

    def __init__(self, bits=32, bins=None, scale=0.25):
        self.bits = bits

        if bins is not None:
            self.binary = bins
        else:
            rand_bit = lambda: np.random.randint(0,2)
            self.binary = [ str(rand_bit()) for i in range(self.bits) ]

        t1 = IntegerTable(
            [[int(c) for c in self.binary]],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": WHITE})
        t1.scale(scale)

        self.table = t1
        self.stages = [ t1 ]


    def get_bit(self, i):
        return (1, self.bits - i)


    def get_bit_cell(self, i):
        return self.table.get_cell(pos=(1, self.bits - i))


    def get_bit_labels(self):
        bit_labels = []
        for i in range(self.bits-1, -1, -1):
            cell = self.table.get_cell(pos=(1, self.bits - i))
            bit_label = Text(r"{}".format(i)).scale(0.2)
            bit_label.set_color('#777777')
            bit_label.next_to(cell, 0.65*DOWN)
            bit_labels.append(bit_label)
        return bit_labels


    def get_segment_label(self, text, start, end, color=BLUE, scale=0.5):
        # Compute the middle bit
        hi = end
        lo = start
        bit = round(np.floor((hi-lo) / 2) + lo)

        # Get the cell for that bit
        cell = self.get_bit_cell(bit)

        # Create and return the label
        label = Text(text).scale(scale)
        label.set_color(color)
        label.next_to(cell, 0.65*UP)
        return label

    def highlight_range(self, start, end, color=BLUE):
        # Create a copy of the tables
        t = self.stages[-1].copy()

        # Highlight sign bit
        for i in range(start, end):
            bit = self.get_bit(i)
            t.add_highlighted_cell(bit, color=color)

        # Append stage and return
        self.stages.append(t)
        return t
