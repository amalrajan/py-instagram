import bs4 as bs
import urllib.request
import os
from tkinter import *
import tkinter.filedialog as filedialog
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox


class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.resizable(False, False)
        self.geometry("700x380+{0}+{1}".format(
            self.winfo_screenwidth() // 2 - 350, self.winfo_screenheight() // 2 - 190))

        self.var0 = StringVar()
        self.var1 = StringVar()
        self.var2 = StringVar()
        self.progress_bar_val = 0

        self.l_title = Label(text="Instagram Image Downloader", font=("Segoe UI", 18))
        self.l_url = Label(text="URL:", font=("Segoe UI", 11))
        self.l_output_location = Label(text="Destination: ", font=("Segoe UI", 11))
        self.e_url = ttk.Entry(self, textvariable=self.var0, font=("Segoe UI", 10))
        self.b_attach_batch = ttk.Button(self, text="Batch", command=self.batch_download)
        self.e_output_directory = ttk.Entry(text="Enter the output location", textvariable=self.var2,
                                            font=("Segoe UI", 10))
        self.b_browse_directory = ttk.Button(self, text="Browse", command=self.browse_directory)
        self.b_download = ttk.Button(self, text="Download Image(s)", command=self.check_entries)
        self.b_advanced_options = ttk.Button(self, text="Advanced Options", command=self.advanced_options)
        self.p_download_progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")

        self.l_title.place(x=350, y=50, anchor=CENTER)
        self.l_url.place(x=60, y=120)
        self.e_url.place(x=100, y=120, width=450, height=30)
        self.b_attach_batch.place(x=560, y=120, width=120, height=30)
        self.l_output_location.place(x=10, y=170)
        self.e_output_directory.place(x=100, y=170, height=30, width=450)
        self.b_browse_directory.place(x=560, y=170, height=30, width=120)
        self.b_download.place(x=560, y=270, height=35, width=120)
        self.b_advanced_options.place(x=560, y=220, width=120, height=30)
        self.p_download_progress.place(x=100, y=270)

    def browse_directory(self):
        self.directory = filedialog.askdirectory()
        self.var2.set(self.directory)

    def advanced_options(self):
        pass

    def check_entries(self):
        self.entries = ["self.e_url", "self.e_output_directory"]
        for entry in self.entries:
            if eval(entry + ".get()") == "":
                messagebox.showinfo("Insufficient data", message="Please check if you've filled all the details.")
                break
        else:
            self.result = messagebox.askyesno("Start downloading?",
                                              message="Are you sure you want to start the download?")
            if self.result:
                self.start_download()

    def batch_download(self):
        self.batchfile_location = filedialog.askopenfilename()
        if str(self.batchfile_location)[-3:] == 'txt':
            with open(self.batchfile_location) as self.batchfile:
                self.data = self.batchfile.read().replace('\n', ';')
                self.var0.set(self.data)

    def run_progress_bar(self):
        self.progress_bar_val += 1
        self.p_


    def start_download(self):
        self.download_list = self.e_url.get().split(';')
        self.p_download_progress["value"] = self.progress_bar_val
        self.p_download_progress["maximum"] = len(self.download_list)

        self.run_progress_bar()
        self.incrementor = 1

        for url in self.download_list:
            self.source = urllib.request.urlopen(url)
            self.soup = bs.BeautifulSoup(self.source, "html5lib")
            self.image = self.soup.find("meta", property="og:image")["content"]
            self.image_title = "image{}.jpg".format(self.incrementor)
            self.incrementor += 1
            self.image_path = os.path.join(self.e_output_directory.get(), self.image_title)
            with open(self.image_path, 'wb') as self.new_image:
                self.new_image.write(urllib.request.urlopen(self.image).read())


app = MainWindow()
app.mainloop()
