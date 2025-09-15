import os
try:
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32
    print("\033[1;30m [/] Paketler Kontrol Ediliyor.. \033[0m")
    import sys
    import ctypes
    import platform
    import psutil
    import shutil
    import time
    import socket
    import subprocess
    import threading
    import random
    import hashlib
    import requests
    import string
    import math
    import json

    import winreg as reg
    import tkinter as tk

    from tkinter import ttk, filedialog, messagebox, colorchooser
    from pystyle import *
    from colorama import *
    from ping3 import ping
    from winreg import OpenKey, SetValueEx, HKEY_CURRENT_USER, KEY_SET_VALUE, REG_DWORD, REG_SZ
except ImportError:
    print("Eksik veya yüklenmemiş kütüphane var. Gerekli Kütüphaneler yükleniyor..")
    try:
        __import__("os").system("py -m pip install psutil keyboard requests pystyle colorama ping3 tkinterdnd2")  # kütüphaneler yoksa yükle
        print("Kütüphaneler yüklendi. lütfen programı tekrar çalıştırın.")
        __import__("time").sleep(2)
    except ImportError as e:
        __import__("os").system(f"msg %username% {e}")

import sys
import ctypes
import platform
import psutil
import shutil
import time
import socket
import subprocess
import threading
import random
import hashlib
import requests
import string
import math
import json

import winreg as reg
import tkinter as tk

from tkinter import ttk, filedialog, messagebox, colorchooser
from pystyle import *
from colorama import *
from ping3 import ping
from winreg import OpenKey, SetValueEx, HKEY_CURRENT_USER, KEY_SET_VALUE, REG_DWORD, REG_SZ

# Konsol penceresinin boyutlandırma stilini kapatalım
GWL_STYLE = -16
WS_SIZEBOX = 0x00040000  # Konsolun yeniden boyutlandırılmasını sağlayan stil
WS_MAXIMIZEBOX = 0x00010000  # Konsolun büyütülmesini sağlayan stil

# Windows API'lerini kullanabilmek için ctypes ile kernel32'yi çağırıyoruz
user32 = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Konsol penceresinin handle'ını al
hwnd = kernel32.GetConsoleWindow()

# Pencerenin mevcut stilini alalım
current_style = user32.GetWindowLongW(hwnd, GWL_STYLE)

# Boyutlandırma ve büyütme seçeneklerini kapatalım
new_style = current_style & ~(WS_SIZEBOX | WS_MAXIMIZEBOX)

# Yeni stil ile pencereyi güncelleyelim
user32.SetWindowLongW(hwnd, GWL_STYLE, new_style)

# Ekranın genişliği ile yüksekliğini al
ekran_genisligi = user32.GetSystemMetrics(0)
ekran_yuksekligi = user32.GetSystemMetrics(1)

# Konsol penceresinin başlangıç boyutları
konsol_genisligi = 1
konsol_yuksekligi = 1

# Konsolu ekranın ortasına yerleştirmek için x ve y hesapla
konum_x = (ekran_genisligi - konsol_genisligi) // 2
konum_y = (ekran_yuksekligi - konsol_yuksekligi) // 2

# Konsol penceresini başlangıçta 1x1 piksel boyutunda ortala
user32.MoveWindow(hwnd, konum_x, konum_y, konsol_genisligi, konsol_yuksekligi, True)

# .ico dosyasının tam yolu (simge dosyanızın konumunu belirtin)
ico_path = os.path.abspath("icon.ico")

# Konsol penceresinin simgesini değiştirmek için gereken Windows API fonksiyonu
hIcon = user32.LoadImageW(0, ico_path, 1, 0, 0, 0x00000010)  # 1 = IMAGE_ICON, 0x00000010 = LR_LOADFROMFILE
user32.SendMessageW(hwnd, 0x80, 0, hIcon)  # 0x80 = WM_SETICON

# Simgeyi küçük simge olarak da ayarlayalım
user32.SendMessageW(hwnd, 0x80, 1, hIcon)  # 1 = küçük simge

SW_MINIMIZE = 6  # Küçültmek için gerekli kod
SW_RESTORE = 9   # Geri getirmek için gerekli kod

System.Title("   Mounoa.v1")

# Konsol penceresini büyütme animasyonu
for i in range(1, 901, 10):
    konsol_genisligi = i
    konsol_yuksekligi = int(i * 0.75)
    konum_x = (ekran_genisligi - konsol_genisligi) // 2
    konum_y = (ekran_yuksekligi - konsol_yuksekligi) // 2
    user32.MoveWindow(hwnd, konum_x, konum_y, konsol_genisligi, konsol_yuksekligi, True)
    time.sleep(0.01)  # Büyüme hızını ayarla

# Colorama ayarları. (pystyle'da geçerli)
init(autoreset=False)

# -- Mounoa Versiyonu --
MOUNOA_VER = "1.0.0"

# --  DEĞERLER (RENK & LOGO gibi)  --
INFO =    f"  {Fore.BLACK}{Back.LIGHTBLUE_EX}[=]{Style.RESET_ALL}"
WARNING = f"  {Fore.BLACK}{Back.YELLOW}[!]{Style.RESET_ALL}"
ERROR =   f"  {Fore.BLACK}{Back.LIGHTRED_EX}[X]{Style.RESET_ALL}"
SUCCESS = f"  {Fore.BLACK}{Back.GREEN}[V]{Style.RESET_ALL}"
TK_BG_COLOR = "#1e1e1e"
TK_BTN_BG_COLOR = "#323232"
TK_FG_COLOR = "#e1ffff"

# --  YAZI STİLLERİ  --
def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
def alt_cizgili_yazi(yazi):
    return "\033[4m" + yazi + "\033[0m"

colrr1,colrg1,colrb1 = 117, 129, 255
colrr2,colrg2,colrb2 = 145, 127, 234
colrr3,colrg3,colrb3 = 172, 124, 214
colrr4,colrg4,colrb4 = 200, 122, 193
colrr5,colrg5,colrb5 = 227, 119, 173
colrr6,colrg6,colrb6 = 255, 117, 152

RGBBANNER = f"""
    {colored(colrr1,colrg1,colrb1,"███████                       ███████")}
    {colored(colrr1,colrg1,colrb1,"███                               ███")}
    {colored(colrr2,colrg2,colrb2,"███             ██    ██          ███")}
    {colored(colrr2,colrg2,colrb2,"███            ███   ███          ███")}
    {colored(colrr3,colrg3,colrb3,"███         ██████████████        ███")}
    {colored(colrr3,colrg3,colrb3,"███           ███   ███           ███")}
    {colored(colrr4,colrg4,colrb4,"███           ███   ███           ███")}
    {colored(colrr4,colrg4,colrb4,"███        ██████████████         ███")}
    {colored(colrr5,colrg5,colrb5,"███          ███   ███            ███")}
    {colored(colrr5,colrg5,colrb5,"███          ██    ██             ███")}
    {colored(colrr6,colrg6,colrb6,"███                               ███")}
    {colored(colrr6,colrg6,colrb6,"███████                       ███████")}
"""
CenterRGBBANNER = f"""
                        {colored(colrr1,colrg1,colrb1,"███████                       ███████")}
                        {colored(colrr1,colrg1,colrb1,"███                               ███")}
                        {colored(colrr2,colrg2,colrb2,"███             ██    ██          ███")}
                        {colored(colrr2,colrg2,colrb2,"███            ███   ███          ███")}
                        {colored(colrr3,colrg3,colrb3,"███         ██████████████        ███")}
                        {colored(colrr3,colrg3,colrb3,"███           ███   ███           ███")}
                        {colored(colrr4,colrg4,colrb4,"███           ███   ███           ███")}
                        {colored(colrr4,colrg4,colrb4,"███        ██████████████         ███")}
                        {colored(colrr5,colrg5,colrb5,"███          ███   ███            ███")}
                        {colored(colrr5,colrg5,colrb5,"███          ██    ██             ███")}
                        {colored(colrr6,colrg6,colrb6,"███                               ███")}
                        {colored(colrr6,colrg6,colrb6,"███████                       ███████")}
"""

# --  İNTRO  --
os.system("cls")
print(Center.Center(CenterRGBBANNER))
time.sleep(4)
os.system("cls")

# -- Winutil --
def winutil():
    def run_command_as_admin(command):
        if sys.platform != 'win32':
            print("Hata: Bu betik yalnızca Windows üzerinde çalışabilir.")
            return
        try:
            executable = "powershell.exe"
            params = f'-NoExit -Command "{command}"'
            return_code = ctypes.windll.shell32.ShellExecuteW(
                None,       # Üst pencere handle'ı (yok)
                "runas",    # Gerçekleştirilecek eylem (yönetici olarak çalıştır)
                executable, # Çalıştırılacak program
                params,     # Programa gönderilecek parametreler
                None,       # Çalışma dizini (varsayılan)
                1           # Pencereyi gösterme durumu (normal göster)
            )

            if return_code <= 32:
                print(f"Komut çalıştırılamadı. Hata kodu: {return_code}")
                print("Olası nedenler:\n- Yönetici izni (UAC) istemini reddetmiş olabilirsiniz.\n- Sisteminizde PowerShell bulunmuyor olabilir.")

        except Exception as e:
            print(f"Beklenmedik bir hata oluştu: {e}")


    if __name__ == "__main__":
        ps_command = "irm 'https://christitus.com/win' | iex"
        print("İstenen PowerShell komutu yönetici olarak çalıştırılacak.")
        print("Bu işlem için Windows sizden yönetici onayı (UAC) isteyecektir.")
        print("-" * 60)
        run_command_as_admin(ps_command)


# -- Dönen Pencereler --
def spinwindow():
    # -- Ses seviyesini almak için gerekli kütüphaneler --
    try:
        # Daha temiz ve hatasız import yöntemi
        import comtypes
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, IAudioMeterInformation
        AUDIO_ENABLED = True
    except ImportError:
        AUDIO_ENABLED = False

    class RotatingWindow:
        def __init__(self, manager, radius=100, speed=0.05, offset_angle=0,
                    width=200, height=100, bg_color="#333333"):
            self.manager = manager
            self.window = tk.Toplevel()
            self.window.title("Dönen Pencere")
            self.window.geometry(f"{width}x{height}")
            self.window.configure(bg=bg_color)
            self.radius = int(radius)
            self.speed = float(speed)
            self.angle = 0.0
            self.angle_offset = float(offset_angle)
            self.width = int(width)
            self.height = int(height)
            self.bg_color = bg_color
            self.direction = 1
            self.paused = False

            self.screen_width = self.window.winfo_screenwidth()
            self.screen_height = self.window.winfo_screenheight()
            self.center_x = self.screen_width // 2
            self.center_y = self.screen_height // 2

            self.move_window()
            self.rotate()
            self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        def move_window(self):
            current_angle = self.angle * self.direction + self.angle_offset
            x = int(self.center_x + self.radius * math.cos(current_angle) - self.width // 2)
            y = int(self.center_y + self.radius * math.sin(current_angle) - self.height // 2)
            try:
                self.window.configure(bg=self.bg_color)
                self.window.geometry(f"{self.width}x{self.height}+{x}+{y}")
            except tk.TclError:
                self.on_close()

        def rotate(self):
            if not self.paused:
                self.angle += self.speed
                if self.angle > 2 * math.pi:
                    self.angle -= 2 * math.pi
            self.move_window()
            self.window.after(20, self.rotate)

        def update_properties(self, radius, speed, direction, width, height, bg_color):
            self.radius = int(radius)
            self.speed = float(abs(speed))
            self.direction = 1 if int(direction) >= 0 else -1
            self.width = int(width)
            self.height = int(height)
            self.bg_color = str(bg_color)

        def toggle_pause(self):
            self.paused = not self.paused

        def on_close(self):
            try:
                self.window.destroy()
            finally:
                if self in self.manager.windows:
                    self.manager.windows.remove(self)


    class ControlPanel:
        def __init__(self, root):
            self.root = root
            self.root.title("Pencere Kontrol Paneli")
            self.root.geometry("450x440+15+20")
            self.root.configure(bg="#212121")
            self.MIN_RADIUS = 50
            self.MAX_RADIUS = 600
            self.num_windows = tk.IntVar(value=3)
            self.width = tk.IntVar(value=200)
            self.height = tk.IntVar(value=100)
            self.radius = tk.IntVar(value=250)
            self.speed = tk.DoubleVar(value=0.03)
            self.direction = tk.IntVar(value=1)
            self.bg_color = "#333333"
            self.mode = tk.IntVar(value=1)
            self.windows = []
            self.audio_level = 0.0
            self.is_running = True

            self.setup_styles()
            self.create_ui()
            self.update_windows()

            if AUDIO_ENABLED:
                audio_thread = threading.Thread(target=self.listen_to_audio, daemon=True)
                audio_thread.start()
            
            self.animate_properties()
            self.root.bind("<plus>", self.inc_speed)
            self.root.bind("<minus>", self.dec_speed)
            self.root.bind("<space>", lambda e: self.toggle_pause_all())
            self.root.protocol("WM_DELETE_WINDOW", self.on_panel_close)

        # --- BU FONKSİYON DEĞİŞTİRİLDİ ---
        def listen_to_audio(self):
            """
            Arka planda çalışarak sistem sesini dinler ve audio_level değişkenini günceller.
            """
            # YENİ: Bu yeni thread için COM kütüphanesini başlat.
            comtypes.CoInitialize()
            try:
                devices = AudioUtilities.GetSpeakers()
                interface = devices.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
                # IAudioMeterInformation arayüzünü de almamız gerekiyor
                volume_meter = interface.QueryInterface(IAudioMeterInformation)
                
                while self.is_running:
                    self.audio_level = volume_meter.GetPeakValue()
                    time.sleep(0.02)
            except Exception as e:
                print(f"Ses aygıtı dinlenirken hata oluştu: {e}")
                self.audio_level = 0.0
            finally:
                # YENİ: Thread sonlandığında COM kütüphanesini serbest bırak.
                comtypes.CoUninitialize()

        def animate_properties(self):
            if self.mode.get() == 2:
                new_radius = self.MIN_RADIUS + (self.audio_level * (self.MAX_RADIUS - self.MIN_RADIUS))
                self.radius.set(int(new_radius))
                self.update_all_properties()
            self.root.after(20, self.animate_properties)

        def setup_styles(self):
            style = ttk.Style()
            style.theme_use('clam')
            style.configure(".", background="#212121", foreground="white", fieldbackground="#333333")
            style.configure("TButton", padding=6, relief="flat", background="#424242", foreground="white")
            style.map("TButton", background=[('active', '#626262')])
            style.configure("TLabel", padding=5, font=('calibri', 10))
            style.configure("TRadiobutton", padding=5, font=('calibri', 10))
            style.map("TRadiobutton", background=[('active', '#212121')])
            style.configure("Horizontal.TScale", sliderlength=20, troughcolor='#424242', background='#626262')

        def create_ui(self):
            main = ttk.Frame(self.root, padding=15)
            main.pack(fill=tk.BOTH, expand=True)
            main.columnconfigure(1, weight=1)
            ttk.Label(main, text="Pencere Sayısı:").grid(row=0, column=0, sticky=tk.W, pady=5)
            ttk.Scale(main, from_=1, to=15, orient=tk.HORIZONTAL, variable=self.num_windows, command=lambda e: self.update_windows()).grid(row=0, column=1, sticky=tk.EW)
            ttk.Label(main, text="Genişlik:").grid(row=1, column=0, sticky=tk.W, pady=5)
            ttk.Scale(main, from_=100, to=500, orient=tk.HORIZONTAL, variable=self.width, command=lambda e: self.update_all_properties()).grid(row=1, column=1, sticky=tk.EW)
            ttk.Label(main, text="Yükseklik:").grid(row=2, column=0, sticky=tk.W, pady=5)
            ttk.Scale(main, from_=60, to=400, orient=tk.HORIZONTAL, variable=self.height, command=lambda e: self.update_all_properties()).grid(row=2, column=1, sticky=tk.EW)
            self.radius_label = ttk.Label(main, text="Yörünge Yarıçapı:")
            self.radius_label.grid(row=3, column=0, sticky=tk.W, pady=5)
            self.radius_scale = ttk.Scale(main, from_=50, to=600, orient=tk.HORIZONTAL, variable=self.radius, command=lambda e: self.update_all_properties())
            self.radius_scale.grid(row=3, column=1, sticky=tk.EW)
            ttk.Label(main, text="Dönme Hızı:").grid(row=4, column=0, sticky=tk.W, pady=5)
            ttk.Scale(main, from_=0.01, to=0.20, orient=tk.HORIZONTAL, variable=self.speed, command=lambda e: self.update_all_properties()).grid(row=4, column=1, sticky=tk.EW)
            bottom_frame = ttk.Frame(main)
            bottom_frame.grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=10)
            ttk.Label(bottom_frame, text="Yön:").pack(side=tk.LEFT, padx=(0, 10))
            ttk.Radiobutton(bottom_frame, text="Saat Yönü", variable=self.direction, value=1, command=self.update_all_properties).pack(side=tk.LEFT)
            ttk.Radiobutton(bottom_frame, text="Ters Yön", variable=self.direction, value=-1, command=self.update_all_properties).pack(side=tk.LEFT, padx=(0, 30))
            ttk.Label(bottom_frame, text="Mod:").pack(side=tk.LEFT, padx=(0, 10))
            ttk.Radiobutton(bottom_frame, text="Normal", variable=self.mode, value=1, command=self.toggle_radius_slider).pack(side=tk.LEFT)
            state = tk.NORMAL if AUDIO_ENABLED else tk.DISABLED
            ttk.Radiobutton(bottom_frame, text="Ses Duyarlı", variable=self.mode, value=2, command=self.toggle_radius_slider, state=state).pack(side=tk.LEFT)
            ttk.Button(main, text="Pencere Rengi Seç", command=self.choose_color).grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)
            btn_row = ttk.Frame(main)
            btn_row.grid(row=7, column=0, columnspan=2, pady=10)
            btn_row.columnconfigure((0, 1, 2), weight=1)
            ttk.Button(btn_row, text="Duraklat / Devam", command=self.toggle_pause_all).grid(row=0, column=0, sticky=tk.EW, padx=5)
            ttk.Button(btn_row, text="Ayarları Kaydet", command=self.save_settings).grid(row=0, column=1, sticky=tk.EW, padx=5)
            ttk.Button(btn_row, text="Ayarları Yükle", command=self.load_settings).grid(row=0, column=2, sticky=tk.EW, padx=5)
        
        def toggle_radius_slider(self):
            if self.mode.get() == 2:
                self.radius_scale.config(state=tk.DISABLED)
                self.radius_label.config(state=tk.DISABLED)
            else:
                self.radius_scale.config(state=tk.NORMAL)
                self.radius_label.config(state=tk.NORMAL)

        def on_panel_close(self):
            self.is_running = False
            self.root.destroy()
        
        def choose_color(self):
            color_code = colorchooser.askcolor(title="Bir renk seçin", initialcolor=self.bg_color)
            if color_code and color_code[1]:
                self.bg_color = color_code[1]
                self.update_all_properties()

        def update_windows(self):
            for w in list(self.windows):
                w.on_close()
            self.windows.clear()
            num = max(1, self.num_windows.get())
            for i in range(num):
                offset = i * (2 * math.pi / num)
                w = RotatingWindow(self, self.radius.get(), self.speed.get(), offset,
                                self.width.get(), self.height.get(), self.bg_color)
                self.windows.append(w)

        def update_all_properties(self):
            num_windows_active = len(self.windows)
            if num_windows_active == 0:
                return
            for i, w in enumerate(self.windows):
                offset = i * (2 * math.pi / num_windows_active)
                w.angle_offset = offset
                w.update_properties(self.radius.get(), self.speed.get(), self.direction.get(),
                                    self.width.get(), self.height.get(), self.bg_color)

        def toggle_pause_all(self):
            for w in self.windows:
                w.toggle_pause()

        def save_settings(self):
            settings = {
                "num_windows": self.num_windows.get(),
                "width": self.width.get(),
                "height": self.height.get(),
                "radius": self.radius.get(),
                "speed": self.speed.get(),
                "direction": self.direction.get(),
                "bg_color": self.bg_color,
            }
            file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Dosyaları", "*.json")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(settings, f, ensure_ascii=False, indent=2)
                messagebox.showinfo("Başarılı", "Ayarlar başarıyla kaydedildi.")

        def load_settings(self):
            file_path = filedialog.askopenfilename(filetypes=[("JSON Dosyaları", "*.json")])
            if file_path:
                with open(file_path, "r", encoding="utf-8") as f:
                    settings = json.load(f)
                self.num_windows.set(settings.get("num_windows", 3))
                self.width.set(settings.get("width", 200))
                self.height.set(settings.get("height", 100))
                self.radius.set(settings.get("radius", 150))
                self.speed.set(settings.get("speed", 0.05))
                self.direction.set(settings.get("direction", 1))
                self.bg_color = settings.get("bg_color", "#333333")
                self.update_windows()
                messagebox.showinfo("Başarılı", "Ayarlar başarıyla yüklendi.")

        def inc_speed(self, _=None):
            self.speed.set(min(0.20, round(self.speed.get() + 0.01, 2)))
            self.update_all_properties()

        def dec_speed(self, _=None):
            self.speed.set(max(0.01, round(self.speed.get() - 0.01, 2)))
            self.update_all_properties()


    if __name__ == "__main__":
        root = tk.Tk()
        app = ControlPanel(root)
        root.mainloop()

# -- AĞ TARAMASI --
def netscan():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()

    print(f"{INFO}    Yerel IP adresiniz: {local_ip}")
    base_ip = ".".join(local_ip.split(".")[:-1]) + "."
    print(f"{INFO}    Tarama aralığı: {base_ip}1 - {base_ip}255")

    threads = []
    start_time = time.time()

    # İç içe ping fonksiyonu
    def ping_ip(ip):
        try:
            response = ping(ip, timeout=1)  # 1 saniye zaman aşımı
            if response is not None:  # None değilse cihaz aktif
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except socket.herror:
                    hostname = "Bilinmiyor"
                print(f"{SUCCESS}    Aktif cihaz: {ip} | Host Adı: {hostname} | Yanıt Süresi: {response*1000:.3f} ms")
        except:
            pass

    # 1-255 arasındaki IP'leri tara
    for i in range(1, 256):
        ip = base_ip + str(i)
        thread = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(thread)
        thread.start()

    # Tüm thread'lerin bitmesini bekle
    for thread in threads:
        thread.join()

    print(f"{INFO}    Tarama tamamlandı. Süre: {time.time() - start_time:.2f} saniye")

#  --  WİNDOWS OPTİMİZE AYAR.  --
def optimize():
    def set_high_performance_power_plan():
        try:
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
            os.system("powercfg -setactive SCHEME_MIN")
            print(f" {SUCCESS} Güç planı yüksek performans moduna ayarlandı.")
        except Exception as e:
            print(f" {ERROR} hata oluştu: {e}")

    def set_best_performance_mode():
        try:
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects"
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_WRITE)
            reg.SetValueEx(reg_key, "VisualFXSetting", 0, reg.REG_DWORD, 2)
            reg.CloseKey(reg_key)

            key_path = r"Control Panel\Desktop"
            reg_key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_WRITE)
            reg.SetValueEx(reg_key, "DragFullWindows", 0, reg.REG_SZ, "0")
            reg.SetValueEx(reg_key, "FontSmoothing", 0, reg.REG_SZ, "0")
            reg.SetValueEx(reg_key, "MenuShowDelay", 0, reg.REG_SZ, "0")
            reg.SetValueEx(reg_key, "UserPreferencesMask", 0, reg.REG_BINARY, b'\x90\x12\x03\x80\x10\x00\x00\x00')
            reg.CloseKey(reg_key)

            ctypes.windll.user32.SystemParametersInfoW(0x1003, 0, None, 0x2)
            print(f" {SUCCESS} Bilgisayar en iyi performans için ayarlandı.")
        except Exception as e:
            print(f" {ERROR} hata oluştu: {e}")

    def arka_plan_degis(renk="000000"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, None, 3)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{renk}.bmp", 3)
        print(f" {SUCCESS} Arka Plan başarıyla değiştirildi.")

    # Windows siyah modu etkinleştirir ve saydamlık efektini kapatır.
    def enable_dark_mode():
        try:
            # Siyah mod
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
            with OpenKey(HKEY_CURRENT_USER, key_path, 0, KEY_SET_VALUE) as key:
                SetValueEx(key, "AppsUseLightTheme", 0, REG_DWORD, 0)
                SetValueEx(key, "SystemUsesLightTheme", 0, REG_DWORD, 0)
            print(f"   {SUCCESS} Siyah mod etkinleştirildi.")

            # Saydamlık efekti kapatma
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
            with OpenKey(HKEY_CURRENT_USER, key_path, 0, KEY_SET_VALUE) as key:
                SetValueEx(key, "EnableTransparency", 0, REG_DWORD, 0)
            print(f"   {SUCCESS} Saydamlık efekti kapatıldı.")
        except Exception as e:
            print(f"   {ERROR} Hata: {e}")

    # Windows fare işaretçisini siyah yapar.
    def change_cursor_to_black():
        try:
            key_path = r"Control Panel\Cursors"
            cursor_path = r"C:\Windows\Cursors"  # İşaretçi dosyalarının bulunduğu dizin
            cursors = {
                "Arrow": f"{cursor_path}\\arrow_r.cur",  # Normal Seçim
                "Help": f"{cursor_path}\\help_r.cur",  # Yardım Seç
                "AppStarting": f"{cursor_path}\\working_r.ani",  # Arka Planda Çalışıyor
                "Wait": f"{cursor_path}\\busy_r.ani",  # Meşgul
                "Crosshair": f"{cursor_path}\\cross_r.cur",  # Hassas Seçim
                "IBeam": f"{cursor_path}\\beam_r.cur",  # Metin Seçimi
                "NWPen": f"{cursor_path}\\pen_r.cur",  # El Yazısı
                "No": f"{cursor_path}\\unavail_r.cur",  # Kullanılamaz
                "SizeNS": f"{cursor_path}\\ns_r.cur",  # Yukarı-Aşağı Boyutlandır
                "SizeWE": f"{cursor_path}\\ew_r.cur",  # Sol-Sağ Boyutlandır
                "SizeNWSE": f"{cursor_path}\\nwse_r.cur",  # Çapraz Boyutlandır (Sağ Alt)
                "SizeNESW": f"{cursor_path}\\nesw_r.cur",  # Çapraz Boyutlandır (Sol Alt)
                "SizeAll": f"{cursor_path}\\move_r.cur",  # Taşı
                "UpArrow": f"{cursor_path}\\up_r.cur",  # Yukarı Ok
                "Hand": f"{cursor_path}\\link_r.cur"  # Bağlantı Seçimi
            }

            with OpenKey(HKEY_CURRENT_USER, key_path, 0, KEY_SET_VALUE) as key:
                for cursor_name, file_name in cursors.items():
                    SetValueEx(key, cursor_name, 0, REG_SZ, file_name)

            # Sistem ayarlarını yeniden yükle
            ctypes.windll.user32.SystemParametersInfoW(0x0057, 0, None, 0x02)
            print(f"   {SUCCESS} Fare işaretçisi 'Windows Siyah (sistem düzeni)' olarak ayarlandı.")
        except Exception as e:
            print(f"   {ERROR} Hata: {e}")

    # Temizleme işlemi için geçici klasörleri temizler.
    def clean_temp_folders():
        temp_dirs = [
            os.getenv("TEMP"),
            os.getenv("TMP"),
            os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Recent"),
            "C:\\Windows\\Prefetch"
        ]

        for temp_dir in temp_dirs:
            if os.path.exists(temp_dir):
                try:
                    shutil.rmtree(temp_dir, ignore_errors=True)
                    os.makedirs(temp_dir, exist_ok=True)  # Klasörü yeniden oluştur
                    print(f"   {SUCCESS} {temp_dir} temizlendi.")
                except Exception as e:
                    print(f"   {ERROR} {temp_dir} temizlenirken hata oluştu: {e}")
            else:
                print(f"   {ERROR} {temp_dir} bulunamadı.")

    try:
        enable_dark_mode()
        change_cursor_to_black()
        clean_temp_folders()
        set_high_performance_power_plan()
        set_best_performance_mode()
        arka_plan_degis()
        print(f"\n {SUCCESS} Windows Optimize Edildi.")
    except Exception as e:
        print(f" {ERROR} Bir hata oluştu: {e}")

# --  RENGARENK YAZI  --
def rainbow():
    # Gökkuşağı renklerini tanımlıyoruz
    rainbow_colors = [Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX]
    # Yazılacak metni belirleyelim
    text = input(f" {WARNING} Lütfen Rengarenk olacak yazıyı yazın: ")

    # Her harfi sırayla bir renk ile yazdırıyoruz
    colored_text = ''
    for i, char in enumerate(text):
        colored_text += rainbow_colors[i % len(rainbow_colors)] + char

    # Stili sıfırlayıp yazıyı yazdırıyoruz
    print("\n     ",colored_text)

# -- PUBLİC İP KAMERALARI --
def cctv():
    print(f" {WARNING} Lütfen Bekleyin.")
    try:
        # Orijinal dosyayı oku
        with open("./list.txt", "r", encoding="utf-8") as f:
            icerik = f.read()  # Dosyanın içeriğini değişkene al
        # Masaüstü yolunu al ve dosya oluştur.
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        yeni_dosya_yolu = os.path.join(desktop, "cameras.txt")
        # Yeni dosyayı oluştur ve içeriği yaz
        with open(yeni_dosya_yolu, "w", encoding="utf-8") as yeni_dosya:
            yeni_dosya.write(icerik)
        print(f"    {SUCCESS} Liste masaüstüne 'cameras.txt' olarak oluşturuldu!")
    except FileNotFoundError:
        print(f" {WARNING} list.txt dosyası bulunamadı!")
    except Exception as e:
        print(f" {WARNING} Bir hata oluştu: {e}")


# --  SİSTEM BİLGİLERİ  --
def sinfo():
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    main = f"""
    {Colors.light_gray}███████                       ███████{Colors.reset}        {colored(colrr1,colrg1,colrb1, alt_cizgili_yazi("+-[Mounoa]-+"))}
    {Colors.light_gray}███                               ███{Colors.reset}
    {Colors.light_gray}███             ██    ██          ███{Colors.reset}        PC NAME  : {platform.node()}
    {Colors.light_gray}███            ███   ███          ███{Colors.reset}        OS       : {platform.system()} {platform.version()}
    {Colors.gray}███         ██████████████        ███{Colors.reset}        RAM      : {memory_info.total / (1024 ** 3):.2f} GB
    {Colors.gray}███           ███   ███           ███{Colors.reset}        CPU      : {psutil.cpu_percent(interval=1)}%
    {Colors.gray}███           ███   ███           ███{Colors.reset}        EKRN     : {user32.GetSystemMetrics(0)}x{user32.GetSystemMetrics(1)}
    {Colors.gray}███        ██████████████         ███{Colors.reset}        ONLINE   : {shutil.which("ping") and "Erişilebilir" or "Erişilemez"}
    {Colors.dark_gray}███          ███   ███            ███{Colors.reset}        REAL IP  : {requests.get('https://api.ipify.org').text}
    {Colors.dark_gray}███          ██    ██             ███{Colors.reset}        Version  : {MOUNOA_VER}
    {Colors.dark_gray}███                               ███{Colors.reset}
    {Colors.dark_gray}███████                       ███████{Colors.reset}        {colored(colrr1,colrg1,colrb1, alt_cizgili_yazi("██"))}  {colored(colrr2,colrg2,colrb2, alt_cizgili_yazi("██"))}  {colored(colrr3,colrg3,colrb3, alt_cizgili_yazi("██"))}  {colored(colrr4,colrg4,colrb4, alt_cizgili_yazi("██"))}  {colored(colrr5,colrg5,colrb5, alt_cizgili_yazi("██"))}  {colored(colrr6,colrg6,colrb6, alt_cizgili_yazi("██"))}

    """
    print(main)

# --  TKT Tkinter's Toolkit  --
def tkt():
    # tkinterdnd2 kütüphanesini kontrol et ve import et
    tkdnd = None
    try:
        import tkinterdnd2
        tkdnd = tkinterdnd2
    except ImportError:
        print("Uyarı: Sürükle-bırak özelliği için 'tkinterdnd2' kütüphanesi kurulu değil.")
        print("Kurmak için: pip install tkinterdnd2")

    # --- Genel Stil Sabitleri (pass_and_user ve IT_SYSTEM'dan esinlenerek) ---
    TK_BG_COLOR = "#2E2E2E"  # Koyu Gri Arkaplan
    TK_FG_COLOR = "#E0E0E0"  # Açık Gri Yazı
    TK_BTN_BG_COLOR = "#3C3C3C" # Buton Arkaplanı
    TK_BTN_FG_COLOR = "#FFFFFF" # Buton Yazı Rengi
    TK_ENTRY_BG_COLOR = "#4A4A4A" # Giriş Alanı Arkaplanı
    TK_TAB_SELECTED_BG = "#1e90ff" # Seçili Sekme Arkaplanı (Mavi)
    TK_TAB_SELECTED_FG = "#FFFFFF" # Seçili Sekme Yazı Rengi
    TK_LABEL_HEADER_FG = "#e10040" # IT Desk Başlık Rengi
    TK_MAVIZ_BLUE = "#9B9BE1" # Maviz İmza Rengi

    # --- Çekirdek Fonksiyonlar (SHA256UI'dan) ---
    def calculate_sha256_hash(file_path):
        """Verilen dosyanın SHA256 hash değerini hesaplar."""
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for block in iter(lambda: f.read(4096), b""):
                    sha256.update(block)
            return sha256.hexdigest()
        except FileNotFoundError:
            messagebox.showerror("Dosya Hatası", f"Dosya bulunamadı: {file_path}", parent=root)
            return None
        except Exception as e:
            messagebox.showerror("Hash Hesaplama Hatası", f"Dosya okunurken bir hata oluştu: {str(e)}", parent=root)
            return None

    def download_file(url, save_path):
        """Verilen URL'den dosyayı indirir ve belirtilen yola kaydeder."""
        try:
            response = requests.get(url, stream=True, timeout=30) # Timeout eklendi
            response.raise_for_status()  # HTTP hatalarını kontrol et
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            return True
        except requests.exceptions.Timeout:
            messagebox.showerror("İndirme Hatası", f"URL zaman aşımına uğradı: {url}", parent=root)
            return False
        except requests.exceptions.RequestException as e:
            messagebox.showerror("İndirme Hatası", f"Dosya indirilemedi: {str(e)}", parent=root)
            return False
        except Exception as e:
            messagebox.showerror("İndirme Hatası", f"Bilinmeyen bir indirme hatası: {str(e)}", parent=root)
            return False

    def verify_hash_and_show_message(calculated_hash, expected_hash, file_description="Dosyanın"):
        """Hesaplanan ve beklenen hash değerlerini karşılaştırır ve kullanıcıya bilgi verir."""
        if calculated_hash and expected_hash:
            if calculated_hash.lower() == expected_hash.lower():
                messagebox.showinfo("Doğrulama Başarılı", f"✅ SHA256 uyuşuyor!\n\n{file_description} SHA256:\n{calculated_hash}", parent=root)
                return True
            else:
                messagebox.showwarning("Doğrulama Başarısız", f"❌ SHA256 uyuşmuyor!\n\nBeklenen: {expected_hash}\nHesaplanan: {calculated_hash}", parent=root)
                return False
        elif calculated_hash and not expected_hash: # Sadece hesaplama yapıldıysa
            messagebox.showinfo("SHA256 Değeri", f"{file_description} SHA256 Değeri:\n{calculated_hash}", parent=root)
            return True # Hash hesaplandı, beklenen olmadığı için doğrulama yapılmadı ama işlem başarılı.
        return False

    # --- Çekirdek Fonksiyonlar (pass_and_user'dan) ---
    UNLULER = "aeiou"
    SESSIZLER = "bcdfghjklmnprstvyz"

    def marka_stili_uret(uzunluk=6):
        sonuc = ""
        for i in range(uzunluk):
            if i % 2 == 0:
                sonuc += random.choice(SESSIZLER)
            else:
                sonuc += random.choice(UNLULER)
        return sonuc.capitalize()

    def rastgele_parola_uret(uzunluk=12, harf=True, rakam=True, ozel=True):
        karakter_havuzu = ""
        if harf:
            karakter_havuzu += string.ascii_letters
        if rakam:
            karakter_havuzu += string.digits
        if ozel:
            karakter_havuzu += string.punctuation

        if not karakter_havuzu:
            return "Seçim yapılmadı"

        try:
            import secrets
            return ''.join(secrets.choice(karakter_havuzu) for _ in range(uzunluk))
        except ImportError:
            return ''.join(random.choice(karakter_havuzu) for _ in range(uzunluk))

    # --- Ana Uygulama ---
    def main_application():
        global root

        if tkdnd:
            root = tkdnd.TkinterDnD.Tk()
        else:
            root = tk.Tk()

        root.title("Hepsi Bir Arada Araç Kutusu (Mounoa & Maviz)")
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(script_dir, "icon.ico")
            if os.path.exists(icon_path):
                root.iconbitmap(icon_path)
            else:
                print(f"Uyarı: İkon dosyası bulunamadı: {icon_path}")
        except tk.TclError:
            print("Uyarı: İkon dosyası yüklenemedi. 'icon.ico' dosyasının doğru formatta ve konumda olduğundan emin olun.")
        except NameError:
            print("Uyarı: Script yolu belirlenemediği için ikon yüklenemedi.")


        WIDTH, HEIGHT = 600, 500 # Yüksekliği biraz artırdık
        root.resizable(False, False)

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (WIDTH/2))
        y_cordinate = int((screen_height/2) - (HEIGHT/2))
        root.geometry(f"{WIDTH}x{HEIGHT}+{x_cordinate}+{y_cordinate}")
        root.configure(bg=TK_BG_COLOR)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background=TK_BG_COLOR)
        style.configure("TLabel", background=TK_BG_COLOR, foreground=TK_FG_COLOR, padding=5)
        style.configure("Header.TLabel", background=TK_BG_COLOR, foreground=TK_FG_COLOR, font=('Arial', 12, 'bold'))
        style.configure("TButton", background=TK_BTN_BG_COLOR, foreground=TK_BTN_FG_COLOR, borderwidth=1, padding=6, font=('Arial', 9))
        style.map("TButton",
                background=[("active", TK_TAB_SELECTED_BG), ("pressed", TK_TAB_SELECTED_BG)],
                foreground=[("active", TK_TAB_SELECTED_FG), ("pressed", TK_TAB_SELECTED_FG)])
        style.configure("Danger.TButton", background="#e74c3c", foreground=TK_BTN_FG_COLOR)
        style.map("Danger.TButton", background=[("active", "#c0392b"), ("pressed", "#c0392b")])
        style.configure("TEntry", fieldbackground=TK_ENTRY_BG_COLOR, foreground=TK_FG_COLOR, borderwidth=1, insertbackground=TK_FG_COLOR)
        style.map("TEntry", fieldbackground=[('focus', '#555555')])
        style.configure("TCheckbutton", background=TK_BG_COLOR, foreground=TK_FG_COLOR, indicatorcolor=TK_ENTRY_BG_COLOR, padding=5)
        style.map("TCheckbutton",
                background=[("active", TK_BG_COLOR)],
                indicatorcolor=[("selected", TK_TAB_SELECTED_BG), ("pressed", TK_TAB_SELECTED_BG)])
        style.configure("TNotebook", background=TK_BG_COLOR, borderwidth=1)
        style.configure("TNotebook.Tab", background=TK_BTN_BG_COLOR, foreground=TK_FG_COLOR, padding=[10, 5], font=('Arial', 10))
        style.map("TNotebook.Tab",
                background=[("selected", TK_TAB_SELECTED_BG), ("active", '#4A4A4A')],
                foreground=[("selected", TK_TAB_SELECTED_FG), ("active", TK_FG_COLOR)])

        tab_control = ttk.Notebook(root, style="TNotebook")

        # --- Sekme 1: SHA256 Aracı (Değişiklik yok, kısaltıldı) ---
        def setup_sha256_tab(parent_tab_control):
            sha_tab = ttk.Frame(parent_tab_control, style="TFrame", padding=10)
            parent_tab_control.add(sha_tab, text='SHA256 Aracı')
            sha_notebook = ttk.Notebook(sha_tab, style="TNotebook")
            # Yerel Dosya Alt Sekmesi
            local_tab = ttk.Frame(sha_notebook, style="TFrame", padding=10)
            sha_notebook.add(local_tab, text='Yerel Dosya')
            ttk.Label(local_tab, text="📂 Dosya Yolu (sürükleyip bırakabilirsin):", style="Header.TLabel").pack(pady=(5,0), anchor="w")
            entry_local_file_path = ttk.Entry(local_tab, width=60)
            entry_local_file_path.pack(pady=5, padx=5, fill=tk.X)
            ttk.Label(local_tab, text="🔑 Beklenen SHA256 (Doğrulama için - İsteğe Bağlı):", style="Header.TLabel").pack(pady=(5,0), anchor="w")
            entry_local_expected_hash = ttk.Entry(local_tab, width=60)
            entry_local_expected_hash.pack(pady=5, padx=5, fill=tk.X)
            ttk.Label(local_tab, text="🔎 Hesaplanan SHA256:", style="Header.TLabel").pack(pady=(5,0), anchor="w")
            entry_local_calculated_hash = ttk.Entry(local_tab, width=60, state='readonly')
            entry_local_calculated_hash.pack(pady=5, padx=5, fill=tk.X)
            def handle_local_file_operation():
                file_path = entry_local_file_path.get()
                expected_hash = entry_local_expected_hash.get().strip()
                if not file_path:
                    messagebox.showwarning("Eksik Bilgi", "Lütfen bir dosya yolu girin veya seçin.", parent=sha_tab)
                    return
                if not os.path.exists(file_path):
                    messagebox.showerror("Hata", f"Belirtilen dosya bulunamadı:\n{file_path}", parent=sha_tab)
                    return
                calculated_hash = calculate_sha256_hash(file_path)
                entry_local_calculated_hash.config(state='normal')
                entry_local_calculated_hash.delete(0, tk.END)
                if calculated_hash:
                    entry_local_calculated_hash.insert(0, calculated_hash)
                entry_local_calculated_hash.config(state='readonly')
                if calculated_hash:
                    verify_hash_and_show_message(calculated_hash, expected_hash if expected_hash else None, f"'{os.path.basename(file_path)}' dosyasının")
            def browse_local_file():
                dosya = filedialog.askopenfilename(parent=sha_tab)
                if dosya:
                    entry_local_file_path.delete(0, tk.END)
                    entry_local_file_path.insert(0, dosya)
            def on_drop_local_file(event):
                file_path = event.data.strip('{}')
                if os.path.exists(file_path) and os.path.isfile(file_path):
                    entry_local_file_path.delete(0, tk.END)
                    entry_local_file_path.insert(0, file_path)
                elif os.path.isdir(file_path):
                    messagebox.showwarning("Sürükle Bırak Uyarısı", "Lütfen bir klasör değil, bir dosya sürükleyin.", parent=sha_tab)
            buttons_frame_local = ttk.Frame(local_tab, style="TFrame")
            buttons_frame_local.pack(pady=10, fill=tk.X)
            ttk.Button(buttons_frame_local, text="📁 Dosya Seç", command=browse_local_file, width=20).pack(side=tk.LEFT, padx=5)
            ttk.Button(buttons_frame_local, text="⚙️ Hesapla / Doğrula", command=handle_local_file_operation, width=20).pack(side=tk.LEFT, padx=5)
            if tkdnd:
                entry_local_file_path.drop_target_register(tkdnd.DND_FILES)
                entry_local_file_path.dnd_bind("<<Drop>>", on_drop_local_file)
            else:
                ttk.Label(local_tab, text="Sürükle-bırak için 'tkinterdnd2' kurulu değil.", foreground="orange").pack(pady=5, anchor="w")
            # URL Dosyası Alt Sekmesi
            url_tab_sha = ttk.Frame(sha_notebook, style="TFrame", padding=10)
            sha_notebook.add(url_tab_sha, text='URL Dosyası')
            ttk.Label(url_tab_sha, text="🔗 Dosya URL:", style="Header.TLabel").pack(pady=(5,0), anchor="w")
            entry_url_path = ttk.Entry(url_tab_sha, width=60)
            entry_url_path.pack(pady=5, padx=5, fill=tk.X)
            ttk.Label(url_tab_sha, text="🔑 Beklenen SHA256 (Doğrulama için - İsteğe Bağlı):", style="Header.TLabel").pack(pady=(5,0), anchor="w")
            entry_url_expected_hash = ttk.Entry(url_tab_sha, width=60)
            entry_url_expected_hash.pack(pady=5, padx=5, fill=tk.X)
            status_label_url = ttk.Label(url_tab_sha, text="", style="TLabel")
            def handle_url_calculate_hash_only():
                url = entry_url_path.get()
                if not url:
                    messagebox.showwarning("Eksik Bilgi", "Lütfen dosya URL'sini girin.", parent=sha_tab)
                    return
                temp_filename = "temp_downloaded_file_for_hash"
                status_label_url.config(text="İndiriliyor ve hesaplanıyor...")
                root.update_idletasks()
                if download_file(url, temp_filename):
                    calculated_hash = calculate_sha256_hash(temp_filename)
                    if calculated_hash:
                        messagebox.showinfo("SHA256 Değeri (URL'den)", f"'{os.path.basename(url)}' dosyasının SHA256'sı:\n{calculated_hash}", parent=sha_tab)
                    if os.path.exists(temp_filename):
                        try: os.remove(temp_filename)
                        except Exception as e: print(f"Geçici dosya silinirken hata: {e}")
                status_label_url.config(text="")
            def handle_url_download_and_verify():
                url = entry_url_path.get()
                expected_hash = entry_url_expected_hash.get().strip()
                if not url:
                    messagebox.showwarning("Eksik Bilgi", "Lütfen dosya URL'sini girin.", parent=sha_tab)
                    return
                if not expected_hash:
                    messagebox.showwarning("Eksik Bilgi", "Doğrulama için beklenen SHA256 değerini girin.", parent=sha_tab)
                    return
                temp_filename = "temp_downloaded_file_for_verify"
                status_label_url.config(text="İndiriliyor ve doğrulanıyor...")
                root.update_idletasks()
                if download_file(url, temp_filename):
                    calculated_hash = calculate_sha256_hash(temp_filename)
                    if calculated_hash:
                        verify_hash_and_show_message(calculated_hash, expected_hash, f"URL'den indirilen '{os.path.basename(url)}' dosyasının")
                    if os.path.exists(temp_filename):
                        try: os.remove(temp_filename)
                        except Exception as e: print(f"Geçici dosya silinirken hata: {e}")
                status_label_url.config(text="")
            buttons_frame_url = ttk.Frame(url_tab_sha, style="TFrame")
            buttons_frame_url.pack(pady=10, fill=tk.X)
            ttk.Button(buttons_frame_url, text="🔍 Sadece SHA256 Hesapla", command=handle_url_calculate_hash_only, width=25).pack(side=tk.LEFT, padx=5)
            ttk.Button(buttons_frame_url, text="📥 İndir ve Doğrula", command=handle_url_download_and_verify, width=25).pack(side=tk.LEFT, padx=5)
            status_label_url.pack(pady=5, anchor="w")
            sha_notebook.pack(expand=1, fill='both', padx=5, pady=5)
        setup_sha256_tab(tab_control)

        # --- Sekme 2: Parola & Kullanıcı Adı Üretici ---
        def setup_pass_user_tab(parent_tab_control):
            pass_user_tab = ttk.Frame(parent_tab_control, style="TFrame", padding=10)
            parent_tab_control.add(pass_user_tab, text='Parola & Kullanıcı Adı')

            pass_user_notebook = ttk.Notebook(pass_user_tab, style="TNotebook")

            # Parola Üretici Alt Sekmesi
            frame_parola = ttk.Frame(pass_user_notebook, style="TFrame", padding=15)
            pass_user_notebook.add(frame_parola, text='🔐 Parola Üretici')

            ttk.Label(frame_parola, text="Parola Uzunluğu:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
            entry_parola_uzunluk = ttk.Entry(frame_parola, width=10)
            entry_parola_uzunluk.insert(0, "16")
            entry_parola_uzunluk.grid(row=0, column=1, sticky="w", padx=5, pady=5)

            harf_var = tk.BooleanVar(value=True)
            rakam_var = tk.BooleanVar(value=True)
            ozel_var = tk.BooleanVar(value=True)

            check_frame = ttk.Frame(frame_parola, style="TFrame")
            ttk.Checkbutton(check_frame, text="Harf (a-z, A-Z)", variable=harf_var).pack(side=tk.LEFT, padx=5)
            ttk.Checkbutton(check_frame, text="Rakam (0-9)", variable=rakam_var).pack(side=tk.LEFT, padx=5)
            ttk.Checkbutton(check_frame, text="Özel (!@#)", variable=ozel_var).pack(side=tk.LEFT, padx=5)
            check_frame.grid(row=1, column=0, columnspan=2, sticky="w", pady=5) # columnspan 2 olarak güncellendi

            def parola_uret_action():
                try:
                    uzunluk = int(entry_parola_uzunluk.get())
                    if uzunluk <= 0 or uzunluk > 128:
                        messagebox.showerror("Hata", "Parola uzunluğu 1 ile 128 arasında olmalıdır!", parent=pass_user_tab)
                        return
                    parola = rastgele_parola_uret(uzunluk, harf_var.get(), rakam_var.get(), ozel_var.get())
                    entry_parola.delete(0, tk.END)
                    entry_parola.insert(0, parola)
                except ValueError:
                    messagebox.showerror("Hata", "Geçerli bir sayı girin!", parent=pass_user_tab)

            def panoya_kopyala(entry_widget, tab_parent):
                try:
                    root.clipboard_clear()
                    root.clipboard_append(entry_widget.get())
                    messagebox.showinfo("Kopyalandı", "Sonuç panoya kopyalandı!", parent=tab_parent)
                except tk.TclError:
                    messagebox.showwarning("Hata", "Panoya kopyalama başarısız. Pano meşgul olabilir.", parent=tab_parent)

            # --- DÜZELTİLMİŞ YERLEŞİM BAŞLANGICI (PAROLA) ---
            ttk.Button(frame_parola, text="🔑 Parola Üret", command=parola_uret_action).grid(row=2, column=0, columnspan=2, pady=(10,5), sticky="w")

            ttk.Label(frame_parola, text="Oluşturulan Parola:").grid(row=3, column=0, sticky="w", padx=5, pady=(5,0), ipadx=0) # ipadx=0 eklendi

            # Sonuçların gösterileceği Entry widget'ını Kopyala butonu lambda'sından önce tanımla
            entry_parola = ttk.Entry(frame_parola, width=30) # Genişlik ayarlandı
            entry_parola.grid(row=4, column=0, padx=5, pady=(0,10), sticky="ew")

            ttk.Button(frame_parola, text="📋 Kopyala", command=lambda: panoya_kopyala(entry_parola, pass_user_tab)).grid(row=4, column=1, sticky="w", padx=(0,5), pady=(0,10)) # entry_parola ile aynı satır, sağında
            # --- DÜZELTİLMİŞ YERLEŞİM SONU (PAROLA) ---


            # Kullanıcı Adı Üretici Alt Sekmesi
            frame_kullanici = ttk.Frame(pass_user_notebook, style="TFrame", padding=15)
            pass_user_notebook.add(frame_kullanici, text='👤 Kullanıcı Adı Üretici')

            ttk.Label(frame_kullanici, text="İsim Uzunluğu (örn: 4-10):").grid(row=0, column=0, sticky="w", padx=5, pady=5)
            entry_isim_uzunluk = ttk.Entry(frame_kullanici, width=10)
            entry_isim_uzunluk.insert(0, "6")
            entry_isim_uzunluk.grid(row=0, column=1, sticky="w", padx=5, pady=5)

            def kullanici_adi_uret_action():
                try:
                    uzunluk = int(entry_isim_uzunluk.get())
                    if uzunluk <= 1 or uzunluk > 20:
                        messagebox.showerror("Hata", "Kullanıcı adı uzunluğu 2 ile 20 arasında olmalıdır!", parent=pass_user_tab)
                        return
                    isim = marka_stili_uret(uzunluk)
                    entry_kullanici_adi.delete(0, tk.END)
                    entry_kullanici_adi.insert(0, isim)
                except ValueError:
                    messagebox.showerror("Hata", "Geçerli bir uzunluk girin!", parent=pass_user_tab)

            # --- DÜZELTİLMİŞ YERLEŞİM BAŞLANGICI (KULLANICI ADI) ---
            ttk.Button(frame_kullanici, text="👤 Kullanıcı Adı Üret", command=kullanici_adi_uret_action).grid(row=1, column=0, columnspan=2, pady=(10,5), sticky="w")

            ttk.Label(frame_kullanici, text="Oluşturulan Kullanıcı Adı:").grid(row=2, column=0, sticky="w", padx=5, pady=(5,0), ipadx=0) # ipadx=0 eklendi

            # Sonuçların gösterileceği Entry widget'ını Kopyala butonu lambda'sından önce tanımla
            entry_kullanici_adi = ttk.Entry(frame_kullanici, width=25) # Genişlik ayarlandı
            entry_kullanici_adi.grid(row=3, column=0, padx=5, pady=(0,10), sticky="ew")

            ttk.Button(frame_kullanici, text="📋 Kopyala", command=lambda: panoya_kopyala(entry_kullanici_adi, pass_user_tab)).grid(row=3, column=1, sticky="w", padx=(0,5), pady=(0,10)) # entry_kullanici_adi ile aynı satır, sağında
            # --- DÜZELTİLMİŞ YERLEŞİM SONU (KULLANICI ADI) ---

            pass_user_notebook.pack(expand=1, fill='both', padx=5, pady=5)
        setup_pass_user_tab(tab_control)

        # --- Sekme 3: IT Desk (Değişiklik yok, kısaltıldı) ---
        def setup_it_system_tab(parent_tab_control):
            it_tab = ttk.Frame(parent_tab_control, style="TFrame", padding=10)
            parent_tab_control.add(it_tab, text='IT Desk')
            title = ttk.Label(it_tab, text="IT Desk", font='Arial 20 bold', foreground=TK_LABEL_HEADER_FG, style="TLabel")
            title.pack(pady=(5,0))
            description = ttk.Label(it_tab, text="(Bilgi Teknolojileri Masası)", font='Arial 9', style="TLabel")
            description.pack(pady=(0,10))
            button_frame = ttk.Frame(it_tab, style="TFrame")
            button_frame.pack(expand=True, fill=tk.BOTH)
            def sistem_bilgisi():
                bilgi = platform.uname()
                messagebox.showinfo("Sistem Bilgisi", f"Sistem: {bilgi.system}\nSürüm: {bilgi.version}\nMakine: {bilgi.machine}\nİşlemci: {bilgi.processor}", parent=it_tab)
            def ag_bilgisi():
                try:
                    hostname = socket.gethostname()
                    ip_adresi = socket.gethostbyname(hostname)
                    messagebox.showinfo("Ağ Bilgisi", f"Hostname: {hostname}\nIP Adresi: {ip_adresi}", parent=it_tab)
                except socket.gaierror:
                    messagebox.showerror("Ağ Hatası", "IP adresi alınamadı. Ağ bağlantınızı kontrol edin.", parent=it_tab)
            def disk_kullanimi():
                try:
                    disk = psutil.disk_usage('/')
                    messagebox.showinfo("Disk Kullanımı (C:)", f"Toplam: {disk.total / (1024**3):.2f} GB\nKullanılan: {disk.used / (1024**3):.2f} GB ({disk.percent}%)\nBoş: {disk.free / (1024**3):.2f} GB", parent=it_tab)
                except Exception as e:
                    messagebox.showerror("Hata", f"Disk bilgisi alınamadı: {e}", parent=it_tab)
            def cpu_kullanimi():
                try:
                    cpu_percent = psutil.cpu_percent(interval=0.5)
                    cpu_cores = psutil.cpu_count(logical=False)
                    logical_cores = psutil.cpu_count(logical=True)
                    messagebox.showinfo("CPU Kullanımı", f"Anlık CPU Kullanımı: %{cpu_percent}\nFiziksel Çekirdek: {cpu_cores}\nMantıksal Çekirdek: {logical_cores}", parent=it_tab)
                except Exception as e:
                    messagebox.showerror("Hata", f"CPU bilgisi alınamadı: {e}", parent=it_tab)
            def bellek_kullanimi():
                try:
                    bellek = psutil.virtual_memory()
                    messagebox.showinfo("Bellek Kullanımı", f"Toplam: {bellek.total / (1024**3):.2f} GB\nKullanılan: {bellek.used / (1024**3):.2f} GB ({bellek.percent}%)\nBoş: {bellek.available / (1024**3):.2f} GB", parent=it_tab)
                except Exception as e:
                    messagebox.showerror("Hata", f"Bellek bilgisi alınamadı: {e}", parent=it_tab)
            def calisan_surecler():
                try:
                    surecler = [proc.info for proc in psutil.process_iter(['pid', 'name', 'username'])][:15]
                    sonuc = "PID | İsim | Kullanıcı\n" + "-"*30 + "\n"
                    sonuc += "\n".join([f"{p['pid']} | {p['name']} | {p['username'] if p['username'] else 'N/A'}" for p in surecler])
                    msg_window = tk.Toplevel(root)
                    msg_window.title("Çalışan Süreçler (İlk 15)")
                    msg_window.geometry("400x300")
                    msg_window.configure(bg=TK_BG_COLOR)
                    text_area = tk.Text(msg_window, wrap=tk.WORD, bg=TK_ENTRY_BG_COLOR, fg=TK_FG_COLOR, relief=tk.FLAT, font=("Courier New", 9))
                    text_area.insert(tk.END, sonuc)
                    text_area.config(state=tk.DISABLED)
                    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
                    ttk.Button(msg_window, text="Kapat", command=msg_window.destroy).pack(pady=5)
                    msg_window.transient(root)
                    msg_window.grab_set()
                except Exception as e:
                    messagebox.showerror("Hata", f"Süreç bilgileri alınamadı: {e}", parent=it_tab)
            def komut_calistir_ve_goster(baslik, komut):
                try:
                    process = subprocess.Popen(komut, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='cp857', errors='replace')
                    result, error = process.communicate(timeout=10)
                    output_window = tk.Toplevel(root)
                    output_window.title(baslik)
                    output_window.geometry("600x400")
                    output_window.configure(bg=TK_BG_COLOR)
                    text_widget = tk.Text(output_window, wrap=tk.WORD, bg=TK_ENTRY_BG_COLOR, fg=TK_FG_COLOR, relief=tk.FLAT, font=("Courier New", 9))
                    text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
                    if process.returncode == 0:
                        text_widget.insert(tk.END, result)
                    else:
                        text_widget.insert(tk.END, f"Hata Kodu: {process.returncode}\n\nSTDOUT:\n{result}\n\nSTDERR:\n{error}")
                    text_widget.config(state=tk.DISABLED)
                    ttk.Button(output_window, text="Kapat", command=output_window.destroy).pack(pady=5)
                    output_window.transient(root)
                    output_window.grab_set()
                except subprocess.TimeoutExpired:
                    messagebox.showerror("Zaman Aşımı", f"'{komut}' komutu zaman aşımına uğradı.", parent=it_tab)
                except FileNotFoundError:
                    messagebox.showerror("Hata", f"Komut bulunamadı. ({komut.split()[0]}) Sisteminizde kurulu olduğundan emin olun.", parent=it_tab)
                except Exception as e:
                    messagebox.showerror("Hata", f"{baslik} alınamadı: {e}", parent=it_tab)
            def netbios_durumu(): komut_calistir_ve_goster("NetBIOS Durumu", "nbtstat -n")
            def arp_tablosu(): komut_calistir_ve_goster("ARP Tablosu", "arp -a")
            def route_tablosu(): komut_calistir_ve_goster("Route Tablosu", "route print")
            def pil_durumu():
                try:
                    pil = psutil.sensors_battery()
                    if pil:
                        messagebox.showinfo("Pil/Güç Durumu", f"Şarj: %{pil.percent}\nKalan Süre: {pil.secsleft // 60 if hasattr(pil, 'secsleft') and pil.secsleft != psutil.POWER_TIME_UNLIMITED and pil.secsleft != psutil.POWER_TIME_UNKNOWN else 'Bilinmiyor'} dakika\nDurum: {'Şarj Oluyor' if pil.power_plugged else 'Şarj Olmuyor'}", parent=it_tab)
                    else:
                        messagebox.showinfo("Pil/Güç Durumu", "Pil bilgisi desteklenmiyor veya pil yok.", parent=it_tab)
                except Exception as e:
                    messagebox.showerror("Hata", f"Pil bilgisi alınamadı: {e}", parent=it_tab)
            def confirm_and_execute(action_name, command):
                if messagebox.askyesno("Onay", f"{action_name} istediğinize emin misiniz?", icon='warning', parent=it_tab):
                    try:
                        os.system(command)
                    except Exception as e:
                        messagebox.showerror("Hata", f"{action_name} başarısız: {e}", parent=it_tab)
            def sistem_yeniden_baslat(): confirm_and_execute("Sistemi yeniden başlatmak", "shutdown /r /t 1")
            def sistem_kapat(): confirm_and_execute("Sistemi kapatmak", "shutdown /s /t 1")
            butonlar = [
                ("Sistem Bilgisi", sistem_bilgisi), ("Ağ Bilgisi", ag_bilgisi),
                ("Disk Kullanımı", disk_kullanimi), ("CPU Kullanımı", cpu_kullanimi),
                ("Bellek Kullanımı", bellek_kullanimi), ("Çalışan Süreçler", calisan_surecler),
                ("NetBIOS Durumu", netbios_durumu), ("ARP Tablosu", arp_tablosu),
                ("Route Tablosu", route_tablosu), ("Pil/Güç Durumu", pil_durumu),
            ]
            güç_butonları = [
                ("Sistemi Yeniden Başlat", sistem_yeniden_baslat, "Danger.TButton"),
                ("Sistemi Kapat", sistem_kapat, "Danger.TButton"),
            ]
            for i, (text, command) in enumerate(butonlar):
                row, col = divmod(i, 2)
                btn = ttk.Button(button_frame, text=text, command=command, width=25, style="TButton")
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="ew")
            last_row = (len(butonlar) -1 ) // 2 + 1
            for i, (text, command, btn_style) in enumerate(güç_butonları):
                btn = ttk.Button(button_frame, text=text, command=command, width=25, style=btn_style)
                btn.grid(row=last_row, column=i, padx=5, pady=10, sticky="ew")
            button_frame.grid_columnconfigure(0, weight=1)
            button_frame.grid_columnconfigure(1, weight=1)
        setup_it_system_tab(tab_control)

        # --- Sekme 4: Yapımcı (Değişiklik yok, kısaltıldı) ---
        def setup_developer_tab(parent_tab_control):
            dev_tab = ttk.Frame(parent_tab_control, style="TFrame", padding=20)
            parent_tab_control.add(dev_tab, text='Yapımcı')
            ttk.Label(dev_tab, text="Bu Araç Kutusu Hakkında", font=('Arial', 16, 'bold'), style="Header.TLabel").pack(pady=(10,5))
            ttk.Label(dev_tab, text="Bu uygulama, çeşitli araçları tek bir arayüzde toplamak amacıyla geliştirilmiştir.", justify=tk.CENTER, wraplength=WIDTH-60).pack(pady=5)
            separator = ttk.Separator(dev_tab, orient='horizontal')
            separator.pack(fill='x', pady=15, padx=10)
            ttk.Label(dev_tab, text="Geliştirici & Düzenleyen:", font=('Arial', 12, 'bold'), style="Header.TLabel").pack(pady=(10,0))
            ttk.Label(dev_tab, text="Maviz", font=('Arial', 11)).pack()
            separator2 = ttk.Separator(dev_tab, orient='horizontal')
            separator2.pack(fill='x', pady=15, padx=10)
            ttk.Label(dev_tab, text="Made with <3", font=('Arial', 10, 'italic'), foreground=TK_MAVIZ_BLUE).pack(pady=10, side=tk.BOTTOM)
        setup_developer_tab(tab_control)

        tab_control.pack(expand=1, fill='both', padx=10, pady=10)

        status_bar_text = tk.StringVar()
        status_bar_text.set("Hazır.")
        status_bar = ttk.Label(root, textvariable=status_bar_text, relief=tk.SUNKEN, anchor=tk.W, style="TLabel", padding=(5,2))
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        root.mainloop()

    if __name__ == "__main__":
        main_application()

# -- EKRAN KORUYUCUSU --
def screen_saver():
    class AdvancedScreenSaver:
        def __init__(self, root):
            self.root = root
            self.root.attributes('-fullscreen', True)
            self.root.configure(bg="black")
            self.root.bind("<Escape>", self.exit_screensaver)

            self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
            self.canvas.pack(fill="both", expand=True)

            self.screen_width = self.root.winfo_screenwidth()
            self.screen_height = self.root.winfo_screenheight()

            self.waves = []
            self.create_waves()

            # Orantısal boyutlar
            rect_width = self.screen_width * 0.3
            rect_height = self.screen_height * 0.12
            font_size = int(self.screen_width * 0.035)  # Orantılı font
            exit_font_size = int(self.screen_width * 0.015)

            center_x = self.screen_width // 2
            center_y = self.screen_height // 2

            # Saat çerçevesi
            self.clock_border = self.canvas.create_rectangle(
                center_x - rect_width // 2,
                center_y - rect_height // 2,
                center_x + rect_width // 2,
                center_y + rect_height // 2,
                outline="white",
                width=3
            )

            # Saat metni
            self.clock_text = self.canvas.create_text(
                center_x,
                center_y,
                text="",
                font=("Roboto Mono", font_size, "bold"),
                fill="white"
            )

            # Çıkış mesajı
            self.exit_message = self.canvas.create_text(
                center_x,
                self.screen_height - (exit_font_size * 3),
                text="Çıkmak için ESC tuşuna basın",
                font=("Roboto Mono", exit_font_size),
                fill="gray"
            )

            self.update_clock()
            self.animate_waves()

        def create_waves(self):
            gradient_colors = self.generate_gradient("#550055", "#000055", 10)
            for i in range(10):
                wave_color = gradient_colors[i]
                wave = {
                    "line": self.canvas.create_line(0, 0, 0, 0, fill=wave_color, width=2, smooth=True),
                    "amplitude": random.randint(20, 50),
                    "frequency": random.uniform(0.005, 0.03),
                    "speed": random.uniform(0.02, 0.05),
                    "offset": random.uniform(0, math.pi * 2),
                    "y_base": random.randint(50, self.screen_height - 100)
                }
                self.waves.append(wave)

        def generate_gradient(self, start_color, end_color, steps):
            start_r = int(start_color[1:3], 16)
            start_g = int(start_color[3:5], 16)
            start_b = int(start_color[5:7], 16)
            end_r = int(end_color[1:3], 16)
            end_g = int(end_color[3:5], 16)
            end_b = int(end_color[5:7], 16)

            gradient = []
            for step in range(steps):
                r = start_r + (end_r - start_r) * step // (steps - 1)
                g = start_g + (end_g - start_g) * step // (steps - 1)
                b = start_b + (end_b - start_b) * step // (steps - 1)
                gradient.append(f"#{r:02x}{g:02x}{b:02x}")
            return gradient

        def animate_waves(self):
            for wave in self.waves:
                points = []
                for x in range(0, self.screen_width, 15):
                    y = wave["y_base"] + wave["amplitude"] * math.sin(wave["frequency"] * x + wave["offset"])
                    points.extend([x, y])
                self.canvas.coords(wave["line"], *points)
                wave["offset"] += wave["speed"]
            self.root.after(40, self.animate_waves)

        def update_clock(self):
            current_time = time.strftime("%H:%M:%S")
            self.canvas.itemconfig(self.clock_text, text=current_time)
            self.root.after(1000, self.update_clock)

        def exit_screensaver(self, event):
            self.root.destroy()

    if __name__ == "__main__":
        root = tk.Tk()
        root.attributes('-topmost', True)
        AdvancedScreenSaver(root)
        root.mainloop()

# -- KOMUTLAR --
komutlar = f"""
    ·- -- -[{Colors.light_blue}Komutlar{Fore.RESET}]-- --- - ·

    !h                 {Fore.LIGHTBLACK_EX}= Komutları Gösterir.{Fore.RESET}
    !re                {Fore.LIGHTBLACK_EX}= Mounoa için en iyi gereksinimleri gösterir.{Fore.RESET}

    !spinwindow        {Fore.LIGHTBLACK_EX}= Pencere oluşturur ve masaüstünde döndürür.{Fore.RESET}
    !winutil           {Fore.LIGHTBLACK_EX}= ChrisTitusTech/winutil çalıştırır.{Fore.RESET}
    !rainbow           {Fore.LIGHTBLACK_EX}= Yazılan Şeyi Rengarenk Yapar.{Fore.RESET}
    !cctv              {Fore.LIGHTBLACK_EX}= Açık IP Kameraların listesi.{Fore.RESET}
    !TKT               {Fore.LIGHTBLACK_EX}= Tkinter ile yapılmış araç kitini açar.{Fore.RESET}
    !scrnsaver         {Fore.LIGHTBLACK_EX}= Ekran Koruyucusu açar.{Fore.RESET}

    !myfetch           {Fore.LIGHTBLACK_EX}= Sistem Özelliklerini verir.{Fore.RESET}
    !optimize          {Fore.LIGHTBLACK_EX}= PC'yi Optimize Etmek için Ayar yapar.{Fore.RESET}
    !netscan           {Fore.LIGHTBLACK_EX}= Ağ Tarama yapar.{Fore.RESET}

    !clear             {Fore.LIGHTBLACK_EX}= Ekranı Temizler.{Fore.RESET}
    !credit            {Fore.LIGHTBLACK_EX}= Yapımcıyı gösterir.{Fore.RESET}

    !exit {Fore.LIGHTBLACK_EX}veya{Fore.RESET} !quit   {Fore.LIGHTBLACK_EX}= Çıkış Yapar.{Fore.RESET}
"""
info = f"    {Fore.BLACK}{Back.WHITE} Komutları !h Yazarak Bakabilirsin. {Fore.RESET}{Back.RESET}"
request = f"""
    {colored(colrr1,colrg1,colrb1, alt_cizgili_yazi("---    o-[Mounoa]-o    ---"))}

    {Fore.LIGHTRED_EX}-> En iyi kullanım için Gereksinimler

    {Fore.WHITE}Konsol Font ve Boyutu = {Fore.LIGHTBLACK_EX}JetBrainsMono NFM ExtraBold, 20
    {Colorate.Horizontal(Colors.green_to_yellow, "Python Sürümü", 1)} = {Fore.LIGHTBLACK_EX}3.12.10
    {Fore.LIGHTBLUE_EX}Windows Sürümü = {Fore.LIGHTBLACK_EX}10 Pro

"""
credit = f"""
    {colored(colrr1,colrg1,colrb1, alt_cizgili_yazi("Mounoa"))} {MOUNOA_VER}

    {Fore.LIGHTBLACK_EX}Yapımcı : {Fore.LIGHTBLUE_EX}Maviz{Fore.RESET}

    {Fore.LIGHTRED_EX}@YOUTUBE:  https://www.youtube.com/@MavizOffical{Fore.RESET}
    {Fore.LIGHTBLACK_EX}@GITHUB:   https://github.com/Mav1zz{Fore.RESET}
    {Fore.LIGHTBLUE_EX}@DISCORD:  maviz{Fore.RESET}
"""

# -- BAŞLANGIÇ ANA KOD --
os.system("cls")
print(RGBBANNER + "\n")
time.sleep(0.9)
print(info)
def menu():
    while True:
        sec = input(f"{"\n"}{Fore.RESET}    [#] {colored(colrr1,colrg1,colrb1, alt_cizgili_yazi("Mounoa"))} > {Fore.LIGHTBLACK_EX}")
        print(f"{Fore.RESET}")
        if sec == str("!h"):
            print(komutlar)
        elif sec == str("!re"):
            print(request)
        elif sec == str("!rainbow"):
            rainbow()
        elif sec == str("!winutil"):
            winutil
        elif sec == str("!myfetch"):
            sinfo()
        elif sec == str("!optimize"):
            optimize()
        elif sec == str("!cctv"):
            cctv()
        elif sec == str("!netscan"):
            netscan()
        elif sec == str("!credit"):
            print(credit)
        elif sec == str("!clear") or sec == str("!cls"):
            os.system("cls")
            print(RGBBANNER + "\n")
            time.sleep(0.9)
            print(info)
        elif sec == str("!scrnsaver"):
            # Görev çubuğuna küçült ve tüm pencereleri gizle
            user32.ShowWindow(hwnd, SW_MINIMIZE)
            # Ekran koruyucuyu çalıştır
            screen_saver()
            # Konsolu geri getir
            user32.ShowWindow(hwnd, SW_RESTORE)
        elif sec == str("!TKT"):
            print(f" {INFO} Tkinter arayüzü açılıyor..")
            time.sleep(1)
            # Görev çubuğuna küçült
            user32.ShowWindow(hwnd, SW_MINIMIZE)
            tkt()
            # Konsolu geri getirmek için:
            user32.ShowWindow(hwnd, SW_RESTORE)
            print(f" {INFO} Tkinter arayüzü kapandı.")
        elif sec == str("!spinwindow"):
             # Görev çubuğuna küçült ve tüm pencereleri gizle
            user32.ShowWindow(hwnd, SW_MINIMIZE)
            # Ekran koruyucuyu çalıştır
            spinwindow()
            # Konsolu geri getir
            user32.ShowWindow(hwnd, SW_RESTORE)
            os.system("cls")
            print(RGBBANNER + "\n")
            time.sleep(0.9)
            print(info)
        elif sec == str("exit") or sec == str("quit") or sec == str("!exit") or sec == str("!quit"):
            sys.exit()
        else:
            print(f" {WARNING} Üzgünüm ama hattalı bir kod girdin herhalde :D")
            print("       Komutlara !h yazarak bakabilirsin!")

menu()
