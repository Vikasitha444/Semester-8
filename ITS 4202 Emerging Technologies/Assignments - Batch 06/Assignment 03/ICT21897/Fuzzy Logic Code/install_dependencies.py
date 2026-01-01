"""
Quick Installation Script
Run this first to install all required dependencies
"""

import subprocess
import sys

def install_packages():
    """Install required packages"""
    
    print("\n" + "="*70)
    print("  📦 INSTALLING REQUIRED PACKAGES")
    print("="*70 + "\n")
    
    packages = [
        'numpy',
        'matplotlib',
        'scikit-fuzzy',
        'pandas',
        'scipy',
        'networkx'
    ]
    
    print("Installing the following packages:")
    for pkg in packages:
        print(f"  - {pkg}")
    print()
    
    for i, package in enumerate(packages, 1):
        print(f"[{i}/{len(packages)}] Installing {package}...")
        try:
            subprocess.check_call([
                sys.executable, 
                '-m', 
                'pip', 
                'install', 
                package,
                '--quiet'
            ])
            print(f"  ✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Error installing {package}: {e}")
            print(f"  Try manually: pip install {package}")
        print()
    
    print("\n" + "="*70)
    print("  ✅ INSTALLATION COMPLETE!")
    print("="*70)
    print("\nYou can now run:")
    print("  python fuzzy_greenhouse_system.py")
    print("  python optimization_module.py")
    print("  python gui_interface.py")
    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    print("""
    This script will install all required Python packages for the
    Smart Greenhouse Fuzzy Control System.
    
    Required packages:
    - numpy (numerical operations)
    - matplotlib (visualizations)
    - scikit-fuzzy (fuzzy logic)
    - pandas (data handling)
    - scipy (scientific computing)
    - networkx (graph operations for skfuzzy)
    
    """)
    
    response = input("Press ENTER to start installation (or Ctrl+C to cancel)...")
    
    try:
        install_packages()
    except KeyboardInterrupt:
        print("\n\n⚠️  Installation cancelled by user.\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("\nTry manual installation:")
        print("  pip install numpy matplotlib scikit-fuzzy pandas scipy networkx")
        sys.exit(1)