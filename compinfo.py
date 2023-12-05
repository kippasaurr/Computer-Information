import psutil

cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freqs = psutil.cpu_freq(percpu=True)
print("CPU Usage per core:")
for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freqs), start=1):
    print(f"Core {i}: {percent}% Frequency: {freq.current} MHz")

virtual_mem = psutil.virtual_memory()
swap = psutil.swap_memory()

print("\nVirtual Memorty:")
print(f"Total: {virtual_mem.total / (1024 ** 3):.2f} GB")
print(f"Available: {virtual_mem.available / (1024 ** 3):.2f} GB")
print(f"Used: {virtual_mem.used / (1024 ** 3):.2f} GB")
print(f"Percent Used: {virtual_mem.percent}%")
print(f"Swap Total: {swap.total / (1024 ** 3):.2f} GB")
print(f"Swap Used {swap.used / (1024 ** 3):.2f} GB")

network = psutil.net_io_counters()
print("\nNetwork Information:")
print(f"Bytes received: {network.bytes_recv}")
print(f"Bytes sent: {network.bytes_sent}")

# Check if system supports retrieving temperature information
if hasattr(psutil, 'sensors_temperatures'):
    temperatures = psutil.sensors_temperatures()
    if temperatures:
        print("\nTemperatures:")
        for name, enteries in temperatures.items():
            for entry in enteries:
                print(f"{name}: {entry.current}°C")
    else:
        print("\nTemperature information unavailable.")
else:
    print("\nTemperature information unavailable on this operating system.")

# Battery information (if it's a laptop)
battery = psutil.sensors_battery()
if battery:
    plugged = "Plugged in" if battery.power_plugged else "Not Plugged in"
    print (f"\nBattery Status: {plugged}, {battery.percent}%")
else:
    print("\nBattery information unavailable.")

disk = psutil.disk_usage('/')
print("\nDisk Information:")
print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")


