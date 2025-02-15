import os
import shutil
import subprocess

def delete_temp_files():
    print("Deleting temporary files...")
    temp_dir = os.environ.get("TEMP")
    try:
        for root, dirs, files in os.walk(temp_dir):
            for f in files:
                try:
                    os.remove(os.path.join(root, f))
                except Exception:
                    pass
            for d in dirs:
                try:
                    shutil.rmtree(os.path.join(root, d))
                except Exception:
                    pass
        print("Temporary files deleted.\n")
    except Exception as e:
        print("Error deleting temporary files:", e)

def clear_prefetch_superfetch():
    print("Clearing Prefetch & Superfetch files...")
    prefetch_dir = r"C:\Windows\Prefetch"
    try:
        for filename in os.listdir(prefetch_dir):
            file_path = os.path.join(prefetch_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception:
                pass
        print("Prefetch & Superfetch files cleared.\n")
    except Exception as e:
        print("Error clearing Prefetch & Superfetch:", e)

def clear_windows_update_cache():
    print("Clearing Windows Update Cache...")
    wu_cache_dir = r"C:\Windows\SoftwareDistribution\Download"
    try:
        for filename in os.listdir(wu_cache_dir):
            file_path = os.path.join(wu_cache_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception:
                pass
        print("Windows Update Cache cleared.\n")
    except Exception as e:
        print("Error clearing Windows Update Cache:", e)

def clean_memory_standby_list():
    print("Cleaning Memory Standby List...")
    exe_path = os.path.join(os.getcwd(), "EmptyStandbyList.exe")
    if os.path.exists(exe_path):
        subprocess.run(f'"{exe_path}" workingsets', shell=True)
        print("Memory Standby List cleaned.\n")
    else:
        print("EmptyStandbyList.exe not found. Skipping Memory Standby List cleaning.\n")

def one_click_optimization():
    print("Running one‑click optimization...")
    delete_temp_files()
    clear_prefetch_superfetch()
    clear_windows_update_cache()
    clean_memory_standby_list()
    # Recommended performance tweaks
    from .performance import disable_startup_delay, disable_background_apps, optimize_windows_services
    disable_startup_delay()
    disable_background_apps()
    optimize_windows_services()
    print("One‑click optimization completed.\n")

# === Undo Functions ===

def undo_delete_temp_files():
    print("Undo for deleting temporary files is not supported.")

def undo_clear_prefetch_superfetch():
    print("Undo for clearing Prefetch & Superfetch is not supported.")

def undo_clear_windows_update_cache():
    print("Undo for clearing Windows Update Cache is not supported.")

def undo_clean_memory_standby_list():
    print("Undo for cleaning Memory Standby List is not supported.")
