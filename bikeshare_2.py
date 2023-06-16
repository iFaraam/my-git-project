import pandas as pd
import numpy as np 
import time

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ('chicago', 'new york city', 'washington')
    months_check = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    days_check = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    while True:

        city = input("Select the city you want to analyze (chicago, new york city, washington)\n").lower()
        if city in cities:
            break
        else:
            print("Invalid city selection. Please make sure you provide the correct city name.\n")

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input("Select which month you want to filter by, or type 'all' if you don't want to aplly filter by month.\n").lower()
        if month in months_check:
            break
        else:
            print("Invalid month selection. Please make sure you provide the correct month name.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day you want to filter by ? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday. Alternatively, you can enter 'all' if you don't want to filter by a specific day.\n").lower()
        if day in days_check:
            break 
        else:
            print("Invalid day selection. Please make sure you provide the correct day name.\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
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
    Displays rows of data upon user request.

    Args:
        data_frame (pandas.DataFrame): The DataFrame containing the data.

    Returns:
        None
    """
    start_loc = 0
    user_display = input("Would you like to view 5 rows of raw data? Enter 'yes' or 'no': ").lower()
    while user_display == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        user_display = input("Do you wish to continue? Enter 'yes' or 'no': ").lower()


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0] # Mode returns a series of most occured element
    print("Displaying the most common month: ", most_common_month)
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Displaying the most common day of week: ", most_common_day)
    # display the most common start hour
    # first create a new column using dt submodule contains hours 
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("Displaying the most common hour of the day: ", most_common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

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

    print("Most common start station and end station combination: ", start_station, "-", end_station, "Count: ", count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip = df['Trip Duration'].sum()
    print("Total travel time in Hours: ", total_trip / 3600, "Hours")


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time in Minutes: ", mean_travel_time / 60, "Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("User types:\n", user_types_count)

    try:
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('Gender counts:\n', gender_counts)
    except KeyError:
        # Handle the case when 'Gender' column is not present
        print('Gender information not available.')

    try:
        # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print("The earliest birth year:\n", earliest_year)

        recent_year = df['Birth Year'].max()
        print("The most recent birth year:\n", recent_year)

        common_year = df['Birth Year'].mode()[0]
        print("The most common birth year:\n", common_year)
    except KeyError:
        # Handle the case when 'Birth Year' column is not present
        print('Birth year information not available.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
