import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    # Cell 1: Import marimo UI module and data analysis libraries
    # Outputs: mo (marimo module for UI components), np, pd
    # Data flow: This cell provides foundational modules for subsequent cells
    import marimo as mo
    import numpy as np
    import pandas as pd
    return mo, np, pd


@app.cell
def _(mo, np):
    # Cell 2: Generate sample dataset for analysis
    # Inputs: mo, np, pd (from Cell 1)
    # Outputs: df (DataFrame with sample data), sample_size_slider (interactive widget)
    # Data flow: np.random -> DataFrame creation -> slider widget for sample size control
    np.random.seed(42)

    # Interactive slider to control sample size
    sample_size_slider = mo.ui.slider(10, 1000, value=100, label="Sample Size")


    return (sample_size_slider,)


@app.cell
def _(np, pd, sample_size_slider):
    # Generate sample dataset based on slider value
    n = sample_size_slider.value
    df = pd.DataFrame({
        'x': np.random.normal(0, 1, n),
        'y': np.random.normal(0, 1, n),
        'category': np.random.choice(['A', 'B', 'C'], n)
    })

    return (df,)


@app.cell
def _(df, mo):
    # Cell 3: Calculate correlation and create interactive analysis
    # Inputs: mo (from Cell 1), df, sample_size_slider (from Cell 2)
    # Outputs: correlation_slider (threshold control), analysis display
    # Data flow: df -> correlation calculation -> threshold slider -> filtered results -> markdown output

    # Interactive slider for correlation threshold
    correlation_slider = mo.ui.slider(0.0, 1.0, step=0.1, value=0.3, label="Correlation Threshold")

    # Calculate correlation between x and y
    correlation = df['x'].corr(df['y'])

    return correlation, correlation_slider


@app.cell
def _(correlation, correlation_slider, df, mo, sample_size_slider):
    # Cell 4: Generate dynamic markdown report
    # Inputs: mo (from Cell 1), df, sample_size_slider (from Cell 2), correlation_slider, correlation (from Cell 3)
    # Outputs: Interactive markdown display with analysis results
    # Data flow: All previous cell outputs -> conditional analysis -> formatted markdown display

    # Determine if correlation exceeds threshold
    exceeds_threshold = abs(correlation) > correlation_slider.value

    # Create dynamic visualization indicators
    status_indicator = "🟢" if exceeds_threshold else "🔴"
    strength_bars = "📊" * int(abs(correlation) * 10)

    # Generate comprehensive analysis report
    mo.md(f"""
    ## Interactive Data Analysis Report

    **Dataset Configuration:**
    {sample_size_slider}

    **Correlation Analysis:**
    {correlation_slider}

    **Results:**
    - Sample Size: {len(df)} observations
    - X-Y Correlation: {correlation:.3f} {status_indicator}
    - Correlation Strength: {strength_bars}
    - Threshold Status: {'✅ Exceeds' if exceeds_threshold else '❌ Below'} threshold

    **Data Summary:**
    - Categories: {df['category'].value_counts().to_dict()}
    - X mean: {df['x'].mean():.3f}, Y mean: {df['y'].mean():.3f}
    """)
    return


@app.cell
def _():
    # Cell 5: Email identifier and data flow documentation
    # Inputs: None
    # Outputs: None
    # Email: 23f3003060@ds.study.iitm.ac.in
    # 
    # Data Flow Summary:
    # Cell 1 → Cell 2: mo, np, pd modules
    # Cell 2 → Cell 3: df (dataset), sample_size_slider
    # Cell 3 → Cell 4: correlation_slider, correlation value
    # Cell 4: Consumes all outputs to generate interactive analysis report
    return


if __name__ == "__main__":
    app.run()
