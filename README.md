# Plotting for LaTeX is EZ

This is a utility to make it easy to generate plots that look nice in academic papers which follow a LaTeX template.

It serves as an interface for `matplotlib` that aims to achieve plug-and-play plotting, abstracting away much of the boilerplate-type code used to control stylistic aspects of the plots (such as sizing and fonts), allowing for easy creation of professional, aesthetically-pleasing plots.

The workflow design for this package is to define how much vertical space your figure will take within a column and generate a figure within those bounds, rather than the common workflow of designing a figure and later trying to fit it into the paper.
This not only prevents illegible figures due to shrinking fonts too small while resizing, but also makes fitting the paper to a page limit easier, as it is possible to define how much height your figure will take ahead of time, allowing you to then work on generating a figure that fits inside that size.

## Basic Usage

The package defines a set of supported conference templates (listed in `plez/plotters.py`).
These can then be used as a context manager to generate a figure via access to `plt` and `fig` methods, which correspond to the typical `import matplotlib.pyplot as plt` and `fig = plt.figure()` constructions.
Upon closure of the context manager, the package will save the plot in `.pdf` format in the appropriate size to be inserted into a LaTeX document without resizing, i.e. `\includegraphics[width=\columnwidth]{plot.pdf}`.


Here is some example usage:
```
import numpy as np

from plez import IEEE_Conference_Plotter

with IEEE_Conference_Plotter("plot.pdf", height=0.9) as P:

    P.fig.suptitle(r"\textbf{HERE IS A TITLE}")

    P.plt.xlabel(r"\textit{italic} text: 1.3\% math: $\pi 1.3\% \mathbf{X}\in\mathbb{C}^{L\times R}$")

    P.plt.scatter(np.random.rand(10), np.random.rand(10))

    P.fig.tight_layout()
```
You can also use this construction, which is useful when you want to generate multiple plots with the same parameters.
```
import numpy as np

from plez import IEEE_Conference_Plotter

plotter = IEEE_Conference_Plotter(height_unit="ratio", col_span=1)

with plotter("plot.pdf", height=0.9) as P:

    P.fig.suptitle(r"\textbf{HERE IS A TITLE}")

    P.plt.xlabel(r"\textit{italic} text: 1.3\% math: $\pi 1.3\% \mathbf{X}\in\mathbb{C}^{L\times R}$")

    P.plt.scatter(np.random.rand(10), np.random.rand(10))

    P.fig.tight_layout()
```

These examples generate `plot.pdf`, which matches the IEEE conference style and single-column width, and is 0.9 times as tall as it is wide.

## Installation

To install, do `pip install .`, or `pip install -e .` for an editable version, which can be useful for adding new templates. 

The package also requires a `pdflatex` install and possibly `lualatex` and/or `xelatex` as well.

## API Information

The following named arguments are available:
- **height** This is the height of the figure, in units defined by **height_unit**. Default is "ratio", i.e. proportional to the column width.
- **height_unit** This is the unit for the **height** parameter. Can be "ratio", "in", or "cm". Ratio is as a proportion of the column width.
- **col_span** This is either 1 or 2, depending on if you want your figure to span a single column or be a multi-column figure.
- **scale** This scales the canvas. If for some reason you need to generate a figure smaller than a column (e.g. subfigures), set **scale** equal to the fraction of `\columwidth` used in the LaTeX code.
- **style** If you have an mplstyle file, you can use it here and it will be applied, with LaTeX template-relevant parameters overwritten.
- **extra_preamble** A list of LaTeX lines to be included in the preamble, e.g. `[r"\usepackage{amsmath}"]`

## Helpful Tips and Tricks
### Getting sizes in LaTeX

`\the\columnwidth` and `\the\linewidth` print the respective parameters in pts.

If you want to determine a font size, the following macro is useful:
```
\makeatletter
\newcommand\thefontsize[1]{{\f@size pt}}
\makeatother
```
You can then use `\thefontsize{}` to print the current font size.
