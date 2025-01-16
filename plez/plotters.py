from .core import Plotter

__all__ = [
    "IEEE_Plotter"
]

IN = 1.0
CM = 1 / 2.54

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
