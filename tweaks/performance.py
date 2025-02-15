import subprocess

def disable_startup_delay():
    print("Disabling startup delay...")
    cmd = r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Startup delay disabled.\n")

def disable_background_apps():
    print("Disabling background apps...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Background apps disabled.\n")

def optimize_windows_services():
    print("Optimizing Windows services...")
    cmds = [
        r'sc config DiagTrack start= disabled',
        r'sc config XblGameSave start= disabled',
        r'sc config XblAuthManager start= disabled',
        r'sc config XboxNetApiSvc start= disabled'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Windows services optimized.\n")

# === Undo Functions ===

def undo_disable_startup_delay():
    print("Reverting startup delay setting...")
    cmd = r'reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /t REG_DWORD /d 2000 /f'
    subprocess.run(cmd, shell=True)
    print("Startup delay reverted.\n")

def undo_disable_background_apps():
    print("Reverting background apps setting...")
    cmd = r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications" /v GlobalUserDisabled /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Background apps setting reverted.\n")

def undo_optimize_windows_services():
    print("Reverting Windows services optimization...")
    cmds = [
        r'sc config DiagTrack start= auto',
        r'sc config XblGameSave start= auto',
        r'sc config XblAuthManager start= auto',
        r'sc config XboxNetApiSvc start= auto'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Windows services optimization reverted.\n")
