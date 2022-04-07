from rich.console import Console
import time
from time import sleep
import datetime

start = time.time()
console = Console()

data = list(range(0,5))
total = len(data)

print("\n")

with console.status(f"[bold cyan]Sedang mengambil data...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.print(f"[cyan]✅ {datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')} [green]Selesai mengambil data[/green] [red]Data #{num+1}")

    console.print(f'\n✅ [bold]Total Data : {total} | Status : [green]Selesai[/green] | Elapsed time : [red]{str(time.time() - start)[0:6]} detik')