import argparse
from pathlib import Path

import pandas as pd


def main(input_path: str, output_path: str):
    df = pd.read_csv(input_path)
    X = df.drop(columns=["target"])
    y = df["target"]

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    X.to_csv(f"{output_path}_X.csv", index=False)
    y.to_csv(f"{output_path}_y.csv", index=False)
    print(f"Features saved to {output_path}_*.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.input, args.output)
