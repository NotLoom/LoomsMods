import os
import sys
import subprocess

def remove_bloatware():
    print("Starting Windows 11 debloating process...")
    packages = [
        "*Microsoft.3DBuilder*",
        "*Microsoft.GetHelp*",
        "*Microsoft.Getstarted*",
        "*Microsoft.MicrosoftOfficeHub*",
        "*Microsoft.MicrosoftSolitaireCollection*",
        "*Microsoft.Office.OneNote*",
        "*Microsoft.People*",
        "*Microsoft.SkypeApp*",
        "*Microsoft.WindowsFeedbackHub*",
        "*Microsoft.ZuneMusic*",
        "*Microsoft.ZuneVideo*",
        "*Microsoft.Cortana*"
    ]
    for pkg in packages:
        print(f"Processing package: {pkg}")
        cmd1 = (
            f"Get-AppxPackage -AllUsers -Name \"{pkg}\" -ErrorAction SilentlyContinue "
            f"| ForEach-Object {{ Remove-AppxPackage -Package $_.PackageFullName -ErrorAction SilentlyContinue }}"
        )
        subprocess.run(["powershell", "-Command", cmd1], shell=True)
        cmd2 = (
            f"Get-AppxProvisionedPackage -Online | Where-Object {{ $_.DisplayName -like \"{pkg}\" }} "
            f"| ForEach-Object {{ Remove-AppxProvisionedPackage -Online -PackageName $_.PackageName -ErrorAction SilentlyContinue }}"
        )
        subprocess.run(["powershell", "-Command", cmd2], shell=True)
    print("Debloating complete.\n")

def apply_network_tweaks():
    print("Applying network tweaks...")
    cmds = [
        "netsh int tcp set global autotuninglevel=normal",
        "netsh int tcp set global chimney=enabled",
        "netsh int tcp set global rss=enabled",
        "netsh int tcp set global congestionprovider=ctcp"
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Network tweaks applied.\n")

def set_run_on_startup(enabled):
    reg_key = r'HKCU\Software\Microsoft\Windows\CurrentVersion\Run'
    value_name = "Windows11TweakUtility"
    script_path = os.path.abspath(sys.argv[0])
    if enabled:
        cmd = f'reg add "{reg_key}" /v {value_name} /t REG_SZ /d "{script_path}" /f'
        subprocess.run(cmd, shell=True)
        print("Set to run on startup.")
    else:
        cmd = f'reg delete "{reg_key}" /v {value_name} /f'
        subprocess.run(cmd, shell=True)
        print("Removed run on startup setting.")

# === Undo Functions ===

def undo_remove_bloatware():
    print("Undo for Remove Bloatware is not supported.")

def undo_apply_network_tweaks():
    print("Reverting network tweaks...")
    cmds = [
        "netsh int tcp set global autotuninglevel=disabled",
        "netsh int tcp set global chimney=disabled",
        "netsh int tcp set global rss=disabled",
        "netsh int tcp set global congestionprovider=default"
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True)
    print("Network tweaks reverted.\n")

def undo_run_on_startup():
    reg_key = r'HKCU\Software\Microsoft\Windows\CurrentVersion\Run'
    value_name = "Windows11TweakUtility"
    cmd = f'reg delete "{reg_key}" /v {value_name} /f'
    subprocess.run(cmd, shell=True)
    print("Run on startup entry removed.\n")
