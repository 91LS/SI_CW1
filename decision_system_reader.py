import os
import my_dialogs
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox

from decision_system import DecisionSystem


class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.system_file_path = ''
        self.type_filename = ''
        self.__initUI__()

    def __initUI__(self):
        self.parent.title("Decision System Reader")
        self.pack(fill=BOTH, expand=True)

        system_load_frame = Frame(self)  # 1st frame
        system_load_frame.pack(fill=X)

        self.load_system_button = Button(system_load_frame, text="Load system",
                                         command=self.__get_system_filename__, width=15)
        self.load_system_button.pack(side=LEFT, padx=5, pady=5)

        self.system_text_box = Entry(system_load_frame)
        self.system_text_box.pack(fill=X, padx=5, expand=True)
        self.system_text_box.configure(state=DISABLED)

        type_load_button = Frame(self) # 2nd frame
        type_load_button.pack(fill=X)

        self.load_type_button = Button(type_load_button, text="Load system type", state=DISABLED,
                                       command=self.__get_system_type_filename__, width=15)
        self.load_type_button.pack(side=LEFT, padx=5, pady=5)

        self.type_text_box = Entry(type_load_button)
        self.type_text_box.pack(fill=X, padx=5, expand=True)
        self.type_text_box.configure(state=DISABLED)

        start_button_frame = Frame(self)  # 3rd frame // GO!
        start_button_frame.pack(fill=X)

        self.start_button = Button(start_button_frame, text="GO!", state=DISABLED, command=self.__get_decision_system__)
        self.start_button.pack(padx=5, pady=5, fill=X)

        empty_frame = Frame(self)  # 4th frame for empty space between third and fifth frame
        empty_frame.pack(pady=10)

        decision_classes_frame = Frame(self)  # 5th frame // Decision Classes
        decision_classes_frame.pack(fill=X)

        self.decision_classes_button = Button(decision_classes_frame, text="Show Decision Classes", state=DISABLED,
                                              command=self.__show_decision_classes__)
        self.decision_classes_button.pack(padx=5, pady=5, fill=X)

        classes_frequency_frame = Frame(self)  # 6th frame // Decision Classes With Frequency
        classes_frequency_frame.pack(fill=X)

        self.classes_frequency_button = Button(classes_frequency_frame, text="Show Decision Classes With Frequencies",
                                               state=DISABLED, command=self.__show_classes_frequency__)
        self.classes_frequency_button.pack(padx=5, pady=5, fill=X)

        min_max_frame = Frame(self)  # 7th frame // Minimum and Maximum Values for Numeric
        min_max_frame.pack(fill=X)

        self.min_max_button = Button(min_max_frame, text="Show Minimum And Maximum Values For Numeric Attributes",
                                     state=DISABLED, command=self.__show_min_max_for_numeric__)
        self.min_max_button.pack(padx=5, pady=5, fill=X)

        unique_attributes_frame = Frame(self)  # 8ht frame // Number Of Unique Values For Attributes
        unique_attributes_frame.pack(fill=X)

        self.attributes_count_button = Button(unique_attributes_frame, command=self.__show_unique_values__,
                                              text="Show Number Of Unique Values For Attributes", state=DISABLED)
        self.attributes_count_button.pack(padx=5, pady=5, fill=X)

        unique_list_frame = Frame(self)  # 9th frame // Unique Values For Attributes
        unique_list_frame.pack(fill=X)

        self.unique_list_button = Button(unique_list_frame, text="Show Unique Values For Attributes", state=DISABLED,
                                         command=self.__show_unique_list__)
        self.unique_list_button.pack(padx=5, pady=5, fill=X)

        standard_deviation_frame = Frame(self)  # 10th frame // Standard Deviation
        standard_deviation_frame.pack(fill=X)

        self.standard_deviation_button = Button(standard_deviation_frame, command=self.__show_standard_deviation__,
                                                text="Show Standard Deviation For Numeric Attributes", state=DISABLED)
        self.standard_deviation_button.pack(padx=5, pady=5, fill=X)

    def __get_system_filename__(self):
        self.system_file_path = filedialog.askopenfilename(filetypes=[('Txt files', '*.txt')])
        self.system_text_box.configure(state=NORMAL)
        self.system_text_box.delete(0, "end")
        self.system_text_box.insert(0, self.system_file_path)
        self.system_text_box.configure(state=DISABLED)
        if self.system_text_box.get() != '':
            self.load_type_button.config(state=NORMAL)

    def __get_system_type_filename__(self):
        system_type = "{}-type.txt".format(os.path.splitext(os.path.basename(self.system_file_path))[0])
        self.type_filename = filedialog.askopenfilename(filetypes=[('Txt files', system_type)])
        self.type_text_box.configure(state=NORMAL)
        self.type_text_box.delete(0, "end")
        self.type_text_box.insert(0, self.type_filename)
        self.type_text_box.configure(state=DISABLED)
        if self.type_text_box.get() != '':
            self.start_button.config(state=NORMAL)

    def __get_decision_system__(self):
        try:
            system_file = open(self.system_file_path)
            info_file = open(self.type_filename)
            self.decision_system = DecisionSystem(system_file, info_file)
            self.__switch_buttons__(TRUE)
            system_file.close()
            info_file.close()
        except FileNotFoundError:
            messagebox.showerror("Error", "Oops! Two files needed!")

    def __are_two_files_loaded__(self):
        return self.system_text_box.get() != '' and self.type_text_box.get() != ''

    def __show_decision_classes__(self):
        my_dialogs.DecisionsDialog(self.parent, self.decision_system.get_decision_classes())

    def __show_classes_frequency__(self):
        my_dialogs.FrequencyDialog(self.parent, self.decision_system.get_decision_classes_with_frequency())

    def __show_min_max_for_numeric__(self):
        my_dialogs.NumericMinMaxDialog(self.parent, self.decision_system.get_numeric_attributes())

    def __show_unique_values__(self):
        my_dialogs.UniqueAttributesDialog(self.parent, self.decision_system.get_attributes())

    def __show_unique_list__(self):
        my_dialogs.UniqueAttributeListDialog(self.parent, self.decision_system.get_attributes())

    def __show_standard_deviation__(self):
        my_dialogs.StandardDeviationDialog(self.parent, self.decision_system.get_numeric_attributes(),
                                           self.decision_system.get_additional_info())

    def __switch_buttons__(self, enable_buttons):
        current_state = NORMAL if enable_buttons else DISABLED  # @TODO: use enable/disable, not only to enable once
        self.decision_classes_button.config(state=current_state)
        self.classes_frequency_button.config(state=current_state)
        self.min_max_button.config(state=current_state)
        self.attributes_count_button.config(state=current_state)
        self.unique_list_button.config(state=current_state)
        self.standard_deviation_button.config(state=current_state)


def main():
    main_frame = Tk()
    ex = MainFrame(main_frame)
    main_frame.geometry("500x350+500+300")
    main_frame.mainloop()


if __name__ == '__main__':
    main()
