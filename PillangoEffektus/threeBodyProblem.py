from manim import *


def g_x(k, x, y):
    return (k * x) / ((x * x + y * y) ** (3 / 2))


def g_y(k, x, y):
    return (k * y) / ((x * x + y * y) ** (3 / 2))


def getAccelerationOf(x1, y1, x2, y2, x3, y3, k1, k3):
    x21 = x2 - x1
    y21 = y2 - y1
    x32 = x3 - x2
    y32 = y3 - y2
    ax2 = g_x(k1, x21, y21) + g_x(k3, x32, y32)
    ay2 = g_y(k1, x21, y21) + g_y(k3, x32, y32)
    return [ax2, ay2]


class ThreeBodyProblem(Scene):
    def construct(self):
        # Set the time step (dt)
        dt = 0.1

        # Create particles
        p1 = Dot(radius=0.1, color=RED)
        p2 = Dot(radius=0.1, color=GREEN)
        p3 = Dot(radius=0.1, color=BLUE)

        # Set initial positions
        p1.move_to([0, 1, 0])
        p2.move_to([2, 0, 0])
        p3.move_to([0, 0, 0])

        # Set initial velocities
        vy1 = 0.5
        vx1 = 0
        vy2 = -0.5
        vx2 = 0
        vy3 = 0
        vx3 = 0

        # Set constants
        k1 = 150000
        k2 = 150000
        k3 = 1000

        self.add(p1, p2, p3)
        self.camera.frame_height = 4
        self.camera.frame_width = 4

        for _ in range(500):
            # Calculate accelerations
            a1 = getAccelerationOf(
                p1.get_x(),
                p1.get_y(),
                p2.get_x(),
                p2.get_y(),
                p3.get_x(),
                p3.get_y(),
                k1,
                k3,
            )
            a2 = getAccelerationOf(
                p2.get_x(),
                p2.get_y(),
                p1.get_x(),
                p1.get_y(),
                p3.get_x(),
                p3.get_y(),
                k2,
                k3,
            )
            a3 = getAccelerationOf(
                p3.get_x(),
                p3.get_y(),
                p1.get_x(),
                p1.get_y(),
                p2.get_x(),
                p2.get_y(),
                k1,
                k2,
            )

            # Update velocities
            vy1 += a1[1] * dt
            vx1 += a1[0] * dt
            vy2 += a2[1] * dt
            vx2 += a2[0] * dt
            vy3 += a3[1] * dt
            vx3 += a3[0] * dt

            # Update positions
            p1.shift([vx1 * dt, vy1 * dt, 0])
            p2.shift([vx2 * dt, vy2 * dt, 0])
            p3.shift([vx3 * dt, vy3 * dt, 0])

            self.wait(dt)

        self.wait(2)
