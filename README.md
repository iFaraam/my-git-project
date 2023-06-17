
### Date created
Created on June 17, 2023

### Project Title
Explore US Bikeshare Data

## Software Requirements

Before running the script, make sure you have the following software installed on your local machine:

- Python 3
- Pandas library
- Numpy library 
- Text editor, VS Code (Recommended)

### Description

This project focuses on analyzing bikeshare data using Python. The script prompts the user to input a city, month, and day to filter and analyze the bikeshare data. It then loads the data from the corresponding CSV file and applies the specified filters. The analysis provides insights into various aspects of bikeshare usage.

## Getting Started

To get started with the bikeshare data analysis, follow the steps below:

1. **Clone the Repository:** Clone the project repository to your local machine using the following command:

```bash 
git clone <repository_url>
```


2. **Install Dependencies:** Ensure that the required dependencies, such as pandas and numpy, are installed. You can install them using the following command:

```bash
pip install pandas numpy
```

3. **Run the Script:** Open your terminal or command prompt and make sure you navigate to the project directory where you cloned the git repository. Execute the following command to run the script:
```bash
python bikeshare_2.py
```

## How to use:

The script will prompt you to provide the following inputs:

1. **City:** The city you want to analyze (chicago, new york city, washington.)

2. **Month:** Which month you want to filter by, or type 'all' if you don't want to apply filter by month (months are from January up until June)

3. **Day:** Choose the day of the week you want to filter the data by, or select "all" to apply no day filter.

After providing the inputs, the script will perform the analysis and display various statistics related to the bikeshare data.

## Functionality

The script provides the following functionality:

1. **Data Loading:** The script loads the bikeshare data from the corresponding CSV file based on the selected city.

2. **Data Filtering:** The script filters the data based on the specified month and day to focus the analysis on specific time periods.

3. **Statistical Analysis:** The script calculates and displays statistics on the most frequent times of travel, popular stations and trips, trip durations, and user statistics (user types, gender, and birth year).

4. **Data Display:** Upon request, the script allows users to view raw data rows in batches of 5.

## Additional Notes

- The script relies on the availability of CSV data files for each city (chicago.csv, new_york_city.csv, washington.csv). Ensure that these files are located in the project directory before running the script.

- The script provides a user-friendly interface for input validation, ensuring that only valid cities, months, and days are accepted.





### Files Used

The project utilizes the following files for the analysis:

- `chicago.csv`: Contains bikeshare data for the city of Chicago.
- `new_york_city.csv`: Contains bikeshare data for the city of New York City.
- `washington.csv`: Contains bikeshare data for the city of Washington. Gender/Birth year not included.

These files are loaded into the script using the `pd.read_csv()` function to analyze and extract insights from the bikeshare data for the specified city, month, and day.
