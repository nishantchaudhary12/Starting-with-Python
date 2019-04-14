#Galilean Moons of Jupiter


def radius():
    radius_dict = {'Io': 1821.6, 'Europa': 1560.8, 'Ganymede': 2634.1, 'Callisto': 2410.3}
    return radius_dict


def sur_gravity():
    sur_gravity_dict = {'Io': 1.796, 'Europa': 1.314, 'Ganymede': 1.428, 'Callisto': 1.235}
    return sur_gravity_dict


def orbital_per():
    orbital_per_dict = {'Io': 1.769, 'Europa': 3.551, 'Ganymede': 7.154, 'Callisto': 16.689}
    return orbital_per_dict


def info(user_input, radius_dict, sur_gravity_dict, orbital_per_dict):
    print("Moon's mean radius:", radius_dict[user_input])
    print("Moon's surface gravity:", sur_gravity_dict[user_input])
    print("Moon's orbital period:", orbital_per_dict[user_input])


def main():
    user_input = input('Enter the name of a Galilean moons of Jupiter: ')
    radius_dict = radius()
    sur_gravity_dict = sur_gravity()
    orbital_per_dict = orbital_per()
    if user_input in radius_dict:
        info(user_input, radius_dict, sur_gravity_dict, orbital_per_dict)
    else:
        print('No info, check the name again.')


if __name__ == '__main__':
    main()
