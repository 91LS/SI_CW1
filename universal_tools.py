"""Contains universal tools to work with AI"""
import math


def get_min_and_max(table):
    """Return minimum and maximum"""
    minimum = maximum = table[0]
    for number in table[1:]:
        if number < minimum:
            minimum = number
        if number > maximum:
            maximum = number
    return minimum, maximum


def get_sum(table):
    """Return sum"""
    sum_of_table = 0
    for number in table:
        sum_of_table += number
    return sum_of_table


def get_average(table):
    """Return average"""
    sum_of_table = 0
    for number in table:
        sum_of_table += number
    average = sum_of_table/len(table)
    return average


def get_average_and_standard_deviation_table(table):
    """Return average and standard deviation"""
    sum_of_table, variance = 0, 0

    for number in table:
        sum_of_table += number
    average = sum_of_table/len(table)

    for number in table:
        variance += (number - average) * (number - average)
    variance /= len(table)
    standard_deviation = math.sqrt(variance)
    return average, standard_deviation


def get_column_from_table(table, column_index):
    """Return values from required column"""
    values_from_column = []
    for row in table:
        values_from_column.append(row[column_index])
    return values_from_column


def get_unique(table):
    """Return list of unique values"""
    unique = []
    for number in table:
        if number not in unique:
            unique.append(number)
    return unique


def get_unique_and_frequency(table):
    """Return dictionary of unique values and theirs frequencies"""
    dictionary = {}
    for number in table:
        if number in dictionary:
            dictionary[number] += 1
        else:
            dictionary[number] = 1
    return dictionary


def get_column_if(table, column_index, decision_column_index, decision_value):
    """Return list of values from column equals decision value"""
    column = []
    for row in table:
        if row[decision_column_index] == decision_value:
            column.append((row[column_index]))
    return column
