# %% Bulk_MTJ_Rigid

# Set up lattice
vector_a = [2.866, 0.0, 0.0]*Angstrom
vector_b = [0.0, 2.866, 0.0]*Angstrom
vector_c = [0.0, 0.0, 34.67640000000001]*Angstrom
lattice = UnitCell(vector_a, vector_b, vector_c)

# Define elements
elements = [Iron, Cobalt, Iron, Cobalt, Iron, Cobalt, Iron, Cobalt, Magnesium,
            Oxygen, Oxygen, Magnesium, Magnesium, Oxygen, Oxygen, Magnesium,
            Magnesium, Oxygen, Cobalt, Iron, Cobalt, Iron, Cobalt, Iron,
            Cobalt, Iron]

# Define coordinates
fractional_coordinates = [[ 0.25          ,  0.25          ,  0.020662467846],
                          [ 0.75          ,  0.75          ,  0.061987403537],
                          [ 0.25          ,  0.25          ,  0.103312339228],
                          [ 0.75          ,  0.75          ,  0.144637274919],
                          [ 0.25          ,  0.25          ,  0.18596221061 ],
                          [ 0.75          ,  0.75          ,  0.227287146301],
                          [ 0.25          ,  0.25          ,  0.268612081992],
                          [ 0.75          ,  0.75          ,  0.309937017683],
                          [ 0.25          ,  0.25          ,  0.373380743099],
                          [ 0.75          ,  0.75          ,  0.373380743099],
                          [ 0.25          ,  0.25          ,  0.43669037155 ],
                          [ 0.75          ,  0.75          ,  0.43669037155 ],
                          [ 0.25          ,  0.25          ,  0.5           ],
                          [ 0.75          ,  0.75          ,  0.5           ],
                          [ 0.25          ,  0.25          ,  0.56330962845 ],
                          [ 0.75          ,  0.75          ,  0.56330962845 ],
                          [ 0.25          ,  0.25          ,  0.626619256901],
                          [ 0.75          ,  0.75          ,  0.626619256901],
                          [ 0.75          ,  0.75          ,  0.690062982317],
                          [ 0.25          ,  0.25          ,  0.731387918008],
                          [ 0.75          ,  0.75          ,  0.772712853699],
                          [ 0.25          ,  0.25          ,  0.81403778939 ],
                          [ 0.75          ,  0.75          ,  0.855362725081],
                          [ 0.25          ,  0.25          ,  0.896687660772],
                          [ 0.75          ,  0.75          ,  0.938012596463],
                          [ 0.25          ,  0.25          ,  0.979337532154]]

# Set up configuration
bulk_mtj_rigid = BulkConfiguration(
    bravais_lattice=lattice,
    elements=elements,
    fractional_coordinates=fractional_coordinates
    )

# Add tags
bulk_mtj_rigid.addTags('rigid', [0, 1, 2, 3, 22, 23, 24, 25])
bulk_mtj_rigid_name = "bulk_mtj_rigid"


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
nlsave('bulk_fixed_relaxed.hdf5', initial_spin)


# %% Set LCAOCalculator

# %% LCAOCalculator

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
    GGABasis.Iron_SingleZetaPolarized,
    GGABasis.Cobalt_SingleZetaPolarized,
    ]

density_mesh_cutoff = calculateDefaultDensityMeshCutoff(
    calculator_type=LCAOCalculator,
    configuration=bulk_mtj_rigid,
    basis_set=basis_set,
    wave_function_cutoff=None
)

k_point_sampling = MonkhorstPackGrid(
    na=7,
    nb=7,
    nc=2
)

numerical_accuracy_parameters = NumericalAccuracyParameters(
    density_mesh_cutoff=density_mesh_cutoff,
    k_point_sampling=k_point_sampling,
    occupation_method=FermiDirac(
        broadening=1200.0*Kelvin
    )
)

calculator = LCAOCalculator(
    basis_set=basis_set,
    exchange_correlation=exchange_correlation,
    numerical_accuracy_parameters=numerical_accuracy_parameters,
    checkpoint_handler=NoCheckpointHandler
)


# %% Set Calculator

bulk_mtj_rigid.setCalculator(
    calculator=calculator,
    initial_spin=initial_spin
)

nlsave('bulk_fixed_relaxed.hdf5', bulk_mtj_rigid)


# %% OptimizeGeometry

fix_atom_indices_0 = bulk_mtj_rigid.indicesFromTags(['rigid'])

constraints = [
    FixStrain(True, True, True),
    FixAtomConstraints(fix_atom_indices_0)
]

restart_strategy = RestartFromTrajectory(
    trajectory_filename='bulk_fixed_relaxed.hdf5',
    object_id='optimize_trajectory'
)

optimized_configuration = OptimizeGeometry(
    configuration=bulk_mtj_rigid,
    constraints=constraints,
    trajectory_filename='bulk_fixed_relaxed.hdf5',
    trajectory_object_id='optimize_trajectory',
    optimize_cell=False,
    restart_strategy=restart_strategy
)

nlsave('bulk_fixed_relaxed.hdf5', optimized_configuration)
