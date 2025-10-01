# ESS563-2025
Advanced Seismology

---
title: "ESS 563 – Advanced Seismology"
layout: course
permalink: /teaching/ess563/
---


## Course description
ESS 563 is a graduate course on seismic wave propagation, earthquake source mechanics, and modern computational seismology.  Weekly theoretical lectures draw on *Quantitative Seismology* and *Source Mechanisms of Earthquakes*, while practical sessions use Python/ObsPy, FDSN web services, finite‑difference and spectral‑element modeling (SPECFEM3D/sem3D), and Instaseis to explore real and synthetic seismograms.  Students study continuum mechanics, radiation patterns, layered media, moment tensors, dynamic rupture, and full‑waveform inversion, and apply these concepts to recent large earthquakes and slow‑slip events.

## Learning outcomes
- Derive and apply the equations of dynamic elasticity to describe seismic wave propagation in homogeneous and layered media.  
- Analyze point‑source radiation patterns and moment tensors to interpret earthquake mechanisms and rupture kinematics.  
- Implement numerical methods (finite‑difference and spectral‑element) to generate synthetic seismograms and evaluate their accuracy.  
- Use Python/ObsPy to retrieve, process, and visualize seismic data from global networks, and compare observations with synthetic predictions.  
- Interpret finite‑fault and dynamic rupture models of large earthquakes and assess their implications for seismic hazard and earthquake physics.  
- Explain the role of slow‑slip events and tremor in the earthquake cycle and evaluate emerging tools for earthquake detection and characterization.

## Installation

### Prerequisites
This course requires Python 3.9+ with scientific computing packages. We recommend using conda to manage the environment.

### Setting up the environment
1. **Clone this repository:**
   ```bash
   git clone https://github.com/UW-geophysics-edu/ESS563-2025.git
   cd ESS563-2025
   ```

2. **Create and activate the conda environment:**
   ```bash
   conda env create -f env.yml
   conda activate ess563-2025
   python -m ipykernel install --user --name ess563-2025 --display-name "ess563-2025"
   ```

3. **Verify installation:**
   ```bash
   python -c "import obspy, matplotlib, pandas, scipy; print('All packages imported successfully!')"
   ```


### Running Jupyter notebooks
After setting up the environment, start Jupyter to work with the course notebooks:
```bash
jupyter lab
# or
jupyter notebook
```

### Troubleshooting
- If you encounter issues with ObsPy installation, try installing it separately: `conda install -c conda-forge obspy`
- For plotting issues, ensure you have a GUI backend: `conda install -c conda-forge pyqt`
- If you're on macOS with Apple Silicon, make sure to use the `conda-forge` channel for better compatibility

## Resources
- [Notebook repository](https://github.com/UW-geophysics-edu/ESS563-2025/) – Python notebooks used in class  
- [10‑week course plan](https://denolle-lab.github.io/teaching/ess563/) – overview of weekly topics, readings, and assignments  
- Contact the instructor via Canvas for detailed syllabus and assignments.

## Schedule

<table class="schedule-table">
<thead>
<tr>
<th>Week</th>
<th>Monday – Theory (10:00–11:20 AM)</th>
<th>Wednesday – Practice (10:00–11:20 AM)</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Week 1</strong></td>
<td><strong>Fundamentals of seismic waves and elasticity</strong> – review continuum mechanics, stress–strain relations, dynamic elasticity and Green's functions.</td>
<td><strong>Python: stress &amp; strain tensors</strong> – compute stress and strain tensors for simple deformations and verify reciprocity; plot shear stress vs. displacement.</td>
</tr>
<tr>
<td><strong>Week 2</strong></td>
<td><strong>Point dislocation sources and radiation patterns</strong> – representation theorems, double‑couple sources, body‑force equivalents.</td>
<td><strong>Python: radiation pattern simulation</strong> – code P‑ and S‑wave radiation patterns for a double‑couple moment tensor; visualize azimuthal variation.</td>
</tr>
<tr>
<td><strong>Week 3</strong></td>
<td><strong>Plane waves and boundary interactions</strong> – plane waves in homogeneous media, reflection and transmission at interfaces, inhomogeneous/interface waves.</td>
<td><strong>Python: reflection/transmission coefficients</strong> – calculate and plot reflection and conversion coefficients for P/S waves at contrasting half‑spaces; explore impedance contrasts.</td>
</tr>
<tr>
<td><strong>Week 4</strong></td>
<td><strong>Spectral‑element methods and full‑waveform modelling</strong> – introduce SEM, mesh construction, accuracy and convergence; discuss SPECFEM3D/sem3D workflows.</td>
<td><strong>Numerical lab: running SPECFEM/sem3D</strong> – prepare simple 1‑D/3‑D velocity models, generate input files, and run a forward simulation; compare results from a 1‑D finite‑difference solver.</td>
</tr>
<tr>
<td><strong>Week 5</strong></td>
<td><strong>Wave propagation in layered and depth‑dependent media</strong> – generalized rays, reflectivity methods, ray theory; inversion of travel‑times.</td>
<td><strong>Python: ray tracing &amp; inversion</strong> – implement multi‑layer ray tracing, compute travel times and invert synthetic data to estimate layer velocities.</td>
</tr>
<tr>
<td><strong>Week 6</strong></td>
<td><strong>Kinematics of earthquake sources and moment tensors</strong> – far‑ and near‑field signatures, centroid moment tensor theory, source inversion basics.</td>
<td><strong>Python/ObsPy: moment tensor inversion</strong> – generate synthetic seismograms for specified moment tensors and station geometries; invert synthetic waveforms to recover orientation.</td>
</tr>
<tr>
<td><strong>Week 7</strong></td>
<td><strong>Fracture mechanics and dynamic rupture</strong> – crack propagation, stress intensity, fracture energy, boundary‑integral methods; introduction to supershear.</td>
<td><strong>Python: 1‑D spring‑block model</strong> – simulate a Burridge–Knopoff system to explore frictional parameters and observe transitions from subshear to supershear rupture speeds.</td>
</tr>
<tr>
<td><strong>Week 8</strong></td>
<td><strong>Case studies of recent large earthquakes</strong> – discuss multi‑segment faulting, supershear phases, and slip distributions of recent events (e.g., 2024 Noto Peninsula, 2023 Türkiye).</td>
<td><strong>Instaseis/Syngine lab</strong> – use finite‑fault source models to generate global synthetic seismograms with Instaseis/Syngine; download and process observed data via FDSN services; align and compare synthetic and observed phases.</td>
</tr>
<tr>
<td><strong>Week 9</strong></td>
<td><strong>Slow slip events and the earthquake cycle</strong> – classification of slow slip, tremor, repeating earthquakes, and afterslip; implications for moment release.</td>
<td><strong>Python: detecting slow slip</strong> – analyze GNSS time‑series to identify transient slow slip using cross‑correlation/stacking; compare with tremor catalogues.</td>
</tr>
<tr>
<td><strong>Week 10</strong></td>
<td><strong>Seismometry and advanced topics</strong> – instrumentation, frequency response, dynamic range; discussion of machine learning, dynamic triggering, and earthquake predictability.</td>
<td><strong>Final project workshop</strong> – students build a "synthetic earthquake" (define fault geometry &amp; slip), generate synthetic waveforms, and invert to recover source parameters. Include optional global synthetics using Instaseis/Syngine.</td>
</tr>
</tbody>
</table> |