from operator import itemgetter
import sys
import random
import argparse

DOCUMENTATION = """Greedy Knapsack solver\n example:\n
python greedy_kanpsack.py -c 550 -o 200 -v 15-150 -w 5-75
"""


class Knapsack(object):
    def __init__(self, knapsack_weight, objects):
        self.knapsack_weight = knapsack_weight
        self.objects = objects


    def greedy_value(self):
        value_knap = sorted(self.objects, key=itemgetter(1), reverse=True)
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

def split_ranges(data):
    data = data.split("-")
    return int(data[0]), int(data[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DOCUMENTATION)
    parser.add_argument('-k','--knapsack', type=float, help='knapsack available weight')
    parser.add_argument('-n','--num-objects', type=int, help='number of available objects')
    parser.add_argument('-v','--value', help='ranged value')
    parser.add_argument('-w','--weight', help='ranged weight')
    args = vars(parser.parse_args())
    try:
        knapsack_available_weight = args["knapsack"]
        num_of_objects = args["num_objects"]
        min_value, max_value = split_ranges(args["value"])
        min_weight, max_weight  = split_ranges(args["weight"])
        available_objects = objects_generator(num_of_objects, min_value, max_value, min_weight, max_weight)
        main(knapsack_available_weight, available_objects)
    except (ValueError, IndexError, AttributeError):
        parser.print_help()
