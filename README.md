Beam Bending FEM Analysis
This project provides a finite element method (FEM) analysis of a simply supported beam under a concentrated load. It calculates the displacement profile of the beam using FEM and compares the results with theoretical displacement values. The results are visualized using matplotlib and saved in a PDF report using reportlab.

Table of Contents
Purpose
Dependencies
Setup Instructions
Usage
Generating PDF Report
Results
Theoretical Formulas
Purpose
The main goal of this project is to perform a 1D beam bending analysis under a concentrated load using FEM. The analysis involves:

Beam Setup: A simply supported beam with a known load applied at one end.
FEM Analysis: A stiffness matrix is created for the beam's finite elements, and the displacement profile is computed.
Comparison with Theory: The computed FEM displacements are compared with theoretical results from classical beam theory.
The results are visualized in graphs, and a PDF report is generated that includes detailed calculations and results.

Dependencies
Before running the code, make sure the following Python packages are installed:

numpy: For numerical calculations and matrix operations.
matplotlib: For plotting displacement results.
reportlab: For generating the PDF report.
Install the dependencies using pip:
bash
복사
pip install numpy matplotlib reportlab
Setup Instructions
Clone the repository (if you haven't already):

bash
복사
git clone https://github.com/your-username/beam-bending-fem.git
cd beam-bending-fem
Create a virtual environment (optional but recommended):

bash
복사
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
복사
pip install -r requirements.txt
Usage
To run the code and perform the beam bending FEM analysis:

Make sure the Python script equation.py is in the current directory.
Execute the script:
bash
복사
python equation.py
This will perform the following:

Calculate the displacement of the beam using FEM.
Compare the FEM displacement with the theoretical displacement.
Generate a PDF report with the results and mathematical derivations.
Plot the displacement profile of the beam.
Generating PDF Report
The script equation.py will automatically generate a PDF report with the following:

Physical Constants used in the analysis (Young’s modulus, beam dimensions).
Problem Setup (beam length, load applied, number of finite elements).
Stiffness Matrix derivation and calculations.
Displacement Calculations using FEM.
Comparison with Theoretical Results (maximum displacement from beam theory).
The PDF will be saved as beam_bending_analysis.pdf in the current directory.

Results
The displacement of the beam is calculated using both the FEM method and theoretical beam theory.
The displacement results are shown in a plot, where the FEM displacement and the theoretical displacement (linear approximation) can be compared.
The maximum displacement values (both FEM and theoretical) are displayed in the PDF report.
