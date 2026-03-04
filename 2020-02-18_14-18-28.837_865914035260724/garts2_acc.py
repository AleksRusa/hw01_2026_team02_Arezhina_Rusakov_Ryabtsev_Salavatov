import csv
import matplotlib.pyplot as plt

time = []
acc_x = []
acc_y = []
acc_z = []

with open('../2020-02-18_14-18-28.837_865914035260724/accelerometer_1.csv', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader, None)  # пропускаем заголовок, если есть

    for row in reader:
        if not row:  # пропускаем пустые строки
            continue
        try:
            t = float(row[0])
            x = float(row[2])
            y = float(row[3])
            z = float(row[4])
        except ValueError:
            # если не удалось преобразовать в float, пропускаем строку
            continue
        time.append(t)
        acc_x.append(x)
        acc_y.append(y)
        acc_z.append(z)

t_start = time[0]
time2 = []
for t in time:
    t -= t_start
    time2.append(t/1000)

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(time2, acc_x)
plt.ylabel("Acceleration X (m/s²)")

plt.subplot(3, 1, 2)
plt.plot(time2, acc_y)
plt.ylabel("Acceleration Y (m/s²)")

plt.subplot(3, 1, 3)
plt.plot(time2, acc_z)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration Z (m/s²)")

plt.tight_layout()
plt.show()