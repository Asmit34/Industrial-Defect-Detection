import sys
from industrial_safety_monitoring.exception import CustomException 
from industrial_safety_monitoring.logger import get_logger
from industrial_safety_monitoring.config.configuration import ConfigurationManager
from industrial_safety_monitoring.components.data_ingestion import DataIngestion
from industrial_safety_monitoring.entity.artifact_entity import (
    DataIngestionArtifact
)
from industrial_safety_monitoring.components.data_validation import DataValidation

logger = get_logger(__name__)
class TrainPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info("=" * 50)
            logger.info("Starting Data Ingestion")
            logger.info("=" * 50)

            ingestion_config = (
                self.config.get_data_ingestion_config()
            )

            data_ingestion = DataIngestion(
                config=ingestion_config
                )
            artifact = (
                data_ingestion.initiate_data_ingestion()
            )
            logger.info(
                f"Data Ingestion completed and artifact: {artifact}"
            )
            return artifact
        except Exception as e:
            raise CustomException(e, sys)
    def start_data_validation(
        self,
        data_ingestion_artifact
    ):

        try:

            logger.info(
                "=" * 50
            )
            logger.info(
                "Starting Data Validation"
            )
            logger.info(
                "=" * 50
            )

            validation_config = (
                self.config.get_data_validation_config()
            )

            validation = DataValidation(
                data_ingestion_artifact=
                data_ingestion_artifact,

                data_validation_config=
                validation_config
            )

            artifact = (
                validation.initiate_data_validation()
            )

            logger.info(
                f"Validation Artifact : {artifact}"
            )

            return artifact

        except Exception as e:
            raise CustomException(e, sys)
        
    def run_pipeline(self):
        try:
            logger.info("Starting Training Pipeline")
            ingestion_artifact = (
                self.start_data_ingestion()
            )

            validation_artifact = (
                self.start_data_validation(
                    ingestion_artifact
                )
            )

            if not validation_artifact.validation_status:
                raise Exception(
                    "Data Validation Failed"
                )

            logger.info("Training pipeline completed successfully")

            return ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)