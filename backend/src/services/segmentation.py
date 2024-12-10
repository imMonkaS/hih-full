import os
import random
import string

from config.settings import settings
from ultralytics import YOLO
from ultralytics.engine.results import Results

import json


class SegmentationService:
    """ Сервис для работы с моделью"""

    model = YOLO(os.path.join(settings.APP_DIR, 'static/models/car-segment-detector.pt'))

    def get_image_detection_classes(self, path_to_image: str):
        results: list[Results] = self.model(os.path.join(settings.APP_DIR, path_to_image))

        generate_jpg_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
        jpg_path = os.path.join(settings.APP_DIR, f'static/tmp_{generate_jpg_name}.jpg')
        results[0].save(jpg_path)

        res = {
            'classes': [el['name'] for el in json.loads(results[0].to_json())],
            'path_to_file': jpg_path
        }

        return res
