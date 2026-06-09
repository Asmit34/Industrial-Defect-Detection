
import os
from dataclasses import dataclass
import industrial_defect_detection.constants.training_pipeline.constant as tp


# =========================
# TRAINING PIPELINE CONFIG
# =========================

@dataclass
class TrainingPipelineConfig:
    artifact_dir: str = os.path.join(
        tp.ARTIFACT_DIR,
        tp.PIPELINE_NAME,
        tp.TIMESTAMP
    )


# =========================
# DATA INGESTION CONFIG
# =========================

@dataclass
class DataIngestionConfig:
    artifact_dir: str

    def __post_init__(self):
        self.data_ingestion_dir = os.path.join(
            self.artifact_dir, tp.DATA_INGESTION_DIR_NAME
        )

        self.feature_store_path = os.path.join(
            self.data_ingestion_dir, tp.DATA_INGESTION_FEATURE_STORE_DIR
        )

        self.ingested_train_path = os.path.join(
            self.data_ingestion_dir, tp.DATA_INGESTION_INGESTED_DIR, "train"
        )

        self.ingested_test_path = os.path.join(
            self.data_ingestion_dir, tp.DATA_INGESTION_INGESTED_DIR, "test"
        )

        self.data_download_url = tp.DATA_DOWNLOAD_URL

        self.local_data_file_path = os.path.join(
            self.data_ingestion_dir, tp.DATA_INGESTION_LOCAL_DATA_FILE
        )


# =========================
# DATA VALIDATION CONFIG
# =========================

@dataclass
class DataValidationConfig:
    artifact_dir: str

    def __post_init__(self):
        self.data_validation_dir = os.path.join(
            self.artifact_dir, tp.DATA_VALIDATION_DIR_NAME
        )

        self.validation_status_file_path = os.path.join(
            self.data_validation_dir, tp.DATA_VALIDATION_STATUS_FILE
        )


# =========================
# DATA TRANSFORMATION CONFIG
# =========================

@dataclass
class DataTransformationConfig:
    artifact_dir: str

    def __post_init__(self):
        self.data_transformation_dir = os.path.join(
            self.artifact_dir, tp.DATA_TRANSFORMATION_DIR_NAME
        )

        self.transformed_train_dir = os.path.join(
            self.data_transformation_dir, tp.TRANSFORMED_TRAIN_DIR
        )

        self.transformed_test_dir = os.path.join(
            self.data_transformation_dir, tp.TRANSFORMED_TEST_DIR
        )

        self.image_size = tp.IMAGE_SIZE


# =========================
# MODEL TRAINER CONFIG
# =========================

@dataclass
class ModelTrainerConfig:
    artifact_dir: str

    def __post_init__(self):
        self.model_trainer_dir = os.path.join(
            self.artifact_dir, tp.MODEL_TRAINER_DIR_NAME
        )

        self.trained_model_path = os.path.join(
            self.model_trainer_dir,
            tp.MODEL_TRAINER_TRAINED_MODEL_DIR,
            tp.MODEL_TRAINER_MODEL_NAME
        )

        self.batch_size = tp.BATCH_SIZE
        self.epochs = tp.EPOCHS
        self.learning_rate = tp.LEARNING_RATE


# =========================
# MODEL EVALUATION CONFIG
# =========================

@dataclass
class ModelEvaluationConfig:
    artifact_dir: str

    def __post_init__(self):
        self.model_evaluation_dir = os.path.join(
            self.artifact_dir, tp.MODEL_EVALUATION_DIR_NAME
        )

        self.evaluation_file_path = os.path.join(
            self.model_evaluation_dir,
            tp.MODEL_EVALUATION_FILE_NAME
        )


# =========================
# MODEL PUSHER CONFIG
# =========================

@dataclass
class ModelPusherConfig:
    artifact_dir: str

    def __post_init__(self):
        self.model_pusher_dir = os.path.join(
            self.artifact_dir, tp.MODEL_PUSHER_DIR_NAME
        )

        self.saved_model_dir = os.path.join(
            tp.SAVED_MODEL_DIR
        )


# =========================
# INFERENCE CONFIG
# =========================

@dataclass
class InferenceConfig:
    model_path: str
    batch_size: int = tp.INFERENCE_BATCH_SIZE


# =========================
# MONITORING CONFIG
# =========================

@dataclass
class MonitoringConfig:
    artifact_dir: str

    def __post_init__(self):
        self.drift_report_path = os.path.join(
            self.artifact_dir,
            tp.DRIFT_REPORT_FILE_NAME
        )

        self.performance_report_path = os.path.join(
            self.artifact_dir,
            tp.PERFORMANCE_REPORT_FILE_NAME
        )