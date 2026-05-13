import subprocess
import json
from typing import Any

def gh(*args: str) -> str:
    """Exécute une commande gh et retourne la sortie texte."""
    result = subprocess.run(
        ['gh', *args],
        capture_output=True, text=True, check=True
    )
    return result.stdout.strip()

def gh_json(*args: str) -> Any:
    """Exécute une commande gh avec --json et parse le résultat."""
    # On force l'ajout de l'argument --json si on utilise cette fonction
    raw = gh(*args)
    return json.loads(raw) if raw else []

