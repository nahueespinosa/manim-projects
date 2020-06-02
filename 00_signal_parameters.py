from manimlib.imports import *

# Period in miliseconds
PERIOD = 100


def func_to_graph(x):
    return np.sin(2*math.pi*x/PERIOD)


class Period(GraphScene):
    CONFIG = {
        "x_min" : 0,
        "x_max" : 5 * PERIOD,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN - (5, 0, 0),
        "function_color" : RED,
        "axes_color" : GREEN,
        "x_labeled_nums" : range(0, 5 * PERIOD, PERIOD),
        "x_tick_frequency": PERIOD / 2,
        "x_axis_label": "$t[ms]$",
        "y_axis_label": "$V[V]$",
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(func_to_graph, self.function_color)

        vert_line_1 = Line(self.coords_to_point(PERIOD, -1.5), self.coords_to_point(PERIOD, 1.5), color=YELLOW)
        vert_line_2 = Line(self.coords_to_point(PERIOD * 2, -1.5), self.coords_to_point(PERIOD * 2, 1.5), color=YELLOW)

        period_measurement = TexMobject(f"T = {PERIOD} ms")
        period_measurement.set_x(self.coords_to_point(PERIOD, 1.7)[0], LEFT+DOWN)
        period_measurement.set_y(self.coords_to_point(PERIOD, 1.7)[1], LEFT+DOWN)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(vert_line_1), ShowCreation(vert_line_2))
        self.play(ShowCreation(period_measurement))

        self.play(
            ApplyMethod(vert_line_1.move_to, self.coords_to_point(PERIOD * 2.75, 0)),
            ApplyMethod(vert_line_2.move_to, self.coords_to_point(PERIOD * 3.75, 0)),
            ApplyMethod(period_measurement.set_x, self.coords_to_point(PERIOD * 2.75, 0)[0], LEFT+UP)
        )

        self.wait(1)


class Frequency(Period):
    CONFIG = {
        "x_max" : 1200,
        "x_labeled_nums" : range(0, 1100, 200),
        "x_tick_frequency": 100,
    }

    def construct(self):
        self.setup_axes(animate=False)
        func_graph = self.get_graph(func_to_graph, self.function_color)

        vert_line = Line(self.coords_to_point(0, -1.5), self.coords_to_point(0, 1.5), color=YELLOW)

        self.play(ShowCreation(func_graph))
        self.play(ShowCreation(vert_line))

        self.play(
            ApplyMethod(vert_line.move_to, self.coords_to_point(1000, 0))
        )

        self.wait(1)

        count_label = None

        for index, point in enumerate(range(0, 1000, PERIOD)):
            if count_label is not None:
                self.wait(0.1)
                self.play(FadeOut(count_label, run_time=0.1))

            label_coord = self.input_to_graph_point(point+PERIOD/4, func_graph)
            count_label = TexMobject(f"{index+1}")
            count_label.next_to(label_coord, ORIGIN+UP)

            self.play(FadeIn(count_label, run_time=0.1))

        frequency_measurement = TexMobject(f"f = {1000 / PERIOD} Hz")
        frequency_measurement.set_y(self.coords_to_point(0, 1.2)[1], LEFT+DOWN)

        self.play(Transform(count_label, frequency_measurement))    
