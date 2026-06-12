import cv2
import os
import sys

from industrial_safety_monitoring.exception import CustomException
from industrial_safety_monitoring.logger import get_logger

logger = get_logger(__name__)


def verify_image(image_path: str) -> bool:
    """
    Verify image is readable
    """

    try:
        image = cv2.imread(image_path)

        if image is None:
            logger.warning(f"Corrupted image: {image_path}")
            return False

        return True

    except Exception as e:
        raise CustomException(e, sys)


def count_images(directory: str) -> int:
    """
    Count valid images
    """

    try:
        count = 0

        for file in os.listdir(directory):

            if file.lower().endswith(
                (".jpg", ".jpeg", ".png", ".bmp", ".webp")
            ):
                count += 1

        logger.info(f"Total images in {directory}: {count}")

        return count

    except Exception as e:
        raise CustomException(e, sys)


def verify_yolo_label(label_path: str, num_classes: int):
    """
    Verify YOLO annotation format
    """

    try:

        with open(label_path, "r") as file:
            lines = file.readlines()

        for line in lines:

            values = line.strip().split()

            if len(values) != 5:
                return False

            class_id = int(values[0])

            if class_id >= num_classes:
                return False

            coordinates = list(map(float, values[1:]))

            for coord in coordinates:
                if coord < 0 or coord > 1:
                    return False

        return True

    except Exception:
        return False