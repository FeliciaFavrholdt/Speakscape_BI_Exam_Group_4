import json
from datetime import datetime
from pathlib import Path

def save_notebook_and_summary(notebook_name: str, summary: dict, reports_dir: str = "../reports"):
    """
    Save a JSON summary and optionally trigger a frontend save of the current notebook.
    """
    try:
        import IPython
        from IPython.display import display, Javascript
        display(Javascript('IPython.notebook.save_checkpoint();'))
        print("Notebook save triggered.")
    except Exception:
        print("Notebook save skipped (not supported in this interface).")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    summary["notebook"] = f"{notebook_name}.ipynb"
    summary["timestamp"] = timestamp

    Path(reports_dir).mkdir(parents=True, exist_ok=True)
    summary_path = Path(reports_dir) / f"{notebook_name}_summary_{timestamp}.json"

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    print(f"Summary saved to: {summary_path}")
