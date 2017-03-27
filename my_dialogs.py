from tkinter import *
from tkinter import ttk
from tkinter import Toplevel


class DecisionsDialog:
    def __init__(self, parent, classes):
        top = self.top = Toplevel(parent)
        tree = ttk.Treeview(top, selectmode=NONE)

        tree.heading('#0', text='Class name')

        for index, decision in enumerate(classes):
            tree.insert("", index, text=decision)

        tree.pack()


class FrequencyDialog:
    def __init__(self, parent, classes):
        top = self.top = Toplevel(parent)
        tree = ttk.Treeview(top, selectmode=NONE)

        tree.heading('#0', text='Class name')
        tree["columns"] = "frequency"
        tree.column("frequency", width=150)
        tree.heading("frequency", text="Number of object")

        index = 0
        for decision, frequency in classes.items():
            tree.insert("", index, text=decision, values=frequency)
            index += 1

        tree.pack()


class NumericMinMaxDialog:
    def __init__(self, parent, attributes):
        top = self.top = Toplevel(parent)
        tree = ttk.Treeview(top, selectmode=NONE)

        tree.heading('#0', text='Attribute ID')
        tree["columns"] = ("Minimum", "Maximum")
        tree.column("Minimum", width=100)
        tree.column("Maximum", width=100)
        tree.heading("Minimum", text="Minimum")
        tree.heading("Maximum", text="Maximum")

        for index, attribute in enumerate(attributes):
            tree.insert("", index, text=attribute.id, values=(attribute.minimum,attribute.maximum))

        tree.pack()


class UniqueAttributesDialog:
    def __init__(self, parent, attributes):
        top = self.top = Toplevel(parent)
        tree = ttk.Treeview(top, selectmode=NONE)
        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        tree.heading('#0', text='Attribute ID')
        tree["columns"] = "values"
        tree.column("values", width=200)
        tree.heading("values", text="Number of unique values")
        scrollbar.configure(command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        for index, attribute in enumerate(attributes):
            tree.insert("", index, text=attribute.id, values=attribute.number_of_unique_values)

        tree.pack()


class UniqueAttributeListDialog:
    def __init__(self, parent, attributes):
        top = self.top = Toplevel(parent)
        tree = ttk.Treeview(top, selectmode=NONE)
        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        tree.heading('#0', text='Attribute ID')
        tree["columns"] = "values"
        tree.column("values", width=150)
        tree.heading("values", text="Number of unique values")
        scrollbar.configure(command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        for index, attribute in enumerate(attributes):
            tree.insert("", index, attribute.id, text=attribute.id, values=attribute.number_of_unique_values)
            for unique_value in attribute.unique_values:
                tree.insert(attribute.id, index, text=unique_value)

        tree.pack()


class StandardDeviationDialog:
    def __init__(self, parent, numeric_attributes, additional_info):
        top = self.top = Toplevel(parent)
        tree = ttk.Treeview(top, selectmode=NONE)
        scrollbar_y = Scrollbar(top)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x = Scrollbar(top, orient=HORIZONTAL)
        scrollbar_x.pack(side=BOTTOM, fill=X)

        tree.heading('#0', text='Class name')
        columns = []
        for attribute in numeric_attributes:
            columns.append(attribute.id)
        tree["columns"] = columns
        for column in columns:
            tree.column(column, width=50)
            tree.heading(column, text=column)
        scrollbar_y.configure(command=tree.yview)
        tree.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_x.configure(command=tree.xview)
        tree.configure(xscrollcommand=scrollbar_x.set)

        tree.insert("", 1, 1, text="All classes",
                    values=["{0:0.2f}".format(att.standard_deviation) for att in numeric_attributes])

        index = 2
        for decision_class, attributes in additional_info.items():
            standard_deviations = []
            for attribute, info in attributes.items():
                standard_deviations.append(info['Standard deviation'])
            tree.insert(1, index, text=decision_class, values=["{0:0.2f}".format(i) for i in standard_deviations])

        tree.pack()


def center(win):
    """Center dialogs"""
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))