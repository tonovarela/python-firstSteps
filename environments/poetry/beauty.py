from rich.console import Console
from rich.text import Text
import time



console = Console()
mensaje = "Hola, Varela, espero que te encuentres bien."

for letra in mensaje:
    console.print(Text(letra,style="bold green"),end="" )
    time.sleep(0.1)
