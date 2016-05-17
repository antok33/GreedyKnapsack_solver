from operator import itemgetter
import sys
import random
import argparse

DOCUMENTATION = """Greedy Knapsack solver\n example:\n
python greedy_kanpsack.py -c 550 -o 200 -v 15-150 -w 5-75
"""


def split_ranges(data):
    data = data.split("-")
    return int(data[0]), int(data[1])


def generate_pair(item_id , value, weight):
    return (item_id, value, weight, value/float(weight))


def items_generator(num_of_items, min_value, max_value, min_weight, max_weight):
    return [
    generate_pair(item,
     random.randrange(min_value, max_value),
     random.randrange(min_weight, max_weight),
     )
     for item in range(num_of_items)
    ]


class Knapsack(object):
    def __init__(self, knapsack_weight, items):
        self.knapsack_weight = knapsack_weight
        self.items = items


    def calculate_greed(self):
        ratio_knap = sorted(self.items, key=itemgetter(3), reverse=True)
        value_knap = sorted(self.items, key=itemgetter(1), reverse=True)
        weight_knap = sorted(self.items, key=itemgetter(2))

        ratio_results = []
        value_results = []
        weight_results = []

        knap_by_ratio = 0
        knap_by_value = 0
        knap_by_weight = 0
        item = 0
        greed_complete = False

        while item < len(value_knap) and greed_complete is False:
            greed_complete = True
            knap_by_ratio += ratio_knap[item][2]
            knap_by_value += value_knap[item][2]
            knap_by_weight += weight_knap[item][2]

            if knap_by_ratio <= self.knapsack_weight:
                ratio_results.append(ratio_knap[item])
                greed_complete = False

            if knap_by_value <= self.knapsack_weight:
                value_results.append(value_knap[item])
                greed_complete = False

            if knap_by_weight <= self.knapsack_weight:
                weight_results.append(weight_knap[item])
                greed_complete = False

            item += 1

        return ratio_results, value_results, weight_results


    @staticmethod
    def get_total_value(results):
        return [sum(item) for item in zip(*results)][2]


def main(knapsack_available_weight, available_items):
    ins = Knapsack(knapsack_available_weight, available_items)
    print "============ Greedy Knapsack Solver ============\n Available weight of knapsack: ", knapsack_available_weight, "\n"
    print "List of available items:"
    for item in available_items:
        print "Id:", item[0], "Value:", item[1], " Weight:", item[2]
    print ''
    selected_items_ratio, selected_items_value, selected_items_weight = ins.calculate_greed()


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
