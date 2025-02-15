LoomsMods - Windows 11 Tweaking & Optimization Tool

LoomsMods is a modular Windows 11 customization and optimization tool. It allows users to tweak appearance, performance, gaming, network settings, and privacy options.

Features

Appearance Tweaks: Dark mode, custom accent colors, taskbar modifications.

Performance Optimizations: Disable startup delay, disable background apps, optimize Windows services.

Gaming Tweaks: Disable fullscreen optimizations, enable GPU scheduling, reduce input lag.

Privacy Enhancements: Disable telemetry, disable Cortana, remove Edge preloading.

One-Click Optimization: Cleans temporary files, clears caches, and applies performance tweaks automatically.

Installation

Download the latest release (or compile using PyInstaller).

Run LoomsMods.exe as Administrator.

Select your desired tweaks and apply them.

Building from Source

If you want to build your own executable, follow these steps:

Requirements

Python 3.10+

pip install pyinstaller ttkbootstrap

Creating an Executable

Run the following command:

pyinstaller --onefile --noconsole --name LoomsMods main.py

This will generate LoomsMods.exe inside the dist/ folder.

Disclaimer

This software modifies system settings. Use at your own risk. Some tweaks may disable Windows features. Always create a backup before applying modifications.