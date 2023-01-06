import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
import fitz 

class App:
    def __init__(self, root):
        #setting title
        root.title("PDF to Img Converter")
        #setting window size
        width=461
        height=332
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.filename=''
        self.exportDirName=''

        self.select_pdf_btn=tk.Button(root)
        self.select_pdf_btn["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.select_pdf_btn["font"] = ft
        self.select_pdf_btn["fg"] = "#000000"
        self.select_pdf_btn["justify"] = "center"
        self.select_pdf_btn["text"] = "Browse"
        self.select_pdf_btn.place(x=380,y=60,width=70,height=25)
        self.select_pdf_btn["command"] = self.select_pdf_btn_command

        self.select_pdf_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.select_pdf_label["font"] = ft
        self.select_pdf_label["fg"] = "#333333"
        self.select_pdf_label["justify"] = "center"
        self.select_pdf_label["text"] = "Select the PDF File"
        self.select_pdf_label.place(x=0,y=30,width=142,height=30)

        self.pdf_location_textbox=tk.Entry(root)
        self.pdf_location_textbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.pdf_location_textbox["font"] = ft
        self.pdf_location_textbox["fg"] = "#333333"
        self.pdf_location_textbox["justify"] = "left"
        self.pdf_location_textbox["text"] = ""
        self.pdf_location_textbox.place(x=20,y=60,width=346,height=31)

        self.img_export_dir_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.img_export_dir_label["font"] = ft
        self.img_export_dir_label["fg"] = "#333333"
        self.img_export_dir_label["justify"] = "center"
        self.img_export_dir_label["text"] = "Select Image Export Directory"
        self.img_export_dir_label.place(x=0,y=100,width=208,height=30)

        self.img_export_dir_label=tk.Entry(root)
        self.img_export_dir_label["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.img_export_dir_label["font"] = ft
        self.img_export_dir_label["fg"] = "#333333"
        self.img_export_dir_label["justify"] = "left"
        self.img_export_dir_label["text"] = ""
        self.img_export_dir_label.place(x=20,y=140,width=340,height=30)

        self.img_export_browse_btn=tk.Button(root)
        self.img_export_browse_btn["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.img_export_browse_btn["font"] = ft
        self.img_export_browse_btn["fg"] = "#000000"
        self.img_export_browse_btn["justify"] = "center"
        self.img_export_browse_btn["text"] = "Browse"
        self.img_export_browse_btn.place(x=380,y=140,width=70,height=25)
        self.img_export_browse_btn["command"] = self.img_export_browse_btn_command

        self.img_names_textbox=tk.Entry(root)
        self.img_names_textbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.img_names_textbox["font"] = ft
        self.img_names_textbox["fg"] = "#333333"
        self.img_names_textbox["justify"] = "left"
        self.img_names_textbox["text"] = ""
        self.img_names_textbox.place(x=20,y=210,width=431,height=30)

        self.file_name_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.file_name_label["font"] = ft
        self.file_name_label["fg"] = "#333333"
        self.file_name_label["justify"] = "center"
        self.file_name_label["text"] = "Images Name"
        self.file_name_label.place(x=0,y=180,width=117,height=30)

        self.convert_btn=tk.Button(root)
        self.convert_btn["activebackground"] = "#393d49"
        self.convert_btn["bg"] = "#e9ffed"
        ft = tkFont.Font(family='Times',size=10)
        self.convert_btn["font"] = ft
        self.convert_btn["fg"] = "#000000"
        self.convert_btn["justify"] = "center"
        self.convert_btn["text"] = "Convert"
        self.convert_btn.place(x=90,y=260,width=252,height=30)
        self.convert_btn["command"] = self.convert_btn_command

    def select_pdf_btn_command(self):
        print("select pdf btn pressed")
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a PDF File",filetypes = (("PDF Files","*.pdf"),("PDf files","*.pdf")))
        self.pdf_location_textbox.delete(0, tk.END)
        self.pdf_location_textbox.insert(0,self.filename)
        print('file selected is ',self.filename)

    def img_export_browse_btn_command(self):
        print("select directory  btn pressed")
        self.exportDirName = filedialog.askdirectory(initialdir = "/", title = "Select Image Export Directory")
        self.img_export_dir_label.delete(0, tk.END)
        self.img_export_dir_label.insert(0,self.exportDirName)
        print('file selected is ',self.exportDirName)


    def convert_btn_command(self):
        export_img_files_name=self.img_names_textbox.get()
        if self.filename=='' and self.exportDirName=='' and export_img_files_name=='':
           print('cannot be empty')
           tk.messagebox.showwarning(title='Error', message='All the fields are required')
        else: 
            doc = fitz.open(self.filename)  # open document
            i=1
            for page in doc:
                pix = page.get_pixmap()  # render page to an image
                pix.save(f"{self.exportDirName}/{export_img_files_name}_{i}.png")
                i=i+1
            print("Converting Completed")
            tk.messagebox.showinfo(title='Completed', message='PDF has been converted')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
