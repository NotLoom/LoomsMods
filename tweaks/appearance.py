import subprocess

def enable_dark_mode():
    print("Enabling Windows Dark Mode...")
    cmds = [
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v SystemUsesLightTheme /t REG_DWORD /d 0 /f'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Dark Mode enabled.\n")

def custom_accent_color():
    print("Applying custom accent color...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\DWM" /v AccentColor /t REG_DWORD /d 4278228471 /f'
    subprocess.run(cmd, shell=True)
    print("Custom accent color applied.\n")

def taskbar_transparency():
    print("Enabling taskbar transparency...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v EnableTransparency /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Taskbar transparency enabled.\n")

def start_menu_layout_customization():
    print("Customizing Start Menu layout...")
    cmd = r'reg add "HKCU\Software\CustomTweaks" /v StartMenuLayout /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Start Menu layout customized.\n")

# === Undo Functions ===

def undo_enable_dark_mode():
    print("Reverting dark mode...")
    cmds = [
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v SystemUsesLightTheme /t REG_DWORD /d 1 /f'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Dark mode reverted.\n")

def undo_custom_accent_color():
    print("Reverting custom accent color...")
    cmd = r'reg delete "HKCU\Software\Microsoft\Windows\DWM" /v AccentColor /f'
    subprocess.run(cmd, shell=True)
    print("Custom accent color reverted.\n")

def undo_taskbar_transparency():
    print("Reverting taskbar transparency...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v EnableTransparency /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Taskbar transparency reverted.\n")

def undo_start_menu_layout_customization():
    print("Reverting start menu layout customization...")
    cmd = r'reg delete "HKCU\Software\CustomTweaks" /v StartMenuLayout /f'
    subprocess.run(cmd, shell=True)
    print("Start menu layout reverted.\n")
