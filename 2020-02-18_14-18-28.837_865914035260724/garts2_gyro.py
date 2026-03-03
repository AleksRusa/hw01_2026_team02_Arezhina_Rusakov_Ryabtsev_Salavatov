import csv
import matplotlib.pyplot as plt

time = []
gyro_x = []
gyro_y = []
gyro_z = []

with open('../2020-02-18_14-18-28.837_865914035260724\gyroscope_2.csv', newline='') as f:
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
        gyro_x.append(x)
        gyro_y.append(y)
        gyro_z.append(z)

# Переводим timestamp в секунды и начинаем от 0
# start_time = time[0]
# time = [t - start_time for t in time]

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