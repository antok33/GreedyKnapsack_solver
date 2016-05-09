from operator import itemgetter
import sys
import random
import argparse

DOCUMENTATION = """Greedy Knapsack solver\n example:\n
python greedy_kanpsack.py -c 550 -o 200 -v 15-150 -w 5-75
"""


class Knapsack(object):
    def __init__(self, knapsack_weight, items):
        self.knapsack_weight = knapsack_weight
        self.items = items


    def greedy_value(self):
        value_knap = sorted(self.items, key=itemgetter(1), reverse=True)
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
        value_knap = sorted(self.items, key=itemgetter(2))
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
        for item in self.items:
            ratio = item[1]/float(item[2])
            item += (ratio,)
            value_knap.append(item)
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


def items_generator(num_of_items, min_value, max_value, min_weight, max_weight):
    return [
    (
    "#{0}".format(item),
     random.randrange(min_value, max_value),
     random.randrange(min_weight, max_weight)
     )
     for item in range(num_of_items)
    ]

def main(knapsack_available_weight, available_items):

    ins = Knapsack(knapsack_available_weight, available_items)
    print "============ Greedy Knapsack Solver ============\n Available weight of knapsack: ", knapsack_available_weight, "\n"
    print "List of available items:"
    for item in available_items:
        print "Id:", item[0], "Value:", item[1], " Weight:", item[2]
    print ''
    selected_items_value = ins.greedy_value()
    selected_items_weight = ins.greedy_weight()
    selected_items_ratio = ins.greedy_ratio()

    print "Greedy criterion: The most valuable in."
    print "items selected:"
    for item in selected_items_value:
        print "Id: ", item[0], "Value: ", item[1], " Weight: ", item[2]
    print "Total value in the Knapsack:", Knapsack.getTotal_Value(selected_items_value), "\n"

    print "Greedy criterion: The lightest in."
    print "items selected:"
    for item in selected_items_weight:
        print "Id: ", item[0], "Value: ", item[1], " Weight: ", item[2]
    print "Total value in the Knapsack:", Knapsack.getTotal_Value(selected_items_weight), "\n"

    print "Greedy criterion: The greatest ratio in."
    print "items selected:"
    for item in selected_items_ratio:
        print "Id: ", item[0], "Value: ", item[1], " Weight: ", item[2]
    print "Total value in the Knapsack:", Knapsack.getTotal_Value(selected_items_ratio), "\n"

def split_ranges(data):
    data = data.split("-")
    return int(data[0]), int(data[1])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DOCUMENTATION)
    parser.add_argument('-k','--knapsack', type=float, help='knapsack available weight')
    parser.add_argument('-n','--num-items', type=int, help='number of available items')
    parser.add_argument('-v','--value', help='ranged value')
    parser.add_argument('-w','--weight', help='ranged weight')
    args = vars(parser.parse_args())
    try:
        knapsack_available_weight = args["knapsack"]
        num_of_items = args["num_items"]
        min_value, max_value = split_ranges(args["value"])
        min_weight, max_weight  = split_ranges(args["weight"])
    except (ValueError, IndexError, AttributeError):
        parser.print_help()
    else:
        available_items = items_generator(num_of_items, min_value, max_value, min_weight, max_weight)
        main(knapsack_available_weight, available_items)
