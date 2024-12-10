from typing import Annotated

from fastapi import Depends

from services.segmentation import SegmentationService


SegmentationServiceDependency = Annotated[SegmentationService, Depends(SegmentationService)]
