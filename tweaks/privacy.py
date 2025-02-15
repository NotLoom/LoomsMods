import subprocess

def disable_telemetry():
    print("Disabling telemetry and data collection...")
    cmd = r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Telemetry disabled.\n")

def disable_cortana():
    print("Disabling Cortana...")
    cmd = r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Cortana disabled.\n")

def remove_edge_preloading():
    print("Removing Microsoft Edge preloading...")
    cmd = r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Edge" /v PreloadEnabled /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Microsoft Edge preloading removed.\n")

# === Undo Functions ===

def undo_disable_telemetry():
    print("Reverting telemetry settings...")
    cmd = r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\DataCollection" /v AllowTelemetry /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Telemetry settings reverted.\n")

def undo_disable_cortana():
    print("Reverting Cortana setting...")
    cmd = r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Cortana setting reverted.\n")

def undo_remove_edge_preloading():
    print("Reverting Edge preloading setting...")
    cmd = r'reg add "HKLM\SOFTWARE\Policies\Microsoft\Edge" /v PreloadEnabled /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Edge preloading setting reverted.\n")
