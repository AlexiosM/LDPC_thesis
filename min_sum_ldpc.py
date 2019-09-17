class Node:

	def __init__(self, neighboors):
		self.neighboors = neighboors


	def printNeighboors(self):
		print self.neighboors



#a = [2,3,4,5,6,7] 
#n = Node(a)
#n.printNeighboors()

class TannerGraph(Node):
	
	def __init__(self):
		self.BinaryNodes = []
		self.CheckNodes = []

	def addBinaryNode(self,BN):
		BinaryNodes.append(BN)

	def addCheckNode(self,CN):
		CheckNodes.append(CN)




CN = Node([1,2,3,4])
BN = Node([3,4,5])
tg = TannerGraph()
tg.addCheckNode(CN)
tg.addBinaryNode(BN)

