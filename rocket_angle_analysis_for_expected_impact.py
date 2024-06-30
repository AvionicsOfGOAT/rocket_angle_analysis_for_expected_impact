import numpy as np
import matplotlib.pyplot as plt

def simulate_rocket_trajectory(theta):
    G = 9.81  # Gravitational acceleration (m/s^2)
    RHO = 1.128  # Air density (kg/m^3)
    CD = 0.8  # Drag coefficient
    A = 0.007854  # Cross-sectional area (m^2)
    M = 4.5  # Mass (kg)
    V0 = 87.5  # Initial velocity (m/s)

    # Initial conditions
    x, y = 0, 0  # Initial position
    vx, vy = V0 * np.cos(theta), V0 * np.sin(theta)  # Initial velocity components
    dt = 0.01  # Time interval

    # Lists for storing results
    x_data, y_data = [x], [y]

    # Simulation loop
    while y >= 0:
        # Update velocity
        v = np.sqrt(vx ** 2 + vy ** 2)
        ax = - (CD * RHO * A * v * vx) / (2 * M)
        ay = -G - (CD * RHO * A * v * vy) / (2 * M)
        vx += ax * dt
        vy += ay * dt

        # Update position
        x += vx * dt
        y += vy * dt

        # Save results
        x_data.append(x)
        y_data.append(y)

    return x_data, y_data

TARGET_DISTANCE = 100  # Desired horizontal distance
THETA_MIN = np.radians(10)  # Minimum angle
THETA_MAX = np.radians(90)  # Maximum angle
THETA_STEP = np.radians(0.1)  # Angle increment (in radians)
EPSILON = 10  # Allowable error (m)
suitable_angles_and_positions = []  # List to store suitable angles and impact positions

theta = THETA_MIN
while theta <= THETA_MAX:
    x_data, y_data = simulate_rocket_trajectory(theta)
    impact_position = x_data[-1]
    if impact_position < TARGET_DISTANCE and TARGET_DISTANCE - impact_position < EPSILON:
        suitable_angles_and_positions.append((np.degrees(theta), impact_position))
        degrees_value = np.degrees(theta)
        plt.plot(x_data, y_data, "--", label=f'Theta: {degrees_value:.2f}, Impact Position: {impact_position:.2f} m')
    theta += THETA_STEP

if suitable_angles_and_positions:
    print("Suitable launch angles and impact positions:")
    for theta, impact_pos in suitable_angles_and_positions:
        print(f"Theta: {theta:.2f} degrees, Impact Position: {impact_pos:.2f} m")
else:
    print("Could not find launch angles that reach the target distance.")

plt.legend()
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.title('Trajectory for Expected Near Miss Falls within 100 Meters by Theta Angles')
plt.show()
