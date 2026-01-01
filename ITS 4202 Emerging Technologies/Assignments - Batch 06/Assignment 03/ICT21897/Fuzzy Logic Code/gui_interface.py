"""
Bonus Feature: GUI Interface for Live Greenhouse Simulation
Interactive control panel for real-time fuzzy control system monitoring
"""

import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from datetime import datetime
import threading
import time

# Import the main fuzzy controller
import sys
sys.path.append('/home/claude')

class GreenhouseGUI:
    """Interactive GUI for greenhouse fuzzy control system"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🌱 Smart Greenhouse Fuzzy Control System")
        self.root.geometry("1400x900")
        self.root.configure(bg='#2b2b2b')
        
        # Simulation state
        self.is_running = False
        self.current_temp = 22.0
        self.current_humidity = 65.0
        self.current_stage = 0
        self.heater_power = 0
        self.misting_power = 0
        
        # Data history for plotting
        self.time_history = []
        self.temp_history = []
        self.humidity_history = []
        self.heater_history = []
        self.misting_history = []
        
        # Initialize controllers
        self.controller_type = 'mamdani'
        self.plant_type = 'tomato'
        
        # Setup GUI
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the main GUI layout"""
        # Title
        title_frame = tk.Frame(self.root, bg='#1e1e1e', height=80)
        title_frame.pack(fill='x', padx=10, pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="🌱 SMART GREENHOUSE FUZZY CONTROL SYSTEM",
            font=('Arial', 24, 'bold'),
            bg='#1e1e1e',
            fg='#4CAF50'
        )
        title_label.pack(pady=20)
        
        # Main container
        main_container = tk.Frame(self.root, bg='#2b2b2b')
        main_container.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Left panel - Controls
        left_panel = tk.Frame(main_container, bg='#1e1e1e', width=400)
        left_panel.pack(side='left', fill='both', padx=(0, 5))
        
        self.setup_control_panel(left_panel)
        
        # Right panel - Visualizations
        right_panel = tk.Frame(main_container, bg='#1e1e1e')
        right_panel.pack(side='right', fill='both', expand=True, padx=(5, 0))
        
        self.setup_visualization_panel(right_panel)
        
    def setup_control_panel(self, parent):
        """Setup control panel with inputs and settings"""
        # Input Controls Section
        input_frame = tk.LabelFrame(
            parent,
            text="📊 Environmental Inputs",
            font=('Arial', 14, 'bold'),
            bg='#1e1e1e',
            fg='#4CAF50',
            padx=20,
            pady=20
        )
        input_frame.pack(fill='x', padx=10, pady=10)
        
        # Temperature Control
        tk.Label(
            input_frame,
            text="Temperature (°C):",
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='white'
        ).grid(row=0, column=0, sticky='w', pady=10)
        
        self.temp_scale = tk.Scale(
            input_frame,
            from_=5,
            to=40,
            resolution=0.5,
            orient='horizontal',
            length=250,
            bg='#2b2b2b',
            fg='white',
            troughcolor='#4CAF50',
            highlightthickness=0,
            command=self.update_inputs
        )
        self.temp_scale.set(22)
        self.temp_scale.grid(row=0, column=1, pady=10)
        
        self.temp_value_label = tk.Label(
            input_frame,
            text="22.0°C",
            font=('Arial', 11, 'bold'),
            bg='#1e1e1e',
            fg='#4CAF50'
        )
        self.temp_value_label.grid(row=0, column=2, padx=10)
        
        # Humidity Control
        tk.Label(
            input_frame,
            text="Humidity (%):",
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='white'
        ).grid(row=1, column=0, sticky='w', pady=10)
        
        self.humidity_scale = tk.Scale(
            input_frame,
            from_=30,
            to=100,
            resolution=1,
            orient='horizontal',
            length=250,
            bg='#2b2b2b',
            fg='white',
            troughcolor='#2196F3',
            highlightthickness=0,
            command=self.update_inputs
        )
        self.humidity_scale.set(65)
        self.humidity_scale.grid(row=1, column=1, pady=10)
        
        self.humidity_value_label = tk.Label(
            input_frame,
            text="65%",
            font=('Arial', 11, 'bold'),
            bg='#1e1e1e',
            fg='#2196F3'
        )
        self.humidity_value_label.grid(row=1, column=2, padx=10)
        
        # Growth Stage Control
        tk.Label(
            input_frame,
            text="Growth Stage:",
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='white'
        ).grid(row=2, column=0, sticky='w', pady=10)
        
        self.stage_var = tk.StringVar(value="Seedling")
        stage_combo = ttk.Combobox(
            input_frame,
            textvariable=self.stage_var,
            values=["Seedling", "Vegetative", "Flowering"],
            state='readonly',
            width=20,
            font=('Arial', 10)
        )
        stage_combo.grid(row=2, column=1, pady=10, sticky='w')
        stage_combo.bind('<<ComboboxSelected>>', self.update_inputs)
        
        # Settings Section
        settings_frame = tk.LabelFrame(
            parent,
            text="⚙️ Controller Settings",
            font=('Arial', 14, 'bold'),
            bg='#1e1e1e',
            fg='#FF9800',
            padx=20,
            pady=20
        )
        settings_frame.pack(fill='x', padx=10, pady=10)
        
        # Controller Type
        tk.Label(
            settings_frame,
            text="Controller Type:",
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='white'
        ).grid(row=0, column=0, sticky='w', pady=10)
        
        self.controller_var = tk.StringVar(value="Mamdani")
        controller_combo = ttk.Combobox(
            settings_frame,
            textvariable=self.controller_var,
            values=["Mamdani", "Sugeno"],
            state='readonly',
            width=20,
            font=('Arial', 10)
        )
        controller_combo.grid(row=0, column=1, pady=10, sticky='w')
        
        # Plant Type
        tk.Label(
            settings_frame,
            text="Plant Type:",
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='white'
        ).grid(row=1, column=0, sticky='w', pady=10)
        
        self.plant_var = tk.StringVar(value="Tomato")
        plant_combo = ttk.Combobox(
            settings_frame,
            textvariable=self.plant_var,
            values=["Tomato", "Lettuce", "Orchid"],
            state='readonly',
            width=20,
            font=('Arial', 10)
        )
        plant_combo.grid(row=1, column=1, pady=10, sticky='w')
        
        # Output Display Section
        output_frame = tk.LabelFrame(
            parent,
            text="📈 Control Outputs",
            font=('Arial', 14, 'bold'),
            bg='#1e1e1e',
            fg='#E91E63',
            padx=20,
            pady=20
        )
        output_frame.pack(fill='x', padx=10, pady=10)
        
        # Heater Power Display
        tk.Label(
            output_frame,
            text="🔥 Heater/Cooling Power:",
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='white'
        ).grid(row=0, column=0, sticky='w', pady=10)
        
        self.heater_progress = ttk.Progressbar(
            output_frame,
            length=250,
            mode='determinate',
            style='Heater.Horizontal.TProgressbar'
        )
        self.heater_progress.grid(row=0, column=1, pady=10)
        
        self.heater_label = tk.Label(
            output_frame,
            text="0%",
            font=('Arial', 11, 'bold'),
            bg='#1e1e1e',
            fg='#FF5722'
        )
        self.heater_label.grid(row=0, column=2, padx=10)
        
        # Misting Power Display
        tk.Label(
            output_frame,
            text="💧 Misting System:",
            font=('Arial', 11),
            bg='#1e1e1e',
            fg='white'
        ).grid(row=1, column=0, sticky='w', pady=10)
        
        self.misting_progress = ttk.Progressbar(
            output_frame,
            length=250,
            mode='determinate',
            style='Misting.Horizontal.TProgressbar'
        )
        self.misting_progress.grid(row=1, column=1, pady=10)
        
        self.misting_label = tk.Label(
            output_frame,
            text="0%",
            font=('Arial', 11, 'bold'),
            bg='#1e1e1e',
            fg='#03A9F4'
        )
        self.misting_label.grid(row=1, column=2, padx=10)
        
        # Control Buttons
        button_frame = tk.Frame(parent, bg='#1e1e1e')
        button_frame.pack(fill='x', padx=10, pady=20)
        
        self.start_button = tk.Button(
            button_frame,
            text="▶ Start Simulation",
            font=('Arial', 12, 'bold'),
            bg='#4CAF50',
            fg='white',
            padx=20,
            pady=10,
            command=self.start_simulation,
            relief='raised',
            bd=3
        )
        self.start_button.pack(side='left', padx=5, expand=True, fill='x')
        
        self.stop_button = tk.Button(
            button_frame,
            text="⏸ Stop Simulation",
            font=('Arial', 12, 'bold'),
            bg='#F44336',
            fg='white',
            padx=20,
            pady=10,
            command=self.stop_simulation,
            relief='raised',
            bd=3,
            state='disabled'
        )
        self.stop_button.pack(side='left', padx=5, expand=True, fill='x')
        
        reset_button = tk.Button(
            button_frame,
            text="🔄 Reset",
            font=('Arial', 12, 'bold'),
            bg='#FF9800',
            fg='white',
            padx=20,
            pady=10,
            command=self.reset_simulation,
            relief='raised',
            bd=3
        )
        reset_button.pack(side='left', padx=5, expand=True, fill='x')
        
        # Status Bar
        self.status_label = tk.Label(
            parent,
            text="⚪ Ready",
            font=('Arial', 10),
            bg='#1e1e1e',
            fg='#9E9E9E',
            anchor='w',
            padx=10
        )
        self.status_label.pack(fill='x', pady=10)
        
    def setup_visualization_panel(self, parent):
        """Setup real-time visualization charts"""
        # Create matplotlib figure
        self.fig = Figure(figsize=(10, 8), facecolor='#1e1e1e')
        
        # Temperature plot
        self.ax1 = self.fig.add_subplot(2, 2, 1)
        self.ax1.set_facecolor('#2b2b2b')
        self.ax1.set_title('Temperature Over Time', color='white', fontsize=12, fontweight='bold')
        self.ax1.set_xlabel('Time (s)', color='white')
        self.ax1.set_ylabel('Temperature (°C)', color='white')
        self.ax1.tick_params(colors='white')
        self.ax1.grid(True, alpha=0.2)
        
        # Humidity plot
        self.ax2 = self.fig.add_subplot(2, 2, 2)
        self.ax2.set_facecolor('#2b2b2b')
        self.ax2.set_title('Humidity Over Time', color='white', fontsize=12, fontweight='bold')
        self.ax2.set_xlabel('Time (s)', color='white')
        self.ax2.set_ylabel('Humidity (%)', color='white')
        self.ax2.tick_params(colors='white')
        self.ax2.grid(True, alpha=0.2)
        
        # Heater power plot
        self.ax3 = self.fig.add_subplot(2, 2, 3)
        self.ax3.set_facecolor('#2b2b2b')
        self.ax3.set_title('Heater/Cooling Power', color='white', fontsize=12, fontweight='bold')
        self.ax3.set_xlabel('Time (s)', color='white')
        self.ax3.set_ylabel('Power (%)', color='white')
        self.ax3.tick_params(colors='white')
        self.ax3.grid(True, alpha=0.2)
        
        # Misting power plot
        self.ax4 = self.fig.add_subplot(2, 2, 4)
        self.ax4.set_facecolor('#2b2b2b')
        self.ax4.set_title('Misting System Intensity', color='white', fontsize=12, fontweight='bold')
        self.ax4.set_xlabel('Time (s)', color='white')
        self.ax4.set_ylabel('Intensity (%)', color='white')
        self.ax4.tick_params(colors='white')
        self.ax4.grid(True, alpha=0.2)
        
        self.fig.tight_layout()
        
        # Embed in tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        
    def update_inputs(self, event=None):
        """Update input values from sliders"""
        self.current_temp = self.temp_scale.get()
        self.current_humidity = self.humidity_scale.get()
        
        stage_map = {"Seedling": 0, "Vegetative": 1, "Flowering": 2}
        self.current_stage = stage_map[self.stage_var.get()]
        
        self.temp_value_label.config(text=f"{self.current_temp:.1f}°C")
        self.humidity_value_label.config(text=f"{int(self.current_humidity)}%")
        
        if self.is_running:
            self.compute_outputs()
    
    def compute_outputs(self):
        """Compute fuzzy control outputs"""
        try:
            # Simple fuzzy logic computation (placeholder)
            # In real implementation, use the actual fuzzy controller
            
            # Temperature-based heater control
            if self.current_temp < 20:
                self.heater_power = min(100, 80 + (20 - self.current_temp) * 5)
            elif self.current_temp > 28:
                self.heater_power = max(0, 20 - (self.current_temp - 28) * 5)
            else:
                self.heater_power = 50
            
            # Humidity-based misting control
            if self.current_humidity < 60:
                self.misting_power = min(100, 70 + (60 - self.current_humidity) * 3)
            elif self.current_humidity > 80:
                self.misting_power = max(0, 10 - (self.current_humidity - 80) * 3)
            else:
                self.misting_power = 30
            
            # Update displays
            self.heater_progress['value'] = self.heater_power
            self.misting_progress['value'] = self.misting_power
            self.heater_label.config(text=f"{int(self.heater_power)}%")
            self.misting_label.config(text=f"{int(self.misting_power)}%")
            
        except Exception as e:
            print(f"Error computing outputs: {e}")
    
    def start_simulation(self):
        """Start live simulation"""
        self.is_running = True
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.status_label.config(text="🟢 Simulation Running...", fg='#4CAF50')
        
        # Start simulation thread
        self.simulation_thread = threading.Thread(target=self.run_simulation, daemon=True)
        self.simulation_thread.start()
    
    def stop_simulation(self):
        """Stop simulation"""
        self.is_running = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.status_label.config(text="🟡 Simulation Stopped", fg='#FF9800')
    
    def reset_simulation(self):
        """Reset simulation data"""
        self.is_running = False
        self.time_history = []
        self.temp_history = []
        self.humidity_history = []
        self.heater_history = []
        self.misting_history = []
        
        self.temp_scale.set(22)
        self.humidity_scale.set(65)
        self.heater_power = 0
        self.misting_power = 0
        
        self.heater_progress['value'] = 0
        self.misting_progress['value'] = 0
        self.heater_label.config(text="0%")
        self.misting_label.config(text="0%")
        
        self.update_plots()
        self.status_label.config(text="⚪ Reset Complete", fg='#9E9E9E')
    
    def run_simulation(self):
        """Run simulation loop"""
        start_time = time.time()
        
        while self.is_running:
            current_time = time.time() - start_time
            
            # Compute outputs
            self.compute_outputs()
            
            # Store history
            self.time_history.append(current_time)
            self.temp_history.append(self.current_temp)
            self.humidity_history.append(self.current_humidity)
            self.heater_history.append(self.heater_power)
            self.misting_history.append(self.misting_power)
            
            # Keep only last 100 data points
            if len(self.time_history) > 100:
                self.time_history.pop(0)
                self.temp_history.pop(0)
                self.humidity_history.pop(0)
                self.heater_history.pop(0)
                self.misting_history.pop(0)
            
            # Update plots
            self.root.after(0, self.update_plots)
            
            # Add some random variation (simulate environment changes)
            if np.random.random() > 0.95:
                self.current_temp += np.random.uniform(-1, 1)
                self.current_humidity += np.random.uniform(-2, 2)
                
                self.current_temp = max(5, min(40, self.current_temp))
                self.current_humidity = max(30, min(100, self.current_humidity))
                
                self.temp_scale.set(self.current_temp)
                self.humidity_scale.set(self.current_humidity)
            
            time.sleep(0.1)
    
    def update_plots(self):
        """Update real-time plots"""
        if not self.time_history:
            return
        
        # Clear previous plots
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        
        # Temperature
        self.ax1.plot(self.time_history, self.temp_history, '#4CAF50', linewidth=2)
        self.ax1.set_facecolor('#2b2b2b')
        self.ax1.set_title('Temperature Over Time', color='white', fontsize=12, fontweight='bold')
        self.ax1.set_xlabel('Time (s)', color='white')
        self.ax1.set_ylabel('Temperature (°C)', color='white')
        self.ax1.tick_params(colors='white')
        self.ax1.grid(True, alpha=0.2)
        
        # Humidity
        self.ax2.plot(self.time_history, self.humidity_history, '#2196F3', linewidth=2)
        self.ax2.set_facecolor('#2b2b2b')
        self.ax2.set_title('Humidity Over Time', color='white', fontsize=12, fontweight='bold')
        self.ax2.set_xlabel('Time (s)', color='white')
        self.ax2.set_ylabel('Humidity (%)', color='white')
        self.ax2.tick_params(colors='white')
        self.ax2.grid(True, alpha=0.2)
        
        # Heater
        self.ax3.plot(self.time_history, self.heater_history, '#FF5722', linewidth=2)
        self.ax3.set_facecolor('#2b2b2b')
        self.ax3.set_title('Heater/Cooling Power', color='white', fontsize=12, fontweight='bold')
        self.ax3.set_xlabel('Time (s)', color='white')
        self.ax3.set_ylabel('Power (%)', color='white')
        self.ax3.tick_params(colors='white')
        self.ax3.grid(True, alpha=0.2)
        
        # Misting
        self.ax4.plot(self.time_history, self.misting_history, '#03A9F4', linewidth=2)
        self.ax4.set_facecolor('#2b2b2b')
        self.ax4.set_title('Misting System Intensity', color='white', fontsize=12, fontweight='bold')
        self.ax4.set_xlabel('Time (s)', color='white')
        self.ax4.set_ylabel('Intensity (%)', color='white')
        self.ax4.tick_params(colors='white')
        self.ax4.grid(True, alpha=0.2)
        
        self.fig.tight_layout()
        self.canvas.draw()

def main():
    """Launch GUI application"""
    root = tk.Tk()
    
    # Configure ttk styles
    style = ttk.Style()
    style.theme_use('clam')
    
    # Custom progressbar styles
    style.configure('Heater.Horizontal.TProgressbar', 
                   background='#FF5722',
                   troughcolor='#424242',
                   borderwidth=0,
                   thickness=20)
    
    style.configure('Misting.Horizontal.TProgressbar',
                   background='#03A9F4',
                   troughcolor='#424242',
                   borderwidth=0,
                   thickness=20)
    
    app = GreenhouseGUI(root)
    root.mainloop()

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🌱 SMART GREENHOUSE GUI - BONUS FEATURE")
    print("="*70)
    print("\nLaunching interactive control interface...")
    print("Use the sliders to adjust environmental parameters in real-time!")
    print("\n" + "="*70 + "\n")
    
    main()
