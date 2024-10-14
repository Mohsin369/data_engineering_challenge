import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('trip_sample_data.db')

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   FHV TRIPDATA ANALYSIS
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1 SQL Query: Peak Hours for Taxi Usage 
query_fhv_peak_hours = """
SELECT
    strftime('%H', pickup_datetime) AS pickup_hour,
    COUNT(*) AS trip_count
FROM
    fhv_tripdata
GROUP BY
    pickup_hour
ORDER BY
    trip_count DESC;
"""
df_fhv_peak_hours = pd.read_sql_query(query_fhv_peak_hours, conn)

# Visualization: Bar Plot for Peak Hours
plt.figure(figsize=(10, 6))
sns.barplot(x='pickup_hour', y='trip_count', data=df_fhv_peak_hours, palette='magma')
plt.title('FHV: Peak Hours for Taxi Usage', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Number of Trips', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#---------------------------------------------------------------------------------------------------------------------
# cannot calculate passenger count that affect the trip fare because passegner count and fair is no available in this dataset
#---------------------------------------------------------------------------------------------------------------------




# SQL Query: Trends in Taxi Usage Over the Year
query_fhv_trends_over_year = """
SELECT
    strftime('%Y-%m', pickup_datetime) AS year_month,
    COUNT(*) AS trip_count
FROM
    fhv_tripdata
GROUP BY
    year_month
ORDER BY
    year_month;
"""
df_fhv_trends_over_year = pd.read_sql_query(query_fhv_trends_over_year, conn)

# Visualization: Line Plot for Yearly Taxi Usage Trends (Month-wise)
df_fhv_trends_over_year['year_month'] = pd.to_datetime(df_fhv_trends_over_year['year_month'])
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='year_month', y='trip_count', data=df_fhv_trends_over_year, marker='o', color='blue', ax=ax)
plt.title('FHV: Taxi Usage Trends Over the Year (Month-wise)', fontsize=16)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Number of Trips', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True)
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.show()






# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   FHVHV TRIPDATA ANALYSIS
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------








# SQL Query: Peak Hours for Taxi Usage
query_fhvhv_peak_hours = """
SELECT
    strftime('%H', pickup_datetime) AS pickup_hour,
    COUNT(*) AS trip_count
FROM
    fhvhv_tripdata
GROUP BY
    pickup_hour
ORDER BY
    trip_count DESC;
"""
df_fhvhv_peak_hours = pd.read_sql_query(query_fhvhv_peak_hours, conn)

# Visualization: Bar Plot for Peak Hours
plt.figure(figsize=(10, 6))
sns.barplot(x='pickup_hour', y='trip_count', data=df_fhvhv_peak_hours, color='skyblue')
plt.title('FHVHV: Peak Hours for Taxi Usage', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Number of Trips', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# SQL Query: Base Passenger Fare vs Trip Miles

query_fhvhv_fare_vs_trip_miles = """
SELECT
    trip_miles,
    AVG(base_passenger_fare) AS avg_fare,
    COUNT(*) AS trip_count
FROM
    fhvhv_tripdata
GROUP BY
    trip_miles
ORDER BY
    avg_fare DESC;
"""
df_fhvhv_fare_vs_trip_miles = pd.read_sql_query(query_fhvhv_fare_vs_trip_miles, conn)



# Visualization: Scatter Plot for Base Passenger Fare vs Trip Miles
plt.figure(figsize=(10, 6))
sns.scatterplot(x='trip_miles', y='avg_fare', data=df_fhvhv_fare_vs_trip_miles, sizes=(20, 200),alpha=0.9)

plt.title('FHVHV: Base Passenger Fare vs Trip Miles', fontsize=16)
plt.xlabel('Trip Miles', fontsize=14)
plt.ylabel('Average Fare ($)', fontsize=14)
#plt.legend(title='Average Fare and Trip Count', loc='upper left', bbox_to_anchor=(1, 1), borderaxespad=0)
plt.tight_layout()
plt.show()




# SQL Query: Trends in Taxi Usage Over the Year

query_fhvhv_trends_over_year = """
SELECT
    strftime('%Y-%m', pickup_datetime) AS year_month,
    COUNT(*) AS trip_count
FROM
    fhvhv_tripdata
GROUP BY
    year_month
ORDER BY
    year_month;
"""
df_fhvhv_trends_over_year = pd.read_sql_query(query_fhvhv_trends_over_year, conn)

# Visualization: Line Plot for Yearly Taxi Usage Trends (Month-wise)
df_fhvhv_trends_over_year['year_month'] = pd.to_datetime(df_fhvhv_trends_over_year['year_month'])

# Convert 'year_month' to datetime to extract both year and month for plotting
df_fhvhv_trends_over_year['year_month'] = pd.to_datetime(df_fhvhv_trends_over_year['year_month'])
df_fhvhv_trends_over_year['year'] = df_fhvhv_trends_over_year['year_month'].dt.year
df_fhvhv_trends_over_year['month'] = df_fhvhv_trends_over_year['year_month'].dt.month

# Set the range for x-axis (limited from 2019 to mid-2024) and y-axis based on data range
fig, ax = plt.subplots(figsize=(14, 8))

sns.lineplot(x='year_month', y='trip_count', data=df_fhvhv_trends_over_year, marker='o', color='green', ax=ax)

# Set the title and axis labels
plt.title('FHVHV: Taxi Usage Trends Over the Year (Month-wise)', fontsize=18)
plt.xlabel('Year-Month', fontsize=14)
plt.ylabel('Number of Trips', fontsize=14)

# Adjust grid
plt.grid(visible=True, which='both', axis='both', color='gray', linestyle='--', linewidth=0.5)

# Limit the x-axis range from 2019 to mid-2024
ax.set_xlim(pd.Timestamp('2019-01-01'), pd.Timestamp('2024-06-01'))

# Adjust the y-axis based on the trip_count range
min_trip_count = df_fhvhv_trends_over_year['trip_count'].min()
max_trip_count = df_fhvhv_trends_over_year['trip_count'].max()
ax.set_ylim(min_trip_count - 100, max_trip_count + 100)

# Handle x-axis ticks to avoid overlap
plt.xticks(rotation=45, ha='right')

# Adjust layout to avoid clipping
plt.tight_layout()
plt.show()




# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   GREEN TRIPDATA ANALYSIS
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# SQL Query: Peak Hours for Taxi Usage 

query_green_peak_hours = """
SELECT
    strftime('%H', lpep_pickup_datetime) AS pickup_hour,
    COUNT(*) AS trip_count
FROM
    green_tripdata
GROUP BY
    pickup_hour
ORDER BY
    trip_count DESC;
"""
df_green_peak_hours = pd.read_sql_query(query_green_peak_hours, conn)

# Visualization: Bar Plot for Peak Hours
plt.figure(figsize=(10, 6))
sns.barplot(x='pickup_hour', y='trip_count', data=df_green_peak_hours, palette='Set3')
plt.title('Green: Peak Hours for Taxi Usage', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Number of Trips', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# SQL Query: Passenger Count vs Total Fare

query_green_passenger_count_vs_fare = """
SELECT
    passenger_count,
    AVG(total_amount) AS avg_fare,
    COUNT(*) AS trip_count
FROM
    green_tripdata
GROUP BY
    passenger_count
ORDER BY
    avg_fare DESC;
"""
df_green_passenger_count_vs_fare = pd.read_sql_query(query_green_passenger_count_vs_fare, conn)

# Visualization: Bar Plot for Passenger Count vs Total Fare
plt.figure(figsize=(10, 6))
sns.barplot(x='passenger_count', y='avg_fare', data=df_green_passenger_count_vs_fare, palette='rocket')
plt.title('Green: Passenger Count vs Total Fare', fontsize=16)
plt.xlabel('Passenger Count', fontsize=14)
plt.ylabel('Average Fare ($)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# SQL Query: Trends in Taxi Usage Over the Year 

query_green_trends_over_year = """
SELECT
    strftime('%Y-%m', lpep_pickup_datetime) AS year_month,
    COUNT(*) AS trip_count
FROM
    green_tripdata
GROUP BY
    year_month
ORDER BY
    year_month;
"""
df_green_trends_over_year = pd.read_sql_query(query_green_trends_over_year, conn)

# Visualization: Line Plot for Yearly Taxi Usage Trends (Month-wise)
df_green_trends_over_year['year_month'] = pd.to_datetime(df_green_trends_over_year['year_month'])
df_green_trends_over_year['year_month'] = pd.to_datetime(df_green_trends_over_year['year_month'])
df_green_trends_over_year['year'] = df_green_trends_over_year['year_month'].dt.year

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(x='year_month', y='trip_count', data=df_green_trends_over_year, marker='o', color='orange', ax=ax)
plt.title('Green: Taxi Usage Trends Over the Year (Month-wise)', fontsize=16)
plt.xlabel('Year-Month', fontsize=12)
plt.ylabel('Number of Trips', fontsize=12)
plt.xticks(rotation=45, ha='right')
ax.set_xlim(pd.Timestamp('2019-01-01'), pd.Timestamp('2024-06-01'))
plt.grid(True)
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.show()






# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                   YELLOW TRIPDATA ANALYSIS
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# SQL Query: Peak Hours for Taxi Usage 

query_yellow_peak_hours = """
SELECT
    strftime('%H', tpep_pickup_datetime) AS pickup_hour,
    COUNT(*) AS trip_count
FROM
    yellow_tripdata
GROUP BY
    pickup_hour
ORDER BY
    trip_count DESC;
"""
df_yellow_peak_hours = pd.read_sql_query(query_yellow_peak_hours, conn)

# Visualization: Bar Plot for Peak Hours (Yellow Taxi)
plt.figure(figsize=(10, 6))
sns.barplot(x='pickup_hour', y='trip_count', data=df_yellow_peak_hours, palette='cubehelix')
plt.title('Yellow: Peak Hours for Taxi Usage', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Number of Trips', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




# SQL Query: Passenger Count vs Total Fare

query_yellow_passenger_count_vs_fare = """
SELECT
    passenger_count,
    AVG(total_amount) AS avg_fare,
    COUNT(*) AS trip_count
FROM
    yellow_tripdata
GROUP BY
    passenger_count
ORDER BY
    avg_fare DESC;
"""
df_yellow_passenger_count_vs_fare = pd.read_sql_query(query_yellow_passenger_count_vs_fare, conn)

# Visualization: Bar Plot for Passenger Count vs Total Fare (Yellow Taxi)
plt.figure(figsize=(10, 6))
sns.barplot(x='passenger_count', y='avg_fare', data=df_yellow_passenger_count_vs_fare, palette='muted')
plt.title('Yellow Taxi: Passenger Count vs Total Fare', fontsize=16)
plt.xlabel('Passenger Count', fontsize=14)
plt.ylabel('Average Fare ($)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()




# SQL Query: Trends in Taxi Usage Over the Year 

query_yellow_trends_over_year = """
SELECT
    strftime('%Y-%m', tpep_pickup_datetime) AS year_month,
    COUNT(*) AS trip_count
FROM
    yellow_tripdata
GROUP BY
    year_month
ORDER BY
    year_month;
"""
df_yellow_trends_over_year = pd.read_sql_query(query_yellow_trends_over_year, conn)

# Visualization: Line Plot for Yearly Taxi Usage Trends (Month-wise)
df_yellow_trends_over_year['year_month'] = pd.to_datetime(df_yellow_trends_over_year['year_month'])

df_yellow_trends_over_year['year_month'] = pd.to_datetime(df_yellow_trends_over_year['year_month'])
df_yellow_trends_over_year['year'] = df_yellow_trends_over_year['year_month'].dt.year
df_yellow_trends_over_year['month'] = df_yellow_trends_over_year['year_month'].dt.month

fig, ax = plt.subplots(figsize=(14, 8))

sns.lineplot(x='year_month', y='trip_count', data=df_yellow_trends_over_year, marker='o', color='yellow', ax=ax)

plt.title('Yellow: Taxi Usage Trends Over the Year (Month-wise)', fontsize=18)
plt.xlabel('Year-Month', fontsize=14)
plt.ylabel('Number of Trips', fontsize=14)

# Adjust grid
plt.grid(visible=True, which='both', axis='both', color='gray', linestyle='--', linewidth=0.5)

# Limit the x-axis range from 2019 to mid-2024
ax.set_xlim(pd.Timestamp('2019-01-01'), pd.Timestamp('2024-06-01'))

# Adjust the y-axis based on the trip_count range
min_trip_count = df_yellow_trends_over_year['trip_count'].min()
max_trip_count = df_yellow_trends_over_year['trip_count'].max()
ax.set_ylim(min_trip_count - 100, max_trip_count + 100)

# Handle x-axis ticks to avoid overlap
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()


# Close the connection to the database
conn.close()
