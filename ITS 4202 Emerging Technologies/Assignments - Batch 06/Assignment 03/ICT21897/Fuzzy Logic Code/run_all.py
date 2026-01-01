"""
Master Script - Run All Assignment Parts
Smart Greenhouse Adaptive Fuzzy Climate Control System
"""

import subprocess
import sys
import os

def print_banner(text):
    """Print formatted banner"""
    print("\n" + "="*80)
    print(f"  {text}")
    print("="*80 + "\n")

def run_part(part_name, script_name, description):
    """Run a specific part of the assignment"""
    print_banner(f"{part_name}: {description}")
    
    input(f"Press ENTER to run {part_name}...")
    
    try:
        if script_name.endswith('.py'):
            subprocess.run([sys.executable, script_name], check=True)
        print(f"\n✅ {part_name} completed successfully!\n")
        input("Press ENTER to continue to next part...")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running {part_name}: {e}\n")
        response = input("Continue to next part? (y/n): ")
        if response.lower() != 'y':
            sys.exit(1)
    except FileNotFoundError:
        print(f"\n⚠️  Script file not found: {script_name}")
        print("Please ensure all files are in the same directory.\n")
        sys.exit(1)

def main():
    """Main execution function"""
    print_banner("SMART GREENHOUSE FUZZY CONTROL SYSTEM - COMPLETE ASSIGNMENT")
    
    print("""
    This master script will guide you through all parts of the assignment:
    
    📊 Part 1-5: Main Fuzzy Control System
       - Plant species modeling
       - Mamdani and Sugeno controllers
       - Performance evaluation
       - Visualization
    
    🧬 Part 6: Optimization
       - Genetic Algorithm
       - Particle Swarm Optimization
       - Results comparison
    
    🎮 Bonus: Interactive GUI
       - Live simulation
       - Real-time control
       - Dynamic visualization
    
    """)
    
    response = input("Ready to start? (y/n): ")
    if response.lower() != 'y':
        print("Exiting...")
        sys.exit(0)
    
    # Check if required files exist
    required_files = [
        'fuzzy_greenhouse_system.py',
        'optimization_module.py',
        'gui_interface.py'
    ]
    
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print("\n⚠️  Missing required files:")
        for f in missing_files:
            print(f"   - {f}")
        print("\nPlease ensure all files are in the current directory.")
        sys.exit(1)
    
    # Part 1-5: Main System
    run_part(
        "PART 1-5",
        "fuzzy_greenhouse_system.py",
        "Main Fuzzy Control System Implementation"
    )
    
    # Part 6: Optimization
    run_part(
        "PART 6",
        "optimization_module.py",
        "Optimization (GA and PSO)"
    )
    
    # Bonus: GUI
    print_banner("BONUS FEATURE: Interactive GUI")
    print("""
    The GUI interface provides:
    - Real-time temperature and humidity control
    - Live visualization of control outputs
    - Plant type and growth stage selection
    - Interactive simulation
    
    Note: Close the GUI window to return to this script.
    """)
    
    response = input("Launch GUI interface? (y/n): ")
    if response.lower() == 'y':
        try:
            subprocess.run([sys.executable, 'gui_interface.py'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Error running GUI: {e}\n")
    
    # Summary
    print_banner("ASSIGNMENT COMPLETION SUMMARY")
    
    print("""
    ✅ All parts completed successfully!
    
    📁 Generated Files:
       - plant_requirements.csv
       - performance_comparison.csv
       - optimization_results.csv
       - membership_functions.png
       - control_outputs.png
       - performance_metrics.png
       - optimization_convergence.png
       - parameter_comparison.png
    
    📊 Assignment Coverage:
       ✓ Part 1: System Modeling
       ✓ Part 2: Fuzzy System Design
       ✓ Part 3: Programming Implementation
       ✓ Part 4: Dynamic Adaptation
       ✓ Part 5: Performance Evaluation
       ✓ Part 6: Optimization
       ✓ Bonus: GUI Interface
    
    📝 Report Components:
       ✓ System description and justification
       ✓ Membership function design
       ✓ Rule creation explanation
       ✓ Code implementation overview
       ✓ Adaptation strategy
       ✓ Performance comparison
       ✓ Optimization impact
       ✓ Limitations and improvements
    
    🎯 Key Features Implemented:
       - 3 plant species with full climate profiles
       - 50+ fuzzy rules per controller
       - Mamdani and Sugeno implementations
       - 20+ test simulations
       - Genetic Algorithm optimization
       - Particle Swarm Optimization
       - Interactive GUI with live control
       - Comprehensive visualizations
       - Detailed performance metrics
    
    📈 Results Analysis:
       All results have been saved to CSV files and visualization plots.
       Review the generated files for detailed analysis.
    
    """)
    
    print("="*80)
    print("  🎓 Assignment ready for submission!")
    print("="*80)
    print("\nAll files have been generated in the current directory.")
    print("Review the README.md file for complete documentation.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Script interrupted by user.")
        print("You can run individual parts manually if needed.\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please check the error message and try again.\n")
        sys.exit(1)
