import os
from datetime import datetime

# =========================
# GENERAL PIPELINE CONFIG
# =========================

PIPELINE_NAME: str = "industrial_defect_detection"
ARTIFACT_DIR: str = "artifacts"

TIMESTAMP: str = datetime.now().strftime("%Y%m%d_%H%M%S")

# =========================
# DATA INGESTION CONSTANTS
# =========================

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/uc?id=1Ire26eVZD3pUtOhgItiBgbBRFUEOXuhx"

DATA_INGESTION_LOCAL_DATA_FILE: str = "data.zip"

# =========================
# DATA VALIDATION CONSTANTS
# =========================

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"

# =========================
# DATA TRANSFORMATION CONSTANTS
# =========================

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
TRANSFORMED_TRAIN_DIR: str = "train"
TRANSFORMED_TEST_DIR: str = "test"

# Image size (important for DL)
IMAGE_SIZE: tuple = (224, 224)

# =========================
# MODEL TRAINER CONSTANTS
# =========================

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_MODEL_NAME: str = "model.pth"

# Training params (default values)
BATCH_SIZE: int = 32
EPOCHS: int = 10
LEARNING_RATE: float = 0.001

# =========================
# MODEL EVALUATION CONSTANTS
# =========================

MODEL_EVALUATION_DIR_NAME: str = "model_evaluation"
MODEL_EVALUATION_FILE_NAME: str = "evaluation.json"

# =========================
# MODEL PUSHER CONSTANTS
# =========================

MODEL_PUSHER_DIR_NAME: str = "model_pusher"
SAVED_MODEL_DIR: str = "saved_models"

# =========================
# INFERENCE CONSTANTS
# =========================

INFERENCE_BATCH_SIZE: int = 1

# =========================
# MONITORING CONSTANTS
# =========================

DRIFT_REPORT_FILE_NAME: str = "drift_report.json"
PERFORMANCE_REPORT_FILE_NAME: str = "performance_report.json"