# CoFe/MgO/CoFe Magnetic Tunnel Junction (MTJ)

## 📌 Project Overview
**Author:** Pradyut Mishra  
**Tools:** QuantumATK (LCAO-DFT)

This project simulates the spin-dependent electron transport in a "clean limit" **CoFe/MgO/CoFe** Magnetic Tunnel Junction (MTJ). The device features a crystalline **MgO(001)** tunnel barrier (6 layers) sandwiched between **B2-ordered CoFe** electrodes.

The study calculates the **Tunneling Magnetoresistance (TMR)** ratio by comparing the conductance in Parallel (P) and Anti-Parallel (AP) magnetic configurations.

## 🚀 Key Results
The simulation demonstrates efficient spin filtering with the following performance metrics:

| Metric | Value |
| :--- | :--- |
| **Optimistic TMR** | **14,955%** |
| **Pessimistic TMR** | **98.68%** |
| **Parallel Conductance ($G_P$)** | $1.35 \times 10^{-8}$ S |
| **Anti-Parallel Conductance ($G_{AP}$)** | $8.95 \times 10^{-11}$ S |

> **Note:** The high TMR ratio is attributed to the symmetry-based spin filtering of the $\Delta_1$ band in the CoFe/MgO(001) structure.

## ⚙️ Methodology

### 1. Structure Construction
* **Electrodes:** B2-CoFe (Wairauite) created by substituting Co into BCC Fe.
* **Barrier:** Rocksalt MgO (Periclase) rotated by 45° to match the CoFe lattice ($a_{CoFe} \approx a_{MgO}/\sqrt{2}$).
* **Device:** The final device coordinates were obtained after a rigid geometry optimization of the bulk stack to minimize interfacial forces.

### 2. Transport Calculation
Spin-polarized transport was calculated using the **Non-Equilibrium Green's Function (NEGF)** method.
* **Calculator:** SGGA-PBE with Double-Zeta Polarized basis (Fe, Co) and PseudoDojo Medium (Mg, O).
* **K-points:** $9 \times 9 \times 100$ (Electronic Structure), $151 \times 151$ (Transmission).
* **Configurations:**
    * **Parallel (P):** Left and Right Electrodes spin-aligned (Up/Up).
    * **Anti-Parallel (AP):** Right Electrode spin-flipped (Up/Down).

## 📦 How to Run

1.  **Relax the Bulk (Pre-requisite step):**
    This script performs the geometry optimization on the bulk `CoFe|MgO|CoFe` stack. It minimizes the forces to find the relaxed atomic coordinates.
    * *Note: The output coordinates from this step were used to define the geometry in the device scripts below.*
    ```bash
    atkpython scripts/01_bulk_relaxation.py
    ```

2.  **Calculate Parallel Transport:**
    Runs the NEGF transport calculation for the **Parallel (P)** spin configuration.
    * This script constructs the device using the optimized coordinates from Step 1 and calculates the transmission spectrum.
    ```bash
    atkpython scripts/02_device_parallel.py
    ```

3.  **Calculate Anti-Parallel Transport:**
    Runs the NEGF transport calculation for the **Anti-Parallel (AP)** spin configuration.
    * This script is identical to the parallel case but with the Right Electrode's spins flipped.
    ```bash
    atkpython scripts/03_device_antiparallel.py
    ```

4.  **Analyze TMR:**
    Reads the `.hdf5` outputs from steps 2 & 3 to extract conductance values and compute the TMR ratio.
    ```bash
    atkpython scripts/04_analyze_tmr.py
    ```
