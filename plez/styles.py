def fontsize(size):
    font_params = [
        "font.size",
        "axes.titlesize",
        "axes.labelsize",
        "xtick.labelsize",
        "ytick.labelsize",
        "legend.fontsize",
        "figure.titlesize",
        "figure.labelsize",
    ]
    return {param: f"{size}" for param in font_params}

def black_color(color):
    color_params = [
        "patch.edgecolor",
        "hatch.color",
        "boxplot.flierprops.color",
        "boxplot.flierprops.markeredgecolor",
        "boxplot.boxprops.color",
        "boxplot.whiskerprops.color",
        "boxplot.capprops.color",
        "text.color",
        "axes.edgecolor",
        "axes.labelcolor",
        "xtick.color",
        "ytick.color",
    ]
    return {param: color for param in color_params}
