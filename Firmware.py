import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 400)
heartbeat = np.sin(2 * np.pi * 1.5 * t) * 100
drift = 40 * t
noise = np.random.normal(0, 15, len(t))
signal = heartbeat + drift + noise + 5000

threshold = drift + 5050 

beats_t, beats_val = [], []
resets_t, resets_val = [], []

is_above_threshold = False

for i in range(len(t)):
    if signal[i] > threshold[i] and not is_above_threshold:
        is_above_threshold = True
        beats_t.append(t[i])
        beats_val.append(signal[i])
    elif signal[i] < threshold[i] and is_above_threshold:
        is_above_threshold = False
        resets_t.append(t[i])
        resets_val.append(signal[i])

plt.figure(figsize=(10, 5))
plt.plot(t, signal, label="Vyhlazený PPG signál", color="#1f77b4")
plt.plot(t, threshold, label="Dynamický práh", color="purple", linestyle="--")

plt.scatter(beats_t, beats_val, color="red", s=120, zorder=5, label="🔴 Záznam tepu (průraz nahoru)")
plt.scatter(resets_t, resets_val, color="green", s=120, marker="v", zorder=5, label="🟢 Reset algoritmu (pokles dolů)")

plt.title("Vizualizace detekce tepu: Logika stoupající a klesající hrany")
plt.xlabel("Čas (s)")
plt.ylabel("Hodnota signálu (relativní j.)")
plt.legend(loc="lower right")
plt.grid(True, linestyle=":", alpha=0.7)
plt.tight_layout()
plt.show()
