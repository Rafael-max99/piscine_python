#!/usr/bin/env python3

import sys
import importlib
from typing import Any

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError:
    pd = None  # type: ignore
    plt = None  # type: ignore


def check_dependency(module_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, '__version__', 'unknown')
        return (True, version)
    except ImportError:
        return (False, 'not installed')


def load_dependencies() -> tuple[dict[str, Any], list[str]]:
    dependencies = {}
    required_modules = {
            'pandas': 'Data manipulation ready',
            'numpy': 'Numerical computation ready',
            'matplotlib': 'Visualization ready',
            'requests': 'Network access ready (optional)'
            }

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    missing = []

    for module_name, description in required_modules.items():
        installed, version = check_dependency(module_name)

        if installed:
            print(f"[OK] {module_name} ({version}) - {description}")
            dependencies[module_name] = importlib.import_module(module_name)
        else:
            if module_name == 'requests':
                print(f"[SKIP] {module_name} - {description}")
            else:
                print(f"[MISSING] {module_name} - {description}")
                missing.append(module_name)

    return dependencies, missing


def show_installation_instructions(missing: list[str]) -> None:
    if not missing:
        return

    print("\nMISSING DEPENDENCIES!")
    print("\nTo install with pip:")
    print("pip install -r requirements.txt")
    print("\nTo install with Poetry:")
    print("poetry install")
    print("poetry run python loading.py")


def analyze_matrix_data(numpy_module: Any) -> None:
    try:
        print("\nAnalyzing Matrix data...")

        num_points = 1000
        print(f"Processing {num_points} data points...")

        data = numpy_module.random.normal(loc=0, scale=1, size=num_points)

        df = pd.DataFrame({
            'matrix_values': data,
            'timestamp': range(num_points)
            })

        mean = df['matrix_values'].mean()
        std = df['matrix_values'].std()

        print(f"Mean: {mean:.4f}")
        print(f"Std Dev: {std:.4f}")

        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.hist(df['matrix_values'], bins=50, edgecolor='black')
        plt.title('Matrix Data Distribution')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.savefig('matrix_analysis.png')
        plt.close()

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except Exception as e:
        print(f"Error during analysis: {e}")


def main() -> None:
    print()
    dependencies, missing = load_dependencies()

    if missing:
        show_installation_instructions(missing)
        sys.exit(1)

    if 'numpy' in dependencies and 'pandas' in dependencies:
        analyze_matrix_data(dependencies['numpy'])
    else:
        print("\nCannot proceed without pandas and numpy")


if __name__ == "__main__":
    main()
