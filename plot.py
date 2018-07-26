""" 
The graph is plotiing the car speed and vibration with repect to time
Auther: Asis Nath 
"""
print(" The Auther :")
print("     /|    _____       ____ ")
print("    / |   |        |  |     ")
print("   /__|   |_____   |  |____ ")
print("  /   |        |   |      | ")
print(" /    |   _____|   |  ____| \n")
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Car_signal.csv')
Car_speed_x = data['Car_speed']
Car_vibration_y = data['Car_vibration ']
plt.plot(Car_vibration_y, 'r')
plt.plot(Car_speed_x, 'b')
plt.xlabel('time ')
plt.ylabel('Car vibration & speed')
plt.title('Car speed & Vibration')
plt.legend(['Vibration', 'Speed'])
plt.show()

