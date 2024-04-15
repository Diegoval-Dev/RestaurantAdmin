import sys
from pathlib import Path
script_location = Path(__file__).absolute()
project_root = script_location.parent.parent
sys.path.append(str(project_root))

from services.fectutaService import Cliente


def ClienteController(countid):
    try:
        result = Cliente(countid)
        if result["success"]:
            return result["data"]
        else:
            return []
    except Exception as e:
        return []
