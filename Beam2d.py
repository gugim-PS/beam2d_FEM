import numpy as np
import matplotlib.pyplot as plt

# Physical constants (assuming steel, Fe)
E = 210e9  # Young's modulus for steel (Pa)
b = 0.1    # Beam width (m)
h = 0.02   # Beam height (m)
I = (b * h**3) / 12  # Second moment of area for rectangular cross-section (m^4)

# Problem setup
L = 10.0  # Length of the beam (m)
q = 1000  # Concentrated load (N)
N = 20    # Number of elements (Elements)
h_elem = L / N  # Length of each element

# Function to calculate the stiffness matrix (Beam Bending Stiffness)
def element_stiffness(E, I, h_elem):
    return E * I / h_elem**3 * np.array([[12, 6*h_elem, -12, 6*h_elem],
                                         [6*h_elem, 4*h_elem**2, -6*h_elem, 2*h_elem**2],
                                         [-12, -6*h_elem, 12, -6*h_elem],
                                         [6*h_elem, 2*h_elem**2, -6*h_elem, 4*h_elem**2]])

# Create the global stiffness matrix
K = np.zeros((2*(N+1), 2*(N+1)))

# Add the stiffness matrices for each element
for i in range(N):
    ke = element_stiffness(E, I, h_elem)
    dof = np.array([2*i, 2*i+1, 2*(i+1), 2*(i+1)+1])
    for a in range(4):
        for b in range(4):
            K[dof[a], dof[b]] += ke[a, b]

# Create the load vector (assuming a concentrated load at the right end of the beam)
F = np.zeros(2*(N+1))
F[2*N] = -q  # Apply concentrated load at the right end of the beam

# Boundary conditions (left end fixed)
fixed = [0, 1]  # Fixed at the left end (degrees of freedom 0 and 1)
free = np.setdiff1d(np.arange(2*(N+1)), fixed)  # The free degrees of freedom

# Calculate the displacement vector
displacements = np.zeros(2*(N+1))  # Initialize displacement as 0
K_ff = K[free, :][:, free]  # The stiffness matrix corresponding to free degrees of freedom
F_f = F[free]  # The load vector corresponding to free degrees of freedom

# Solve for displacements at free degrees of freedom
displacements[free] = np.linalg.solve(K_ff, F_f)  # Solve for the displacements

# Function to extract displacement into bending displacement (y-direction displacement)
def displacement_to_bending(displacements, N):
    x = np.linspace(0, L, N+1)  # x-coordinates
    y = displacements[::2]  # y-direction displacements (selecting every second value in the 2D array)
    return x, y

# Calculate the displacement
x, y = displacement_to_bending(displacements, N)

# Resetting the displacement vector to the initial state (zero displacement)
initial_displacements = np.zeros(2*(N+1))
initial_displacements[free] = 0  # Initial state has zero displacement

# Calculate initial displacements
x_initial, y_initial = displacement_to_bending(initial_displacements, N)

# Function to calculate the theoretical maximum displacement (for validation)
def theoretical_max_displacement(q, L, E, I):
    return (q * L**3) / (3 * E * I)

# Theoretical maximum displacement value
delta_max_theoretical = theoretical_max_displacement(q, L, E, I)

# Function to calculate theoretical displacement profile (linear approximation)
def theoretical_displacement_1st(x, q, L, E, I):
    return (q * (L - x)) / (E * I)

# Theoretical displacement profile (linear approximation)
y_theoretical_1st = theoretical_displacement_1st(x, q, L, E, I)

# Visualize results (showing two graphs side by side)
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot initial displacement graph
axs[0].plot(x_initial, y_initial, label="Initial Displacement", color='b', linewidth=2)
axs[0].set_title("Initial Beam Displacement", fontsize=14)
axs[0].set_xlabel("Length (m)", fontsize=12)
axs[0].set_ylabel("Displacement (m)", fontsize=12)
# axs[0].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[0].legend(fontsize=12)
axs[0].tick_params(axis='both', which='major', labelsize=10)

# Plot final displacement graph
axs[1].plot(x, y, label="Final Displacement", color='r', linewidth=2)
# axs[1].plot(x, y_theoretical_1st, label="Theoretical 1st Displacement", color='g', linestyle='--', linewidth=2)
axs[1].set_title("Final Beam Displacement with Load", fontsize=14)
axs[1].set_xlabel("Length (m)", fontsize=12)
axs[1].set_ylabel("Displacement (m)", fontsize=12)
# axs[1].grid(True, which='both', linestyle='--', linewidth=0.5)
axs[1].legend(fontsize=12)
axs[1].tick_params(axis='both', which='major', labelsize=10)

# Set x and y limits for both graphs
axs[0].set_xlim([0, L])
axs[1].set_xlim([0, L])

# Adjust y-axis limits (set the maximum value to 0.025)
max_displacement = max(np.max(y), np.max(y_theoretical_1st))
min_displacement = min(np.min(y), np.min(y_theoretical_1st))

# Adjust y-axis range based on max_displacement
axs[0].set_ylim([min_displacement - 0.005, 5])
axs[1].set_ylim([min_displacement - 0.005, 5])

# Display maximum displacement (both FEM and theoretical values)
axs[1].text(0.5, 0.8 * max_displacement, f"Max FEM Displacement: {min(y):.4e} m", 
            fontsize=12, color='r', ha='center', va='center', fontweight='bold')

# Layout adjustment
plt.tight_layout()

# Show the plots
plt.show()

# Output theoretical maximum displacement
print(f"Theoretical Max Displacement: {delta_max_theoretical:.4e} m")
print(f"Maximum FEM Displacement: {min(y):.4e} m")
