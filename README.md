# Stock Price Prediction Tool

## Repository Overview
Welcome to the DS4002 Project 2 Repo for Hudson Noyes, Akan Ndem, and Ali Nilforoush. Our project focused using past stock prices to make predictions of future prices. This repo contains: this README and a LICENSE file and DATA, SCRIPT, and OUTPUT folders.

---

## Section 1: Software and Platform  
This project was developed using the following software and tools:

- **Software Used:**  
  - [Python]
  - [Apla Vantage API]   
  
- **Add-On Packages:**  
  - [PANDAS] – [Used for data manipulation and analysis]
  - [REQUESTS] - [Used for JSON accessing]
  - [MAPLOTLIB.PYPLOT] - [Used for data visualization]
  - [TIME] - [Used for time related functions]
  - [SCIPY] - [Used for analysis of AI detection results]
  - [SKLEARN] - [Used for model training and testing R^2 values]
  - [OS] - [Used for directory access to make code more modular]
 
- **Platform Compatibility:**  
  - ✅ Windows  
  - ✅ macOS (used during project)  
  - ✅ Linux  

Ensure you have the required software installed before proceeding.

---

## Section 2: Project Structure  
Below is a map of the repository, illustrating the hierarchy of files and folders:

📂 Project_Folder/ │-- 📂 DATA/ # Stock price data in csv form from 1999-12-31 - 2025-03-21 │-- 📂 SCRIPTS/ # Code for data processing, training, testing, and analysis │ │-- preliminar_plots.py # Pull data using Alpha Vantage API and store in CSV files for each ticker │ │-- data_preprocessing.py # Data cleaning and normalizing │  │-- model_training.py # training, testing, and analyzing data │-- 📂 RESULTS/ # Output files (graphs) │-- 📂 RESULTS/ # results of analysis performed on data, showing regression model test against data after 2020-04-01 │ │-- README.md # This orientation file
