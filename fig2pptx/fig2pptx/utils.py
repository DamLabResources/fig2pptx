

def bbox_to_pptx(left, bottom, width, height):
    """ Convert matplotlib bounding box format to pptx format
    Parameters
    ----------
    bottom : float
    left : float
    width : float
    height : float

    Returns
    -------
    left, top, width, height


    """

    return left, bottom-height, width, height


def pptx_to_bbox(left, top, width, height):
    """ Convert matplotlib bounding box format to pptx format
    Parameters
    ----------
    left : float
    top : float
    width : float
    height : float

    Returns
    -------
    bottom, left, width, height


    """

    return top-height, left, width, height


def corners_to_pptx(corners):

    top = corners[:,1].max()
    right = corners[:,0].max()
    left = corners[:,0].min()
    bottom = corners[:,1].min()

    height = top-bottom
    width = right-left

    return left, top, width, height