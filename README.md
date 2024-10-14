
# New York Taxi Data Processing

## Project Overview

This project is a Data Engineering challenge focused on processing New York Taxi Trip Data. The objective is to design and implement a scalable data pipeline that automates the extraction of taxi trip data, processes it to clean and transform it, and then loads it into a database for further analysis.

Due to machine limitations and the time-consuming nature of processing the full dataset, I have randomly selected 5000 rows from each file for processing. This ensures that the project runs efficiently while still providing meaningful insights and visualizations based on the sampled data.

The project also involves generating insights and visualizations from the processed data to derive useful trends and patterns from the taxi trip data

### Dataset

The dataset includes the following categories:

- **FHV** (For-Hire Vehicles)
- **FHVHV** (High-Volume For-Hire Vehicles)
- **Green Taxis**
- **Yellow Taxis**

Each dataset contains information such as pickup time, drop-off time, trip distances, fares, passenger counts, etc.

## Environment Setup

### Requirements

To set up the development environment for this project, you'll need the following software installed:

- **Python 3.x** (Recommended: Python 3.8+)
- **SQLite3** for the database
- **Pandas** for data manipulation
- **selenium** for data extraction
- **Seaborn** and **Matplotlib** for data visualization

You can install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain the following libraries:

```txt
pandas
matplotlib
seaborn
sqlite3
```

### Database Setup

The project uses **SQLite** for storing the processed data. The database will be created automatically when the scripts are run, and data will be inserted into tables based on the taxi data categories (FHV, FHVHV, Green, and Yellow).

## Running the Project

Follow these steps to run the project:

### 1. Data Extraction

The `scrapper.py` script is used to automate the downloading of New York taxi trip data from the year 2019. It handles network errors and retries as needed.

To run the scrapper:

```bash
python scrapper.py
```

### 2. Data Processing

The `etl.py` script is responsible for cleaning, transforming, and loading the data into the SQLite database. It cleans missing or corrupt data, derives new columns such as trip duration and average speed, and aggregates the data for analysis.

To run the ETL process:

```bash
python etl.py
```

This script will:
- Load the data from the downloaded CSV files
- Clean and process the data
- Insert the cleaned data into the SQLite database

### 3. Data Analysis and Reporting

The `reporting.py` script generates SQL queries to answer key analytical questions and visualizes the results using Seaborn and Matplotlib. The key questions include:
- What are the peak hours for taxi usage?
- How does passenger count affect the trip fare?
- What are the trends in taxi usage over the year?

To run the analysis:

```bash
python reporting.py
```

This will output SQL query results and visualizations such as bar charts, line plots, and scatter plots.

## Project Structure

```
- scrapper.py          # Script to download the taxi trip data
- etl.py               # ETL script to process and load the data into SQLite
- reporting.py         # Script to analyze data and generate reports
- README.md            # Project documentation (this file)
- requirements.txt     # Python dependencies
- trip_data.db         # SQLite database (generated after running ETL)
```

## Example Outputs

- **Peak Hours for Taxi Usage**
- **Trends in Taxi Usage Over the Year**
- **Passenger Count vs. Total Fare**

The visualizations are saved as images and displayed using Matplotlib, showing trends and insights for each taxi category.

## Submission Guidelines

- The project is version-controlled in a Git repository with meaningful commit messages.
- The repository is public for review.

