# Automated_Weather_Data_Pipeline_Version_2
My degree focused heavily on traditional software development, so I wanted to teach myself cloud-native data pipelines. This Is my attempt after the Automated_Weather_Data_Pipeline project to make a serverless ETL pipeline myself without AI.

This automated Python pipeline fetches daily weather data from **OpenWeatherMap.org**, organizes it into a clean format, and appends it to a historical CSV ledger using GitHub Actions. After this, a separate program can be used by users at home to search and view the data collected.

## Features
* **Data Pulling**: This program will pull forecast data from the *openweathermap.org* website 3 times a day via API calls through GitHub Actions workflows.
* **Automated committing and Error Catching**: This program can self commit new data to the repository and run its own backend python unittests.
* **User Interface**: This project has a user program that can be run from home and allows users to search for the weather forecasts for any day the project has records for.

## Requirements
* This project requires users to have **Python version 3.x or higher**.
* To upgrade to this use the command for MacOS
```bash
brew upgrade python
```
for Windows
```bash
winget upgrade Python.Python.3
```
for linux
```bash
sudo apt update && sudo apt install -y python3 python3-pip
```
  
* This project requires the python packages: **requests**, **pandas**, **pyarrow**, and **tkcalendar**
* To install these dependences use the command:
```bash
pip install requests pandas pyarrow tkcalendar
```
## Project API Key Acquisition
* Sign up for a free account at **openweathermap.org**.
* Create an API key with **openweathermap.org**.
* Add your new API key to your GitHub repository secrets as **OPENWEATHERMAP_API_KEY**.
