import pytest
from fig2pptx import utils

class TestConvertBoxes(object):

    def test_bbox_to_pptx(self):

        # bottom, left, width, height
        res = utils.bbox_to_pptx(5, 2, 4, 3)
        assert res == (8, 2, 4, 3)


    def test_pptx_to_bbox(self):

        # top, left, width, height
        res = utils.pptx_to_bbox(5, 2, 4, 3)
        assert res == (2, 2, 4, 3)
