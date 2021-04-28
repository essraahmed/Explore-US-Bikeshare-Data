import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input("Choose the city you want: Chicago, New York City or Washington: ")
       city = city.lower()
       if city in ['chicago', 'new york city', 'washington']:
            break
       else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:    
        month = input("\nchoose the month you want, January, February, March, April, May, June or type 'all': ")
        month = month.lower()
        if month in('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print("invalid input. Please enter a valid input")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want details specific to a particular day? If yes, type day name else type 'all'")
        day = day.lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("invalid input. Please enter a valid input")
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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    #convert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month and day of week from start time to create a new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #filter by month to create the new dataframe
        df = df[df['month'] == month]

        #filter by day
    if day != 'all':
        #filter by day to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
   
    return df


def raw_data(df):
#display raw data according to user answer

    x = 0;
    #ask user if he/she wants to view the first 5 rows
    user_input = input('Would you want to view the first 5 rows of the data? yes/no: ').lower()
    

    while True:
        if user_input == 'no':
            break
       #print 5 rows     
        print(df[x: x+5])
        user_input = input('Would you want to view the next 5 rows of the data? yes/no: ').lower()
        
        x += 5
   
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
   
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('most common day of week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('most common hour', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].mode()[0]
    print('Most Commonly used start station:', most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].mode()[0]
    print('\nMost Commonly used end station:', most_common_end)


    # TO DO: display most frequent combination of start station and end station trip
    combination_of_start_and_end_station = (df['Start Station']+ '/' + df['End Station']).mode()[0]
    print('Combination of Start Station and End Station Trip:',  combination_of_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time:', total_time, 'in seconds, or', total_time/3600, 'hours')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_time, 'in seconds, or', mean_time/3600, 'hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
      gender = df['Gender'].value_counts()
      print('\nGender Types:\n', gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\nEarliest Year:', earliest_birth_year)
        
        most_recent = int(df['Birth Year'].max())
        print('\nMost Recent Year:', most_recent)

        most_common_year = int(df['Birth Year'].mode())
        print('\nMost Common Year:', most_common_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
