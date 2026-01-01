# 🌱 Smart Greenhouse Adaptive Fuzzy Climate Control System

## Course Assignment: Fuzzy Logic and Control Systems

### 📋 Assignment Overview

This project implements a comprehensive adaptive fuzzy control system for greenhouse climate management using Python. The system controls temperature and humidity based on plant species and growth stages, featuring both Mamdani and Sugeno fuzzy controllers.

---

## 🎯 Project Features

### ✅ All Assignment Parts Completed

- **Part 1: System Modeling** ✓
  - 3 plant species (Tomato, Lettuce, Orchid)
  - Climate requirements for each growth stage
  - Comprehensive comparison tables
  - Justification for fuzzy logic vs PID

- **Part 2: Fuzzy System Design** ✓
  - 5+ membership functions per input
  - Mamdani controller implementation
  - Takagi-Sugeno controller implementation
  - 50+ fuzzy rules for each controller

- **Part 3: Programming Implementation** ✓
  - Full Python implementation with skfuzzy
  - Custom fuzzy logic computations
  - Object-oriented design

- **Part 4: Dynamic Adaptation** ✓
  - Automatic plant type switching
  - Growth stage adaptation
  - Real-time parameter adjustment
  - Comprehensive adaptation logging

- **Part 5: Performance Evaluation** ✓
  - 20+ random test simulations
  - Detailed performance metrics
  - Mamdani vs Sugeno comparison
  - Statistical analysis

- **Part 6: Optimization** ✓
  - Genetic Algorithm implementation
  - Particle Swarm Optimization
  - Before/after comparison
  - Convergence analysis

- **Bonus Features** ✓
  - Interactive GUI with live simulation
  - Real-time visualization
  - Dynamic control adjustment

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Manual Installation (if needed)

```bash
pip install numpy matplotlib scikit-fuzzy pandas scipy
```

---

## 📦 Project Structure

```
greenhouse-fuzzy-control/
│
├── fuzzy_greenhouse_system.py    # Main controller implementation
├── optimization_module.py          # GA and PSO optimization
├── gui_interface.py                # Interactive GUI (Bonus)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🎮 How to Run

### 1. Main Simulation (Parts 1-5)

```bash
python fuzzy_greenhouse_system.py
```

**Output:**
- Plant requirements comparison table
- Controller performance metrics
- Mamdani vs Sugeno analysis
- Multiple visualization plots
- CSV files with results

### 2. Optimization Module (Part 6)

```bash
python optimization_module.py
```

**Output:**
- Genetic Algorithm optimization results
- PSO optimization results
- Convergence plots
- Parameter comparison charts

### 3. GUI Interface (Bonus)

```bash
python gui_interface.py
```

**Features:**
- Real-time temperature and humidity control
- Live output visualization
- Plant type and growth stage selection
- Controller type switching
- Interactive graphs

---

## 📊 Generated Files

After running the simulations, you'll get:

### CSV Files
- `plant_requirements.csv` - Plant climate requirements
- `performance_comparison.csv` - Controller performance metrics
- `optimization_results.csv` - Optimization outcomes

### Visualizations
- `membership_functions.png` - Fuzzy membership functions
- `control_outputs.png` - Control output comparison
- `performance_metrics.png` - Performance analysis
- `optimization_convergence.png` - Optimization progress
- `parameter_comparison.png` - Before/after parameters

---

## 🧪 Test Cases

The system automatically generates:
- 20 random environmental scenarios
- Varying temperature (10-35°C)
- Varying humidity (35-95%)
- Different growth stages
- Multiple plant types

---

## 📈 Performance Metrics

The system evaluates controllers based on:

1. **Response Time** - Speed of control computation (ms)
2. **Average Error** - Deviation from target conditions
3. **Energy Usage** - Combined heater and misting power (%)
4. **Smoothness Score** - Control output stability

---

## 🌿 Supported Plant Species

### 1. Tomato 🍅
- **Seedling:** 20-25°C, 65-75% humidity
- **Vegetative:** 22-28°C, 60-70% humidity
- **Flowering:** 18-24°C, 50-65% humidity

### 2. Lettuce 🥬
- **Seedling:** 15-20°C, 70-80% humidity
- **Vegetative:** 15-22°C, 65-75% humidity
- **Flowering:** 12-18°C, 60-70% humidity

### 3. Orchid 🌸
- **Seedling:** 22-28°C, 75-85% humidity
- **Vegetative:** 24-30°C, 70-80% humidity
- **Flowering:** 20-26°C, 65-75% humidity

---

## 🔧 Controller Details

### Mamdani Controller
- **Type:** Mamdani fuzzy inference
- **Defuzzification:** Centroid method
- **Rules:** 50+ fuzzy rules
- **Best for:** Human-interpretable logic

### Sugeno Controller
- **Type:** Takagi-Sugeno fuzzy inference
- **Defuzzification:** Weighted average
- **Rules:** 50+ fuzzy rules
- **Best for:** Computational efficiency

---

## 🎯 Why Fuzzy Logic?

### Advantages over Crisp Logic:
1. **Handles Uncertainty** - Real-world sensors have noise
2. **Smooth Control** - No abrupt changes in output
3. **Natural Language Rules** - Easy to understand and maintain
4. **Multiple Inputs** - Considers temp, humidity, growth stage

### Advantages over PID:
1. **Nonlinear Systems** - Better for complex plant responses
2. **Multi-objective** - Controls multiple outputs simultaneously
3. **Linguistic Variables** - Uses human expert knowledge
4. **Adaptability** - Easy to add new rules

---

## 📖 Code Highlights

### Membership Functions
```python
# 5 fuzzy sets for Temperature
- very_cold: 5-16°C
- cold: 12-22°C
- optimal: 20-28°C
- warm: 26-34°C
- very_warm: 32-40°C
```

### Adaptive Features
```python
# Dynamic plant type switching
controller.adapt_to_plant('lettuce')

# Automatic parameter adjustment
heater, misting = controller.compute_with_adaptation(
    temp=22, humid=65, growth_stage=0
)
```

### Optimization
```python
# Genetic Algorithm
ga = GeneticAlgorithmOptimizer(population_size=50)
best_params = ga.optimize(test_data)

# Particle Swarm
pso = ParticleSwarmOptimizer(num_particles=30)
best_params = pso.optimize(test_data)
```

---

## 🎨 GUI Features

- **Real-time Control Sliders**
  - Temperature: 5-40°C
  - Humidity: 30-100%
  
- **Growth Stage Selection**
  - Seedling
  - Vegetative
  - Flowering
  
- **Live Visualizations**
  - Temperature trends
  - Humidity trends
  - Heater power output
  - Misting system intensity
  
- **Controller Options**
  - Mamdani / Sugeno switching
  - Plant type selection

---

## 📝 Report Components

The implementation addresses all report requirements:

1. ✅ System description and justification
2. ✅ Membership function design reasoning
3. ✅ Rule creation explanation
4. ✅ Code implementation overview
5. ✅ Adaptation strategy details
6. ✅ Performance comparison analysis
7. ✅ Optimization impact assessment
8. ✅ Real-world limitations discussion

---

## 🚨 Real-World Limitations

1. **Sensor Accuracy** - Real sensors have ±0.5°C error
2. **Actuator Lag** - Heaters/misters take time to respond
3. **External Factors** - Sun radiation, wind not modeled
4. **Plant Variability** - Individual plant differences
5. **Energy Constraints** - Power availability limits
6. **Maintenance** - System degradation over time

---

## 🔮 Future Improvements

1. **Machine Learning Integration**
   - Reinforcement learning for rule evolution
   - Neural-fuzzy hybrid systems
   
2. **IoT Integration**
   - Real sensor data integration
   - Cloud-based monitoring
   
3. **Multi-zone Control**
   - Different zones for different plants
   - Coordinated control strategy
   
4. **Predictive Control**
   - Weather forecast integration
   - Energy price optimization
   
5. **Mobile App**
   - Remote monitoring
   - Alert notifications

---

## 📚 References

1. Mamdani, E.H. (1974). Application of fuzzy algorithms for control
2. Takagi, T. & Sugeno, M. (1985). Fuzzy identification of systems
3. Zadeh, L.A. (1965). Fuzzy sets

---

## 👨‍💻 Technical Details

### Development Environment
- **Language:** Python 3.8+
- **Libraries:** NumPy, Matplotlib, scikit-fuzzy, Pandas
- **GUI Framework:** Tkinter
- **Optimization:** Custom GA and PSO implementations

### System Requirements
- **RAM:** 4GB minimum
- **CPU:** Any modern processor
- **Storage:** 100MB free space
- **OS:** Windows, macOS, or Linux

---

## 📞 Support

For questions or issues:
- Check the code comments for detailed explanations
- Review the generated CSV files for data
- Examine the visualization plots for insights

---

## ✅ Assignment Checklist

- [x] 3 plant species defined
- [x] Climate requirements table
- [x] Fuzzy logic justification
- [x] 5+ membership functions per input
- [x] Mamdani controller implemented
- [x] Sugeno controller implemented
- [x] 25+ rules per controller (50+ actually)
- [x] Dynamic adaptation mechanism
- [x] 20+ test simulations
- [x] Performance comparison table
- [x] Genetic Algorithm optimization
- [x] PSO optimization
- [x] Before/after analysis
- [x] Comprehensive documentation
- [x] GUI interface (Bonus)

---

## 🏆 Project Highlights

- **Lines of Code:** 2000+
- **Fuzzy Rules:** 50+ per controller
- **Test Cases:** 20+ automated scenarios
- **Visualizations:** 5+ detailed charts
- **Optimization Methods:** 2 (GA + PSO)
- **Plant Species:** 3 fully modeled
- **Documentation:** Complete with examples

---

## 💡 Tips for Running

1. **Start Simple:** Run main simulation first
2. **Check Outputs:** Review CSV files and plots
3. **Try Optimization:** See improvement results
4. **Explore GUI:** Interactive live control
5. **Modify Parameters:** Experiment with values

---

## 🎓 Learning Outcomes

This project demonstrates:
- Fuzzy logic controller design
- Real-time adaptive systems
- Performance optimization techniques
- Software engineering practices
- Data visualization skills
- GUI development
- Algorithm comparison

---

**Project Status:** ✅ Complete and Ready for Submission

**Estimated Completion Time:** All parts implemented successfully

**Code Quality:** Production-ready with comprehensive documentation

---

*Happy Greenhouse Controlling! 🌱*
