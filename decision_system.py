"""Object oriented Decision System"""
import system_tools
import universal_tools


class DecisionSystem:
    """Contains list of DecisionObjects and list of Attributes"""
    def __init__(self, system_data, system_type):
        """Create system from data and type files"""
        self.attributes = system_tools.get_system_attributes(system_type)  # list of Attributes
        self.objects = system_tools.get_system_objects(system_data, self.attributes)  # list of Decision Objects
        self.decision_classes = self.__set_decision_classes__()  # dictionary of decisions and count of Decision Objects
        self.__set_numeric_attributes_values__()  # set basic information about all Attributes
        self.decision_classes_additional_info = self.__get_additional_info_about_classes__()  # additional info about DC

    def __get_additional_info_about_classes__(self):
        """Private method. Return additional information about all decision classes from current Decision System"""
        additional_info = {}
        self.__set_dictionary_of_decision_classes__(additional_info)
        self.__correct_dictionary_of_decision_classes(additional_info)
        return additional_info

    def __set_dictionary_of_decision_classes__(self, additional_info):
        """Private method. Set in dictionary structure from current Decision System."""
        for decision_object in self.objects:
            if decision_object.decision in additional_info:
                for descriptor in decision_object.descriptors:
                    if descriptor.attribute.attribute_type == 'n':
                        additional_info[decision_object.decision][descriptor.attribute.id][0].append(descriptor.value)

            else:
                additional_info[decision_object.decision] = {}
                for descriptor in decision_object.descriptors:
                    if descriptor.attribute.attribute_type == 'n':
                        additional_info[decision_object.decision][descriptor.attribute.id] = [[descriptor.value]]

    def __correct_dictionary_of_decision_classes(self, additional_info):
        """Private method. Remove unnecessary information and format dictionary to final version"""
        for decision in additional_info:
            for attribute in additional_info[decision]:
                info = system_tools.get_basic_information_of_numeric_attribute(additional_info[decision][attribute][0])
                del additional_info[decision][attribute][0]
                info_dictionary = {'Minimum': info[0],
                                   'Maximum:': info[1],
                                   'Average': info[2],
                                   'Standard deviation': info[3]}
                additional_info[decision][attribute] = info_dictionary

    def __set_decision_classes__(self):
        """Private method. Count all unique decision in current Decision System"""
        decisions = []
        for decision_object in self.objects:
            decisions.append(decision_object.decision)
        return universal_tools.get_unique_and_frequency(decisions)

    def __set_numeric_attributes_values__(self):
        """Private method. Set basic information about Attributes from current Decision System"""
        for index, attribute in enumerate(self.attributes):
            attribute_values = self.__get_values_from_attribute__(index)
            attribute.__set_basic_values__(attribute_values)

    def __get_values_from_attribute__(self, index):
        """Get values of Attribute from current Decision System by index"""
        attribute_values = []
        for decision_object in self.objects:
            attribute_values.append(decision_object.descriptors[index].value)
        return attribute_values

    def get_decision_classes(self):
        return list(self.decision_classes.keys())  # return decision classes from Decision System

    def get_decision_classes_with_frequency(self):
        return self.decision_classes  # return decisions and frequencies from Decision System

    def get_numeric_attributes(self):
        numeric_attributes = []
        for attribute in self.attributes:
            if attribute.attribute_type == 'n':
                numeric_attributes.append(attribute)
        return numeric_attributes  # return list of Attributes

    def get_attributes(self):
        return self.attributes

    def get_additional_info(self):
        return self.decision_classes_additional_info


class DecisionObject:
    """Contains list of Descriptors"""
    def __init__(self, descriptors, decision):
        self.descriptors = descriptors
        self.decision = decision


class Descriptor:
    """Information about descriptor. Contains Attribute and his value"""
    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value


class Attribute:
    """Information about attribute. Contains id, type, basic calculated values."""
    def __init__(self, id, attribute_type):
        self.id = id
        self.attribute_type = attribute_type

    def __set_basic_values__(self, values_of_attribute):
        """Set information about min, max, average and standard deviation in current attribute from current system"""
        if self.attribute_type == 'n':
            self.minimum, \
            self.maximum, \
            self.average, \
            self.standard_deviation, \
            self.unique_values = system_tools.get_basic_information_of_numeric_attribute(values_of_attribute)
        else:
            self.unique_values = universal_tools.get_unique(values_of_attribute)
        self.number_of_unique_values = len(self.unique_values)
