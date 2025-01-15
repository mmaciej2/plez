from importlib.resources import files

import matplotlib
matplotlib.use('pgf')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pgf import PdfPages

plt.rcParams.update({
    "text.usetex": True,
    "pgf.texsystem": "pdflatex",
    "pgf.rcfonts": False,
    "pgf.preamble": "\n".join([
         r"\usepackage{times}",
         r"\usepackage{amsmath}",
         r"\usepackage{amssymb}",
    ]),
})

class Plotter:
    def __init__(self, filename):
        plt.style.use(files("plez.mplstyle") / "IEEE.mplstyle")
        self.filename = filename

    def __enter__(self):
        self.pdf = PdfPages(self.filename)
        self.plt = plt
        self.fig = self.plt.figure(figsize=(3.39, 3))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.pdf.savefig()
        self.pdf.close()
