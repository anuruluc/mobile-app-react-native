import os
import sys
from pathlib import Path

def get_root_dir():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_app_dir():
    return os.path.join(get_root_dir(), 'mobile-app-react-native')

def get_assets_dir():
    return os.path.join(get_app_dir(), 'assets')

def get_js_dir():
    return os.path.join(get_assets_dir(), 'js')

def get_build_dir():
    return os.path.join(get_app_dir(), 'build')

def get_dist_dir():
    return os.path.join(get_app_dir(), 'dist')

def main():
    root_dir = get_root_dir()
    print(f"Root directory: {root_dir}")
    print(f"App directory: {get_app_dir()}")
    print(f"Assets directory: {get_assets_dir()}")
    print(f"JS directory: {get_js_dir()}")
    print(f"Build directory: {get_build_dir()}")
    print(f"Distribution directory: {get_dist_dir()}")

if __name__ == "__main__":
    main()