import json
import os

CONFIG_FILE = "config.json"

def load_config():
    default_config = {
        "debloat": False,
        "network_tweaks": False,
        "run_on_startup": False,
        "remove_taskbar_items": False,
        "align_taskbar": False,
        "rounded_corners": False,
        "dark_mode": False,
        "custom_accent_color": False,
        "taskbar_transparency": False,
        "start_menu_layout": False,
        "disable_startup_delay": False,
        "disable_background_apps": False,
        "optimize_windows_services": False,
        "disable_fullscreen_optimizations": False,
        "enable_gpu_scheduling": False,
        "reduce_input_lag": False,
        "change_dns_for_gaming": False,
        "disable_telemetry": False,
        "disable_cortana": False,
        "remove_edge_preloading": False,
        "delete_temp_files": False,
        "clear_prefetch": False,
        "clear_wu_cache": False,
        "clean_standby_list": False
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                config = json.load(f)
            default_config.update(config)
        except Exception as e:
            print("Error loading config:", e)
    return default_config

def save_config(config):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
        print("Config saved successfully.")
    except Exception as e:
        print("Error saving config:", e)
