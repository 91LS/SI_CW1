"""Contains useful tools to work with decision system"""
import decision_system
import universal_tools
import math


def get_system_attributes(system_type_file):
    """Return attributes and their values from system type file"""
    arguments_type, row = [], []
    for line in system_type_file:
        if line.strip() != '':  # true if line isn't empty
            row = line.rstrip().split(' ')  # remove from end all white chars and split row by ' '
            arguments_type.append(decision_system.Attribute(row[0], row[1]))  # return list of Attributes
    return arguments_type


def get_system_objects(system_file, attributes):
    """get info about system, return list of Decision Objects and unique decisions"""
    objects = []
    for line in system_file:
        if line.strip() != '':  # true if line isn't empty
            objects.append(__get_object__(line, attributes))  # append Decision Object to list of objects
    return objects


def __get_object__(line, attributes):
    """Private method. Return Decision Object with list of descriptors and decision"""
    descriptors = []
    line = line.rstrip().split(' ')  # remove from end all white chars and split row by ' '
    for index, attribute in enumerate(attributes):
        descriptor = decision_system.Descriptor(attribute,  # create new descriptor
                                                float(line[index]) if attribute.attribute_type == 'n' else line[index])
        descriptors.append(descriptor)
    decision = line[-1]  # last value from current line is decision for current object
    decision_object = decision_system.DecisionObject(descriptors, decision)
    return decision_object


def get_basic_information_of_numeric_attribute(attribute_values):
    """Return minimum, maximum, average, standard deviation and unique values for numeric attribute"""
    unique_values = [attribute_values[0]]
    minimum = maximum = sum_of_table = attribute_values[0]
    variance = 0

    for number in attribute_values[1:]:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
        sum_of_table += number
        if number not in unique_values:
            unique_values.append(number)

    average = sum_of_table / len(attribute_values)

    for number in attribute_values:
        variance += (number - average) * (number - average)
    variance /= len(attribute_values)
    standard_deviation = math.sqrt(variance)

    return minimum, maximum, average, standard_deviation, unique_values
