class Node:
	def __init__(self,val):
		self.lchild = None
		self.rchild = None
		self.val = val 

def getHeight(head):
	if head == None:
		return (True,0)
	isBl = getHeight(head.lchild) 
	if isBl[0] == False:
		return (False,0)
	isBr = getHeight(head.rchild)
	if isBr[0] == False:
		return (False,0)
	if (isBl[1]-isBr[1])>1:
		return (False,0)
	return (True,max(isBl[1],isBr[1])+1)

if __name__ == '__main__':
	head = Node(1)
	head.lchild = Node(2)
	#head.rchild = Node(3)
	head.lchild.lchild = Node(4)
	head.lchild.rchild = Node(5)
	#head.rchild.lchild = Node(6)
	res = getHeight(head)
	print(res[0])
	print(res[1])
