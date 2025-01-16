from .core import Plotter

__all__ = [
    "IEEE_Plotter",
    "Interspeech2025_Plotter",
]

IN = 1.0
CM = 1 / 2.54
MM = 1 / 25.4

class IEEE_Plotter(Plotter):
    def __init__(self, filename, **kwargs):
        self.widths=[3.39*IN]
        kwargs["style"] = "IEEE.mplstyle"
        kwargs["preamble"] = [
            r"\usepackage{times}",
            r"\usepackage{amsmath}",
            r"\usepackage{amssymb}",
        ]
        super().__init__(filename, **kwargs)

class Interspeech2025_Plotter(Plotter):
    def __init__(self, filename, **kwargs):
        self.widths=[80*MM, 170*MM]
        kwargs["style"] = "IEEE.mplstyle"
        kwargs["preamble"] = [
            r"\usepackage{spconf,amssymb,amsmath,graphicx,remove_margins}",
#            r"\usepackage{amssymb,amsmath,bm}",
#            r"\renewcommand{\sfdefault}{phv}",
#            r"\renewcommand{\rmdefault}{ptm}",
#            r"\renewcommand{\ttdefault}{pcr}",
        ]
        super().__init__(filename, **kwargs)
