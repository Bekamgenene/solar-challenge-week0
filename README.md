# 🌞 Solar Challenge Week 0: Exploratory Data Analysis for Benin and Togo Solar Irradiance Data


[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-green.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.5%2B-red.svg)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.11%2B-blue.svg)](https://seaborn.pydata.org/)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Description](#data-description)
- [Notebooks](#notebooks)
- [Results and Visualizations](#results-and-visualizations)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Overview

This project is part of the **Solar Challenge Week 0**, focusing on comprehensive Exploratory Data Analysis (EDA) of solar irradiance data collected from monitoring stations in **Benin (Malanville)** and **Togo (Dapaong)**. The analysis aims to uncover patterns, correlations, and insights into solar radiation, temperature, wind, and other meteorological factors to support solar energy optimization.

Key objectives include:

- Data cleaning and outlier detection
- Time series analysis of solar irradiance
- Correlation and relationship studies
- Wind and temperature pattern analysis
- Monthly and hourly trend identification

## ✨ Features

- **Data Loading & Cleaning**: Handles missing values, outliers, and data type conversions.
- **Comprehensive EDA**: Includes statistical summaries, visualizations, and advanced plots like wind roses and bubble charts.
- **Automated Plot Generation**: Saves high-resolution images for reports and presentations.
- **Modular Notebooks**: Separate analyses for Benin and Togo datasets.
- **Reproducible Code**: Well-documented Jupyter notebooks with clear sections.

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/solar-challenge-week0.git
   cd solar-challenge-week0
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:

   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```

3. **Data Setup**:
   - Place the raw data files in the `../data/` directory:
     - `benin-malanville.csv` for Benin data
     - `togo-dapaong_qc.csv` for Togo data
   - The notebooks will generate cleaned data and images in `../data/` and `../images/` respectively.

## 🚀 Usage

1. **Run the Notebooks**:

   - Open `notebooks/benin_eda.ipynb` for Benin analysis.
   - Open `notebooks/togo_eda.ipynb` for Togo analysis.
   - Execute cells sequentially to perform EDA and generate plots.

2. **View Results**:

   - Cleaned data will be saved as `../data/benin_clean.csv` and `../data/togo_clean.csv`.
   - Visualizations will be saved in `../images/benin/` and `../images/togo/` directories.

3. **Customization**:
   - Modify paths, thresholds, or analysis parameters in the notebooks as needed.

## 📊 Data Description

The datasets contain meteorological and solar irradiance measurements from solar monitoring stations:

- **Benin (Malanville)**: Data from a station in Benin, including GHI, DNI, DHI, module temperatures, wind speed, humidity, etc.
- **Togo (Dapaong)**: Similar data from Togo, with quality-controlled measurements.

Key columns:

- `Timestamp`: Date and time of measurements.
- `GHI`, `DNI`, `DHI`: Global, Direct, and Diffuse Horizontal Irradiance (W/m²).
- `ModA`, `ModB`: Module irradiance measurements.
- `Tamb`: Ambient temperature (°C).
- `RH`: Relative humidity (%).
- `WS`, `WD`: Wind speed (m/s) and direction (°).
- `BP`: Barometric pressure (hPa).

## 📓 Notebooks

- **`notebooks/benin_eda.ipynb`**: EDA for Benin solar data, including data cleaning, time series, correlations, and visualizations.
- **`notebooks/togo_eda.ipynb`**: EDA for Togo solar data, mirroring the Benin analysis for comparative insights.

Each notebook includes:

- Library imports and path definitions.
- Data loading and summary statistics.
- Cleaning and outlier handling.
- Various analyses with plot generation.

## 📈 Results and Visualizations

The analysis generates a variety of plots to illustrate key findings. Below are some examples (images are saved in `../images/benin/` and `../images/togo/`):

### Correlation Heatmap

![Correlation Heatmap](../images/benin/correlation_heatmap.png)
_Figure 1: Correlation between solar irradiance, temperature, wind, and humidity variables._

### Time Series of GHI

![Time Series GHI](../images/benin/time_series_GHI.png)
_Figure 2: Global Horizontal Irradiance (GHI) over time, showing daily and seasonal patterns._

### Wind Rose

![Wind Rose](../images/benin/wind_rose.png)
_Figure 3: Average wind speed by direction, visualized as a polar plot._

### Monthly Trends

![Monthly Trends](../images/benin/monthly_trends.png)
_Figure 4: Average monthly values for GHI, DNI, DHI, and temperature._

### Scatter Plot: Wind Speed vs GHI

![Scatter WS vs GHI](../images/benin/scatter_WS_vs_GHI.png)
_Figure 5: Relationship between wind speed and solar irradiance._

Additional plots include histograms, bubble charts, and hourly trends, providing a full picture of the data.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-analysis`).
3. Commit your changes (`git commit -m 'Add new analysis'`).
4. Push to the branch (`git push origin feature/new-analysis`).
5. Open a Pull Request.

For major changes, please open an issue first to discuss.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

_Prepared for Solar Challenge Week 0. For questions or feedback, contact [your-email@example.com].
This repository contains the code and resources for the Solar Challenge Week 0 project.

## Project Structure

```
├── .vscode/              # VS Code settings
├── .github/              # GitHub Actions workflows
├── images/              # images of some graphs
├── src/                  # Source code
├── notebooks/            # Jupyter notebooks
├── tests/               # Unit tests
└── scripts/             # Utility scripts
```

## Setup Instructions

1. Clone the repository:

```bash
git clone (https://github.com/Bekamgenene/solar-challenge-week0.git)
cd solar-challenge-week0
```

2. Create and activate a virtual environment:

For Windows:

```bash
python -m venv venv
.\myenv\Scripts\activate
```

For Unix/MacOS:

```bash
python -m venv myenv
source myenv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Development

- Code formatting is handled by `black`
- Linting is done with `pylint`
- Tests are written using `pytest`

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Submit a pull request

## License


## Exploratory Data Analysis (EDA)

The EDA was performed for three countries: **Benin (Malanville)**, **Sierra Leone (Bumbuna)**, and **Togo (Dapaong)**. The analysis included:

- **Data Loading & Cleaning:**
	- Datasets were loaded and timestamps parsed.
	- Outliers were detected using Z-scores (|Z| > 3) for key variables (GHI, DNI, DHI, ModA, ModB, WS, WSgust).
	- Missing values in critical columns (GHI, DNI, DHI, Tamb) were imputed with the median.
	- Cleaned datasets were prepared for further analysis.

- **Descriptive Statistics & Missing Data:**
	- Summary statistics were generated for each country’s key performance indicators.
	- Missing data percentages were reported, highlighting any columns with >5% missingness.

- **Visualizations:**
	- Time series plots of solar irradiance (GHI, DNI, DHI) for January 2023.
	- Bar plots showing the impact of cleaning on module performance (ModA).
	- Correlation heatmaps for financial and risk variables (GHI, DNI, DHI, Tamb, TModA, RH, WS).

### Country Highlights

#### Benin (Malanville)
- Data showed typical seasonal and daily solar patterns.
- Outliers and missing values were handled as described above.
- Cleaning activities had a measurable positive impact on module output.
- Correlation analysis revealed strong relationships between irradiance and module performance.

#### Sierra Leone (Bumbuna)
- Similar EDA steps as Benin.
- Some differences in missing data patterns and outlier frequency.
- Cleaning and correlation patterns were consistent with Benin, with some site-specific variations.

#### Togo (Dapaong)
- EDA followed the same process.
- Data quality and trends were comparable to the other sites.
- Cleaning and correlation analyses provided actionable insights for site management.

For detailed code and plots, see the [notebooks](notebooks).

[MIT License](LICENSE)
