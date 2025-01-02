###################################
# Build a Time Calculator Project #
###################################
"""
Write a function named add_time that takes in two required parameters and one optional parameter:
    - a start time in the 12-hour clock format (ending in AM or PM)
    - a duration time that indicates the number of hours and minutes
    - (optional) a starting day of the week, case-insensitive

The function should add the duration time to the start time and return the result.

- If the result will be the next day, it should show (next day) after the time. If the
    result will be more than one day later, it should show (n days later) after the time,
    where "n" is the number of days later.

- If the function is given the optional starting day of the week parameter, then the
    output should display the day of the week of the result. The day of the week in the
    output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle.
Pay close attention to the spacing and punctuation of the results.

    add_time('3:00 PM', '3:10')
    # Returns: 6:10 PM

    add_time('11:30 AM', '2:32', 'Monday')
    # Returns: 2:02 PM, Monday

    add_time('11:43 AM', '00:20')
    # Returns: 12:03 PM

    add_time('10:10 PM', '3:30')
    # Returns: 1:40 AM (next day)

    add_time('11:43 PM', '24:20', 'tueSday')
    # Returns: 12:03 AM, Thursday (2 days later)

    add_time('6:30 PM', '205:12')
    # Returns: 7:42 AM (9 days later)

Do not import any Python libraries. Assume that the start times are valid times.
The minutes in the duration time will be a whole number less than 60, but the hour
can be any whole number.
"""

WEEK_DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

N_HOURS_IN_A_DAY = 24
CLOCK_FORMAT = 12
N_MIN_IN_SECS = 60


def add_time(start, duration, starting_day=''):
    """
    Adds the duration time to the start time.

    :param start: a start time in the 12-hour clock format (ending in AM or PM).
    :param duration: a duration time that indicates the number of hours and minutes.
    :param starting_day: (optional) a starting day of the week, case-insensitive.
    :return: new time which is addition of duration time to the start time formatted as required
    """
    is_error, valid_values_or_error_msg = validate_input(start, duration, starting_day)

    if is_error:
        return valid_values_or_error_msg
    else:
        start_hour, start_min, start_label, duration_hour, duration_min, starting_day = valid_values_or_error_msg

    # converts start_hour to a 24-hour clock format
    start_hour = start_hour if start_label == 'AM' else start_hour + CLOCK_FORMAT
    # adds start and duration hours, and excess hour from minutes sum if any
    hour_sum = start_hour + duration_hour + (start_min + duration_min) // N_MIN_IN_SECS
    # adds start and duration minutes, (discarding excess minutes which are upto an hour)
    new_time_min = (start_min + duration_min) % N_MIN_IN_SECS
    # converts sum of the hours into 24-hour format clock
    new_time_hour = hour_sum % N_HOURS_IN_A_DAY
    # gets the excess hours in days (i.e. excess hours which are upto an day(s))
    n_days = hour_sum // N_HOURS_IN_A_DAY
    # gets the correct clock label for the new time
    new_time_label = 'AM' if new_time_hour < CLOCK_FORMAT else 'PM'
    # gets name for the new time day, in required format
    if starting_day != '':
        new_time_day = WEEK_DAYS[(WEEK_DAYS.index(starting_day) + n_days) % len(WEEK_DAYS)]
        new_time_day = f', {new_time_day}'
    else:
        new_time_day = ''
    # add '0' to make the minute double-digit if not
    if new_time_min < 10:
        new_time_min = '0' + str(new_time_min)
    # converts new_time_hour to a 12-hour clock format
    new_time_hour %= CLOCK_FORMAT
    if new_time_hour == 0:
        new_time_hour = 12  # changes the 0 to 12

    new_time = f'{new_time_hour}:{new_time_min} {new_time_label}{new_time_day}{get_time_label_string(n_days)}'
    print(new_time)
    return new_time


def get_time_label_string(n_days):
    """
    Compute days after start day in the required format.

    :param n_days: number of days after start day.
    :return: return string in required format days after start day.
    """
    if n_days == 1:
        return ' (next day)'
    elif n_days > 1:
        return f' ({n_days} days later)'
    else:
        return ''


def validate_input(start, duration, starting_day):
    """
    Checks if all parameters are of required format

    :param start: a start time in the 12-hour clock format (ending in AM or PM).
    :param duration: a duration time that indicates the number of hours and minutes.
    :param starting_day: (optional) a starting day of the week, case-insensitive.
    :return: error message OR tokenized values of the parameters
    """
    is_error = True     # True if not in required format
    start_time, start_label = start.split(' ')
    start_hour, start_min = start_time.split(':')
    duration_hour, duration_min = duration.split(":")
    starting_day = starting_day.title()

    start_hour, start_min, start_label, duration_hour, duration_min, starting_day = (
        int(start_hour), int(start_min), start_label, int(duration_hour), int(duration_min), starting_day)

    is_valid_start_hour = 0 <= start_hour <= CLOCK_FORMAT
    is_valid_start_min = 0 <= start_min < N_MIN_IN_SECS
    is_valid_start_label = start_label == 'AM' or 'PM'
    is_valid_start = is_valid_start_hour and is_valid_start_min and is_valid_start_label
    if not is_valid_start:
        return [is_error, 'Error: Invalid start time.']

    is_duration_hour = duration_hour >= 0
    is_duration_min = 0 <= duration_min < N_MIN_IN_SECS
    is_valid_duration = is_duration_hour and is_duration_min
    if not is_valid_duration:
        return [is_error, 'Error: Invalid duration time.']

    if starting_day not in WEEK_DAYS and starting_day != '':
        return [is_error, 'Error: Invalid starting day.']

    is_error = False
    return [is_error, (start_hour, start_min, start_label, duration_hour, duration_min, starting_day)]


# TESTS
add_time('3:30 PM', '2:12')
print('5:42 PM <== Expected\n')

add_time('11:55 AM', '3:12')
print('3:07 PM <== Expected\n')

add_time('2:59 AM', '24:00')
print('2:59 AM (next day) <== Expected\n')

add_time('11:59 PM', '24:05')
print('12:04 AM (2 days later) <== Expected\n')

add_time('8:16 PM', '466:02')
print('6:18 AM (20 days later) <== Expected\n')

add_time('3:30 PM', '2:12', 'Monday')
print('5:42 PM, Monday <== Expected\n')

add_time('2:59 AM', '24:00', 'saturDay')
print('2:59 AM, Sunday (next day) <== Expected\n')

add_time('11:59 PM', '24:05', 'Wednesday')
print('12:04 AM, Friday (2 days later) <== Expected\n')

add_time('8:16 PM', '466:02', 'tuesday')
print('6:18 AM, Monday (20 days later) <== Expected\n')

add_time('3:00 PM', '3:10')
print('6:10 PM <== Expected\n')

add_time('11:30 AM', '2:32', 'Monday')
print('2:02 PM, Monday <== Expected\n')

add_time('11:43 AM', '00:20')
print('12:03 PM <== Expected\n')

add_time('10:10 PM', '3:30')
print('1:40 AM (next day) <== Expected\n')

add_time('11:43 PM', '24:20', 'tueSday')
print('12:03 AM, Thursday (2 days later) <== Expected\n')

add_time('6:30 PM', '205:12')
print('7:42 AM (9 days later) <== Expected\n')