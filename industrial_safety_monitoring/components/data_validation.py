import os
import sys

from industrial_safety_monitoring.logger import get_logger
from industrial_safety_monitoring.exception import CustomException

from industrial_safety_monitoring.entity.config_entity import (
    DataValidationConfig
)

from industrial_safety_monitoring.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact
)

from industrial_safety_monitoring.utils.image_utils import (
    verify_image,
    verify_yolo_label
)

from industrial_safety_monitoring.constants.training_pipeline.constant import (
    NUM_CLASSES
)

logger = get_logger(__name__)


class DataValidation:

    def __init__(
        self,
        data_ingestion_artifact: DataIngestionArtifact,
        data_validation_config: DataValidationConfig
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise CustomException(e, sys)

    # =====================================
    # DATASET STRUCTURE
    # =====================================

    def validate_dataset_structure(self) -> bool:

        dataset_path = (
            self.data_ingestion_artifact.feature_store_path
        )

        required_splits = ["train", "test", "valid"]

        for split in required_splits:

            split_path = os.path.join(
                dataset_path,
                split
            )

            if not os.path.exists(split_path):
                raise Exception(
                    f"{split} folder not found"
                )

            image_dir = os.path.join(
                split_path,
                "images"
            )

            label_dir = os.path.join(
                split_path,
                "labels"
            )

            if not os.path.exists(image_dir):
                raise Exception(
                    f"{split}/images folder missing"
                )

            if not os.path.exists(label_dir):
                raise Exception(
                    f"{split}/labels folder missing"
                )

        logger.info(
            "Dataset structure validation passed"
        )

        return True

    # =====================================
    # IMAGE-LABEL MATCHING
    # =====================================

    def validate_image_label_count(self) -> bool:

        dataset_path = (
            self.data_ingestion_artifact.feature_store_path
        )

        splits = ["train", "test", "valid"]

        for split in splits:

            image_dir = os.path.join(
                dataset_path,
                split,
                "images"
            )

            label_dir = os.path.join(
                dataset_path,
                split,
                "labels"
            )

            image_files = {
                os.path.splitext(file)[0]
                for file in os.listdir(image_dir)
            }

            label_files = {
                os.path.splitext(file)[0]
                for file in os.listdir(label_dir)
            }

            missing_labels = image_files - label_files
            missing_images = label_files - image_files

            if missing_labels:
                raise Exception(
                    f"{split}: Missing labels for "
                    f"{len(missing_labels)} images"
                )

            if missing_images:
                raise Exception(
                    f"{split}: Missing images for "
                    f"{len(missing_images)} labels"
                )

        logger.info(
            "Image-label count validation passed"
        )

        return True

    # =====================================
    # CORRUPTED IMAGES
    # =====================================

    def validate_images(self) -> bool:

        dataset_path = (
            self.data_ingestion_artifact.feature_store_path
        )

        splits = ["train", "test", "valid"]

        for split in splits:

            image_dir = os.path.join(
                dataset_path,
                split,
                "images"
            )

            for image_file in os.listdir(image_dir):

                image_path = os.path.join(
                    image_dir,
                    image_file
                )

                if not verify_image(image_path):

                    raise Exception(
                        f"Corrupted image found: "
                        f"{image_path}"
                    )

        logger.info(
            "Image validation passed"
        )

        return True

    # =====================================
    # YOLO LABEL VALIDATION
    # =====================================

    def validate_labels(self) -> bool:

        dataset_path = (
            self.data_ingestion_artifact.feature_store_path
        )

        splits = ["train", "test", "valid"]

        for split in splits:

            label_dir = os.path.join(
                dataset_path,
                split,
                "labels"
            )

            for label_file in os.listdir(label_dir):

                label_path = os.path.join(
                    label_dir,
                    label_file
                )

                if not verify_yolo_label(
                    label_path,
                    NUM_CLASSES
                ):

                    raise Exception(
                        f"Invalid label file: "
                        f"{label_path}"
                    )

        logger.info(
            "YOLO label validation passed"
        )

        return True

    # =====================================
    # EMPTY FOLDER VALIDATION
    # =====================================

    def validate_non_empty_dataset(self) -> bool:

        dataset_path = (
            self.data_ingestion_artifact.feature_store_path
        )

        splits = ["train", "test", "valid"]

        for split in splits:

            image_dir = os.path.join(
                dataset_path,
                split,
                "images"
            )

            total_images = len(
                os.listdir(image_dir)
            )

            if total_images == 0:
                raise Exception(
                    f"{split} folder contains no images"
                )

        logger.info(
            "Dataset is not empty"
        )

        return True

    # =====================================
    # MAIN VALIDATION
    # =====================================

    def initiate_data_validation(
        self
    ) -> DataValidationArtifact:

        try:

            logger.info(
                "Starting Data Validation"
            )

            os.makedirs(
                self.data_validation_config.data_validation_dir,
                exist_ok=True
            )

            status = (
                self.validate_dataset_structure()
                and self.validate_non_empty_dataset()
                and self.validate_image_label_count()
                and self.validate_images()
                and self.validate_labels()
            )

            with open(
                self.data_validation_config.validation_status_file_path,
                "w"
            ) as file:

                file.write(
                    f"validation_status={status}"
                )

            artifact = DataValidationArtifact(
                validation_status=status,
                message="Validation Successful"
            )

            logger.info(
                f"Validation completed successfully"
            )

            return artifact

        except Exception as e:

            logger.error(
                f"Validation failed : {str(e)}"
            )

            raise CustomException(e, sys)