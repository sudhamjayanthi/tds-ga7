import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    # Add interactive widgets
    slider = mo.ui.slider(1, 100)

    return (slider,)


@app.cell
def _(mo, slider):
    # Create dynamic Markdown
    mo.md(f"{slider} {"🟢" * slider.value}")
    return


@app.cell
def _():
    # Your email (23f3003060@ds.study.iitm.ac.in) as a comment
    return


if __name__ == "__main__":
    app.run()
