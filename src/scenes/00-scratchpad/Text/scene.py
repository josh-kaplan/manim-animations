from manim import *
import numpy as np


class Text01(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        logo_cyan = "#2AB3CB"
        logo_green = "#42B373"
        logo_magenta = "#C5305F"
        logo_black = "#343434"
        logo_white = "#e8e8e8"

        # Built-in templates
        #tex = Tex(r'$x^2 + y^2 = z^2$', tex_template=TexTemplateLibrary.threeb1b, font_size=96)
        
        # Exploring fonts ...
        # These are the ones I like.
        fonts = [
            'apple_chancery',
            'biolinum',
            'chalkboard_se',
            'droid_sans',
            'ecf_augie',
            'electrum_adf',
            'french_cursive',
            'latin_modern_tw',
            'slitex',
            'venturis_adf_fourier_it'            
        ]
        _vshift = [2.75, 2.75] 

        # Build parts
        parts = []
        for i in range(len(fonts)):
            font = fonts[i]
            template = getattr(TexFontTemplates, font)
            tex = Tex(r'$x^2 + y^2 = z^2$', tex_template=template, font_size=64)
            label = Tex(r'$({})$'.format(font), tex_template=template, font_size=18)

            # If col 1
            if i < len(fonts)/2: 
                hshift = 3.25 * LEFT
                vshift = _vshift[0]*UP
                labelvshift = (_vshift[0]-0.55) * UP
                _vshift[0] -= 1.5
            else:
                hshift = 3.25 * RIGHT
                vshift = _vshift[1]*UP
                labelvshift = (_vshift[1]-0.55) * UP
                _vshift[1] -= 1.5
            
            tex.shift(hshift + vshift)
            label.shift(hshift + labelvshift)
            self.add(tex)
            self.add(label)

        tex = Tex(r'$Exploring Fonts$', tex_template=TexFontTemplates.apple_chancery, font_size=64)
        tex.shift(3.6*UP)
        self.add(tex)

