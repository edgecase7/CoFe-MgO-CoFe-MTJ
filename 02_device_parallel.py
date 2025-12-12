# %% Device: CoFe_relaxed

# -------------------------------------------------------------
# Left Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [2.866, 0.0, 0.0]*Angstrom
vector_b = [0.0, 2.866, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.72454981996]*Angstrom
left_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
left_electrode_elements = [Iron, Cobalt, Iron, Cobalt, Iron, Cobalt]

# Define coordinates
left_electrode_coordinates = [[ 0.7165        ,  0.7165        ,  0.754108722325],
                              [ 2.1495        ,  2.1495        ,  2.18710872232 ],
                              [ 0.7165        ,  0.7165        ,  3.620108722316],
                              [ 2.1495        ,  2.1495        ,  5.053108722311],
                              [ 0.716499426454,  0.716499998249,  6.532029910307],
                              [ 2.14949948446 ,  2.149499998304,  7.970441097635]]*Angstrom

# Set up configuration
left_electrode = BulkConfiguration(
    bravais_lattice=left_electrode_lattice,
    elements=left_electrode_elements,
    cartesian_coordinates=left_electrode_coordinates
    )

# -------------------------------------------------------------
# Right Electrode
# -------------------------------------------------------------

# Set up lattice
vector_a = [2.866, 0.0, 0.0]*Angstrom
vector_b = [0.0, 2.866, 0.0]*Angstrom
vector_c = [0.0, 0.0, 8.724545319624]*Angstrom
right_electrode_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
right_electrode_elements = [Cobalt, Iron, Cobalt, Iron, Cobalt, Iron]

# Define coordinates
right_electrode_coordinates = [[ 2.149501032576,  2.149499998578,  0.754087889774],
                               [ 0.716501396648,  0.716499998221,  2.192515403469],
                               [ 2.1495        ,  2.1495        ,  3.671457429864],
                               [ 0.7165        ,  0.7165        ,  5.104457429859],
                               [ 2.1495        ,  2.1495        ,  6.537457429854],
                               [ 0.7165        ,  0.7165        ,  7.97045742985 ]]*Angstrom

# Set up configuration
right_electrode = BulkConfiguration(
    bravais_lattice=right_electrode_lattice,
    elements=right_electrode_elements,
    cartesian_coordinates=right_electrode_coordinates
    )

# -------------------------------------------------------------
# Central Region
# -------------------------------------------------------------

# Set up lattice
vector_a = [2.866, 0.0, 0.0]*Angstrom
vector_b = [0.0, 2.866, 0.0]*Angstrom
vector_c = [0.0, 0.0, 34.75159661206897]*Angstrom
central_region_lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
central_region_elements = [Iron, Cobalt, Iron, Cobalt, Iron, Cobalt, Iron, Cobalt, Magnesium,
                           Oxygen, Oxygen, Magnesium, Oxygen, Magnesium, Magnesium, Oxygen,
                           Oxygen, Magnesium, Cobalt, Iron, Cobalt, Iron, Cobalt, Iron,
                           Cobalt, Iron]

# Define coordinates
central_region_coordinates = [[  0.7165        ,   0.7165        ,   0.754108722325],
                              [  2.1495        ,   2.1495        ,   2.18710872232 ],
                              [  0.7165        ,   0.7165        ,   3.620108722316],
                              [  2.1495        ,   2.1495        ,   5.053108722311],
                              [  0.716499426454,   0.716499998249,   6.532029910307],
                              [  2.14949948446 ,   2.149499998304,   7.970441097635],
                              [  0.7164957711  ,   0.716499995086,   9.478658542285],
                              [  2.149490543874,   2.149499993794,  10.822470987753],
                              [  0.716495973477,   0.716500001186,  12.85625012741 ],
                              [  2.149501277   ,   2.149499999133,  12.975072713755],
                              [  0.716509710935,   0.716500004989,  15.151749695033],
                              [  2.149502415792,   2.149500006238,  15.164266658779],
                              [  2.149500201811,   2.149500029335,  17.375648996131],
                              [  0.716500067342,   0.716499983717,  17.375865189152],
                              [  2.149497852985,   2.149500003887,  19.586836259963],
                              [  0.716491162554,   0.716500004899,  19.600135637651],
                              [  2.149496596479,   2.149500017131,  21.777293337988],
                              [  0.716501885971,   0.71650001611 ,  21.895022520547],
                              [  2.149507663546,   2.149499998891,  23.929105563488],
                              [  0.716504354021,   0.716499996393,  25.272963402671],
                              [  2.149501032576,   2.149499998578,  26.781139182219],
                              [  0.716501396648,   0.716499998221,  28.219566695914],
                              [  2.1495        ,   2.1495        ,  29.698508722309],
                              [  0.7165        ,   0.7165        ,  31.131508722304],
                              [  2.1495        ,   2.1495        ,  32.564508722299],
                              [  0.7165        ,   0.7165        ,  33.997508722295]]*Angstrom

# Set up configuration
central_region = BulkConfiguration(
    bravais_lattice=central_region_lattice,
    elements=central_region_elements,
    cartesian_coordinates=central_region_coordinates
    )

device_cofe_relaxed = DeviceConfiguration(
    central_region,
    [left_electrode, right_electrode],
    equivalent_electrode_lengths=[8.72454981996, 8.724545319624]*Angstrom,
    transverse_electrode_repetitions=[[1, 1], [1, 1]],
    )

# Add tags
device_cofe_relaxed.addTags('rigid', [0, 1, 2, 3, 22, 23, 24, 25])
device_cofe_relaxed_name = "device_cofe_relaxed"


# %% InitialSpin

scaled_spins = [
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    0.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,
]
initial_spin = InitialSpin(
    scaled_spins=scaled_spins
)
nlsave('MTJ_V2_Para.hdf5', initial_spin)


# %% Set DeviceLCAOCalculator

# %% DeviceLCAOCalculator

#----------------------------------------
# Exchange-Correlation
#----------------------------------------
exchange_correlation = SGGA.PBE

#----------------------------------------
# Basis Set
#----------------------------------------
basis_set = [
    BasisGGAPseudoDojo.Oxygen_Medium,
    BasisGGAPseudoDojo.Magnesium_Medium,
    GGABasis.Iron_DoubleZetaPolarized,
    GGABasis.Cobalt_DoubleZetaPolarized,
    ]

density_mesh_cutoff = calculateDefaultDensityMeshCutoff(
    calculator_type=DeviceLCAOCalculator,
    configuration=device_cofe_relaxed,
    basis_set=basis_set,
    wave_function_cutoff=None
)

k_point_sampling = MonkhorstPackGrid(
    na=9,
    nb=9,
    nc=100
)

numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=density_mesh_cutoff,
    k_point_sampling=k_point_sampling,
    occupation_method=FermiDirac(
        broadening=300.0*Kelvin
    )
)

calculator = DeviceLCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    checkpoint_handler=NoCheckpointHandler
)


# %% Set Calculator

device_cofe_relaxed.setCalculator(
    calculator=calculator,
    initial_spin=initial_spin
)

device_cofe_relaxed.update()

nlsave('MTJ_V2_Para.hdf5', device_cofe_relaxed)


# %% MullikenPopulation

mulliken_population = MullikenPopulation(
    configuration=device_cofe_relaxed
)
nlsave('MTJ_V2_Para.hdf5', mulliken_population)


# %% TransmissionSpectrum

kpoints = MonkhorstPackGrid(
    na=151,
    nb=151
)

transmission_spectrum = TransmissionSpectrum(
    configuration=device_cofe_relaxed,
    kpoints=kpoints
)
nlsave('MTJ_V2_Para.hdf5', transmission_spectrum)
