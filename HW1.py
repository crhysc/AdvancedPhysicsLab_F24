import numpy as np
import scipy as sc
from scipy import stats
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
# Array of temperature measurements of water.
temps = np.array([98.51, 98.50, 98.50, 98.49, 98.52, 98.49, 98.52, 98.45, 98.47])
# Array of times corresponding to each temperature measurement
times = [datetime.time(14, x, 16) for x in np.arange(45, 54, 1)]
minutesElapsed = np.arange(0, len(temps), 1)
# Arithmetic mean of the temperature measurements.
meanTemp = np.mean(temps)
print(meanTemp)
# Standard deviation of the temperature measurements.
tempsStDev = round(np.std(temps), 5)
print(tempsStDev)
# Individual temperature measurement uncertanties for cases A, B, and C.
ATempUncertainty = 0.000
BTempUncertainty = 0.01
CTempUncertainty = 0.02
# Calculating the overall uncertanty for cases A, B, and C.
def getOverallUnvertanty(caseTempUncertainty, stDev):
    overallUncertainty = np.sqrt(caseTempUncertainty ** 2 + stDev ** 2)
    return round(overallUncertainty, 5)
ovUncertA = getOverallUnvertanty(ATempUncertainty, tempsStDev)
ovUncertB = getOverallUnvertanty(BTempUncertainty, tempsStDev)
ovUncertC = getOverallUnvertanty(CTempUncertainty, tempsStDev)
print(ovUncertA, ovUncertB, ovUncertC)
# Create a line of best fit of the temperature measurements over time
slope, intercept, r_value, p_value, std_err = stats.linregress(minutesElapsed, temps)
lineOfBestFit = np.poly1d([slope, intercept])
print(slope)
# Plot temperature measurements over minutes elapsed
plt.scatter(minutesElapsed, temps, color="Blue", label="Temperature Measurements")
plt.plot(minutesElapsed, lineOfBestFit(minutesElapsed), color="Red", label="Line of Best Fit")
plt.title("Water temperature measurements over time")
plt.xlabel("Elapsed time (minutes)")
plt.ylabel("Water temperature (degree Celsius)")
plt.show()
