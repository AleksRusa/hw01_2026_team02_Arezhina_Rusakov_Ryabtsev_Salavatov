import csv
import matplotlib.pyplot as plt

time = []
gyro_x = []
gyro_y = []
gyro_z = []

with open('repeat_experiments\exp2-gyro\Raw Data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)

    for row in reader:
        time.append(float(row[0]))
        gyro_x.append(float(row[1]))
        gyro_y.append(float(row[2]))
        gyro_z.append(float(row[3]))

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(time, gyro_x)
plt.ylabel("Angular velocity X (rad/s)")

plt.subplot(3, 1, 2)
plt.plot(time, gyro_y)
plt.ylabel("Angular velocity Y (rad/s)")

plt.subplot(3, 1, 3)
plt.plot(time, gyro_z)
plt.xlabel("Time (s)")
plt.ylabel("Angular velocity Z (rad/s)")

plt.tight_layout()
plt.show()