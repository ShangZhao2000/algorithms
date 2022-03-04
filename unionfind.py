#Written by Nathan Companez for FIT2004 sem 2 2020, lecture 10
import math

class UnionFind:

	def __init__(self, V):
		self.V = V
		self.disjointSet = [-1 for i in range(self.V)]

	def find(self, u):
		if self.disjointSet[u] < 0:
			return u
		return self.find(self.disjointSet[u])

	def union(self, u, v):
		u = self.find(u)
		v = self.find(v)
		if v == u:
			return False
		if -self.disjointSet[u] > -self.disjointSet[v]:
			self.disjointSet[u] = self.disjointSet[v] + self.disjointSet[u]
			self.disjointSet[v] = u
			
		else:
			self.disjointSet[v] = self.disjointSet[v] + self.disjointSet[u]
			self.disjointSet[u] = v
			
		return True

	def __str__(self):
		max_width = int(math.log(self.V) + 3)
		ids = [i for i in range(self.V)]

		formatting = ('{' + ':^{}'.format(max_width) + '}|')*self.V
		line1 = formatting.format(*ids)
		line2 = formatting.format(*self.disjointSet)

		return "{}\n{}".format(line1, line2)


if __name__ == "__main__":
	V = 10
	ds = UnionFind(V)
	#0, 1, 2, 3, 4, 7
	ds.union(0,3)
	ds.union(2,7)
	ds.union(0,1)
	ds.union(0,4)
	ds.union(4,7)
	print(ds)
	