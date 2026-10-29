from pathlib import Path

import numpy as np
import pandas as pd


DATASET_PATH = Path(__file__).parent / "data" / "student_performance_5000.csv"


def generate_student_dataset(
    n_samples: int = 5_000,
    random_state: int = 42,
) -> pd.DataFrame:
    """Create a reproducible synthetic student-performance dataset."""
    rng = np.random.default_rng(random_state)
    study_hours = rng.uniform(0, 8, n_samples)
    attendance_pct = rng.uniform(50, 100, n_samples)
    assignment_score = rng.uniform(0, 100, n_samples)
    sleep_hours = rng.uniform(4, 10, n_samples)
    noise = rng.normal(0, 7, n_samples)

    exam_score = (
        5
        + 5.4 * study_hours
        + 0.2 * attendance_pct
        + 0.2 * assignment_score
        + 0.7 * sleep_hours
        + noise
    )
    exam_score = np.clip(exam_score, 0, 100).round(2)

    return pd.DataFrame(
        {
            "study_hours": study_hours.round(2),
            "attendance_pct": attendance_pct.round(2),
            "assignment_score": assignment_score.round(2),
            "sleep_hours": sleep_hours.round(2),
            "exam_score": exam_score,
            "passed": (exam_score >= 60).astype(int),
        }
    )


if __name__ == "__main__":
    dataset = generate_student_dataset()
    DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(DATASET_PATH, index=False)
    print(f"Saved {len(dataset):,} rows to {DATASET_PATH}")
