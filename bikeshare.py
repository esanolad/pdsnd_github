import time
import pandas as pd
import numpy as np
from tabulate import tabulate

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
    print ('Welcome to Bikeshare Analytics')
    print ('********MENU*********')
    print('1. Chicago\n2. New York City\n3. Washington\n')
    cityList=['chicago','new york city', 'washington']
    try:
        cityNumber = int(input('Which City would you like to see data from (1-3)? '))
    except ValueError as e:
        cityNumber=400 #supplies invalid integer 
    except KeyboardInterrupt as e:
        print('\n Exiting the program....')
        exit(0)
        
    while not cityNumber in [1,2,3]:
        print('Invalid Input! ')
        try:
            cityNumber = int(input('Which City would you like to see data from (1-3)? '))
        except ValueError as e:
            cityNumber=400 #supplies invalid integer 
        except KeyboardInterrupt as e:
            print('\n Exiting the program....')
            exit(0)
    city=cityList[cityNumber-1]    
  
    # TO DO: get user input for month (all, january, february, ... , june)
    monthList=['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('\n','*'*10,'Month Filter','*'*10)
    print('0. No filter\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n')
    try:
        monthNumber=int(input('Which Month would you like to filter on(0-6)? '))
    except ValueError as e:
        monthNumber=400 #supplies invalid integer 
    except KeyboardInterrupt as e:
        print('\n Exiting the program....')
        exit(0)
    while not monthNumber in range(7):
        print('Invalid Input!')
        try:
            monthNumber = int(input('Please select menu from 0-6: '))
        except ValueError as e:
            monthNumber=400 #supplies invalid integer 
        except KeyboardInterrupt as e:
            print('\n Exiting the program...     ')       
            exit(0)
    month=monthList[monthNumber]
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    dayList=['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('\n','*'*10,'Day Filter','*'*10)
    print('0. No filter \n1. Monday \n2. Tuesday \n3. Wednesday \n4. Thursday \n5. Friday \n6. Saturday \n7. Sunday \n')
    try:
        dayNumber=int(input('Which Day of the Week would you like to filter on(0-7)? '))
    except ValueError as e:
        dayNumber=400 #supplies invalid integer 
    except KeyboardInterrupt as e:
        print('\n Exiting the program...     ')       
        exit(0)
    while not dayNumber in range(8):
        print('Invalid Input! ')
        try:
            dayNumber = int(input('Please select menu from 0-7: '))
        except ValueError as e:
            dayNumber=400 #supplies invalid integer 
        except KeyboardInterrupt as e:
            print('\n Exiting the program...     ')       
            exit(0)
    day=dayList[dayNumber]
        
    print('-'*40)
    return city,month,day

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
    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])
     # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
   
     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
   
    df['day_of_week'] = df['Start Time'].dt.day_name()
        
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month=month.capitalize()
        # filter by month to create the new dataframe
        df = df[(df['month']==month)]
    if day != 'all':
        # filter by day of week to create the new dataframe
        day=day.capitalize()
        df = df[(df['day_of_week']==day)]
    return df 


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        df - Pandas DataFrame containing city data
    
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: ', df['month'].mode()[0])

        
    # TO DO: display the most common day of week
    print('The most common day of the week is: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df_temp=df.copy() #make a copy of the dataframe
    df_temp['hour']=df_temp['Start Time'].dt.hour
    print('The most common start hour is: ', df_temp['hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    
    Displays statistics on the most popular stations and trip.
    
    Args:
        df - Pandas DataFrame containing city data
    
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common used start station is: ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('The most common used end station is: ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df_temp=df.copy()  #make a copy of the dataframe
    df_temp['route']=df_temp['Start Station']+' ==> '+df_temp['End Station']
    print('The most frequent combination of start station and end station trip is: ', df_temp['route'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        df - Pandas DataFrame containing city data
        
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is: ',df['Trip Duration'].sum())
    
    # TO DO: display mean travel time
    print('Mean travel time is: ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    
    Args:
        df - Pandas DataFrame containing city data
    
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('*'*5,'User Type Statistics','*'*5)
    print(df['User Type'].value_counts().to_string())

    # TO DO: Display counts of gender
    print('\n','*'*5,'User Gender Statistics','*'*5)
    try:
        print(df['Gender'].value_counts().to_string())
    except KeyError as e:
        print('Selected city does not have gender column')
    

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\n','*'*5,'Year of Birth Statistics','*'*5)
    try:
        #print(df['Gender'].value_counts().to_string())
        print('Earliest Year of Birth:',df['Birth Year'].min().round(0).astype(int))
        print('Most recent Year of Birth:',df['Birth Year'].max().round(0).astype(int))
        print('Most Common Year of Birth:',df['Birth Year'].mode()[0].round(0).astype(int))
    except KeyError as e:
        print('Selected city does not have year of birth column')
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_raw_data(df):
    """
    Displays bikeshare raw data.
    
    Args:
        df - Pandas DataFrame containing city data
    
    """
    try:
        see_data = input('\nWould you like to see first five lines of data? Enter yes or no.\n')
    except KeyboardInterrupt as e:
        print('\nExiting the program....')
        exit(0)
    row=0
    while see_data.lower()=='yes':
        if row>=df.shape[0]:
            print('No more data to display')
            break
        print(tabulate(df[row:row+5], headers="keys"))
        try:
            see_data = input('\nWould you like to see next five lines of data? Enter yes or no.\n')
            
        except KeyboardInterrupt as e:
            print('\nExiting the program....')
            exit(0)
        row+=5

def main():
    while True:
        city, month, day = get_filters()
        
        print ('STATISTICS FOR', city.upper(), 'FOR MONTH:', month.upper(), 'AND WEEKDAY:', day.upper())
        print ('*'*70)
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)
        try:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
        except KeyboardInterrupt as e:
            print('\nExiting the program....')
            exit(0)
        
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
