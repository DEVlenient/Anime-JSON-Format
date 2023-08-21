import tkinter as tk
from tkinter import ttk
import urllib.request as req
import json

class TableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("查詢最新動漫資訊")
        self.root.geometry("1500x400")

        self.tree = ttk.Treeview(root, height=11, show="headings")  # 设置 Treeview 的高度为 20 行
        self.tree["columns"] = ("動畫名稱", "集數", "年份", "季節", "字幕組")
        
        self.tree.heading("#1", text="動畫名稱")
        self.tree.heading("#2", text="集數")
        self.tree.heading("#3", text="年份")
        self.tree.heading("#4", text="季節")
        self.tree.heading("#5", text="字幕組")

        self.tree.column("#1", width=450)  # 设置作品列的宽度为 200 像素
        self.tree.column("#2", width=200)  # 设置狀態列的宽度为 100 像素
        self.tree.column("#3", width=200)  # 设置年份列的宽度为 100 像素
        self.tree.column("#4", width=200)  # 设置季節列的宽度为 100 像素
        self.tree.column("#5", width=200)  # 设置季節列的宽度为 100 像素

        self.tree.pack()

        self.load_data()

    def load_data(self):
        url = "https://d1zquzjgwo9yb.cloudfront.net/?_=1691262454209"
        request = req.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        })

        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")

        data = json.loads(data)

        for i in range(11):
            row_data = data[i][1:6]
            self.tree.insert("", "end", values=row_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = TableApp(root)
    root.mainloop()