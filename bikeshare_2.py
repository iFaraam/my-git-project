import pandas as pd
import numpy as np 
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_input(prompt, valid_inputs):
    """
    Prompt user for input and validate against a list of valid inputs.

    Args:
        prompt (str): The prompt message to display to the user.
        valid_inputs (list): List of valid input values.

    Returns:
        str: The user-selected input value.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_filters():
    """
    Prompts user for input and returns selected city, month, and day for data analysis.

    Returns:
        (str) city - User-selected city to analyze. Must be either 'chicago', 'new york city', or 'washington'.
        (str) month - User-selected month to filter data by, or "all" to apply no month filter.
        (str) day - User-selected day of the week to filter data by, or "all" to apply no day filter.
    """
    print('Hello! Let\'s explore some US bikeshare datnha!')

    city = get_input("\nPlease select the city you want to analyze (chicago, new york city, washington):\n", ['chicago', 'new york city', 'washington'])
    month = get_input("\nPlease select which month you want to filter by, or type 'all' if you don't want to apply a month filter:\n", ['january', 'february', 'march', 'april', 'may', 'june', 'all'])
    day = get_input("\nPlease enter the day you want to filter by (e.g., Sunday, Monday, Tuesday, etc.), or enter 'all' if you don't want to filter by a specific day:\n", ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'])

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city, filtering by month and day if applicable.

    Args:
        (str) city - User-selected city to analyze.
        (str) month - User-selected month to filter data by, or "all" to apply no month filter.
        (str) day - User-selected day of the week to filter data by, or "all" to apply no day filter.

    Returns:
        df - pandas DataFrame containing city data filtered by month and day.
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name().str.title()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def display_data(df):
    """
    Displays rows of data in response to user's request.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data to display.

    Returns:
        None
    """
    start_loc = 0
    user_display = input("\nWould you like to view 5 rows of raw data? Enter 'yes' or 'no':\n").lower()
    while user_display == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        user_display = input("\nDo you wish to continue? Enter 'yes' or 'no':\n").lower()


def time_stats(df):
    """
    Calculates and displays statistics on the most frequent times of travel.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("Displaying the most common month: ", df['month'].mode()[0])
    # display the most common day of week
    print("Displaying the most common day of week: ", df['day_of_week'].mode()[0])
    # display the most common start hour
    # first create a new column using dt submodule contains hours 
    df['hour'] = df['Start Time'].dt.hour
    print("Displaying the most common hour of the day: ", df['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Calculates and displays statistics on the most popular stations and trip.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print("Most common start station: ", common_startstation)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most common end station: ", common_end_station)

    # display most frequent combination of start station and end station trip
    #Group the two stations to extract cominations.

    stations_combined = df.groupby(['Start Station', 'End Station']).size() # size() returns a series of counts for each combination
    common_comb_index = stations_combined.idxmax()
    print("Most Common Combination Index:")
    print(common_comb_index)

    start_station = common_comb_index[0]
    end_station = common_comb_index[1]
    count = stations_combined[common_comb_index]

    print("Most frequent trip from {} to {}, was made {} times".format(start_station, end_station, count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Calculates and displays statistics on the total and average trip duration.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total Travel Time: ", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean Travel Time: ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """
    Calculates and displays statistics on bikeshare users.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        city (str): The name of the city.

    Returns:
        None
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("Displaying counts of user types:\n", user_type)

    if city != 'washington': # The washington file does not have gender and birth year column
        # Display counts of gender
        gender_count = df['Gender'].value_counts()
        print("Displaying counts of gender:\n", gender_count)

        # Display earliest, most recent, and most common year of birth
        earliest_birthyear = df['Birth Year'].min()
        print("Displaying the earliest year of birth: ", earliest_birthyear)

        most_recent_birthyear = df['Birth Year'].max()
        print("Displaying the most recent year of birth: ", most_recent_birthyear)

        most_common_birthyear = df['Birth Year'].mode()[0]
        print("Displaying the most common year of birth: ", most_common_birthyear)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
