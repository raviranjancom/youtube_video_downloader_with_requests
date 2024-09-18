import tkinter as tk
from tkinter import ttk,filedialog
import requests
import os
# https://download-cdn.jetbrains.com/python/pycharm-professional-2023.1.2-aarch64.dmg
# https://r4---sn-qxaeenlz.gvt1.com/edgedl/android/studio/install/2024.1.2.12/android-studio-2024.1.2.12-windows.exe?cms_redirect=yes&mh=q1&mip=103.230.154.226&mm=28&mn=sn-qxaeenlz&ms=nvh&mt=1726689144&mv=m&mvi=4&pl=24&shardbypass=sd&smhost=r1---sn-qxaeenl6.gvt1.com

class downloader:
    def __init__(self):
        self.saveto = ""
        self.window = tk.Tk()
        self.window.title("YouTube Downloader")
        self.url_label = tk.Label(text="Enter URL")
        self.url_label.pack()
        self.url_entry = tk.Entry()
        self.url_entry.pack()
        self.browse_button = tk.Button(text="Browser",command = self.browse_file)
        self.browse_button.pack()
        self.download_button = tk.Button(text="Download",command=self.download)
        self.download_button.pack()
        self.window.geometry("400x400")
        self.progress_bar=ttk.Progressbar(self.window, orient = "horizontal", maximum=100,length=300, mode="determinate")
        self.progress_bar.pack()
        self.window.mainloop()

    def download(self):
        url = self.url_entry.get()
        response = requests.get(url, stream=True)
        # total_size_in_bytes = int(response.headers.get("content-length"))
        total_size_in_bytes=100
        if(response.headers.get("content-length")):
            total_size_in_bytes = int(response.headers.get("content-length"))
        block_size = 10000
        self.progress_bar["value"]=0
        fileName = self.url_entry.get().split("/")[-1].split("?")[0]
        if(self.saveto == ""):
            self.saveto =fileName
        """if(self.saveto != ""):
            fileName =os.path.join(self.saveto, fileName) """
        
        print(self.saveto)
        with open(self.saveto, "wb") as f:
            for data in response.iter_content(block_size):
                self.progress_bar["value"] += (100*block_size)/total_size_in_bytes
                print(self.progress_bar["value"])
                self.window.update()
                f.write(data)

    def browse_file(self):
        saveto=filedialog.asksaveasfilename(initialfile = self.url_entry.get().split("/")[-1].split("?")[0])
        self.saveto = saveto

downloader()
