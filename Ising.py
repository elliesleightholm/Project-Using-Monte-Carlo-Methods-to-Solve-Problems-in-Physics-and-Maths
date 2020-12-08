# Ising Model in 2D

# Importing the relevant modules
from PIL import Image
import numpy as np
from ipywidgets import interact

# The Ising Model follows the following method:
# for every point in the grid
# energy = my spin * sum of all the spins (+1 or -1)
#           of neighbouring points
# if the energy is improved by switching
#      we switch
# else if we're particularly unlucky
#       switch anyway


# A 2D Lattice Ising Model is a way to take a
# lattice of plus and minus spins and evolve them
# with time.

# We want to create a function that will create
# a lattice of plus and minus spins:

def random_spin_field(N, M):
    return np.random.choice([-1, 1], size=(N, M))


print(random_spin_field(10, 10))

# We can visualise this further instead of just
# looking at an array of numbers

# We use PIL (Python Imaging Library)
# This function will return an image of the random spins


def display_spin_field(field):
    return Image.fromarray(np.uint8(field + 1) * 0.5 * 255)  # fromarray only takes values 0 to 255


# display_spin_field(random_spin_field(200, 200)).show()


# Ising Model
def _ising_update(field, n, m, beta=100):
    total = 0
    N, M = field.shape
    beta = 400
    for i in range(n-1, n+2):
        for j in range(m-1, m+2):
            if i == n and j == m:
                continue
            total += field[i % N, j % M]
    dE = 2 * field[n, m] * total
    if dE <= 0:
        field[n, m] *= -1
    elif np.exp(-dE * beta) > np.random.rand():  # metropolis algorithm
        field[n, m] *= -1


def ising_step(field, beta=0.05):
    N, M = field.shape  # This gives the dimensions of the random field/lattice
    for n in range(N):
        for m in range(M):
            _ising_update(field, n, m, beta)
    return field


# display_spin_field((ising_step(random_spin_field(200, 200)))).show()


# Ising Model - again!
def _ising_update(field, n, m, beta):
    total = 0
    N, M = field.shape
    for i in range(n-1, n+2):
        for j in range(m-1, m+2):
            if i == n and j == m:
                continue
            total += field[i % N, j % M]
    dE = 2 * field[n, m] * total
    if dE <= 0:
        field[n, m] *= -1
    elif np.exp(-dE * beta) > np.random.rand():
        field[n, m] *= -1


def ising_step(field, beta):
    N, M = field.shape
    for n_offset in range(2):
        for m_offset in range(2):
            for n in range(n_offset, N, 2):
                for m in range(m_offset, M, 2):
                    _ising_update(field, n, m, beta)
    return field


display_spin_field((ising_step(random_spin_field(400, 400), 0.4))).show()


# Animate the sequence with ipywidgets

# images = [random_spin_field(200, 200)]
# for i in range(50):
#     images.append(ising_step(images[-1].copy(), 0.4))
#
#
# def display_ising_sequence(images): # Give it some images
#     def _show(frame=(0, len(images)-1)):
#         return display_spin_field(images[frame])  #
#     return interact(_show)
#
#
# display_ising_sequence(images)

