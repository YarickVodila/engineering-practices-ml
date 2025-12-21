import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from classification_module.modeling.train import main as train_main

# Hydra запускается через main(), но мы вызываем напрямую с argv
if __name__ == "__main__":
    train_main()
