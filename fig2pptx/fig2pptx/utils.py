

def bbox_to_pptx(bottom, left, width, height):
    """ Convert matplotlib bounding box format to pptx format
    Parameters
    ----------
    bottom : float
    left : float
    width : float
    height : float

    Returns
    -------
    top, left, width, height


    """

    return bottom+height, left, width, height


def pptx_to_bbox(top, left, width, height):
    """ Convert matplotlib bounding box format to pptx format
    Parameters
    ----------
    top : float
    left : float
    width : float
    height : float

    Returns
    -------
    bottom, left, width, height


    """

    return top-height, left, width, height
