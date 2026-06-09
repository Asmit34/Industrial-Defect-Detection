import sys
from industrial_defect_detection.exception import CustomException 
from industrial_defect_detection.logger import get_logger
from industrial_defect_detection.config.configuration import ConfigurationManager
from industrial_defect_detection.components.data_ingestion import DataIngestion
from industrial_defect_detection.entity.artifact_entity import (
    DataIngestionArtifact
)

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
        
    def run_pipeline(self):
        try:
            logger.info("Starting Training Pipeline")
            ingestion_artifact = (
                self.start_data_ingestion()
            )

            logger.info("Training pipeline completed successfully")

            return ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)