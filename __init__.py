from .nodes import FaceCompareNode

NODE_CLASS_MAPPINGS = { "faceCompare": FaceCompareNode }

NODE_DISPLAY_NAME_MAPPINGS = { "faceCompare": "face compare node" }

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']