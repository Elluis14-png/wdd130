# water_flow.py

# Function to calculate the water column height
def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column."""
    return tower_height + (3 * tank_height) / 4

# Function to calculate pressure gain from water height
def pressure_gain_from_water_height(height):
    """Calculate the pressure gain due to water height."""
    density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density * gravity * height) / 1000  # Pressure in kPa

# Function to calculate pressure loss from pipe
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate the pressure loss due to pipe friction."""
    density = 998.2  # kg/m^3
    return -(friction_factor * pipe_length * density * fluid_velocity ** 2) / (2000 * pipe_diameter)
