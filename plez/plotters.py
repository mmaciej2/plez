from .core import Plotter

__all__ = [
    "IEEE_Conference_Plotter",
    "ICASSP2024_Plotter",
    "ICASSP2025_Plotter",
    "Interspeech2024_Plotter",
    "Interspeech2025_Plotter",
    "WASPAA2025_Plotter",
]

PT = 1 / 72.27  # can be found with \the\columnwidth or \the\textwidth
IN = 1.0
CM = 1 / 2.54
MM = 1 / 25.4

##### General IEEE.cls document types #####

class IEEE_Conference_Plotter(Plotter):
    def __init__(self, filename, pt=10, **kwargs):
        self.widths=[252.0*PT, 516.0*PT]
        kwargs["style"] = f"serif{8 if pt<11 else 9}pt.mplstyle"
        kwargs["preamble"] = [
            r"\renewcommand{\sfdefault}{phv}",
            r"\renewcommand{\rmdefault}{ptm}",
            r"\renewcommand{\ttdefault}{pcr}",
            r"\usepackage{amsmath,amssymb,amsfonts}",
        ]
        super().__init__(filename, **kwargs)

##### ICASSP #####

class ICASSP2024_Plotter(Plotter):
    def __init__(self, filename, **kwargs):
        self.widths=[3.39*IN, 7.0*IN]
        kwargs["style"] = "serif9pt.mplstyle"
        kwargs["preamble"] = [
            r"\renewcommand{\sfdefault}{phv}",
            r"\renewcommand{\rmdefault}{ptm}",
            r"\renewcommand{\ttdefault}{pcr}",
            r"\usepackage{amsmath,amssymb}",
        ]
        super().__init__(filename, **kwargs)

class ICASSP2025_Plotter(ICASSP2024_Plotter):
    pass

##### Interspeech #####

class Interspeech2024_Plotter(Plotter):
    def __init__(self, filename, **kwargs):
        self.widths=[80*MM, 170*MM]
        kwargs["style"] = "serif9pt.mplstyle"
        kwargs["preamble"] = [
            r"\usepackage{amssymb,amsmath,bm}",
            r"\renewcommand{\sfdefault}{phv}",
            r"\renewcommand{\rmdefault}{ptm}",
            r"\renewcommand{\ttdefault}{pcr}",
        ]
        super().__init__(filename, **kwargs)

class Interspeech2025_Plotter(Interspeech2024_Plotter):
    pass

##### WASPAA #####

class WASPAA2025_Plotter(IEEE_Conference_Plotter):
    pass
