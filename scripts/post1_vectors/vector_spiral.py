"""
Spiral scene:

In this scene a spiral of vectors is drawn
"""

from curvipy import GraphingCalculator
from turtle import exitonclick
import math


class Vector:
    def __init__(self, tail, head):
        self.tail = tail
        self.head = head


def spiral_vector_path(
    start_point: tuple[int, int],
    total_vectors: int,
    vectors_length: int,
    initial_angle: float,
    rotation_angle: float,
    rotation_angle_variation: float,
    space_between_vectors: int = 2,
):
    # Define variables
    vectors: list[Vector] = []
    angle = initial_angle
    current_point = start_point

    for _ in range(total_vectors):
        # Get vector given a start point, a vector length and
        # an angle
        vector = (
            math.cos(angle) * vectors_length,
            math.sin(angle) * vectors_length,
        )
        spacing_vector = (
            math.cos(angle) * space_between_vectors,
            math.sin(angle) * space_between_vectors,
        )
        vec_tail = current_point
        vec_head = (vec_tail[0] + vector[0], vec_tail[1] + vector[1])
        vectors.append(Vector(vec_tail, vec_head))

        # Update variables
        current_point = (
            vec_head[0] + spacing_vector[0],
            vec_head[1] + spacing_vector[1],
        )
        angle += rotation_angle
        rotation_angle += rotation_angle_variation
    return vectors


def draw_vectors(
    calc: GraphingCalculator, vector_path: list[Vector], vector_colors: list[str]
):
    for i, vector in enumerate(vector_path):
        calc.vector_color = vector_colors[i % len(vector_colors)]
        calc.draw_vector(vector.head, vector.tail)


def spiral_scene():
    calc = GraphingCalculator(
        drawing_speed=1, vector_width=5, background_color="#FFFFFF", show_axis=False
    )
    total_vectors = 20
    vectors_length = 14
    start_point = (0, -25)
    initial_angle = 0.5
    rotation_angle = 0.6
    rotation_angle_variation = 0.02
    vector_colors = ("#E63946", "#457B9D", "#1D3557")

    input("Press Enter to start animation...")
    vector_path = spiral_vector_path(
        start_point,
        total_vectors,
        vectors_length,
        initial_angle,
        rotation_angle,
        rotation_angle_variation,
    )
    draw_vectors(calc, vector_path, vector_colors)


if __name__ == "__main__":
    spiral_scene()
    exitonclick()
