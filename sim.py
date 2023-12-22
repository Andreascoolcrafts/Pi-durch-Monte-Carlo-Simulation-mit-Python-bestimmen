# (c) Andreas Rittsel, 2023
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

total_points = 1000  # Anzahl der Punkte, die generiert werden sollen
inside_circle_count = 0
inside_square_count = 0
pi_approximations = []

# Seitenlänge des Quadrats & Durchmesser des Kreises
a = 1.0


def monte_carlo_simulation():
  global inside_circle_count, inside_square_count

  x = np.random.uniform(0, a)
  y = np.random.uniform(0, a)

  distance = np.sqrt((x - a / 2)**2 + (y - a / 2)**2)

  inside_square_count += 1

  if distance <= a / 2:
    inside_circle_count += 1

  pi_approximation = (inside_circle_count / inside_square_count) * 4
  pi_approximations.append(pi_approximation)


def update(frame):
  monte_carlo_simulation()

  plt.clf()
  ax1 = plt.subplot(2, 1, 1)
  ax1.set_aspect('equal',
                 adjustable='datalim')  # Hier wird das 1:1-Format gesetzt
  plt.title(
      f'Monte-Carlo Experiment - Punkte: {inside_square_count} | '
      f'Kreis: {inside_circle_count} | Quadrat: {inside_square_count} | '
      f'PI ~ {np.pi:.6f} | Aktuelle Annäherung: {pi_approximations[-1]:.6f}')
  plt.gca().add_patch(
      plt.Rectangle((0, 0), a, a, edgecolor='black', facecolor='none'))
  plt.gca().add_patch(
      plt.Circle((a / 2, a / 2), a / 2, edgecolor='black', facecolor='none'))

  x = np.random.uniform(0, a)
  y = np.random.uniform(0, a)

  color = 'blue' if np.sqrt((x - a / 2)**2 +
                            (y - a / 2)**2) <= a / 2 else 'red'

  plt.scatter(x, y, color=color)

  plt.xlabel('X-Achse')
  plt.ylabel('Y-Achse')

  plt.subplot(2, 1, 2)
  plt.plot(pi_approximations, label='PI Annäherung', color='green')
  plt.axhline(y=np.pi, color='red', linestyle='--', label='Echtes PI')
  plt.title('PI Annäherung über die Zeit')
  plt.xlabel('Iteration')
  plt.ylabel('PI Wert')
  plt.legend()


fig, ax = plt.subplots(2, 1, figsize=(8, 8))
fig.subplots_adjust(hspace=0.5)
animation = FuncAnimation(fig, update, frames=total_points, repeat=False)

plt.tight_layout()
plt.show()
