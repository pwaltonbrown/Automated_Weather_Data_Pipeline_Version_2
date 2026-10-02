# name: User_interface.py
# description: This file contains the user interface for the program.
# Author: Patrick Brown
# date: 10/2/2026

# import libraries
import tkinter as tk
from tkinter import ttk, messagebox as mbox
import sys
import pandas as pd
import requests as req
from io import StringIO as sio
from tkcalendar import DateEntry as cal

# global variables


# GitHub url
CSV_URL = "https://github.com/pwaltonbrown/Automated_Weather_Data_Pipeline/blob/main/weather_history.csv?raw=true"

# date column name
DATE_COL = "timestamp"

def fetch_data():
    try:
        # read csv
        box= pd.read_csv(CSV_URL)

        # strip whitespace
        box.columns = box.columns.str.strip()

        # check if date column exists
        if DATE_COL not in box.columns:

            # raise error
            raise ValueError(f"Column '{DATE_COL}' not found in the CSV file. avalailable columns: {list(box.columns)}")

        #strip comas from column
        box[DATE_COL] = box[DATE_COL].str.replace(',', '')

        # convert the date column to datetime format
        box[DATE_COL] = pd.to_datetime(box[DATE_COL], format='%Y-%m-%d %H:%M:%S')

        # drop rows with no dates
        box = box.dropna(subset=[DATE_COL])

        # return the dataframe
        return box

    except Exception as e:
        mbox.showerror("Error", f"failed to fetch data: {e}")

        return None

def interface():
    pass
        
