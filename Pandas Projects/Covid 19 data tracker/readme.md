# COVID-19 Data Tracker

This project aims to analyze COVID-19 data by tracking cases, recoveries, deaths, and other key metrics across various countries. The data is processed using **Pandas** for efficient manipulation and **Seaborn** for creating visualizations that provide insights into global trends.

## Project Overview

In this project, we load COVID-19 data, clean it, perform data analysis, and visualize trends related to cases, recoveries, and mortality rates. This tracker uses publicly available datasets to analyze the situation across different countries.

### Features

- Load and clean COVID-19 data from a CSV file.
- Calculate key metrics such as:
  - Total confirmed cases
  - Total recovered cases
  - Total deaths
  - Active cases
  - Recovery rate
  - Mortality rate
- Generate insightful visualizations using **Seaborn**:
  - Bar plot showing the top 10 countries by confirmed cases.
  - Scatter plot showing recovery rate vs. mortality rate.
  - Correlation heatmap of COVID-19 statistics.

## Dataset

The dataset used in this project is sourced from publicly available COVID-19 data, provided as a CSV file. The data includes columns such as:
- `Country/Region`: Name of the country.
- `Confirmed`: Total number of confirmed cases.
- `Recovered`: Total number of recovered cases.
- `Deaths`: Total number of deaths.
- `Active Cases`: Calculated as the difference between confirmed, recovered, and deaths.
- `Recovery Rate`: Percentage of recovered cases out of confirmed cases.
- `Mortality Rate`: Percentage of deaths out of confirmed cases.

## Requirements

To run this project, you'll need the following Python libraries installed:

- `pandas`
- `matplotlib`
- `seaborn`

Install them using:

```bash
pip install pandas matplotlib seaborn
