from manimlib.imports import *


class FrecuencyPeriod(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN - (5, 0, 0),
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(0, 10, 2),
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT+UP)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(two_pi))

    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)
