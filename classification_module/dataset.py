import argparse
from pathlib import Path

from sklearn.datasets import load_iris


def main(output_path: str):
    data = load_iris(as_frame=True)
    df = data.frame
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.output)
