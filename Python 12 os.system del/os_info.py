
import psutil

memory_info = psutil.virtual_memory()

memory_bites = memory_info.total

memory_gigabytes = memory_bites / (1024**3)


physical_core = psutil.process_iter()

number_locical_core= psutil.cpu_percent(interval=1)


print(physical_core)
print(number_locical_core)
print(memory_bites)
print(f'{memory_gigabytes :.2f}GB')

physical_core = psutil.cpu_count()
