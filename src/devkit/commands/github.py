import typer
import subprocess
from rich.console import Console
from rich.table import Table
from devkit.utils.gh import gh_json

app = typer.Typer()
console = Console()

def fzf_select(items: list[str], prompt: str = 'Select > ') -> str:
    """Fait passer une liste dans fzf et retourne la ligne sélectionnée."""
    proc = subprocess.run(
        ['fzf', f'--prompt={prompt}', '--height=40%', '--border'],
        input='\n'.join(items),
        capture_output=True, text=True
    )
    return proc.stdout.strip()

@app.command()
def issues(interactive: bool = typer.Option(False, "--interactive", "-i", help="Mode interactif avec fzf")):
    """Liste les issues et permet d'en ouvrir une en mode interactif."""
    data = gh_json('issue', 'list', '--json', 'number,title')
    
    if not data:
        console.print("[yellow]Aucune issue trouvée.[/yellow]")
        return

    if interactive:
        lines = [f"#{i['number']} {i['title']}" for i in data]
        selected = fzf_select(lines, prompt='Issue > ')
        if selected:
            issue_num = selected.split()[0].lstrip('#')
            subprocess.run(['gh', 'issue', 'view', issue_num, '--web'])
    else:
        # --- LA PARTIE À MODIFIER ---
        table = Table(title="GitHub Open Issues", border_style="magenta")
        table.add_column("ID", style="cyan", justify="right")
        table.add_column("Titre", style="white")

        for i in data:
            table.add_row(f"#{i['number']}", i['title'])
        
        console.print(table)
        # ----------------------------

@app.command()
def pr_summary(number: int):
    """Affiche un résumé d'une Pull Request (Titre, corps et fichiers modifiés)."""
    try:
        # On récupère les infos de base
        pr = gh_json('pr', 'view', str(number), '--json', 'title,body,files')
        
        console.rule(f"[bold]PR #{number} : {pr['title']}[/bold]")
        console.print(f"\n[italic]{pr['body'] or 'Pas de description.'}[/italic]\n")
        
        table = Table(title="Fichiers modifiés", border_style="yellow")
        table.add_column("Fichier")
        for f in pr.get('files', []):
            table.add_row(f['path'])
        
        console.print(table)
    except Exception as e:
        console.print(f"[red]PR introuvable ou erreur : {e}[/red]")

@app.command()
def run_status():
    """Affiche le statut des derniers lancements CI/CD (GitHub Actions)."""
    try:
        runs = gh_json('run', 'list', '--limit', '5', '--json', 'displayTitle,status,conclusion,headBranch')
        
        table = Table(title="Derniers Runs CI/CD", border_style="blue")
        table.add_column("Workflow")
        table.add_column("Branche", style="cyan")
        table.add_column("Statut")

        for r in runs:
            color = "green" if r['conclusion'] == "success" else "red" if r['conclusion'] == "failure" else "yellow"
            status = f"[{color}]{r['conclusion'] or r['status']}[/{color}]"
            table.add_row(r['displayTitle'], r['headBranch'], status)
        
        console.print(table)
    except Exception as e:
        console.print(f"[red]Erreur Actions : {e}[/red]")
