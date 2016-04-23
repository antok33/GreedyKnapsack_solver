from operator import itemgetter
import sys
import random


class Knapsack(object):

    def __init__(self, knapsack_weight, objects):
        self.knapsack_weight = knapsack_weight
        self.objects = objects

    def greedy_value(self):
        value_knap = sorted(self.objects, key=itemgetter(1), reverse=True)
        # print value_knap
        knap_current_weight = 0
        item = 0
        results = []
        while item < len(value_knap):
            knap_current_weight += value_knap[item][2]
            if knap_current_weight <= self.knapsack_weight:
                results.append(value_knap[item])
                item += 1
            else:
                break
        return results

    def greedy_weight(self):
        value_knap = sorted(self.objects, key=itemgetter(2))
        # print value_knap
        knap_current_weight = 0
        item = 0
        results = []

        while item < len(value_knap):
            knap_current_weight += value_knap[item][2]
            if knap_current_weight <= self.knapsack_weight:
                results.append(value_knap[item])
                item += 1
            else:
                break
        return results

    def greedy_ratio(self):
        value_knap = []
        for object in self.objects:
            ratio = object[1]/float(object[2])
            object += (ratio,)
            value_knap.append(object)
        value_knap = sorted(value_knap, key=itemgetter(3), reverse=True)
        # print value_knap
        knap_current_weight = 0
        item = 0
        results = []

        while item < len(value_knap):
            knap_current_weight += value_knap[item][2]
            if knap_current_weight <= self.knapsack_weight:
                results.append(value_knap[item])
                item += 1
            else:
                break
        return results

    @staticmethod
    def getTotal_Value(results):
        value = 0
        for item_tuplex in results:
            value += item_tuplex[1]

        return value


def objects_generator(num_of_objects, min_value, max_value, min_weight, max_weight):
    objects = []
    for i in range(num_of_objects):
        value = random.randrange(min_value, max_value)
        weight = random.randrange(min_weight, max_weight)
        object = ('object {}'.format(i + 1), value, weight)
        objects.append(object)
    return objects


def documentation():
    print '''Greedy Knapsack solver

python greedy_kanpsack.py -c <knapsack size/weight> -o <number of available objects> -v <min possible value for an object> <max possible value for an object> -w <min possible weight for an object> <max possible value for an object>

example:
python greedy_kanpsack.py -c 550 -o 200 -v 15 150 -w 5 75

example's exlanation:
knapsack's weight limit 550
number of available objects 200
for each object possible value in [15,150]
for each object possible weight in [5,75]'''


def main(knapsack_available_weight, available_objects):

    ins = Knapsack(knapsack_available_weight, available_objects)
    print "============ Greedy Knapsack Solver ============\n Available weight of knapsack: ", knapsack_available_weight, "\n"
    print "List of available objects:"
    for object in available_objects:
        print "Name: ", object[0], " Value: ", object[1], " Weight: ", object[2]
    print ''
    selected_objcects_value = Knapsack.greedy_value(ins)
    selected_objcects_weight = Knapsack.greedy_weight(ins)
    selected_objcects_ratio = Knapsack.greedy_ratio(ins)

    print "Greedy criterion: The most valuable in."
    print "Objects selected:"
    for object in selected_objcects_value:
        print "Name: ", object[0], " Value: ", object[1], " Weight: ", object[2]
    print "Total value in the Knapsack:", Knapsack.getTotal_Value(selected_objcects_value), "\n"

    print "Greedy criterion: The lightest in."
    print "Objects selected:"
    for object in selected_objcects_weight:
        print "Name: ", object[0], " Value: ", object[1], " Weight: ", object[2]
    print "Total value in the Knapsack:", Knapsack.getTotal_Value(selected_objcects_weight), "\n"

    print "Greedy criterion: The greatest ratio in."
    print "Objects selected:"
    for object in selected_objcects_ratio:
        print "Name: ", object[0], " Value: ", object[1], " Weight: ", object[2]
    print "Total value in the Knapsack:", Knapsack.getTotal_Value(selected_objcects_ratio), "\n"

if __name__ == '__main__':
    # python greedy_kanpsack.py -c 100 -o 100 -v 15 100 -w 111 11
    if len(sys.argv) == 11:
        if sys.argv[1] == '-c' and sys.argv[3] == '-o' and sys.argv[5] == '-v' and sys.argv[8] == '-w':
            try:
                knapsack_available_weight = float(sys.argv[2])
                num_of_objects = int(sys.argv[4])
                min_value = int(sys.argv[6])
                max_value = int(sys.argv[7])
                min_weight = int(sys.argv[9])
                max_weight = int(sys.argv[10])
                available_objects = objects_generator(num_of_objects, min_value, max_value, min_weight, max_weight)
                main(knapsack_available_weight, available_objects)
            except ValueError:
                documentation()
        else:
            documentation()
    else:
        documentation()
