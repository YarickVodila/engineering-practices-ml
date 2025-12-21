from pathlib import Path

import hydra
import joblib
from omegaconf import DictConfig
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


def get_model(cfg: DictConfig):
    if cfg.model.name == "RandomForest":
        return RandomForestClassifier(**cfg.model.params)
    elif cfg.model.name == "LogisticRegression":
        return LogisticRegression(**cfg.model.params)
    else:
        raise ValueError(f"Unknown model: {cfg.model.name}")


@hydra.main(config_path="../../conf", config_name="config", version_base=None)
def main(cfg: DictConfig):
    X = pd.read_csv(cfg.data.processed_prefix + "_X.csv")
    y = pd.read_csv(cfg.data.processed_prefix + "_y.csv").squeeze()
    model = get_model(cfg)
    model.fit(X, y)

    Path(cfg.model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, cfg.model_path)
    print(f"Trained {cfg.model.name}, saved to {cfg.model_path}")


if __name__ == "__main__":
    main()
