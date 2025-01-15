import matplotlib
matplotlib.use('pgf')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pgf import PdfPages

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times"],
    "text.usetex": True,
    "pgf.texsystem": "pdflatex",
    "pgf.rcfonts": False,
    "pgf.preamble": "\n".join([
         r"\usepackage{times}",
         r"\usepackage{amsmath}",
         r"\usepackage{amssymb}",
    ]),
    "xtick.direction": "in",
    "xtick.labelsize": 9,
    "ytick.direction": "in",
    "ytick.labelsize": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "figure.labelsize": 9,
    "figure.titlesize": 9,
    "font.size": 9,
    "legend.fontsize": 9,
    "legend.title_fontsize": 9,
})

class Plotter:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.pdf = PdfPages(self.filename)
        self.plt = plt
        self.fig = self.plt.figure(figsize=(3.39, 3))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.pdf.savefig()
        self.pdf.close()
