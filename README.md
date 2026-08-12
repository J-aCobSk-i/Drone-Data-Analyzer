# 🚁 Drone Data Analyzer

Hi! This is one of my first bigger projects in Python.

I built this application to practice working with **Pandas, NumPy, Matplotlib and CustomTkinter** while doing something related to my interest in drones and aviation.

The idea is pretty simple: load data from a drone flight stored in a CSV file, analyze it and display the results in a small desktop application.

## What can it do?

At the moment, the application can:

* Load drone flight data from a CSV file
* Show basic information about the flight
* Generate a flight report
* Calculate things like:

  * average, minimum and maximum speed
  * average, minimum and maximum altitude
  * battery consumption
  * average temperature
  * number of low-battery measurements
  * time at which maximum altitude was reached
  * maximum descent rate
* Display charts for:

  * altitude
  * speed
  * battery level
  * temperature
* Convert average speed from m/s to km/h

## 🛠️ Built with

* **Python**
* **Pandas** – working with flight data
* **NumPy** – calculations
* **Matplotlib** – charts
* **CustomTkinter** – graphical interface

## 📁 Project structure

```text id="z8p4fc"
DRONE_DATA_ANALYZER/
│
├── data/
│   └── dane_lotu_drona.csv
│
├── analyzer.py
├── data_loader.py
├── main_program.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ▶️ Running the project

Clone the repository:

```bash id="k9v8xw"
git clone https://github.com/YOUR_USERNAME/Drone-Data-Analyzer.git
cd Drone-Data-Analyzer
```

Create a virtual environment:

```bash id="z6c1pd"
python -m venv .venv
```

Activate it on Windows:

```bash id="a8q2nm"
.venv\Scripts\activate
```

Install the required libraries:

```bash id="w0m7rx"
pip install -r requirements.txt
```

Run the application:

```bash id="q3s6kf"
python main_program.py
```

## 📊 Example

The application currently works with a CSV dataset containing drone flight parameters such as flight time, altitude, speed, battery level and temperature.

I plan to expand the project as I learn more about Python and data analysis.

## 🚧 Project status

This is a **beginner/early-stage project**, so the code is definitely not perfect.

I'm still learning Python and there are probably many things that could be done better — whether it's the code structure, error handling, GUI or the way I'm analyzing the data.

**Constructive criticism and suggestions are very welcome!**

If you have any ideas about how I could improve the project or something I should learn next, feel free to let me know.

## 🔮 Possible future improvements

Some things I'd like to add in the future:

* Better GUI
* More flight statistics
* More visualization options
* Better error handling
* Support for other drone data formats
* Flight anomaly detection
* More advanced analysis of drone performance

---

Thanks for checking out the project! 🚁
