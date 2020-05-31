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
        "x_axis_label": "$t[s]$",
        "y_axis_label": "$V[V]$",
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        vert_line_1 = self.get_vertical_line_to_graph(1, func_graph, color=YELLOW)
        vert_line_2 = self.get_vertical_line_to_graph(2, func_graph, color=YELLOW)
        graph_label = self.get_graph_label(func_graph, label="\\cos(x)")
        two_pi = TexMobject("T = 1 segundo")
        label_coord = self.input_to_graph_point(1.5, func_graph)
        two_pi.next_to(label_coord, UP)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(graph_label))
        self.play(ShowCreation(vert_line_1))
        self.play(ShowCreation(vert_line_2), ShowCreation(two_pi))

    def func_to_graph(self, x):
        return np.cos(2*math.pi*x)
