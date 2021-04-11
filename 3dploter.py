import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot the surface
points = [[0, -1, 12],
           [1, 0, 98],
           [0, 0, 46]]

p0, p1, p2 = points
x0, y0, z0 = p0
x1, y1, z1 = p1
x2, y2, z2 = p2

ux, uy, uz = u = [x1-x0, y1-y0, z1-z0]
vx, vy, vz = v = [x2-x0, y2-y0, z2-z0]

u_cross_v = [uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx]

point  = np.array(p0)
normal = np.array(u_cross_v)

d = -point.dot(normal)

xx, yy = np.meshgrid((0, 1), (-1, 0))

z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

#ax = plt.figure().gca(projection='3d')#plt3d
ax.plot_surface(xx, yy, z)


# plot the surface2
points = [[0, -1, 72],
           [1, 0, 37],
           [0, 0, 19]]

p0, p1, p2 = points
x0, y0, z0 = p0
x1, y1, z1 = p1
x2, y2, z2 = p2

ux, uy, uz = u = [x1-x0, y1-y0, z1-z0]
vx, vy, vz = v = [x2-x0, y2-y0, z2-z0]

u_cross_v = [uy*vz-uz*vy, uz*vx-ux*vz, ux*vy-uy*vx]

point  = np.array(p0)
normal = np.array(u_cross_v)

d = -point.dot(normal)

xx, yy = np.meshgrid((0, 1), (-1, 0))

z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

ax = plt.figure().gca(projection='3d')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.plot_surface(xx, yy, z)
plt.show()
