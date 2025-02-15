import tkinter as tk
import platform
import webbrowser
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from config.config_manager import load_config, save_config

# Import tweak modules
from tweaks import system, taskbar, appearance, performance, gaming, privacy, optimization

class TweaksApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")
        self.title("Looms Mods")
        self.geometry("700x600")
        self.resizable(False, False)
        self.config_data = load_config()

        # Control Vars

        # System Tweaks
        self.debloat_var = tk.BooleanVar(value=self.config_data.get("debloat"))
        self.network_tweaks_var = tk.BooleanVar(value=self.config_data.get("network_tweaks"))
        self.run_on_startup_var = tk.BooleanVar(value=self.config_data.get("run_on_startup"))

        # Taskbar Tweaks
        self.taskbar_items_var = tk.BooleanVar(value=self.config_data.get("remove_taskbar_items"))
        self.align_taskbar_var = tk.BooleanVar(value=self.config_data.get("align_taskbar"))
        self.rounded_corners_var = tk.BooleanVar(value=self.config_data.get("rounded_corners"))

        # Appearance
        self.dark_mode_var = tk.BooleanVar(value=self.config_data.get("dark_mode"))
        self.custom_accent_color_var = tk.BooleanVar(value=self.config_data.get("custom_accent_color"))
        self.taskbar_transparency_var = tk.BooleanVar(value=self.config_data.get("taskbar_transparency"))
        self.start_menu_layout_var = tk.BooleanVar(value=self.config_data.get("start_menu_layout"))

        # Performance
        self.disable_startup_delay_var = tk.BooleanVar(value=self.config_data.get("disable_startup_delay"))
        self.disable_background_apps_var = tk.BooleanVar(value=self.config_data.get("disable_background_apps"))
        self.optimize_windows_services_var = tk.BooleanVar(value=self.config_data.get("optimize_windows_services"))

        # Gaming
        self.disable_fullscreen_optimizations_var = tk.BooleanVar(value=self.config_data.get("disable_fullscreen_optimizations"))
        self.enable_gpu_scheduling_var = tk.BooleanVar(value=self.config_data.get("enable_gpu_scheduling"))
        self.reduce_input_lag_var = tk.BooleanVar(value=self.config_data.get("reduce_input_lag"))
        self.change_dns_for_gaming_var = tk.BooleanVar(value=self.config_data.get("change_dns_for_gaming"))

        # Privacy
        self.disable_telemetry_var = tk.BooleanVar(value=self.config_data.get("disable_telemetry"))
        self.disable_cortana_var = tk.BooleanVar(value=self.config_data.get("disable_cortana"))
        self.remove_edge_preloading_var = tk.BooleanVar(value=self.config_data.get("remove_edge_preloading"))

        # Windows Optimization
        self.delete_temp_files_var = tk.BooleanVar(value=self.config_data.get("delete_temp_files"))
        self.clear_prefetch_var = tk.BooleanVar(value=self.config_data.get("clear_prefetch"))
        self.clear_wu_cache_var = tk.BooleanVar(value=self.config_data.get("clear_wu_cache"))
        self.clean_standby_list_var = tk.BooleanVar(value=self.config_data.get("clean_standby_list"))

        self.create_main_layout()

    def create_main_layout(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # --- System Tweaks ---
        lf_system = ttk.Labelframe(main_frame, text="System Tweaks")
        lf_system.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.create_toggle(lf_system, "Remove Bloatware", self.debloat_var)
        self.create_toggle(lf_system, "Network Tweaks", self.network_tweaks_var)
        self.create_toggle(lf_system, "Run on Startup", self.run_on_startup_var)

        # --- Taskbar Tweaks ---
        lf_taskbar = ttk.Labelframe(main_frame, text="Taskbar Tweaks")
        lf_taskbar.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.create_toggle(lf_taskbar, "Hide Search/Task View Icons", self.taskbar_items_var)
        self.create_toggle(lf_taskbar, "Left-Align Taskbar", self.align_taskbar_var)
        self.create_toggle(lf_taskbar, "Rounded Corners", self.rounded_corners_var)

        # --- Appearance ---
        lf_appearance = ttk.Labelframe(main_frame, text="Appearance")
        lf_appearance.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.create_toggle(lf_appearance, "Dark Mode", self.dark_mode_var)
        self.create_toggle(lf_appearance, "Custom Accent Color", self.custom_accent_color_var)
        self.create_toggle(lf_appearance, "Taskbar Transparency", self.taskbar_transparency_var)
        self.create_toggle(lf_appearance, "Start Menu Layout", self.start_menu_layout_var)

        # --- Performance ---
        lf_performance = ttk.Labelframe(main_frame, text="Performance")
        lf_performance.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        self.create_toggle(lf_performance, "Disable Startup Delay", self.disable_startup_delay_var)
        self.create_toggle(lf_performance, "Disable Background Apps", self.disable_background_apps_var)
        self.create_toggle(lf_performance, "Optimize Windows Services", self.optimize_windows_services_var)

        # --- Gaming ---
        lf_gaming = ttk.Labelframe(main_frame, text="Gaming")
        lf_gaming.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        self.create_toggle(lf_gaming, "Disable Fullscreen Optimizations", self.disable_fullscreen_optimizations_var)
        self.create_toggle(lf_gaming, "Enable GPU Scheduling", self.enable_gpu_scheduling_var)
        self.create_toggle(lf_gaming, "Reduce Input Lag", self.reduce_input_lag_var)
        self.create_toggle(lf_gaming, "Change DNS for Gaming", self.change_dns_for_gaming_var)

        # --- Privacy ---
        lf_privacy = ttk.Labelframe(main_frame, text="Privacy & Security")
        lf_privacy.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self.create_toggle(lf_privacy, "Disable Telemetry", self.disable_telemetry_var)
        self.create_toggle(lf_privacy, "Disable Cortana", self.disable_cortana_var)
        self.create_toggle(lf_privacy, "Remove Edge Preloading", self.remove_edge_preloading_var)

        # --- Windows Optimization ---
        lf_optim = ttk.Labelframe(main_frame, text="Windows Optimization")
        lf_optim.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        self.create_toggle(lf_optim, "Delete Temp Files", self.delete_temp_files_var)
        self.create_toggle(lf_optim, "Clear Prefetch & Superfetch", self.clear_prefetch_var)
        self.create_toggle(lf_optim, "Clear Windows Update Cache", self.clear_wu_cache_var)
        self.create_toggle(lf_optim, "Clean Memory Standby List", self.clean_standby_list_var)
        one_click_btn = ttk.Button(lf_optim, text="One‑Click Optimization", bootstyle=PRIMARY, command=optimization.one_click_optimization)
        one_click_btn.pack(pady=5, padx=5, anchor="w")

        # --- System Information ---
        lf_info = ttk.Labelframe(main_frame, text="System Information")
        lf_info.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
        sysinfo = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Release": platform.release(),
            "Machine": platform.machine(),
            "Processor": platform.processor()
        }
        for key, value in sysinfo.items():
            lbl = ttk.Label(lf_info, text=f"{key}: {value}", font=("Segoe UI", 9))
            lbl.pack(anchor="w", padx=5, pady=2)

        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        for i in range(4):
            main_frame.rowconfigure(i, weight=1)

        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(fill="x", padx=10, pady=5)

        apply_btn = ttk.Button(bottom_frame, text="Apply Tweaks", bootstyle=PRIMARY, command=self.apply_tweaks)
        apply_btn.pack(side="left", padx=5)

        save_btn = ttk.Button(bottom_frame, text="Save Config", bootstyle=SUCCESS, command=self.save_current_config)
        save_btn.pack(side="left", padx=5)

        undo_btn = ttk.Button(bottom_frame, text="Undo Tweaks", bootstyle=WARNING, command=self.undo_tweaks)
        undo_btn.pack(side="left", padx=5)

        self.status_label = ttk.Label(bottom_frame, text="", font=("Segoe UI", 9))
        self.status_label.pack(side="left", padx=20)

        made_by_label = ttk.Label(bottom_frame, text="Made by Loom", foreground="#ADD8E6", cursor="hand2")
        made_by_label.pack(side="right", padx=5)
        made_by_label.bind("<Button-1>", lambda e: webbrowser.open("https://discord.gg/MA7kvS5k"))

    def create_toggle(self, parent, text, variable):
        chk = ttk.Checkbutton(parent, text=text, variable=variable, bootstyle="round-toggle")
        chk.pack(anchor="w", pady=3, padx=5)

    def apply_tweaks(self):
        self.status_label.config(text="Applying selected tweaks...")
        dangerous = []
        if self.debloat_var.get():
            dangerous.append("Remove Bloatware")
        if self.optimize_windows_services_var.get():
            dangerous.append("Optimize Windows Services")
        if self.disable_telemetry_var.get():
            dangerous.append("Disable Telemetry")
        if self.disable_cortana_var.get():
            dangerous.append("Disable Cortana")

        if dangerous:
            warning_msg = (
                "Warning: The following modifications may break Windows features:\n\n" +
                "\n".join(dangerous) +
                "\n\nDo you wish to proceed?"
            )
            if not messagebox.askokcancel("Warning", warning_msg):
                self.status_label.config(text="Operation cancelled.")
                return

        if self.debloat_var.get():
            system.remove_bloatware()
        if self.network_tweaks_var.get():
            system.apply_network_tweaks()
        if self.taskbar_items_var.get():
            taskbar.remove_taskbar_items()
        if self.align_taskbar_var.get():
            taskbar.align_taskbar_icons()
        if self.rounded_corners_var.get():
            taskbar.enable_rounded_corners()
        if self.dark_mode_var.get():
            appearance.enable_dark_mode()
        if self.custom_accent_color_var.get():
            appearance.custom_accent_color()
        if self.taskbar_transparency_var.get():
            appearance.taskbar_transparency()
        if self.start_menu_layout_var.get():
            appearance.start_menu_layout_customization()
        if self.disable_startup_delay_var.get():
            performance.disable_startup_delay()
        if self.disable_background_apps_var.get():
            performance.disable_background_apps()
        if self.optimize_windows_services_var.get():
            performance.optimize_windows_services()
        if self.disable_fullscreen_optimizations_var.get():
            gaming.disable_fullscreen_optimizations()
        if self.enable_gpu_scheduling_var.get():
            gaming.enable_gpu_scheduling()
        if self.reduce_input_lag_var.get():
            gaming.reduce_input_lag()
        if self.change_dns_for_gaming_var.get():
            gaming.change_dns_for_gaming()
        if self.disable_telemetry_var.get():
            privacy.disable_telemetry()
        if self.disable_cortana_var.get():
            privacy.disable_cortana()
        if self.remove_edge_preloading_var.get():
            privacy.remove_edge_preloading()
        if self.delete_temp_files_var.get():
            optimization.delete_temp_files()
        if self.clear_prefetch_var.get():
            optimization.clear_prefetch_superfetch()
        if self.clear_wu_cache_var.get():
            optimization.clear_windows_update_cache()
        if self.clean_standby_list_var.get():
            optimization.clean_memory_standby_list()

        system.set_run_on_startup(self.run_on_startup_var.get())
        self.status_label.config(text="Tweaks applied. Some changes may require a restart.")

    def undo_tweaks(self):
        self.status_label.config(text="Undoing selected tweaks...")
        if self.debloat_var.get():
            system.undo_remove_bloatware()
        if self.network_tweaks_var.get():
            system.undo_apply_network_tweaks()
        if self.run_on_startup_var.get():
            system.undo_run_on_startup()
        if self.taskbar_items_var.get():
            taskbar.undo_remove_taskbar_items()
        if self.align_taskbar_var.get():
            taskbar.undo_align_taskbar_icons()
        if self.rounded_corners_var.get():
            taskbar.undo_enable_rounded_corners()
        if self.dark_mode_var.get():
            appearance.undo_enable_dark_mode()
        if self.custom_accent_color_var.get():
            appearance.undo_custom_accent_color()
        if self.taskbar_transparency_var.get():
            appearance.undo_taskbar_transparency()
        if self.start_menu_layout_var.get():
            appearance.undo_start_menu_layout_customization()
        if self.disable_startup_delay_var.get():
            performance.undo_disable_startup_delay()
        if self.disable_background_apps_var.get():
            performance.undo_disable_background_apps()
        if self.optimize_windows_services_var.get():
            performance.undo_optimize_windows_services()
        if self.disable_fullscreen_optimizations_var.get():
            gaming.undo_disable_fullscreen_optimizations()
        if self.enable_gpu_scheduling_var.get():
            gaming.undo_enable_gpu_scheduling()
        if self.reduce_input_lag_var.get():
            gaming.undo_reduce_input_lag()
        if self.change_dns_for_gaming_var.get():
            gaming.undo_change_dns_for_gaming()
        if self.disable_telemetry_var.get():
            privacy.undo_disable_telemetry()
        if self.disable_cortana_var.get():
            privacy.undo_disable_cortana()
        if self.remove_edge_preloading_var.get():
            privacy.undo_remove_edge_preloading()
        if self.delete_temp_files_var.get():
            optimization.undo_delete_temp_files()
        if self.clear_prefetch_var.get():
            optimization.undo_clear_prefetch_superfetch()
        if self.clear_wu_cache_var.get():
            optimization.undo_clear_windows_update_cache()
        if self.clean_standby_list_var.get():
            optimization.undo_clean_memory_standby_list()

        self.status_label.config(text="Undo operations attempted. Some changes may not be reversible.")

    def save_current_config(self):
        self.config_data["debloat"] = self.debloat_var.get()
        self.config_data["network_tweaks"] = self.network_tweaks_var.get()
        self.config_data["run_on_startup"] = self.run_on_startup_var.get()

        self.config_data["remove_taskbar_items"] = self.taskbar_items_var.get()
        self.config_data["align_taskbar"] = self.align_taskbar_var.get()
        self.config_data["rounded_corners"] = self.rounded_corners_var.get()

        self.config_data["dark_mode"] = self.dark_mode_var.get()
        self.config_data["custom_accent_color"] = self.custom_accent_color_var.get()
        self.config_data["taskbar_transparency"] = self.taskbar_transparency_var.get()
        self.config_data["start_menu_layout"] = self.start_menu_layout_var.get()

        self.config_data["disable_startup_delay"] = self.disable_startup_delay_var.get()
        self.config_data["disable_background_apps"] = self.disable_background_apps_var.get()
        self.config_data["optimize_windows_services"] = self.optimize_windows_services_var.get()

        self.config_data["disable_fullscreen_optimizations"] = self.disable_fullscreen_optimizations_var.get()
        self.config_data["enable_gpu_scheduling"] = self.enable_gpu_scheduling_var.get()
        self.config_data["reduce_input_lag"] = self.reduce_input_lag_var.get()
        self.config_data["change_dns_for_gaming"] = self.change_dns_for_gaming_var.get()

        self.config_data["disable_telemetry"] = self.disable_telemetry_var.get()
        self.config_data["disable_cortana"] = self.disable_cortana_var.get()
        self.config_data["remove_edge_preloading"] = self.remove_edge_preloading_var.get()

        self.config_data["delete_temp_files"] = self.delete_temp_files_var.get()
        self.config_data["clear_prefetch"] = self.clear_prefetch_var.get()
        self.config_data["clear_wu_cache"] = self.clear_wu_cache_var.get()
        self.config_data["clean_standby_list"] = self.clean_standby_list_var.get()

        save_config(self.config_data)
        self.status_label.config(text="Configuration saved.")

if __name__ == "__main__":
    app = TweaksApp()
    app.mainloop()
