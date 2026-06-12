from dataclasses import dataclass
from typing import Optional


# =========================
# DATA INGESTION ARTIFACT
# =========================

@dataclass
class DataIngestionArtifact:
    feature_store_path: str
    train_data_path: str
    test_data_path: str


# =========================
# DATA VALIDATION ARTIFACT
# =========================

@dataclass
class DataValidationArtifact:
    validation_status: bool
    # validated_data_path: str
    message: Optional[str] = None


# =========================
# DATA TRANSFORMATION ARTIFACT
# =========================

@dataclass
class DataTransformationArtifact:
    dataset_yaml_path: str
    transformed_data_path: str


# =========================
# MODEL TRAINER ARTIFACT
# =========================

@dataclass
class ModelTrainerArtifact:
    trained_model_path: str
    train_metrics: Optional[dict] = None


# =========================
# MODEL EVALUATION ARTIFACT
# =========================

@dataclass
class ModelEvaluationArtifact:
    evaluation_file_path: str
    evaluation_metrics: Optional[dict] = None


# =========================
# MODEL PUSHER ARTIFACT
# =========================

@dataclass
class ModelPusherArtifact:
    saved_model_path: str

@dataclass
class ViolationArtifact:
    violation_count: int
    violation_type: str