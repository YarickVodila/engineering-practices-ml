import argparse

import joblib
import pandas as pd


def main(model_path: str, X_path: str, output_path: str):
    model = joblib.load(model_path)
    X = pd.read_csv(X_path)
    preds = model.predict(X)
    pd.DataFrame({"prediction": preds}).to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--X", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    main(args.model, args.X, args.output)
