import shutil
from rich.console import Console

console = Console(stderr=True)

# Liste des outils nécessaires et comment les installer
REQUIRED_TOOLS = {
    'gh': 'Install from https://cli.github.com',
    'fzf': 'sudo apt install fzf',
    'bat': 'sudo apt install bat',  # Souvent utilisé pour colorer les sorties
}

def check_tools():
    """Vérifie la présence des outils et arrête le programme s'il en manque."""
    missing = {t: hint for t, hint in REQUIRED_TOOLS.items() if not shutil.which(t)}
    
    if missing:
        console.print('\n[bold red]❌ Erreur : Outils manquants détectés ![/bold red]')
        for tool, hint in missing.items():
            console.print(f'  • [cyan]{tool}[/cyan] — [i]{hint}[/i]')
        console.print('\n[yellow]Installe ces outils puis relance devkit.[/yellow]')
        raise SystemExit(1)
