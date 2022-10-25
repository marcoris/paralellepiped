import numpy as np
import matplotlib.pyplot as plt


class Paralellepiped:
    def __init__(self, sv, vx, vy, vz):
        if len(vx) != 3 or len(vy) != 3 or len(vz) != 3:
            raise Exception('Vektoren sind nicht im Raum R^3!')
        if (not self.isLinearIndependent(vx, vy)) \
                and not self.isLinearIndependent(vx, vz) \
                and not self.isLinearIndependent(vy, vz):
            self.sv = sv
            self.vx = vx
            self.vy = vy
            self.vz = vz

            # Zuweisung der 8 Eckpunkte des Paralellepiped
            self.corners = np.array([
                self.sv,
                self.vx,
                self.vy,
                self.vz,
                self.sv + (self.vx - self.sv) + (self.vy - self.sv),
                self.sv + (self.vz - self.sv) + (self.vy - self.sv),
                self.sv + (self.vx - self.sv) + (self.vz - self.sv),
                self.sv + (self.vx - self.sv) + (self.vy - self.sv) + (self.vz - self.sv)
            ])

            # Ausgabe zur Kontrolle der Koordinaten
            print(self.sv)
            print(self.vx)
            print(self.vy)
            print(self.vz)
            print("-------------")
            print(self.corners)
        else:
            raise Exception('Vektoren sind linear abhängig!')

    # Erstellung der zu zeichnenden Kanten des Parallelepiped
    def getEdges(self):
        corners = self.corners
        cube_edges = [
            (corners[0], corners[1]),
            (corners[0], corners[2]),
            (corners[0], corners[3]),
            (corners[1], corners[4]),
            (corners[1], corners[6]),
            (corners[2], corners[4]),
            (corners[2], corners[5]),
            (corners[3], corners[5]),
            (corners[3], corners[6]),
            (corners[4], corners[7]),
            (corners[5], corners[7]),
            (corners[6], corners[7]),
        ]

        return cube_edges

    # Zeichnen des Parallelepiped im 1. Oktant
    def printInFirstOctant(self, printStartpoint = False):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for edge in self.getEdges():
            start = edge[0]
            end = edge[1]
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]])

        if printStartpoint:
            ax.scatter(start[0], start[1], start[2], c="red", s=75, linewidth=1, edgecolor='k')

        ax.set_xlabel('x-Achse')
        ax.set_ylabel('y-Achse')
        ax.set_zlabel('z-Achse')
        plt.show()

    # Zeichnen des Parallelepiped auf der Ebene (Vogelperspektive)
    def printInBirdPerspective(self, printStartpoint = False):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for edge in self.getEdges():
            start = edge[0]
            end = edge[1]
            ax.plot([start[0], end[0]], [start[1], end[1]])

        if printStartpoint:
            ax.scatter(start[0], start[1], c="red", s=100, linewidth=1, edgecolor='k')
        ax.set_xlabel('x-Achse')
        ax.set_ylabel('y-Achse')
        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
        ax.grid(axis='both', which='both')

        plt.show()

    # Kontrolle ob linear Unabhängig (wenn vielfaches)
    def isLinearIndependent(self, veca, vecb):
        temp1 = veca[0] / vecb[0]
        temp2 = veca[1] / vecb[1]
        temp3 = veca[2] / vecb[2]

        return (temp1 == temp2) and (temp1 == temp3) and (temp2 == temp3)


# Erstellung des Parallelpiped
sv = np.array([1, 1, 3])
vx = np.array([-3, 1, 3])
vy = np.array([2, -2, 5])
vz = np.array([1, 3, -3])

# support vector, vector direction x, vector direction y, vector direction z
paralellepiped = Paralellepiped(sv, vx, vy, vz)

paralellepiped.printInFirstOctant(True)
paralellepiped.printInBirdPerspective(True)

print("********************************")

# Erstellung des Parallelpiped
sv = np.array([0, 0, 0])
vx = np.array([-2, 0, 2])
vy = np.array([1, -1, 4])
vz = np.array([1, 2, -2])

# support vector, vector direction x, vector direction y, vector direction z
paralellepiped = Paralellepiped(sv, vx, vy, vz)

paralellepiped.printInFirstOctant()
paralellepiped.printInBirdPerspective()
