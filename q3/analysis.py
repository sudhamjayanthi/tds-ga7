import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    # Cell 1: Import marimo UI module
    # Outputs: mo (marimo module for UI components)
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    # Cell 2: Create interactive slider widget
    # Inputs: mo (marimo module from Cell 1)
    # Outputs: slider (interactive slider widget with range 1-100)
    slider = mo.ui.slider(1, 100)

    return (slider,)


@app.cell
def _(mo, slider):
    # Cell 3: Generate dynamic markdown display
    # Inputs: mo (marimo module from Cell 1), slider (widget from Cell 2)
    # Outputs: Markdown display with slider value and green circles
    # Data flow: slider.value -> markdown string -> visual output
    mo.md(f"{slider} {"🟢" * slider.value}")
    return


@app.cell
def _():
    # Cell 4: Email identifier comment
    # Inputs: None
    # Outputs: None
    # Your email (23f3003060@ds.study.iitm.ac.in) as a comment
    return


if __name__ == "__main__":
    app.run()
