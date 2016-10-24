import unittest
from node import Node

class TestNodeClass(unittest.TestCase):

    def testConstructor(self):
        testNode = Node(1)
        self.assertEqual(testNode.getHead(), 1)
        self.assertEqual(testNode.getTail(), None)
    
    def testConcatenation(self):
        testNode = Node(1)
        testNode.setTail(2)
        self.assertIsInstance(testNode.getTail(), Node)
        self.assertEqual(testNode.getTail().getHead(), 2)

    def testHeadDefine(self):
        testNode = Node(1)
        self.assertEqual(testNode.getHead(), 1)
        testNode.setHead(2)
        self.assertEqual(testNode.getHead(), 2)

    def testDeleters(self):
        testNode = Node(1)
        testNode.setTail(2)
        print(testNode.toString())
        testNode.amputateTail()
        self.assertIsNone(testNode.getTail())
        testNode.decapitate()
        self.assertIsNone(testNode.getHead())

if __name__ == '__main__':
    unittest.main()