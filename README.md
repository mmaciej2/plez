# Plotting for LaTeX is EZ

This is a utility to make it easy to generate plots that look nice in papers, which follow a LaTeX template.

Here is some example usage:
The basic usage is to import the appropriate plotter and wrap a `with` block with the filename you intend to save to. The plotter will have `fig` and `plt` methods corresponding to the typical `matplotlib` convention.

```
import numpy as np

from plez import IEEE_Plotter

with IEEE_Plotter("plot.pdf", height=0.9, height_unit="ratio", col_span=1) as P:

    P.fig.suptitle(r"\textbf{HERE IS A TITLE}")

    P.plt.xlabel(r"\textbf{Fig. 1}. 9 figure \textit{italic} text: 1.3\% math: $\pi 1.3\% \mathbf{X}\in\mathbb{C}^{L\times R}$")

    P.plt.scatter(np.random.rand(10), np.random.rand(10))

    P.fig.tight_layout()
```
This will automatically generate `plot.pdf`, which matches the IEEE style and single-column width, and is 0.9 times as tall as it is wide.
