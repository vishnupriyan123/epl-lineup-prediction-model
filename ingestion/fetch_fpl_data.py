import requests
import json
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

def fetch_fpl_data(save_to=DATA_DIR / "fpl_bootstrap.json"):
    """Fetch Fantasy Premier League data and save it locally."""
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    print("📡 Fetching FPL player data...")

    response = requests.get(url)
    if response.ok:
        with open(save_to, "w") as f:
            json.dump(response.json(), f, indent=2)
        print(f"✅ Data saved to {save_to}")
    else:
        print(f"❌ Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    fetch_fpl_data()
