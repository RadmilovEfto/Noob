import psutil

processes = psutil.process_iter(['name', 'memory_percent', 'cpu_percent'])


for proc in processes :
    print(f"name {proc.name()} / Memoriy : {proc.memory_percent():.2f}% / CPU :  {proc.cpu_percent(interval=None)} % ")