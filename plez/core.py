from importlib.resources import files

import matplotlib
matplotlib.use('pgf')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pgf import PdfPages

plt.rcParams.update({
    "text.usetex": True,
    "pgf.rcfonts": False,
})

class Plotter:
    def __init__(self,
            filename,
            height=1.0,
            height_unit="ratio",
            col_span=1,
            style=None,
            preamble=None,
            texsystem="pdflatex",
        ):

        self.filename = filename

        # Compute dimensions of figure
        assert height_unit in ["ratio", "in", "cm"], 'Only "ratio", "in", and "cm" are valid units'
        assert col_span in list(range(1, len(self.widths)+1)), "Invalid number of columns for template"
        width = self.widths[col_span-1]
        if height_unit == "ratio":
            self.figsize = (width, width*height)
        elif height_unit == "in":
            self.figsize = (width, height)
        elif height_unit == "cm":
            self.figsize = (width, height*CM)

        # Configure the style
        plt.style.use(files("plez.mplstyle") / style)
        plt.rcParams.update({
            "pgf.texsystem": texsystem,
            "pgf.preamble": "\n".join(preamble)
        })

        self.plt = plt

    def __enter__(self):
        self.fig = self.plt.figure(figsize=self.figsize)
        self.pdf = PdfPages(self.filename)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.pdf.savefig()
        self.pdf.close()
