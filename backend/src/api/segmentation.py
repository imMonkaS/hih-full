import json
import os
import random
import shutil
import string

from config.settings import settings
from fastapi import APIRouter, UploadFile, File
from starlette.responses import FileResponse

from dependencies.segmentation import SegmentationServiceDependency

SEGMENTATION_ROUTER = APIRouter(prefix='/segmentation')


@SEGMENTATION_ROUTER.post('/')
def segment_model(car_image: UploadFile, segment_service: SegmentationServiceDependency):
    uploaded_file_name = 'static/uploaded/' + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8)) + '.jpg'
    with open(os.path.join(settings.APP_DIR, uploaded_file_name), "wb") as buffer:
        shutil.copyfileobj(car_image.file, buffer)

        res = segment_service.get_image_detection_classes(uploaded_file_name)

    return FileResponse(res['path_to_file'], headers={'classes': json.dumps(res['classes'])})