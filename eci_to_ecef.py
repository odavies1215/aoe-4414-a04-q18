# eci_to_ecef.py

# Usage: python3 eci_to_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km
# Description: Converts Year, Month, Day, Hour, Minute, Second, eci_x_km, eci_y_km, eci_z_km inputs from the ECI frame to ECEF coordinates.

# Parameters:
#  year
#  month
#  day
#  hour
#  minute
#  second
#  eci_x_km
#  eci_y_km
#  eci_z_km

# Output:
#  Coordinates in the ecef reference frame (x, y, z), answer in km

# Written by Owen Davies
# Other contributors: None

# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math
import sys

# "constants"
R_E_KM = 6378.137
e_E = 0.081819221456
r_E_km = 6378.1363
w = 0.00007292115
Delta_UT1 = 236.555

# initialize script arguments
year: float(sys.argv[1])
month: float(sys.argv[2])
day: float(sys.argv[3])
hour: float(sys.argv[4])
minute: float(sys.argv[5])
second: float(sys.argv[6])
eci_x_km: float(sys.argv[7])
eci_y_km: float(sys.argv[8])
eci_z_km: float(sys.argv[9])

# parse script arguments
if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  eci_x_km = float(sys.argv[7])
  eci_y_km = float(sys.argv[8])
  eci_z_km = float(sys.argv[9])
else:
  print(\
   'Usage: '\
   'python3 eci_ecef.py year month day hour minute second eci_x_km eci_y_km eci_z_km'\
  )
  exit()
 
# Calculate JD_frac
jd = day-32075+(1461*(year+4800+(month-14)/12)/4)+(367*(month-2-((month-14)/12)*12)/12)-(3*((year+4900+((month-14)/12))/100)/4)
jdint = int(jd)
jdmidnight = jdint-0.5
Dfrac = (second+60*(minute+60*hour))/86400
JDfrac = jdmidnight+Dfrac 

# Calculate GMST Angle
Tut1 = (JDfrac - 2451545.0)/36525
GMSTts = 67310.54841+(876600*60*60+8640184.812866)*Tut1+0.093104*(Tut1**2)+(-6.2*(10**-6))*(Tut1**3)
GMSTangrad = (GMSTts % 86400)*w + 2*math.pi
GMSTrad = (math.fmod(GMSTangrad, 2*math.pi))

# Calculate ECEF coordinates
ecef_x_km = (eci_x_km*math.cos(-GMSTrad))+(eci_y_km*(-math.sin(-GMSTrad)))
ecef_y_km = (eci_x_km*math.sin(-GMSTrad))+(eci_y_km*math.cos(-GMSTrad))
ecef_z_km = (eci_z_km)

# Display final answers
print(f"{ecef_x_km:.3f"})
print(f"{ecef_y_km:.3f"})
print(f"{ecef_z_km:.3f"})

