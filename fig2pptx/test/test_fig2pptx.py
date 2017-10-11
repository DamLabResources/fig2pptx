"""
Tests for `fig2pptx` module.
"""
import pytest
from fig2pptx.fig2pptx import *
import matplotlib.pyplot as plt
import numpy as np



class TestPowerPointBox(object):

    def make_basic(self):

        fig, ax = plt.subplots(1, 1)
        ax.plot(range(10))
        ax.set_xticks(range(0, 10, 2))
        ax.set_yticks(range(1, 10, 4))

        return fig, ax


    def test_init(self):

        fig, ax = self.make_basic()

        tree = PowerPointBox(fig)

    def test_uses_axes_subplot(self):

        fig, ax = self.make_basic()

        tree = PowerPointBox(fig)

        found = False
        for child in tree.children:
            if isinstance(child, SubplotAxisBox):
                found = True
                assert child.mpl_object == ax

        assert found


class TestPlaceTextbox(object):


    def test_figure_placement(self):

        fig, ax = plt.subplots(1, 1, figsize = (3,4))
        ax.plot(range(10))
        ax.set_xticks([])
        ax.set_yticks([])

        with NamedTemporaryFile(suffix='.png') as handle:
            fig.savefig(handle.name)

        left_top = (pptx.util.Inches(1), pptx.util.Inches(2))
        prs, slide = utils.make_blank_slide()
        tree = PowerPointBox(fig, pptx_corners=utils.determine_corners(fig, left_top))
        tree.render(slide)

        found = False
        corners = None
        for shape in slide.shapes:
            if isinstance(shape, pptx.shapes.picture.Picture):
                found = True
                corners = utils.get_corners(shape)
                break

        assert found, 'Could not find image!'

        c1 = (pptx.util.Inches(1), pptx.util.Inches(2))
        c2 = (pptx.util.Inches(1), pptx.util.Inches(2+4))
        c3 = (pptx.util.Inches(1+3), pptx.util.Inches(2))
        c4 = (pptx.util.Inches(1+3), pptx.util.Inches(2+4))
        cor_corners = np.array([c1, c2, c3, c4])

        np.testing.assert_array_equal(corners, cor_corners)

    def test_textbox_placement(self):
        fig, ax = plt.subplots(1, 1, figsize = (3,4))
        ax.plot(range(10))
        fig.text(0.1, 0.1, 'some text', ha='left', va='bottom')

        with NamedTemporaryFile(suffix='.png') as handle:
            fig.savefig(handle.name)

        left_top = (pptx.util.Inches(1), pptx.util.Inches(2))

        prs, slide = utils.make_blank_slide()
        tree = PowerPointBox(fig, pptx_corners=utils.determine_corners(fig, left_top))
        tree.render(slide)
        prs.save('new_text.pptx')

        tbox = utils.find_textbox(slide, text='some text')
        tbox_corners = utils.get_corners(tbox)

        bot_left = (tbox_corners[:, 0].min(), tbox_corners[:, 1].max())
        cor_bot_left = (1188720, 4983480) # determined by inspection

        assert bot_left == cor_bot_left







class TestDetection(object):

    def make_basic(self):

        fig, ax = plt.subplots(1, 1)
        ax.plot(range(10))
        ax.set_ylabel('Y-Label')
        ax.set_xticks(range(0, 10, 2))
        ax.set_yticks(range(1, 10, 4))

        return fig, ax

    def test_detect_axes_subplot(self):

        fig, ax = self.make_basic()

        assert SubplotAxisBox.detect_type(ax)

    def test_detect_text_box(self):

        fig, ax = self.make_basic()
        tbox = ax.yaxis.get_label()

        assert TextBox.detect_type(tbox)
