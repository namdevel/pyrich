import time
from rich.progress import Progress

print("\n")

with Progress() as proses:

    t1 = proses.add_task("[red]Downloading...", total=100)
    t2 = proses.add_task("[green]Processing...", total=100)
    t3 = proses.add_task("[cyan]Installing...", total=100)

    while not proses.finished:
        proses.update(t1, advance=0.9)
        proses.update(t2, advance=0.6)
        proses.update(t3, advance=0.3)
        time.sleep(0.02)