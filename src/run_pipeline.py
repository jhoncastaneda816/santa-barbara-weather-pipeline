import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run_script(script_name: str) -> None:
    script_path = PROJECT_ROOT / "src" / script_name

    print(f"Running {script_name}...")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        check=True,
    )

    print(f"Finished {script_name}.")


def main() -> None:
    run_script("extract.py")
    run_script("transform.py")
    run_script("load.py")
    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()