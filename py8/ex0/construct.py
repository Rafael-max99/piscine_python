#!/usr/bin/env python3

import sys
import os
import site


def is_virtual_environment() -> bool:
    return (sys.prefix != sys.base_prefix
            or os.environ.get('VIRTUAL_ENV') is not None
            or os.path.exists(os.path.join(sys.prefix, 'pyvenv.cfg')))


def get_venv_name() -> str:
    if is_virtual_environment():
        return os.path.basename(sys.prefix)
    return "None"


def get_python_executable() -> str:
    return sys.executable


def get_site_packages() -> str:
    if is_virtual_environment():
        major = sys.version_info.major
        minor = sys.version_info.minor
        python_version = f"python{major}.{minor}"
        return os.path.join(sys.prefix, "lib", python_version, "site-packages")
    else:
        packages = site.getsitepackages()
        return packages[0] if packages else "Not found"


def display_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {get_python_executable()}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


def display_inside_venv() -> None:
    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {get_python_executable()}")
    print(f"Virtual Environment: {get_venv_name()}")
    print(f"Environment Path: {sys.prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(get_site_packages())


def main() -> None:
    print()

    if is_virtual_environment():
        display_inside_venv()
    else:
        display_outside_venv()

    print()


if __name__ == "__main__":
    main()
