import subprocess

def remove_taskbar_items():
    print("Hiding Search/Task View Icons...")
    cmds = [
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v SearchboxTaskbarMode /t REG_DWORD /d 0 /f',
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v ShowTaskViewButton /t REG_DWORD /d 0 /f'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Search/Task View Icons hidden.\n")

def align_taskbar_icons():
    print("Left-aligning the Taskbar icons...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v TaskbarAl /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Taskbar icons left-aligned.\n")

def enable_rounded_corners():
    print("Enabling rounded corners for applications...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\DWM" /v DisableWindowCornerRadius /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Rounded corners enabled.\n")

# === Undo Functions ===

def undo_remove_taskbar_items():
    print("Reverting taskbar items changes...")
    cmds = [
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Search" /v SearchboxTaskbarMode /t REG_DWORD /d 1 /f',
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v ShowTaskViewButton /t REG_DWORD /d 1 /f'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Taskbar items reverted.\n")

def undo_align_taskbar_icons():
    print("Reverting taskbar alignment...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v TaskbarAl /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Taskbar alignment reverted.\n")

def undo_enable_rounded_corners():
    print("Reverting rounded corners setting...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\DWM" /v DisableWindowCornerRadius /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Rounded corners setting reverted.\n")
