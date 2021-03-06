from Dof import Dof
from Interaction import Interaction
def CreatePosition(universe=None, VectorType=None):
	V = universe.dofs["Vector"]
	# V = VectorType or universe.get_type("Vector") or CreateVector(d=2)
	# V = None
	# if VectorType: 
	# 	V = VectorType
	# elif "Vector" in universe:
	# 	V = universe["Vector"]
	# else:
	# 	V = CreateVector(d=2)

	class PositionDegree(Dof):
		def __init__(self):
			super().__init__()
			self.x = V()
			self.v = V()
			self.a = V()

	return PositionDegree

def CreateStaticPosition(universe=None):
	V = universe.dofs["Vector"]

	class StaticPosition(Dof):
		def __init__(self):
			super().__init__()
			self.position = V()

	return StaticPosition

def CreateKinematicPosition(universe=None):
	def BK(pd):
		# print("pos: ", pd.x, pd.v)
		pd.x += pd.v
		pd.v += pd.a
		# pd["x"] += pd["v"]
		# pd["v"] += pd["a"]

	KP = CreatePosition(universe=universe)
	KP.add_interaction(name="basic_kinematics", action=BK)
	# KP.Interactions.append(BasicKinematics(name="basic_kinematics"))
	return KP
