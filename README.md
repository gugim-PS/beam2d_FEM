# Beam Bending Analysis using FEM

This repository demonstrates the analysis of beam bending using Finite Element Method (FEM) for a beam under a concentrated load. The code calculates the displacement of the beam using FEM and compares it with the theoretical displacement using an analytical approach.

## Physical Setup

- **Material:** Steel (Fe)
- **Length of Beam (L):** 10 meters
- **Beam Width (b):** 0.1 meters
- **Beam Height (h):** 0.02 meters
- **Young’s Modulus (E):** 210 GPa
- **Concentrated Load (q):** 1000 N applied at the free end of the beam
- **Number of Elements (N):** 20 (discretization of the beam)
- **Element Length (h_elem):** Calculated based on the number of elements

## Finite Element Method (FEM) Procedure

### 1. Element Stiffness Matrix

Each beam element stiffness matrix is calculated using the following formula:

$$
k_e = \frac{E I}{h_{\text{elem}}^3} 
\begin{bmatrix}
12 & 6h_{\text{elem}} & -12 & 6h_{\text{elem}} \\
6h_{\text{elem}} & 4h_{\text{elem}}^2 & -6h_{\text{elem}} & 2h_{\text{elem}}^2 \\
-12 & -6h_{\text{elem}} & 12 & -6h_{\text{elem}} \\
6h_{\text{elem}} & 2h_{\text{elem}}^2 & -6h_{\text{elem}} & 4h_{\text{elem}}^2
\end{bmatrix}
$$

### 2. Global Stiffness Matrix

The global stiffness matrix is assembled by summing the element stiffness matrices at their respective degrees of freedom (DOF).

### 3. Load Vector

The load vector represents the concentrated force applied at the free end of the beam, assuming the load is applied at the last degree of freedom.

### 4. Boundary Conditions

- **Fixed Support:** The beam is fixed at the left end, which means the displacement at the left end is zero.
- **Free End:** The displacement at the free end is computed by solving the system of equations derived from FEM.

## Displacement Calculation

### 1. FEM Displacement

The displacement at each point is calculated using the stiffness matrix and the load vector, considering the boundary conditions.

### 2. Theoretical Maximum Displacement

The theoretical displacement at the free end of the beam, based on classical beam theory, is given by the formula:

$$
\delta_{\text{max}} = \frac{q L^3}{3 E I}
$$

### 3. Comparison

The maximum displacement from FEM is compared with the theoretical maximum displacement to validate the results.

## Results Visualization

- **Initial Beam Displacement:** The displacement profile at the beginning (zero displacement).
- **Final Beam Displacement:** The displacement profile after the load is applied.

The results are plotted for both the initial and final beam displacement.

### Sample Output:

- **Theoretical Max Displacement**: 1.2345e-04 m
- **Maximum FEM Displacement**: 1.2345e-04 m

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## Installation

To run the code locally, clone the repository and install the required libraries:

```bash
git clone https://github.com/yourusername/beam-bending-fem.git
cd beam-bending-fem
pip install -r requirements.txt
