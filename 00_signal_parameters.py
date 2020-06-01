from manimlib.imports import *


class FrecuencyPeriod(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 5,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN - (5, 0, 0),
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(0, 5, 1),
        "x_axis_label": "$t[ms]$",
        "y_axis_label": "$V[V]$",
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)

        vert_line_1 = Line(self.coords_to_point(1, -1.5), self.coords_to_point(1, 1.5), color=YELLOW)
        vert_line_2 = Line(self.coords_to_point(2, -1.5), self.coords_to_point(2, 1.5), color=YELLOW)

        period_measurement = TexMobject("T = 1 ms")
        period_measurement.set_x(self.coords_to_point(1, 1.7)[0], LEFT+DOWN)
        period_measurement.set_y(self.coords_to_point(1, 1.7)[1], LEFT+DOWN)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(vert_line_1), ShowCreation(vert_line_2))
        self.play(ShowCreation(period_measurement))

        self.play(
            ApplyMethod(vert_line_1.move_to, self.coords_to_point(2.75, 0)),
            ApplyMethod(vert_line_2.move_to, self.coords_to_point(3.75, 0)),
            ApplyMethod(period_measurement.set_x, self.coords_to_point(2.75, 0)[0], LEFT+UP)
        )

        self.wait(1)

    def func_to_graph(self, x):
        return np.cos(2*math.pi*x)
