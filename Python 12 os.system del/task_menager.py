import psutil
import time

processes = list(psutil.process_iter(['name', 'memory_percent', 'cpu_percent']))

for proc in processes :
    proc.cpu_percent(interval=None)

time.sleep(1)

print(f"{'Name':<25}{'Memory':<15}{'CPU':<15}")

for proc in processes :
    print(f"{proc.name() : <10}{proc.memory_percent():<10.2f}{proc.cpu_percent():<10}")