import unittest
from hamlpy import nodes

class TestElementNode(unittest.TestCase):
    
    def testCalculatesIndentationProperly(self):
        noIndentation = nodes.ElementNode('%div')
        self.assertEqual(0, noIndentation.indentation)
        
        threeIndentation = nodes.ElementNode('   %div')
        self.assertEqual(3, threeIndentation.indentation)
        
        sixIndentation = nodes.ElementNode('      %div')
        self.assertEqual(6, sixIndentation.indentation)
        
    def testLinesAreAlwaysStrippedOfWhiteSpace(self):
        someSpace = nodes.ElementNode('   %div')
        self.assertEqual('%div', someSpace.haml)
        
        lotsOfSpace = nodes.ElementNode('      %div    ')
        self.assertEqual('%div', lotsOfSpace.haml)
        
    def testInsertsNodesIntoProperTreeDepth(self):
        noIndentationNode = nodes.ElementNode('%div')
        oneIndentationNode = nodes.ElementNode(' %div')
        twoIndentationNode = nodes.ElementNode('  %div')
        anotherOneIndentation = nodes.ElementNode(' %div')
        
        noIndentationNode.addNode(oneIndentationNode)
        noIndentationNode.addNode(twoIndentationNode)
        noIndentationNode.addNode(anotherOneIndentation)
        
        self.assertEqual(oneIndentationNode, noIndentationNode.internalNodes[0])
        self.assertEqual(twoIndentationNode, noIndentationNode.internalNodes[0].internalNodes[0])
        self.assertEqual(anotherOneIndentation, noIndentationNode.internalNodes[1])

    def test_adds_multiple_nodes_to_one(self):
        startNode = nodes.ElementNode('%div')
        oneNode = nodes.ElementNode('  %div')
        twoNode = nodes.ElementNode('  %div')
        threeNode = nodes.ElementNode('  %div')
        
        startNode.addNode(oneNode)
        startNode.addNode(twoNode)
        startNode.addNode(threeNode)
        
        self.assertEqual(3, len(startNode.internalNodes))