"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day20-Particle-Swarm/input.txt").read_text()

EXAMPLE_INPUT1 = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>"""
EXAMPLE_RESULT1 = 0

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """

    input_string = input_string.replace(',', ' ').replace('>', ' ')
    rows = string_worker(input_string)
    acceleration_dict = {}
    #Find particle with lowest acleration from 0,0,0
    for particle_id in range(len(rows)):
        last_part_of_row = rows[particle_id].split('a=<')[1]
        acceleration_array = last_part_of_row.split()
        acceleration_dict[particle_id] = abs(int(acceleration_array[0])) + \
            abs(int(acceleration_array[1])) + abs(int(acceleration_array[2]))

    min_value = 10000000
    particle_id_closest = -1
    for particle_id in acceleration_dict:
        if acceleration_dict[particle_id] <= min_value:
            min_value = acceleration_dict[particle_id]
            #print('New slow moving particle found:', particle_id, 'accelerations is:', min_value)
            particle_id_closest = particle_id

    solution = particle_id_closest

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 243)
print("\n")

class ParticleRepresentation:
    """Particle Class
    """
    def __init__(self, definition_string, particle_id):
        value_array = []
        self.particle_id = particle_id
        for word in definition_string.split():
            try:
                value_array.append(int(word))
            except ValueError:
                pass #Its not a number

        self._pos_x = value_array[0]
        self._pos_y = value_array[1]
        self._pos_z = value_array[2]

        self._vel_x = value_array[3]
        self._vel_y = value_array[4]
        self._vel_z = value_array[5]

        self._acc_x = value_array[6]
        self._acc_y = value_array[7]
        self._acc_z = value_array[8]

    def move_one_tick(self):
        """Moves one time tick
        """
        self._vel_x += self._acc_x
        self._vel_y += self._acc_y
        self._vel_z += self._acc_z

        self._pos_x += self._vel_x
        self._pos_y += self._vel_y
        self._pos_z += self._vel_z

    def get_pos(self):
        """get position as a string
        """
        return str(self._pos_x) + ':' + str(self._pos_y) + ':' + str(self._pos_z)

def problem_b(input_string, expected_result):
    """Problem B solved function
    """
    input_string = input_string.replace(',', ' ').replace('>', ' ').replace('<', ' ')
    rows = string_worker(input_string)
    all_particles_dict = {}

    for particle_id in range(len(rows)):
        particle_id_ = ParticleRepresentation(rows[particle_id], particle_id)
        all_particles_dict[particle_id] = particle_id_

    for _ in range(10000):
        collision_dict = {}
        particles_to_remove = {}
        for particle_id_ in all_particles_dict:
            all_particles_dict[particle_id_].move_one_tick()
            current_cordinates = all_particles_dict[particle_id_].get_pos()
            if current_cordinates in collision_dict:
                particle_id_already_there = collision_dict[current_cordinates]
                particles_to_remove[particle_id_already_there] = True
                particles_to_remove[particle_id_] = True
            else:
                collision_dict[current_cordinates] = particle_id_
        for particle_id_ in particles_to_remove:
            del all_particles_dict[particle_id_]

    solution = len(all_particles_dict)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b("""p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>
p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>
p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>
p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>""", 1)
problem_b(PROGBLEM_INPUT_TXT, 648)
print("\n")
