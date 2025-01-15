# Plotting for LaTeX is EZ

This is a utility to make it easy to generate plots that look nice in papers, which follow a LaTeX template.

Here is some example usage:
The basic usage is to import the appropriate plotter and wrap a `with` block with the filename you intend to save to. The plotter will have `fig` and `plt` methods corresponding to the typical `matplotlib` convention.

```
import numpy as np

from plez import Plotter

with Plotter("test.pdf") as P:

    P.fig.suptitle(r"\textbf{HERE IS A TITLE}")

    P.plt.xlabel(r"\textbf{Fig. 1}. 9 figure \textit{italic} text: 1.3\% math: $\pi 1.3\% \mathbf{X}\in\mathbb{C}^{L\times R}$")

    P.plt.scatter(np.random.rand(10), np.random.rand(10))

    P.fig.tight_layout()
```
This will automatically generate `test.pdf`.
