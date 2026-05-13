import typer
import subprocess
from rich.console import Console
from rich.panel import Panel
from devkit.utils.gh import gh, gh_json
from devkit.config import load_config

app = typer.Typer()
console = Console()

@app.command('feature-start')
def feature_start(
    name: str = typer.Argument(..., help='Feature name (kebab-case)'),
    issue: int = typer.Option(None, help='Issue number to link'),
):
    '''Lance une nouvelle feature : branche + draft PR + scaffold IA.'''
    console.rule('[bold]Starting Feature[/bold]')
    config = load_config()

    # 1. Création de la branche
    branch = f'feature/{name}'
    try:
        subprocess.run(['git', 'checkout', '-b', branch], check=True, capture_output=True)
        console.print(f'[green]✓[/green] Created branch: [bold]{branch}[/bold]')
        
        # 2. Push de la branche (avec un commit vide obligatoire pour la PR)
        subprocess.run(['git', 'commit', '--allow-empty', '-m', f'chore: start {name}'], check=True, capture_output=True)
        subprocess.run(['git', 'push', '-u', 'origin', branch], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Erreur Git : {e.stderr.decode()}[/red]")
        return

    # 3. Création de la Draft PR (Correction du double --body)
    pr_title = name.replace('-', ' ').title()
    pr_body = f'Closes #{issue}' if issue else ''
    pr_args = ['pr', 'create', '--draft', '--title', pr_title, '--body', pr_body]
    
    pr_url = gh(*pr_args)
    console.print(f'[green]✓[/green] Draft PR created: [blue]{pr_url}[/blue]')
    
    # 4. Scaffold IA (Plan d'implémentation)
    if issue:
        with console.status("[bold cyan]Consulting AI for implementation plan...[/bold cyan]"):
            issue_data = gh_json('issue', 'view', str(issue), '--json', 'title,body')
            prompt = f"I'm starting work on: {issue_data['title']}\n{issue_data['body']}\nSuggest a step-by-step implementation plan."
            
            # Utilise l'outil configuré (claude par défaut)
            tool = config.get('ai_tool', 'claude')
            plan = subprocess.run([f"{tool}.bat", '--no-interactive', prompt], capture_output=True, text=True)
            
        console.print(Panel(plan.stdout.strip(), title='[cyan]AI Implementation Plan[/cyan]', border_style='cyan'))
    
    console.rule('[green]Ready to code![/green]')
