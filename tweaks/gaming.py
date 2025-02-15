import subprocess

def disable_fullscreen_optimizations():
    print("Disabling fullscreen optimizations...")
    cmd = r'reg add "HKCU\System\GameConfigStore" /v GameDVR_FSEBehaviorMode /t REG_DWORD /d 2 /f'
    subprocess.run(cmd, shell=True)
    print("Fullscreen optimizations disabled.\n")

def enable_gpu_scheduling():
    print("Enabling GPU scheduling...")
    cmd = r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d 2 /f'
    subprocess.run(cmd, shell=True)
    print("GPU scheduling enabled.\n")

def reduce_input_lag():
    print("Reducing input lag (Low Latency Mode)...")
    cmd = r'reg add "HKCU\Software\CustomTweaks" /v LowLatencyMode /t REG_DWORD /d 1 /f'
    subprocess.run(cmd, shell=True)
    print("Input lag reduced.\n")

def change_dns_for_gaming():
    print("Changing DNS to Cloudflare (1.1.1.1, 1.0.0.1) for better gaming performance...")
    powershell_command = (
        "Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | "
        "ForEach-Object {"
        "Set-DnsClientServerAddress -InterfaceIndex $_.ifIndex "
        "-ServerAddresses 1.1.1.1,1.0.0.1"
        "}"
    )
    subprocess.run(["powershell", "-Command", powershell_command], shell=True)
    print("DNS changed successfully.\n")

# === Undo Functions ===

def undo_disable_fullscreen_optimizations():
    print("Reverting fullscreen optimizations setting...")
    cmd = r'reg add "HKCU\System\GameConfigStore" /v GameDVR_FSEBehaviorMode /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Fullscreen optimizations reverted.\n")

def undo_enable_gpu_scheduling():
    print("Reverting GPU scheduling setting...")
    cmd = r'reg add "HKLM\SYSTEM\CurrentControlSet\Control\GraphicsDrivers" /v HwSchMode /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("GPU scheduling reverted.\n")

def undo_reduce_input_lag():
    print("Reverting input lag reduction...")
    cmd = r'reg add "HKCU\Software\CustomTweaks" /v LowLatencyMode /t REG_DWORD /d 0 /f'
    subprocess.run(cmd, shell=True)
    print("Input lag reduction reverted.\n")

def undo_change_dns_for_gaming():
    print("Reverting DNS settings for gaming...")
    powershell_command = (
        "Get-NetAdapter | Where-Object {$_.Status -eq 'Up'} | "
        "ForEach-Object {"
        "Set-DnsClientServerAddress -InterfaceIndex $_.ifIndex -ResetServerAddresses"
        "}"
    )
    subprocess.run(["powershell", "-Command", powershell_command], shell=True)
    print("DNS settings reverted.\n")
