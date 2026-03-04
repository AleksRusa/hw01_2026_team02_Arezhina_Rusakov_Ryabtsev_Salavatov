import csv
import matplotlib.pyplot as plt

time = []
acc_x = []
acc_y = []
acc_z = []

with open('repeat_experiments\exp1-acc\Raw Data.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # пропускаем заголовок

    for row in reader:
        time.append(float(row[0]))
        acc_x.append(float(row[1]))
        acc_y.append(float(row[2]))
        acc_z.append(float(row[3]))

stop_index = 0
for i, t in enumerate(time):
    if t >= 32.5:
        stop_index = i
        break

time = time[:stop_index]
acc_x = acc_x[:stop_index]
acc_y = acc_y[:stop_index]
acc_z = acc_z[:stop_index]

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(time, acc_x)
plt.ylabel("Acceleration X (m/s²)")

plt.subplot(3, 1, 2)
plt.plot(time, acc_y)
plt.ylabel("Acceleration Y (m/s²)")

plt.subplot(3, 1, 3)
plt.plot(time, acc_z)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration Z (m/s²)")

plt.tight_layout()
plt.show()

