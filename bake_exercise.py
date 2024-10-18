"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME -  elapsed_bake_time


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.


def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * PREPARATION_TIME
    '''Calculate the preparation time.
 
    :param number_of_layers: int the number of lasagna layers made
    :return: int amount of prep time (in minutes), based on 2 minutes per layer added
 
    This function takes an integer representing the number of layers added to the dish,
    calculating preparation time using a time of 2 minutes per layer added.
    '''

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    PREPARATION_TIME = preparation_time_in_minutes(number_of_layers)
    return PREPARATION_TIME + elapsed_bake_time
    """Calculate the elapsed time.
 
    :param number_of_layers: int the number of layers in the lasagna
    :param elapsed_bake_time: int elapsed cooking time
    :return:  int total time elapsed (in in minutes) preparing and cooking
 
    This function takes two integers representing the number of lasagna layers and the time already spent baking
     and calculates the total elapsed minutes spent cooking the lasagna.
    """

print(elapsed_time_in_minutes(2,10))

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)