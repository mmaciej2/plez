from importlib.resources import files
from contextlib import contextmanager

import matplotlib
matplotlib.use('pgf')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pgf import PdfPages

class Plotter:
    def __init__(self,
            *args,
            filename=None,
            height=1.0,
            height_unit="ratio",
            col_span=1,
            scale=1.0,
            style=None,
            preamble=None,
            extra_preamble=[],
            rcfonts=False,
            texsystem="pdflatex",
        ):

        assert len(args) <= 1
        try:
            self.filename = args[0]
        except IndexError:
            self.filename = filename

        self._figsize = self.parse_plot_configs(height, height_unit, col_span, scale)

        self._style = style
        self._rcfonts = rcfonts
        self._preamble = preamble
        self._extra_preamble = extra_preamble
        self._texsystem = texsystem

        self.plt = plt

    def parse_plot_configs(self, height, height_unit, col_span, scale):
        assert height_unit in ["ratio", "in", "cm"], 'Only "ratio", "in", and "cm" are valid units'
        assert col_span in list(range(1, len(self.widths)+1)), "Invalid number of columns for template"
        width = self.widths[col_span-1] * scale
        if height_unit == "ratio":
            return (width, width*height)
        elif height_unit == "in":
            return (width, height)
        elif height_unit == "cm":
            return (width, height/2.54)

    def configure_backend(self):
        self.plt.style.use(files("plez.mplstyle") / self._style)
        self.plt.rcParams.update({
            "pgf.rcfonts": self._rcfonts,
            "pgf.preamble": "\n".join(self._preamble + self._extra_preamble),
            "pgf.texsystem": self._texsystem,
        })

    def __enter__(self):
        self.configure_backend()
        self.fig = self.plt.figure(figsize=self._figsize)
        self.pdf = PdfPages(self.filename)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.pdf.savefig()
        self.pdf.close()

    @contextmanager
    def __call__(self, filename, height=1.0, height_unit="ratio", col_span=1, scale=1.0):
        figsize = self.parse_plot_configs(height, height_unit, col_span, scale)
        self.configure_backend()
        class PDF_Figure:
            plt = self.plt
            fig = self.plt.figure(figsize=figsize)
            pdf = PdfPages(filename)
        pdf_figure = PDF_Figure()
        try:
            yield pdf_figure
        finally:
            pdf_figure.pdf.savefig()
            pdf_figure.pdf.close()
