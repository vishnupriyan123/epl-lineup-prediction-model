import json
import pandas as pd
from pathlib import Path


# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"

def load_fpl_json(filepath=DATA_DIR/ "fpl_bootstrap.json"):
    """Load FPL data from saved JSON file and convert to DataFrame."""
    with open(filepath, "r") as file:
        data = json.load(file)
    
    # Convert players list to DataFrame
    players = pd.DataFrame(data["elements"])
    teams = pd.DataFrame(data["teams"])
    positions = pd.DataFrame(data["element_types"])

    # Add readable team & position names
    players["team_name"] = players["team"].map(teams.set_index("id")["name"])
    players["position"] = players["element_type"].map(positions.set_index("id")["singular_name"])

    # Select useful columns
    selected_columns = [
        "first_name", "second_name", "team_name", "position", "now_cost",
        "minutes", "form", "total_points", "status", "news"
    ]
    players = players[selected_columns]
    players["full_name"] = players["first_name"] + " " + players["second_name"]

    return players

if __name__ == "__main__":
    df = load_fpl_json()
    print(df.head())
