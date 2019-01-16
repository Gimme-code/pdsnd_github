import time
import pandas as pd
import numpy as np
import SciPy as sp

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
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\nPlease select a city you would like to get data for - Chicago, New York city or Washington: ').lower()
        if city not in ['washington', 'chicago', 'new york city']:
            print('\nYou have entered a city we do not offer data for/an invalid option. Please try entering a valid option')
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease select a month you would like to filter by - January, February. March, April, May or June. If you would like to filter by all, please type all: ').lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print('\nYou have entered an invalid option. Please try entering a valid option')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease select a month you would like to filter by - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. If you would like to filter by all, please type all: ').lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('\nYou have entered an invalid option. Please try entering a valid option')
            continue
        else:
            break

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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
         df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print('Most Common Month:', popular_month)
    # display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('Most Common Day:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most common start station is:', most_common_start_station)
    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('The most common end station is:', most_common_end_station)
    # display most frequent combination of start station and end station trip
    frequent_combination = df[['Start Station', 'End Station']].mode().iloc[0]
    print("The most frequent combination of start station and end station trip is: {}, {}"\
            .format(frequent_combination[0], frequent_combination[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()
        # Display counts of user types
        user_types_count = df['User Type'].value_counts()
        print('The user type count is:', user_types_count)
    except:
        print('No available user types data')
    try:
        # Display counts of gender, based on the availability of such data
        gender_count = df['Gender'].value_counts()
        print('The gender count is:', gender_count)
    except:
        print('No available gender data')

    try:
    # Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('The earliest year is:', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('The most recent year is:', most_recent_year)
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('The most common year is:', most_common_year)
    except:
        print('No available year of birth data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    while True:
        raw_data = input('\nWould you like to see individual trip data? Enter yes or no: ')
        if raw_data == 'yes'.lower():
                row_index = 0
                print(df.iloc[row_index: row_index+5])
                row_index += 5
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
