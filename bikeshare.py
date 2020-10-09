import numpy as np
import pandas as pd
import time
import sys

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def view_city(city):
    """ Prints the contents of the city data 5 lines at a time """
    pd.set_option('display.max_columns', None)
    df = pd.read_csv(CITY_DATA[city])
    response = ['yes', 'no', 'y', 'n']
    count = 0

    print(df.iloc[count:count + 5])
    count += 5
    print('*' * 60)
    raw_input = input("Would you like to continue 'yes' or 'no'? ").lower()
    # print(raw_input)
    # breakpoint()

    while True:
        while raw_input not in response:
            print('*' * 60)
            print('Please only enter one of the following: ', response)
            raw_input = input("Would you like to continue 'yes' or 'no'? ").lower()
            # print(raw_input)
            # breakpoint()
        if raw_input[0] == 'n':
            break

        print(df.iloc[count:count + 5])
        count += 5
        print('*' * 60)
        raw_input = input("Would you like to continue 'yes' or 'no'? ").lower()
        # print(raw_input)
        # breakpoint()


def welcome():
    """" Greets user and Prompts to user to view raw data or analyze data.

    returns (bool) view_data
    """
    view_data = False
    menu_selection = 'none'
    greeting1 = 'Welcome to the Bike Share Analysis program.'
    greeting2 = 'You can view five lines of raw data,\nor review statistics. \n'
    choice_menu = ('Main Menu',
                   'Please selection an option',
                   'Enter "1" to view raw data',
                   'Enter "2" to review statistics.',
                   'Enter "e" to exit the program.'
                   )
    print('*' * 60)
    print(greeting1)
    print(greeting2)

    while menu_selection == 'none':
        for item in choice_menu:
            print(item)

        choice = input('Please enter "1", "2", or "e": ')

        # Evaluate user's choice.
        if choice == '1':
            print("\nYou selected 1, view raw data.\n")
            menu_selection = '1'
            view_data = True

        elif choice == '2':
            print("\nYou selected 2, analyze data.\n")
            menu_selection = '2'
            view_data = False

        elif choice == 'E' or 'e':
            print("\nYou selected 3, exit the program.\n")
            sys.exit()
        else:
            print("\nI don't understand that choice, please try again.\n")
    return view_data


def get_city():
    """ Prompts user to select a city from a menu.

    Returns: (str) city_name

    """
    city_selection = 'none'
    city_name = 'none'
    city_menu = ('Please choose a city.',
                 'Enter "1" to select Chicago.',
                 'Enter "2" to select New York.',
                 'Enter "3" to select Washington.',
                 'Enter "m" to got the the main menu.'
                 )

    while city_selection == 'none':
        for item in city_menu:
            print(item)
        choice = input('Please enter "1", "2", or "3": ')

        # Evaluate user's choice.
        if choice == '1':
            city_selection = '1'
            print("\nYou selected 1, Chicago.\n")
            city_name = 'chicago'
        elif choice == '2':
            city_selection = '2'
            print("\nYou selected 2, New York.\n")
            city_name = 'new york city'
        elif choice == '3':
            city_selection = '3'
            print("\nYou selected 3, Washington.\n")
            city_name = 'washington'
        elif choice == 'M' or 'm':
            city_selection = 'm'
            print("\nYou selected M, go to the main menu.\n")
            welcome()
        else:
            print("\nI don't understand that choice, please try again.\n")

    return city_name


def get_month():
    """ Prompts user to select the month.

      Returns: (str) month_selection

    """
    month_selection = 'none'
    months_2017 = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month_selection == 'none':
        print('Data is available for he first six months of 2017 ')
        choice = (input('Enter the name of the month to filter by or "all" for all available months: ').lower())
        if choice not in months_2017:
            print('Please only enter on of the following: ', months_2017)
        else:
            month_selection = choice
            print('You selected : ', month_selection.title())

    return month_selection


def get_day():
    """ Prompts user to select the day of the week.

         Returns: (str) day_selection

         """
    day_selection = 'none'
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while day_selection == 'none':
        choice = (input('Enter the day of the week to to filter by or "all" for all days of the week: ').lower())
        if choice not in days:
            print('Please only enter on of the following: ', days)
        else:
            day_selection = choice
            print('You selected : ', day_selection.title())

    return day_selection


def load_data(city, month, day):
    """ Loads data for the specified city and filters by month and day if applicable.

    Arguments:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # find the most common month

    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # display the most common day of week
    # find the most common Day
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day:', popular_day)

    # display the most common start hour
    # find the most common hour (from 0 to 23)
    # extract hour from the Start Time column
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Frequent End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    print('The most combination of start station and end station trip is: \n {}'.format((df['combination'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total time traveled is: ', total_time)

    # display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average time traveled is: ', avg_time)

    print("\n (This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bike share users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of gender
    print(df['Gender'].value_counts())
    print('\n')

    # Display earliest, most recent, and most common year of birth
    birth_year_earliest = int(df['Birth Year'].min())
    birth_year_recent = int(df['Birth Year'].max())
    birth_year_most_common = int(df['Birth Year'].mode()[0])
    print('Most earliest birth year:', birth_year_earliest)
    print('Most recent birth year:', birth_year_recent)
    print('Most common birth year:', birth_year_most_common)
    print("\n This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_types_stats(df):
    """ Displays statistics on bike share user types."""
    """ Displays statistics on bike share user types."""
    print('\nCalculating User Type Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df['User Type'].value_counts())
    print('\n')

    print("\n (This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        view_data = welcome()
        city = get_city()
        if view_data:
            view_city(city)
        else:
            # run_analysis
            month = get_month()
            day = get_day()
            df = load_data(city, month, day)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_types_stats(df)
            if city != 'washington':
                user_stats(df)
            else:
                print('No User Stats Available for {}'.format(city).title())
        restart = input('\nWould you like to restart? Enter "yes" or "no".\n').lower()
        if restart[0] != 'y':
            break


if __name__ == "__main__":
    main()
