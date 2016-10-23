import unittest
from node import Node

class TestNodeClass(unittest.TestCase):

    def testConstructor(self):
        testNode = Node(10)
        self.assertEqual(testNode.getHead(), 10)
        self.assertEqual(testNode.getTail(), None)
    
    def testConcatenation(self):
        testNode = Node(10)
        testNode.setTail(20)
        self.assertIsInstance(testNode.getTail(), Node)
        self.assertEqual(testNode.getTail().getHead(), 20)

    def testHeadDefine(self):
        testNode = Node(10)
        self.assertEqual(testNode.getHead(), 10)
        testNode.setHead(20)
        self.assertEqual(testNode.getHead(), 20)

    def testDeleters(self):
        testNode = Node(10)
        testNode.setTail(20)
        print(testNode.toString())
        testNode.amputateTail()
        self.assertIsNone(testNode.getTail())
        testNode.decapitate()
        self.assertIsNone(testNode.getHead())

if __name__ == '__main__':
    unittest.main()