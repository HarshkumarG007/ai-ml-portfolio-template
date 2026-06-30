import argparse
import logging
from pathlib import Path
import joblib

# Optional: Import your ML libraries here
# import pandas as pd
# import torch
# from sklearn.ensemble import RandomForestClassifier

# 1. Configure Production-Standard Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main(data_dir, model_dir):
    """Trains the machine learning model and saves the artifact."""
    logging.info("Starting the training pipeline...")

    # 2. Resolve Absolute Paths (Makes the script crash-proof)
    # This automatically finds the root 'ai-ml-portfolio-template' folder
    project_root = Path(__file__).resolve().parents[1]
    
    input_path = project_root / data_dir / "train_features.csv"
    output_path = project_root / model_dir / "model.pkl"

    # Failsafe: Check if data actually exists before starting
    if not input_path.exists():
        logging.error(f"Data not found at {input_path}. Did you run 'make preprocess'?")
        return

    # --- STEP A: LOAD DATA ---
    logging.info(f"Loading processed data from {input_path}")
    # df = pd.read_csv(input_path)
    # X = df.drop(columns=['target'])
    # y = df['target']

    # --- STEP B: INITIALIZE MODEL ---
    logging.info("Initializing model...")
    # Tip: If writing PyTorch or XGBoost scripts, this is where you map to your local hardware
    # device = "cuda" if torch.cuda.is_available() else "cpu" # Hooks into your RTX GPU
    # model = MyNeuralNet().to(device)
    
    # model = RandomForestClassifier(n_estimators=100, random_state=42)

    # --- STEP C: TRAIN ---
    logging.info("Training in progress... This may take a moment.")
    # model.fit(X, y)

    # --- STEP D: SAVE ARTIFACT ---
    # Ensure the models/ directory actually exists before trying to save
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    logging.info(f"Saving trained model artifact to {output_path}")
    # joblib.dump(model, output_path)
    
    logging.info("Training pipeline completed successfully. 🚀")

if __name__ == "__main__":
    # 3. Command Line Arguments
    parser = argparse.ArgumentParser(description="Train the ML model.")
    parser.add_argument(
        "--data", 
        type=str, 
        default="data/processed", 
        help="Path to the processed data directory."
    )
    parser.add_argument(
        "--model", 
        type=str, 
        default="models", 
        help="Path to save the trained model artifact."
    )
    
    args = parser.parse_args()
    main(args.data, args.model)