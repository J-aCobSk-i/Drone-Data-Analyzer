from data_loader import load_flight_data
from analyzer import battery_consumption, low_battery, maximum_altitude_time
import numpy as np
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigureCanvas
import matplotlib.pyplot as plt

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

print('---DRONE DATA ANALYZER---')
print('Welcome to the Drone Data Analyzer! This tool helps you analyze and visualize data collected from drone flights.')

class DroneAnalyzerGUI(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Drone Data Analyzer")
        self.geometry("1000x600")

        self.flight_data = None

        
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self,width=250,corner_radius=0)

        self.sidebar.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)

        self.logo_label = ctk.CTkLabel(self.sidebar,text="Drone Analyzer",font=ctk.CTkFont(size=20,weight="bold"))

        self.logo_label.pack(padx=20,pady=(20, 10))

        self.btn_load = ctk.CTkButton(self.sidebar,text="Load Data from CSV",command=self.load_csv_data)

        self.btn_load.pack(padx=20, pady=10)
                           
        self.btn_report = ctk.CTkButton(self.sidebar,text="Show Full Report",command=self.show_report,state="disabled",)

        self.btn_report.pack(padx=20, pady=10)

        self.btn_charts = ctk.CTkButton(self.sidebar,text="Draw Charts",command=self.show_charts,state="disabled",)

        self.btn_charts.pack(padx=20, pady=10)

        self.kmh_switch = ctk.CTkSwitch(self.sidebar, text="Convert to km/h")  

        self.kmh_switch.pack(padx=20, pady=20)

        self.main_panel = ctk.CTkFrame(self)

        self.main_panel.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)

        self.textbox = ctk.CTkTextbox(self.main_panel,font=("Consolas", 14))

        self.textbox.pack(fill="both",expand=True,padx=10,pady=10)

    # Creating charts in main panel  
    def show_charts(self):

        self.clear_main_panel()

        if self.flight_data is None:
                    return

        fig, axes = plt.subplots(2, 2, figsize=(8, 5), facecolor="#242020")

        for ax in axes.flat:
            ax.set_facecolor("#1e1e1e")
            ax.xaxis.label.set_color("white")
            ax.yaxis.label.set_color("white")
            ax.title.set_color("white")
            ax.tick_params(colors="white")
            ax.grid(True, color="#444444")

        axes[0, 0].plot(self.flight_data["Czas lotu [s]"], self.flight_data["Wysokość [m]"], color="#00aaff")  # Flight Time [s], Altitude [m]
        axes[0, 0].set_title("Drone Altitude")

        axes[0, 1].plot(self.flight_data["Czas lotu [s]"], self.flight_data["Prędkość [m/s]"], color="#c3ca39") # Flight Time [s], Speed [m/s]
        axes[0, 1].set_title("Drone Speed")

        axes[1, 0].plot(self.flight_data["Czas lotu [s]"], self.flight_data["Poziom baterii [%]"], color="#159f25") # Flight Time [s], Battery Level [%]
        axes[1, 0].set_title("Drone Battery Level")

        axes[1, 1].plot(self.flight_data["Czas lotu [s]"], self.flight_data["Temperatura [°C]"], color="#a50a0a") # Flight Time [s], Temperature [°C]
        axes[1, 1].set_title("Drone Temperature")

        plt.tight_layout()
        
        self.canvas = FigureCanvas(fig, master=self.main_panel)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

    # Loading data from csv
    def load_csv_data(self):
        file_path = "data/drone_flight_data.csv"

        self.flight_data = load_flight_data(file_path)

        self.textbox.delete("1.0", "end")

        self.textbox.insert("1.0","Flight data loaded successfully!\n\n")

        self.textbox.insert("end",f"Number of measurements: {self.flight_data.shape[0]}\n")

        self.btn_report.configure(state="normal")
        self.btn_charts.configure(state="normal")
    def show_report(self):

        self.clear_main_panel()

        measurements = self.flight_data.shape[0]
        avg_speed = self.flight_data['Prędkość [m/s]'].mean()   # Speed [m/s]
        max_speed = self.flight_data['Prędkość [m/s]'].max()    # Speed [m/s]
        min_speed = self.flight_data['Prędkość [m/s]'].min()    # Speed [m/s]
        avg_alt = self.flight_data['Wysokość [m]'].mean()       # Altitude [m]
        max_alt = self.flight_data['Wysokość [m]'].max()        # Altitude [m]
        min_alt = self.flight_data['Wysokość [m]'].min()        # Altitude [m]
        bat_used = battery_consumption(self.flight_data)
        avg_temp = self.flight_data['Temperatura [°C]'].mean()  # Temperature [°C]
        low_bat_cnt = low_battery(self.flight_data)
        max_alt_t = maximum_altitude_time(self.flight_data)
        max_descent = abs(np.min(np.gradient(self.flight_data["Wysokość [m]"], 2)))     # Altitude [m]
        
        
        report = f"--- FLIGHT REPORT ---\n"
        report += f"Measurements: {measurements}\n"
        report += f"Average Speed: {avg_speed:.2f} m/s"
        
        
        if self.kmh_switch.get() == 1:
            report += f" ({avg_speed * 3.6:.2f} km/h)\n"
        else:
            report += "\n"
        
        report += f"Maximum Speed: {max_speed:.2f} m/s\n"
        report += f"Minimum Speed: {min_speed:.2f} m/s\n"
        report += f"Average Altitude: {avg_alt:.2f} m\n"
        report += f"Maximum Altitude: {max_alt:.2f} m\n"
        report += f"Minimum Altitude: {min_alt:.2f} m\n"
        report += f"Battery Used: {bat_used:.2f}%\n"
        report += f"Average Temperature: {avg_temp:.2f} °C\n\n"
        report += f"! Low battery measurements (<20%): {low_bat_cnt}\n"
        report += f"! Maximum altitude reached at: {max_alt_t:.1f} s\n"
        report += f"! Maximum descend rate: {max_descent:.2f} m/s\n"
        
        self.textbox = ctk.CTkTextbox(self.main_panel, font=("Consolas", 14))
        self.textbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.textbox.insert("1.0", report)



    def clear_main_panel(self):
        # This lets you to clear the right panel before displaying something new
        for widget in self.main_panel.winfo_children():
            widget.destroy()
    
    def on_closing(self):
        if hasattr(self, "canvas"):
            plt.close(self.canvas.figure)

        self.destroy()


app = DroneAnalyzerGUI()
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()








