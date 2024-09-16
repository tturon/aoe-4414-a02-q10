# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km
#  Text explaining script usage
# Parameters:
#  lat_deg: latitude in degrees
#  lon_deg: longitude in degrees
#  hae_km: height above ellipsoid in kilometers

# Output:
#  Code that coverts points to ECEF coordinates in kilometers (x, y, z)
#
# Written by Thomas Turon
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys
import math



# "constants"
# e.g., R_E_KM = 6378.137
R_E_KM = 6378.1363 #radius of the earth, km
e_E = 0.081819221456 #eccentricity of the earth

# helper functions

## function description
def calc_denom(ecc,lat_rad):
    return math.sqrt(1.0 - (ecc ** 2) * (math.sin(lat_rad) ** 2))

# initialize script arguments
lat_deg = ''
lon_deg = ''
hae_km = ''

# parse script arguments
if len(sys.argv) == 4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])

else:
    print(\
        'Usage: '\
        'python llh_to_ecef lat_deg lon_deg hae_km'\
        )
    exit()

# write script below this line
lat_rad = math.radians(lat_deg) #latitude in radians
lon_rad = math.radians(lon_deg) #longitude in radians


den = calc_denom(e_E,lat_rad) #denominator
C_E = R_E_KM / den
S_E = (R_E_KM * (1 - e_E**2))/den

r_x = (C_E + hae_km) * math.cos(lat_rad) * math.cos(lon_rad)
r_y = (C_E + hae_km) * math.cos(lat_rad) * math.sin(lon_rad)
r_z = (S_E + hae_km) * math.sin(lat_rad)

print(round(r_x,6))
print(round(r_y,6))
print(round(r_z,6))



