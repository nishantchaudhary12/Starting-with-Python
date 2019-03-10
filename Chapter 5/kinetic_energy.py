#kinetic energy


def kinetic_energy(mass, velocity):
    ke = 1/2 * mass * velocity ** 2
    return ke


def main():
    mass = float(input("Enter the object's mass(in kilograms): "))
    velocity = float(input("Enter the object's velocity(in meter per second): "))
    print('The kinetic energy of the object is:', format(kinetic_energy(mass, velocity), '.2f'))


if __name__ == '__main__':
    main()