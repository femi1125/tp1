import matplotlib.pyplot as plt
rayon = float(input("Entrez le rayon du cercle : "))
cercle = plt.Circle((0, 0), rayon, color='purple', fill=False)
fig, ax = plt.subplots()
ax.add_artist(cercle)
ax.set_xlim(-rayon - 1, rayon + 1)
ax.set_ylim(-rayon - 1, rayon + 1)
ax.set_aspect('equal')  
plt.title(f"Cercle de rayon {rayon}")
plt.show()



