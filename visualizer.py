import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def plot(points, history_m, history_b, history_error):

    x_points = [point[0] for point in points]
    y_points = [point[1] for point in points]

    # X values used to draw the regression line
    x = list(range(50))

    # Create figure
    fig, ax = plt.subplots(figsize=(9, 6))

    # Data points
    ax.scatter(
        x_points,
        y_points,
        color="black",
        s=35,
        zorder=3,
        label="Data points"
    )

    # Initial regression line
    line, = ax.plot(
        x,
        [history_m[0] * value + history_b[0] for value in x],
        color="blue",
        linewidth=2,
        label="Regression line"
    )

    # Information displayed on graph
    info = ax.text(
        0.03,
        0.95,
        "",
        transform=ax.transAxes,
        verticalalignment="top",
        fontsize=11,
        bbox=dict(
            boxstyle="round",
            facecolor="white",
            alpha=0.85
        )
    )

    # Axis configuration
    ax.set_title("Linear Regression Training")
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")

    ax.grid(
        True,
        linestyle="--",
        alpha=0.5
    )

    ax.legend()

    ax.set_xlim(
        min(x_points) - 1,
        max(x) + 1
    )

    ax.set_ylim(
        min(y_points) - 5,
        max(y_points) + 10
    )

    # Animation
    def update(frame):

        m = history_m[frame]
        b = history_b[frame]
        error = history_error[frame]

        # Calculate new regression line
        y = [
            m * value + b
            for value in x
        ]

        # Update line
        line.set_ydata(y)

        # Update information
        info.set_text(
            f"Epoch: {frame + 1}/{len(history_m)}\n"
            f"m = {m:.4f}\n"
            f"b = {b:.4f}\n"
            f"RMSE = {error:.4f}"
        )

        return line, info

    # Create animation
    animation = FuncAnimation(
        fig,
        update,
        frames=len(history_m),
        interval=50,
        repeat=True
    )

    plt.tight_layout()
    plt.show()