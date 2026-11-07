import pyfiglet
from rich.console import Console

banner_console = Console()

def output_banner():
    banner = pyfiglet.figlet_format("VEEX", font="big")

    # Banner
    banner_console.print(f"[bold bright_green]{banner}[/bold bright_green]")

    # Info
    banner_console.print("[bold bright_green]  made by:[/bold bright_green] [white]vxstudio[/white]")
    banner_console.print("[bold bright_green]  version:[/bold bright_green] [white]0.1.0[/white]")
    banner_console.print("[bold bright_green]  goated:[/bold bright_green] [white]true[/white]")

    # End LINE (get it cuz its a line that ends the banner :sob: )
    banner_console.print("[bold bright_green]  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    banner_console.print()