"""
Tests for `fig2pptx` module.
"""
import pytest
from fig2pptx.fig2pptx import *
import matplotlib.pyplot as plt



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
