import marimo

__generated_with = "0.8.15"
app = marimo.App(width="medium")


@app.cell
def __():
    # Author email: 23f3003060@ds.study.iitm.ac.in
    # Cell 1: Define the base dataset for analysis
    # This cell creates the primary data that will flow to other cells
    import pandas as pd
    import marimo as mo
    import numpy as np

    # Create sample dataset with research metrics
    data_df = pd.DataFrame(
        {
            "sample_id": range(1, 21),
            "temperature": np.random.normal(25, 5, 20),
            "pressure": np.random.normal(1013, 50, 20),
            "efficiency": np.random.uniform(0.3, 0.9, 20),
        }
    )

    mo.md("## Interactive Data Analysis Dashboard")
    return data_df, mo, pd, np


@app.cell
def __(mo):
    # Cell 2: Interactive slider widget for threshold selection
    # This cell defines the control parameter that affects downstream analysis
    threshold_slider = mo.ui.slider(
        start=0.0, stop=1.0, step=0.1, value=0.5, label="Efficiency Threshold"
    )

    mo.md(f"**Control Panel:** Adjust the efficiency threshold to filter data")
    return (threshold_slider,)


@app.cell
def __(mo, threshold_slider):
    # Display the slider widget
    threshold_slider


@app.cell
def __(data_df, threshold_slider):
    # Cell 3: Filter and process data based on slider value
    # Data flow: This cell depends on data_df (Cell 1) and threshold_slider (Cell 2)
    # When slider changes, this cell automatically re-executes due to reactive dependencies

    # Filter data based on efficiency threshold
    filtered_df = data_df[data_df["efficiency"] >= threshold_slider.value]

    # Calculate summary statistics for filtered data
    summary_stats = {
        "count": len(filtered_df),
        "avg_temp": filtered_df["temperature"].mean() if len(filtered_df) > 0 else 0,
        "avg_pressure": filtered_df["pressure"].mean() if len(filtered_df) > 0 else 0,
        "avg_efficiency": filtered_df["efficiency"].mean()
        if len(filtered_df) > 0
        else 0,
    }

    return filtered_df, summary_stats


@app.cell
def __(mo, threshold_slider, filtered_df, summary_stats, data_df):
    # Cell 4: Dynamic markdown output based on widget state and processed data
    # Data flow: This cell depends on all previous cells and updates reactively
    # When threshold_slider changes -> filtered_df changes -> this output updates

    percentage_remaining = (
        (len(filtered_df) / len(data_df)) * 100 if len(data_df) > 0 else 0
    )

    mo.md(f"""
    ### Research Data Analysis Results
    
    **Current Filter Settings:**
    - Efficiency Threshold: **{threshold_slider.value:.1f}**
    
    **Filtered Dataset Statistics:**
    - Samples meeting criteria: **{summary_stats["count"]} / {len(data_df)}** ({percentage_remaining:.1f}%)
    - Average Temperature: **{summary_stats["avg_temp"]:.2f}°C**
    - Average Pressure: **{summary_stats["avg_pressure"]:.2f} hPa**
    - Average Efficiency: **{summary_stats["avg_efficiency"]:.3f}**
    
    **Data Flow Documentation:**
    - Cell 1 → Cell 3: Raw dataset (`data_df`) flows to filtering operation
    - Cell 2 → Cell 3: Slider value (`threshold_slider.value`) controls filter criteria  
    - Cell 3 → Cell 4: Processed data (`filtered_df`, `summary_stats`) flows to display
    - Interactive updates: Moving slider triggers reactive execution of Cells 3 & 4
    """)


@app.cell
def __(mo, filtered_df):
    # Cell 5: Display the filtered data table
    # Data flow: Depends on filtered_df from Cell 3
    mo.md("### Filtered Data Sample")
    return


@app.cell
def __(filtered_df):
    # Show first few rows of filtered data
    #
    # DATA FLOW GRAPH (ASCII Representation):
    # =============================================
    #
    #     Cell 1                    Cell 2
    #  ┌──────────────┐          ┌──────────────────┐
    #  │   data_df    │          │ threshold_slider │
    #  │     mo       │────┐     │                  │
    #  │     pd       │    │     └──────────────────┘
    #  │     np       │    │              │
    #  └──────────────┘    │              │
    #           │          │              │
    #           │          │              │
    #           ▼          ▼              ▼
    #        Cell 3 ◄──────────────────────┘
    #  ┌──────────────────────┐
    #  │    filtered_df       │
    #  │   summary_stats      │
    #  └──────────────────────┘
    #           │         │
    #           │         │
    #           ▼         ▼
    #       Cell 4    Cell 5 & 6
    #  ┌─────────────┐ ┌──────────────┐
    #  │  Dynamic    │ │  Data Table  │
    #  │  Markdown   │ │   Display    │
    #  │  Summary    │ │              │
    #  └─────────────┘ └──────────────┘
    #
    # Reactive Flow:
    # - When slider moves → Cell 2 updates → Cell 3 re-runs → Cells 4,5,6 update
    # - All dependencies automatically tracked by Marimo's dataflow graph
    # - No hidden state or execution order dependencies
    #
    filtered_df.head() if len(
        filtered_df
    ) > 0 else "No data meets the current threshold criteria"


if __name__ == "__main__":
    app.run()
