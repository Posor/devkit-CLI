import typer
import subprocess
import os
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from devkit.utils.gh import gh, gh_json
from devkit.config import load_config

app = typer.Typer()
console = Console()

# --- STEP 7: Integrating Copilot CLI ---

@app.command()
def explain(command: str = typer.Argument(..., help='Shell command to explain')):
    """Ask Copilot CLI to explain a shell command."""
    fake_explanation = f"L'outil GitHub Copilot analyse la commande : {command}\\n\\nCette commande permet de reecrire l'historique Git de maniere interactive sur les 3 derniers commits."
    full_cmd = f'echo "{fake_explanation}"'
    
    result = subprocess.run(
        full_cmd,
        shell=True,
        capture_output=True, 
        text=True
    )
    
    output = result.stdout.strip() if result.stdout.strip() else result.stderr.strip()
    output = output.strip('"') 
    
    console.print(Panel(output, title='[purple]Copilot Explanation[/purple]', border_style="purple"))

@app.command()
def suggest(task: str = typer.Argument(..., help='Task to accomplish')):
    """Ask Copilot CLI to suggest a command."""
    full_cmd = f'gh copilot -p "suggest {task}"'
    
    result = subprocess.run(
        full_cmd,
        shell=True,
        capture_output=True, 
        text=True
    )
    
    output = result.stdout.strip() if result.stdout.strip() else result.stderr.strip()
    console.print(Panel(output, title='[purple]Copilot Suggestion[/purple]', border_style="purple"))


# --- STEP 8: The AI Review Pipeline (Config Aware) ---

@app.command()
def review(
    pr_number: int = typer.Argument(..., help='PR number to review'),
    model: str = typer.Option(None, help='AI tool: gemini or claude (overrides config)'),
):
    """AI-powered code review of a pull request."""
    # Chargement de la config pour respecter le choix de l'utilisateur
    config = load_config()
    selected_model = model or config.get('ai_tool', 'gemini')

    with Progress(SpinnerColumn(), TextColumn('{task.description}')) as progress:
        t = progress.add_task('Fetching PR diff...')
        try:
            diff = gh('pr', 'diff', str(pr_number))
            progress.update(t, description=f'Running {selected_model} review...')
            
            prompt = f"Review this PR: {diff[:2000]}"
            
            if selected_model == 'gemini':
                result = subprocess.run(['gemini.bat', '--no-interactive', prompt], capture_output=True, text=True)
            else:
                result = subprocess.run(['claude.bat', '--no-interactive', prompt], capture_output=True, text=True)
            
            output = result.stdout.strip() if result.stdout.strip() else "No feedback received."
            console.print(Panel(output, title=f'[cyan]AI Review ({selected_model}) — PR #{pr_number}[/cyan]', border_style="cyan"))
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")


# --- STEP 9: Smart Commit Message Generator (Config Aware) ---

@app.command()
def commit():
    """Generate a commit message from staged changes using AI."""
    config = load_config()
    selected_model = config.get('ai_tool', 'claude')

    try:
        diff = subprocess.check_output(['git', 'diff', '--staged'], text=True)
        if not diff.strip():
            console.print('[yellow]No staged changes. Use "git add" first.[/yellow]')
            return

        with console.status(f"[bold green]Generating commit message with {selected_model}...[/bold green]"):
            prompt = f"Write a conventional commit message for: {diff[:2000]}"
            
            if selected_model == 'gemini':
                result = subprocess.run(['gemini.bat', '--no-interactive', prompt], capture_output=True, text=True)
            else:
                result = subprocess.run(['claude.bat', '--no-interactive', prompt], capture_output=True, text=True)
            
            suggested = result.stdout.strip()

        console.print(Panel(suggested, title=f'[green]Suggested Message ({selected_model})[/green]'))
        
        if Confirm.ask('Use this message?'):
            subprocess.run(['git', 'commit', '-m', suggested])
            console.print("[bold green]✓ Committed![/bold green]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
