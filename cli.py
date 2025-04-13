import sys
import os

# Adding the root directory to sys.path to make sure Python can find the core and utils modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
from core.optimizer import optimize_model
from utils.logger import log_info, log_error, log_success

VERSION = "0.1.0"

def main():
    parser = argparse.ArgumentParser(
        description="LIMOS: Low Impact Model Optimization System"
    )

    parser.add_argument(
        "--model", type=str, required=True,
        help="Path to the input model file"
    )
    parser.add_argument(
        "--format", type=str, required=True,
        choices=["torch", "onnx", "tflite"],
        help="Format of the input model"
    )
    parser.add_argument(
        "--output", type=str, default="outputs/",
        help="Directory to save the optimized model"
    )
    parser.add_argument(
        "--version", action="version", version=f"LIMOS v{VERSION}"
    )

    args = parser.parse_args()

    model_path = args.model
    model_format = args.format
    output_path = args.output

    log_info("Starting LIMOS Optimization Pipeline...")

    if not os.path.exists(model_path):
        log_error("Model path does not exist.")
        sys.exit(1)

    optimize_model(model_path, model_format, output_path)
    log_success("Optimization completed successfully.")

if __name__ == "__main__":
    main()
