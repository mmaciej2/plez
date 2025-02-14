from .core import Plotter
from . import styles

__all__ = [
    "IEEE_Conference_Plotter",
    "ICASSP2024_Plotter",
    "ICASSP2025_Plotter",
    "Interspeech2024_Plotter",
    "Interspeech2025_Plotter",
    "WASPAA2025_Plotter",
    "Beamer_Gemini_Plotter",
]

PT = 1 / 72.27  # can be found with \the\columnwidth or \the\textwidth
IN = 1.0
CM = 1 / 2.54
MM = 1 / 25.4

##### General IEEE.cls document types #####

class IEEE_Conference_Plotter(Plotter):
    def __init__(self, *args, pt=10, small=True, **kwargs):
        self.widths=[252.0*PT, 516.0*PT]
        self.update_style_params({"font.family": "serif"})
        # The IEEE template uses a smaller font for captions and tables. The
        # default behavior is to use this smaller font, as it is assumed that
        # people are trying to conserve space in a conference paper, and this
        # serves as the "minimum acceptable fontsize". But, you can enable
        # small=False to use the font size of the document body.
        if small:
            self.update_style_params(styles.fontsize(8 if pt<11 else 9))
        else:
            self.update_style_params(styles.fontsize(pt))
        kwargs["preamble"] = [
            r"\renewcommand{\sfdefault}{phv}",
            r"\renewcommand{\rmdefault}{ptm}",
            r"\renewcommand{\ttdefault}{pcr}",
            r"\usepackage{amsmath,amssymb,amsfonts}",
        ]
        super().__init__(*args, **kwargs)

##### ICASSP #####

class ICASSP2024_Plotter(Plotter):
    def __init__(self, *args, **kwargs):
        self.widths=[3.39*IN, 7.0*IN]
        self.update_style_params({"font.family": "serif"})
        self.update_style_params(styles.fontsize(9))
        kwargs["preamble"] = [
            r"\renewcommand{\sfdefault}{phv}",
            r"\renewcommand{\rmdefault}{ptm}",
            r"\renewcommand{\ttdefault}{pcr}",
            r"\usepackage{amsmath,amssymb}",
        ]
        super().__init__(*args, **kwargs)

class ICASSP2025_Plotter(IEEE_Conference_Plotter):
    pass

##### Interspeech #####

class Interspeech2024_Plotter(Plotter):
    def __init__(self, *args, small=False, **kwargs):
        self.widths=[80*MM, 170*MM]
        self.update_style_params({"font.family": "serif"})
        self.update_style_params(styles.fontsize(8 if small else 9))
        kwargs["preamble"] = [
            r"\usepackage{amssymb,amsmath,bm}",
            r"\renewcommand{\sfdefault}{phv}",
            r"\renewcommand{\rmdefault}{ptm}",
            r"\renewcommand{\ttdefault}{pcr}",
        ]
        super().__init__(*args, **kwargs)

class Interspeech2025_Plotter(Interspeech2024_Plotter):
    pass

##### WASPAA #####

class WASPAA2025_Plotter(IEEE_Conference_Plotter):
    pass

##### Beamer Gemini #####

class Beamer_Gemini_Plotter(Plotter):
    def __init__(self, *args, colwidth=0.3*120, sepwidth=0.025*120, small=False, **kwargs):
        self.widths=[colwidth*(n_col+1)*CM + sepwidth*n_col*CM for n_col in range(3)]
        kwargs["texsystem"] = "lualatex"
        self.update_style_params({"font.family": "sans-serif"})
        # The beamer gemini template uses a smaller font for captions than the
        # body. You can enable small=True to use this smaller font, but the
        # default is the larger font for easily-legible posters.
        self.update_style_params(styles.fontsize(20.74 if small else 24.88))
        kwargs["preamble"] = [
            r"\usepackage[T1]{fontenc}",
            r"\usepackage{lmodern}",
            r"\usepackage{amsmath,amssymb}",
            r"\usepackage{fontspec}",
            r"\newfontfamily\Raleway[Ligatures=TeX]{Raleway}",
            r"\newfontfamily\Lato[Ligatures=TeX]{Lato}",
            r"\setsansfont{Lato}[UprightFont=*-Light,ItalicFont=*-LightItalic,BoldFont=*-Regular,BoldItalicFont=*-Italic]",
        ]
        super().__init__(*args, **kwargs)
