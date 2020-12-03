import cv2

from common import HostNode, PreviewNode
from PyFlow.Core.Common import *
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper


class FramePreviewNode(HostNode, PreviewNode):
    def __init__(self, name):
        super(FramePreviewNode, self).__init__(name)
        self.frame = self.createInputPin('frame', 'FramePin')
        self.frame.enableOptions(PinOptions.AllowMultipleConnections)

    @staticmethod
    def pinTypeHints():
        helper = NodePinsSuggestionsHelper()
        helper.addInputDataType('FramePin')
        helper.addInputStruct(StructureType.Multi)
        helper.addInputDataType('StringPin')
        helper.addInputStruct(StructureType.Single)
        return helper

    @staticmethod
    def category():
        return 'Display'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Description in rst format."

    def run(self, *args, **kwargs):
        print("Preview waiting...")
        self.display_frame = self.receive("frame")
        print("Preview updated.")
