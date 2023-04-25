import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import *
from predictionMethods import *

class App:
    def __init__(self, root):
        #setting title
        root.title("Network Based Candidate Gene Prediction")
        #setting window size
        width=747
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_869=tk.Label(root)
        GLabel_869["anchor"] = "center"
        GLabel_869["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_869["font"] = ft
        GLabel_869["fg"] = "#393d49"
        GLabel_869["justify"] = "left"
        GLabel_869["text"] = "Network Based Candidate Gene Prediction"
        GLabel_869["relief"] = "ridge"
        GLabel_869.place(x=190,y=20,width=399,height=32)

        GLabel_291=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_291["font"] = ft
        GLabel_291["fg"] = "#333333"
        GLabel_291["justify"] = "center"
        GLabel_291["text"] = "*Upload PPI file:"
        GLabel_291.place(x=30,y=60,width=110,height=30)

        GButton_179=tk.Button(root)
        GButton_179["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_179["font"] = ft
        GButton_179["fg"] = "#000000"
        GButton_179["justify"] = "center"
        GButton_179["text"] = "Generate graph"
        GButton_179.place(x=40,y=90,width=366,height=30)
        GButton_179["command"] = self.GButton_179_command

        GLabel_403=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_403["font"] = ft
        GLabel_403["fg"] = "#333333"
        GLabel_403["justify"] = "center"
        GLabel_403["text"] = "Choose Function"
        GLabel_403.place(x=20,y=210,width=137,height=30)

        global GListBox_147
        GListBox_147=tk.Listbox(root, selectmode=MULTIPLE)
        GListBox_147["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_147["font"] = ft
        GListBox_147["fg"] = "#333333"
        GListBox_147["justify"] = "left"
        GListBox_147.place(x=40,y=240,width=371,height=62)

        self.var = IntVar()

        GRadio_761=tk.Radiobutton(root, variable = self.var, value=1)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_761["font"] = ft
        GRadio_761["fg"] = "#333333"
        GRadio_761["justify"] = "center"
        GRadio_761["text"] = "     Majority Voting Algorithm"
        GRadio_761.place(x=430,y=310,width=172,height=31)
        GRadio_761["command"] = self.GRadio_761_command
        

        GRadio_841=tk.Radiobutton(root, variable = self.var, value=2)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_841["font"] = ft
        GRadio_841["fg"] = "#333333"
        GRadio_841["justify"] = "center"
        GRadio_841["text"] = "Hishigaki Method"
        GRadio_841.place(x=270,y=310,width=130,height=30)
        GRadio_841["command"] = self.GRadio_841_command

        GLabel_233=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_233["font"] = ft
        GLabel_233["fg"] = "#333333"
        GLabel_233["justify"] = "center"
        GLabel_233["text"] = "Choose an Algorithm"
        GLabel_233.place(x=80,y=310,width=166,height=30)

        GLabel_922=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_922["font"] = ft
        GLabel_922["fg"] = "#333333"
        GLabel_922["justify"] = "center"
        GLabel_922["text"] = "Chosen Function(s)"
        GLabel_922.place(x=490,y=60,width=173,height=30)

        global GListBox_889
        GListBox_889=tk.Listbox(root)
        GListBox_889["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_889["font"] = ft
        GListBox_889["fg"] = "#333333"
        GListBox_889["justify"] = "left"
        GListBox_889.place(x=520,y=90,width=188,height=214)

    
        GLabel_887=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_887["font"] = ft
        GLabel_887["fg"] = "#333333"
        GLabel_887["justify"] = "center"
        GLabel_887["text"] = ""
        GLabel_887.place(x=30,y=320,width=70,height=25)

        GButton_147=tk.Button(root)
        GButton_147["bg"] = "#805f5f"
        ft = tkFont.Font(family='Times',size=10)
        GButton_147["font"] = ft
        GButton_147["fg"] = "#ffffff"
        GButton_147["justify"] = "center"
        GButton_147["text"] = "Predict"
        GButton_147.place(x=230,y=350,width=264,height=30)
        GButton_147["command"] = self.GButton_147_command

        GButton_176=tk.Button(root)
        GButton_176["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_176["font"] = ft
        GButton_176["fg"] = "#000000"
        GButton_176["justify"] = "center"
        GButton_176["text"] = "Export result (.txt)"
        GButton_176.place(x=260,y=500,width=178,height=30)
        GButton_176["command"] = self.GButton_176_command


        global GLabel_125
        GLabel_125=tk.Label(root)
        GLabel_125["anchor"] = "nw"
        GLabel_125["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_125["font"] = ft
        GLabel_125["fg"] = "#333333"
        GLabel_125["justify"] = "left"
        # GLabel_125["text"] = "change"
        GLabel_125.place(x=40,y=390,width=664,height=96)

        GLineEdit_125=tk.Entry(root)
        GLineEdit_125["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_125["font"] = ft
        GLineEdit_125["fg"] = "#333333"
        GLineEdit_125["justify"] = "center"
        GLineEdit_125["text"] = "Entry"
        GLineEdit_125.place(x=40,y=170,width=259,height=30)

        GButton_357=tk.Button(root)
        GButton_357["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_357["font"] = ft
        GButton_357["fg"] = "#000000"
        GButton_357["justify"] = "center"
        GButton_357["text"] = "Import"
        GButton_357.place(x=40,y=170,width=364,height=30)
        GButton_357["command"] = self.GButton_357_command

        GLabel_405=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_405["font"] = ft
        GLabel_405["fg"] = "#333333"
        GLabel_405["justify"] = "center"
        GLabel_405["text"] = "*Upload Functional annotations"
        GLabel_405.place(x=30,y=140,width=191,height=30)

        GButton_954=tk.Button(root)
        GButton_954["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_954["font"] = ft
        GButton_954["fg"] = "#000000"
        GButton_954["justify"] = "center"
        GButton_954["text"] = "Add"
        GButton_954.place(x=440,y=260,width=57,height=30)
        GButton_954["command"] = self.GButton_954_command

        
    def GButton_179_command(self):
        global filename_ppi
        global G

        f_types = [('Text Files', '*.tsv')]
        filename_ppi = filedialog.askopenfilename(filetypes=f_types)
        
        G = createGraphObject(filename_ppi)
        GLabel_125["text"] = f"{outputGraphData(G)}"
        # return G

    # graph_variable = GButton_179_command

    def GRadio_761_command(self):
        GLabel_125["text"] = "You selected Majority Voting Method"


    def GButton_954_command(self):
        # selected = [item for item in GListBox_147.curselection()]
        get_content = GListBox_147.get(0, END)
        GListBox_889.insert(END)
        for item in GListBox_147.curselection():
            GListBox_889.insert(END,get_content[item])
        GListBox_147.select_clear(0, tk.END)

    def GRadio_841_command(self):
        GLabel_125["text"] = "You selected Hishigaki Method"
 


    def GButton_147_command(self):

        get_content = GListBox_889.get(0, END)

        if len(get_content) == 1 and self.var.get() == 1:
            # print(type(G))
            candidate_single_MVA = candidateFunctionSingleMVA(f"{get_content[0]}", G, func_annotation_diction, 2)
            GLabel_125["text"] = f"{candidate_single_MVA}"
            print(candidate_single_MVA)

        elif len(get_content) > 1 and self.var.get() == 1:
            # print(type(G))
            candidate_multi_MVA = candidateFunctionMultipleMVA([item for item in get_content], G, func_annotation_diction, 2)
            GLabel_125["text"] = f"{candidate_multi_MVA}"
            print(candidate_multi_MVA)

        elif len(get_content) == 1 and self.var.get() == 2:
            print(type(G))
            candidate_single_Hishigaki = candidateFunctionSingleHishigaki(f"{get_content[0]}", G, func_annotation_diction, 1)
            GLabel_125["text"] = f"{candidate_single_Hishigaki}"
            # print(candidate_single_Hishigaki)

        elif len(get_content) > 1 and self.var.get() == 2:
            print(type(G))
            candidate_multi_Hishigaki = candidateFunctionMultipleHishigaki([item for item in get_content], G, func_annotation_diction, 1)
            GLabel_125["text"] = f"{candidate_multi_Hishigaki}"
            # print(candidate_multi_Hishigaki)

    def GButton_176_command(self):
        print("command")


    def GButton_880_command(self):
        print("command")


    def GButton_357_command(self):
        global filename_fa
        global func_annotation_diction
        global G

        f_types = [('tsv Files', '*.tsv')]
        filename_fa = filedialog.askopenfilename(filetypes=f_types)
        func_annotation_diction = readSeedList(filename_fa)

        GLabel_125["text"] = "Functional annotations uploaded!"
        
        GListBox_147.insert(END)
        for item in set(func_annotation_diction.values()):
            GListBox_147.insert(END, item)
        



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
