from State import State

TERMINAL_STATE = State(-1, -1, False, -1, -1, 0, None)


class Graph:

	def __init__(self):

		self.bfs_parent = []
		self.dfs_parent = []
		self.visited = []
		self.expandedBFS = 0
		self.expandedDFS = 0

	def BFS(self, s):
		self.expandedBFS = 0
		queue = [s]

		while queue:
			self.expandedBFS += 1

			u = queue.pop(0)
			self.bfs_parent.append(u)

			if u.isGoal():
				print("No of Expanded Nodes: " + str(self.expandedBFS))
				print("No of Explored Nodes: " + str(self.bfs_parent.__len__()))
				queue.clear()
				return self.bfs_parent

			for v in reversed(u.move()):
				if not self.visited.__contains__(v):
					self.visited.append(v)
					queue.append(v)
		return None

	def DFS(self, s):
		self.expandedDFS = 0
		self.DFSHelp(s)
		return None

	def DFSHelp(self, state):
		self.expandedDFS += 1
		self.visited.append(state)
		if state.isGoal():
			print("No of Expanded Nodes: " + str(self.expandedDFS))
			print("No of Explored Nodes: " + str(self.dfs_parent.__len__()))
			return self.dfs_parent
		for v in state.move():
			if not self.dfs_parent.__contains__(v):
				self.dfs_parent.append(state)
				if self.DFSHelp(v) is not None:
					return self.dfs_parent