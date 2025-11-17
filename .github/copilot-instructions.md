# AI Agent Instructions for Data Analysis Project

## Project Overview
This is a data analysis project using Python with key libraries including Pandas, NumPy, Matplotlib, and Seaborn. The project is structured to support both script-based (`*.py`) and notebook-based (`*.ipynb`) analysis workflows.

## Environment Setup
- The project uses a Python virtual environment located in `myenv/`
- Key dependencies:
  - pandas
  - numpy
  - matplotlib
  - seaborn

## Project Structure
```
.
├── analysis.py              # Main analysis script
├── Dataprojects.ipynb      # Jupyter notebook for interactive analysis
└── myenv/                  # Python virtual environment
```

## Development Patterns

### Code Organization
- Analysis code can be written in either:
  - Jupyter notebooks (`.ipynb`) for interactive exploration
  - Python scripts (`.py`) with cell markers (`# %%`) for VS Code's interactive mode
- Both approaches support identical functionality through the same dependencies

### Data Analysis Workflow
1. Always start with import statements in this order:
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   import seaborn as sns
   ```
2. Use Seaborn's built-in datasets for examples/testing (e.g., `sns.load_dataset()`)
3. Utilize cell markers (`# %%`) in `.py` files to maintain interactive capabilities

## Virtual Environment
- The project uses a dedicated virtual environment in `myenv/`
- Activate the environment before running any code:
  - macOS/Linux: `source myenv/bin/activate`
  - Windows: `myenv\Scripts\activate`

## Best Practices
1. Keep visualizations and data analysis cells separate for better organization
2. Use Seaborn for statistical visualizations when possible
3. Include version checks at the start of notebooks/scripts to ensure reproducibility

## Common Commands
- To run Python scripts: `python analysis.py`
- To launch Jupyter notebook: `jupyter notebook Dataprojects.ipynb`
- To check package versions (as shown in the code):
  ```python
  print("Python environment is set up and ready for data analysis.")
  print("Pandas version:", pd.__version__)
  print("NumPy version:", np.__version__)
  print("Matplotlib version:", plt.matplotlib.__version__)
  print("Seaborn version:", sns.__version__)
  ```