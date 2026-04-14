import os
import sys
import zipfile
import gdown

from industrial_defect_detection.logger import get_logger
from industrial_defect_detection.exception import CustomException
from industrial_defect_detection.entity.config_entity import DataIngestionConfig
from industrial_defect_detection.entity.artifact_entity import DataIngestionArtifact

logger = get_logger(__name__)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        try:
            self.config = config
        except Exception as e:
            raise CustomException(e, sys)

    # =========================
    # DOWNLOAD DATA
    # =========================
    def download_data(self) -> str:
        try:
            dataset_url = self.config.data_download_url
            zip_file_path = self.config.local_data_file_path

            os.makedirs(self.config.data_ingestion_dir, exist_ok=True)

            logger.info(f"Downloading data from {dataset_url}")

            # Extract file_id
            file_id = dataset_url.split("/")[-2]
            download_url = f"https://drive.google.com/uc?id={file_id}"

            gdown.download(download_url, zip_file_path, quiet=False)

            logger.info(f"Downloaded file at {zip_file_path}")

            return zip_file_path

        except Exception as e:
            raise CustomException(e, sys)

    # =========================
    # EXTRACT ZIP FILE
    # =========================
    def extract_zip_file(self, zip_file_path: str) -> str:
        try:
            feature_store_path = self.config.feature_store_path
            os.makedirs(feature_store_path, exist_ok=True)

            logger.info(f"Extracting {zip_file_path} to {feature_store_path}")

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(feature_store_path)

            return feature_store_path

        except Exception as e:
            raise CustomException(e, sys)

    # =========================
    # VALIDATE STRUCTURE
    # =========================
    def validate_structure(self, base_path: str):
        try:
            required_dirs = ["train", "test", "valid"]

            for split in required_dirs:
                split_path = os.path.join(base_path, split)

                if not os.path.exists(split_path):
                    raise Exception(f"{split} folder missing")

                images_path = os.path.join(split_path, "images")
                labels_path = os.path.join(split_path, "labels")

                if not os.path.exists(images_path):
                    raise Exception(f"{split}/images missing")

                if not os.path.exists(labels_path):
                    raise Exception(f"{split}/labels missing")

            logger.info("Dataset structure validated successfully")

        except Exception as e:
            raise CustomException(e, sys)

    # =========================
    # MAIN FUNCTION
    # =========================
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logger.info("Starting data ingestion")

            zip_file_path = self.download_data()
            feature_store_path = self.extract_zip_file(zip_file_path)

            # If zip extracts nested folder, handle it
            extracted_folders = os.listdir(feature_store_path)
            if len(extracted_folders) == 1:
                base_path = os.path.join(feature_store_path, extracted_folders[0])
            else:
                base_path = feature_store_path

            self.validate_structure(base_path)

            train_path = os.path.join(base_path, "train")
            test_path = os.path.join(base_path, "test")

            artifact = DataIngestionArtifact(
                feature_store_path=base_path,
                train_data_path=train_path,
                test_data_path=test_path
            )

            logger.info(f"Data Ingestion Artifact: {artifact}")

            return artifact

        except Exception as e:
            raise CustomException(e, sys)