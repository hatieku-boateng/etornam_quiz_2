import argparse
import json
import os
from pathlib import Path

import requests


PREDICT_URL = "https://predict-6adf8484f2520ee816ead250-dproatj77a-uk.a.run.app/predict"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Send an image to the deployed Ultralytics image detection model."
    )
    parser.add_argument("image", type=Path, help="Path to an image file")
    arguments = parser.parse_args()

    api_key = os.environ.get("ULTRALYTICS_API_KEY")
    if not api_key:
        parser.error("Set the ULTRALYTICS_API_KEY environment variable first.")
    if not arguments.image.is_file():
        parser.error(f"Image file not found: {arguments.image}")

    try:
        with arguments.image.open("rb") as image_file:
            response = requests.post(
                PREDICT_URL,
                headers={"Authorization": f"Bearer {api_key}"},
                files={"file": (arguments.image.name, image_file)},
                timeout=120,
            )
        response.raise_for_status()
    except requests.RequestException as error:
        details = error.response.text if error.response is not None else str(error)
        raise SystemExit(f"Inference request failed: {details}") from error

    try:
        print(json.dumps(response.json(), indent=2))
    except requests.JSONDecodeError as error:
        raise SystemExit("The inference endpoint returned a non-JSON response.") from error


if __name__ == "__main__":
    main()
