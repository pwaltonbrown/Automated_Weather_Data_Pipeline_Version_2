# name: User_interface.py
# description: This file contains the user interface for the program.
# Author: Patrick Brown
# date: 10/2/2026

# import libraries
import tkinter as tk
from tkinter import ttk, messagebox as mbox
import pandas as pd
import requests as req
from tkcalendar import DateEntry as dateentry

# global variables

# GitHub url
CSV_URL = "https://github.com/pwaltonbrown/Automated_Weather_Data_Pipeline/blob/main/weather_history.csv?raw=true"

# date column name
DATE_COL = "timestamp"

# fetch data from GitHub
def fetch_data():
    try:
        # read csv
        box1= pd.read_csv(CSV_URL)

        # strip whitespace
        box1.columns = box1.columns.str.strip()

        # check if date column exists
        if DATE_COL not in box1.columns:

            # raise error
            raise ValueError(f"Column '{DATE_COL}' not found in the CSV file. avalailable columns: {list(box.columns)}")

        #strip comas from column
        box1[DATE_COL] = box1[DATE_COL].str.replace(',', '')

        # convert the date column to datetime format
        box1[DATE_COL] = pd.to_datetime(box1[DATE_COL], format='%Y-%m-%d %H:%M:%S')

        # drop rows with no dates
        box1 = box1.dropna(subset=[DATE_COL])

        # return the dataframe
        return box1

    except Exception as e:
        if isinstance(e, ValueError):
            mbox.showerror("Error", f"input was invalid, please try again: {e}")
        elif isinstance(e, req.exceptions.RequestException):
            mbox.showerror("Error", f"failed to fetch data due to request exception, please try again: {e}")
        elif isinstance(e, pd.errors.ParserError):
            mbox.showerror("Error", f"failed to read data due to parser error, please try again: {e}")
        elif isinstance(e, pd.errors.EmptyDataError):
            mbox.showerror("Error", f"failed to read data due to empty data, please try again: {e}")
        elif isinstance(e, pd.errors.DtypeWarning):
            mbox.showerror("Error", f"failed to read data due to column datatype being incorrect, please try again: {e}")a
        else:
            mbox.showerror("Error", f"failed to fetch data, please try again: {e}")

        return None

# create user interface
def interface():

    # create calendar widget
    selectdate = cal.get.date()

    # fetch data
    box2 = fetch_data()

    # check if data was fetched
    if box2 is None:
        return

    # filter by date
    filterbox = box2[box2[DATE_COL].dt.date == selectdate]

    # check if any data was found
    if filterbox.empty:
        
        # display error
        mbox.showinfo("Error", "No data found for the selected date: {selectdate}.")
        
        return

    # copy dataframe
    displaybox = filterbox.copy()

    # format the date column
    displaybox[DATE_COL] = displaybox[DATE_COL].dt.strftime('%Y-%m-%d %H:%M:%S')

    # create a new window for selecting the date
    popup= tk.Toplevel(root)
    popup.title("Weather Data for " + selectdate.strftime("%Y-%m-%d"))
    popup.geometry("700x400")

    # create a frame for the popup
    frame = tk.Frame(popup)
    frame.pack(fill= tk.BOTH, expand=True, padx=10, pady=10)

    # create a table
    columns =list(displaybox.columns)
    table = ttk.Treeview(frame, columns=columns, show="headings")

    # create a scrollbar
    vsb = ttk.Scrollbar(frame, orient="vertical", command=frame.yview)
    hsb = ttk.Scrollbar(frame, orient="horizontal", command=frame.xview)

    # pack the scrollbar
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")

    table.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    # pack the frame
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    # add the columns
    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=130, anchor="center")

    # add the rows
    for _, row in displaybox.iterrows():
        table.insert("", "end", values=list(row))

    # create the main window
    root = tk.Tk()
    root.title("Weather Data for " + selectdate.strftime("%Y-%m-%d"))
    root.geometry("700x400")
    root.eval("tk::PlaceWindow . center")

    label = ttk.Label(root, text="select a date: ", font=("times", 20))
    label.pack(pady=15)

    # create a date entry widget
    cal = dateentry(root, width=12, background='aqua', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
    cal.pack(pady=10)

# submit button
    btn = tk.Button(root, text="Fetch day's data", command=interface, bg="aqua", fg="white", font=("times", 10, "bold"))
    btn.pack(pady=15)

    # start the main loop
    root.mainloop()
            




    
    