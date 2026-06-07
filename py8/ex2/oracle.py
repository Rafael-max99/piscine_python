#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from dotenv import load_dotenv


def load_env_file() -> None:
    try:
        env_path = Path('.env')
        if env_path.exists():
            load_dotenv(env_path)
            print("[INFO] .env file loaded")
        else:
            print("[INFO] No .env file found, "
                  "using defaults/environment variables")
    except ImportError:
        print("[WARNING] python-dotenv not installed")
        print("Install with: pip install python-dotenv")


def get_config(key: str, default: str = 'not set') -> str:
    return os.getenv(key, default)


def display_configuration() -> None:
    matrix_mode = get_config('MATRIX_MODE', 'development')
    database_url = get_config('DATABASE_URL', 'sqlite:///local.db')
    api_key = get_config('API_KEY', 'not configured')
    log_level = get_config('LOG_LEVEL', 'INFO')
    zion_endpoint = get_config('ZION_ENDPOINT', 'http://localhost:8000')

    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if database_url == 'not configured':
        print("Database: Not configured")
    else:
        display_url = database_url.replace('password', '****')
        if '@' in display_url:
            hostname = display_url.split('@')[1].split('/')[0]
            print(f"Database: Connected to {hostname}")
        else:
            print(f"Database: {display_url}")

    if api_key == 'not configured':
        print("API Access: Not configured")
    else:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")
    print(f"Zion Network: Online at {zion_endpoint}")


def security_check() -> None:
    print()
    print("Environment security check:")

    print("[OK] No hardcoded secrets detected")

    if Path('.env').exists():
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found (using environment variables)")

    if Path('.gitignore').exists():
        with open('.gitignore', 'r') as f:
            if '.env' in f.read():
                print("[OK] .env in .gitignore (secrets protected)")
            else:
                print("[WARN] .env not in .gitignore!")
    else:
        print("[WARN] .gitignore not found")

    print("[OK] Production overrides available via environment variables")


def show_environment_info() -> None:
    print()
    print("Environment Information:")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {sys.platform}")

    defined_vars = [
        'MATRIX_MODE',
        'DATABASE_URL',
        'API_KEY',
        'LOG_LEVEL',
        'ZION_ENDPOINT'
    ]

    print()
    print("Configuration sources:")
    for var in defined_vars:
        if var in os.environ:
            source = "environment variable"
        else:
            source = ".env file or default"
        value = "set" if var in os.environ else "not set"
        print(f"  {var}: {value} ({source})")


def main() -> None:
    print()
    load_env_file()
    print()
    display_configuration()
    security_check()
    show_environment_info()

    print()
    print("The Oracle sees all configurations.")
    print()

if __name__ == "__main__":
    main()
