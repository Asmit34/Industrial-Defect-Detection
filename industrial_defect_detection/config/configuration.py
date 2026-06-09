
import os

from industrial_defect_detection.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig,
    MonitoringConfig
)

from industrial_defect_detection.logger import get_logger

logger = get_logger(__name__)


class ConfigurationManager:
    def __init__(self):
        """
        Initialize base pipeline config
        """
        self.training_pipeline_config = TrainingPipelineConfig()

        # Create artifact root directory
        os.makedirs(self.training_pipeline_config.artifact_dir, exist_ok=True)

        logger.info(f"Artifact directory created at: {self.training_pipeline_config.artifact_dir}")


    # =========================
    # DATA INGESTION CONFIG
    # =========================

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = DataIngestionConfig(
            artifact_dir=self.training_pipeline_config.artifact_dir
        )

        os.makedirs(config.data_ingestion_dir, exist_ok=True)

        logger.info(f"Data Ingestion Config: {config}")

        return config


    # =========================
    # DATA VALIDATION CONFIG
    # =========================

    def get_data_validation_config(self) -> DataValidationConfig:

        config = DataValidationConfig(
            artifact_dir=self.training_pipeline_config.artifact_dir
        )

        os.makedirs(config.data_validation_dir, exist_ok=True)

        logger.info(f"Data Validation Config: {config}")

        return config


    # =========================
    # DATA TRANSFORMATION CONFIG
    # =========================

    def get_data_transformation_config(self) -> DataTransformationConfig:

        config = DataTransformationConfig(
            artifact_dir=self.training_pipeline_config.artifact_dir
        )

        os.makedirs(config.data_transformation_dir, exist_ok=True)

        logger.info(f"Data Transformation Config: {config}")

        return config


    # =========================
    # MODEL TRAINER CONFIG
    # =========================

    def get_model_trainer_config(self) -> ModelTrainerConfig:

        config = ModelTrainerConfig(
            artifact_dir=self.training_pipeline_config.artifact_dir
        )

        os.makedirs(config.model_trainer_dir, exist_ok=True)

        logger.info(f"Model Trainer Config: {config}")

        return config


    # =========================
    # MODEL EVALUATION CONFIG
    # =========================

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:

        config = ModelEvaluationConfig(
            artifact_dir=self.training_pipeline_config.artifact_dir
        )

        os.makedirs(config.model_evaluation_dir, exist_ok=True)

        logger.info(f"Model Evaluation Config: {config}")

        return config


    # =========================
    # MODEL PUSHER CONFIG
    # =========================

    def get_model_pusher_config(self) -> ModelPusherConfig:

        config = ModelPusherConfig(
            artifact_dir=self.training_pipeline_config.artifact_dir
        )

        os.makedirs(config.model_pusher_dir, exist_ok=True)

        logger.info(f"Model Pusher Config: {config}")

        return config


    # =========================
    # MONITORING CONFIG
    # =========================

    def get_monitoring_config(self) -> MonitoringConfig:

        config = MonitoringConfig(
            artifact_dir=self.training_pipeline_config.artifact_dir
        )

        logger.info(f"Monitoring Config: {config}")

        return config