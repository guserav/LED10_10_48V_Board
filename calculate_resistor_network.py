from fractions import Fraction
from operator import itemgetter, attrgetter

ADC_ACCURACY = 2 ** 10
COMMON_VALUES = [
        12,
        15,
        18,
        22,
        27,
        33,
        39,
        47,
        51,
        56,
        68,
        82
]

# COMMON_VALUES = [
#         1,
#         3,
#         8,
# ]

class Resistor():
    """
    class representing a resistor or set of resistors
    it has a high and low resistants
    accordingly a low i.e. worse conductance
    and a high i.e. better conductance
    """
    def __init__(self, resistants, accuracy=Fraction(1, 100)):
        assert isinstance(accuracy, Fraction)
        self.resistants = Fraction(resistants)
        self.high_resistants = self.resistants * (1 + accuracy)
        self.low_resistants = self.resistants * (1 - accuracy)

    def get_low_resistants(self):
        return self.low_resistants

    def get_low_conductance(self):
        return 1 / self.get_high_resistants()

    def get_high_resistants(self):
        return self.high_resistants

    def get_high_conductance(self):
        return 1 / self.get_low_resistants()

    def get_resistants(self):
        return self.resistants

    def get_conductance(self):
        return 1 / self.resistants

    def __repr__(self):
        val = float(self.get_resistants())
        return f"R({val:.1e})"

    def get_part_count(self):
        return 1


class ResistorNetwork(Resistor):
    def __init__(self, parallel, *resistors):
        self.resistors = resistors
        self.parallel = parallel
        if parallel:
            self.resistants = 1 / sum(r.get_conductance() for r in self.resistors)
            self.high_resistants = 1 / sum(r.get_low_conductance() for r in self.resistors)
            self.low_resistants = 1 / sum(r.get_high_conductance() for r in self.resistors)
        else:
            self.resistants = sum(r.get_resistants() for r in self.resistors)
            self.high_resistants = sum(r.get_high_resistants() for r in self.resistors)
            self.low_resistants = sum(r.get_low_resistants() for r in self.resistors)

    def __repr__(self):
        assert self.get_high_resistants() > self.get_low_resistants()
        if self.parallel:
            seperator = "_"
        else:
            seperator = "+"
        concat = seperator.join(repr(r) for r in self.resistors)
        return f"S({concat})"

    def get_part_count(self):
        return sum(r.get_part_count() for r in self.resistors)


class DipSwitchNetwork():
    def __init__(self, ground_resistor, *resistors):
        self.ground_resistor = ground_resistor
        self.resistors = resistors
        self.accuracy = None

    def yield_values(self):
        # yield no switches immediatly
        yield Fraction(1), Fraction(1), Fraction(1)
        # other dip positions skipping the first
        for num in range(1, 2 ** len(self.resistors)):
            conductance, low_conductance, high_conductance = 0, 0, 0
            for i, resistor in  enumerate(self.resistors):
                if (1 << i) & num:  # resistor is part of the network
                    conductance += resistor.get_conductance()
                    low_conductance += resistor.get_low_conductance()
                    high_conductance += resistor.get_high_conductance()
            value = self.ground_resistor.get_resistants() / ((1 / conductance) + self.ground_resistor.get_resistants())
            low_value = self.ground_resistor.get_low_resistants() / ((1 / low_conductance) + self.ground_resistor.get_low_resistants())
            high_value = self.ground_resistor.get_high_resistants() / ((1 / high_conductance) + self.ground_resistor.get_high_resistants())
            other_value_1 = self.ground_resistor.get_high_resistants() / ((1 / low_conductance) + self.ground_resistor.get_high_resistants())
            other_value_2 = self.ground_resistor.get_low_resistants() / ((1 / high_conductance) + self.ground_resistor.get_low_resistants())
            # assert low_value <= other_value_1
            # assert low_value <= other_value_2
            # assert low_value <= high_value
            # assert high_value >= other_value_1
            # assert high_value >= other_value_2
            # assert high_value >= low_value
            # assert low_value < value < high_value
            yield low_value, value, high_value


    def calculate_values(self):
        values = list(self.yield_values())
        return sorted(values, key=itemgetter(1))

    def get_accuracy(self):
        values = self.calculate_values()
        prev_values = [v[2] * ADC_ACCURACY for v in values[:-1]]
        next_values = [v[0] * ADC_ACCURACY for v in values[1:]]
        accuracy = ADC_ACCURACY
        for next_value, prev_value in zip(next_values, prev_values):
            difference = next_value - prev_value
            if difference < accuracy:
                if difference <= 0:
                    return 0
                accuracy = difference
        # print("A", accuracy)
        # print("L", prev_values)
        # print("H", next_values)
        return accuracy

    def determine_accuracy(self):
        if self.accuracy is None:
            self.accuracy = self.get_accuracy()
        return self.accuracy

    def __repr__(self):
        resistors = "+".join(repr(x) for x in self.resistors)
        return f"{self.ground_resistor},{resistors}"


def yield_resistor_pairs(input_resistors):
    for i, r1 in enumerate(input_resistors):
        for r2 in input_resistors[i:]:
            yield ResistorNetwork(True, r1, r2)
            yield ResistorNetwork(False, r1, r2)


def yield_basic_resistors(input_values, accuracy=Fraction(1,100)):
    for shift in [1, 10]:
        for val in input_values:
            yield Resistor(val * shift, accuracy)


def generate_resistors(input_values):
    basic_resistors = list(yield_basic_resistors(input_values))
    resistor_pairs = list(yield_resistor_pairs(basic_resistors))
    return basic_resistors + resistor_pairs


def generate_dip_switch_networks(resistors):
    count = 1
    for ground_resistor in resistors:
        for i, r1 in enumerate(resistors):
            for j, r2 in enumerate(resistors[i:]):
                for k, r3 in enumerate(resistors[i+j:]):
                    for r4 in resistors[i+j+k:]:
                        yield DipSwitchNetwork(ground_resistor, r1, r2, r3, r4), count
                        count += 1

def count_dip_switch_networks(resistors):
    r_count = len(resistors)
    count = 0
    for i in range(r_count):
        for j in range(r_count - i):
            for k in range(r_count - j - i):
                m = r_count - k - i - j
                count += m
    return r_count * count

def get_accuracy(*values):
    for x, y in zip(values, sorted(values)):
        if x != y:
            return 0
    resistors = [Resistor(x) for x in values]
    return DipSwitchNetwork(Resistor(1), *resistors).get_accuracy()


def range_f(mi, ma, st):
    x = mi
    while x <= ma:
        yield x
        x += st


def get_best_from_2_d(x, y, mi, ma, st):
    if x > y:
        return 0
    best_accuracy = 0
    data = (None, None)
    for i in range_f(mi, ma, st):
        for j in range_f(i, ma, st):
            accuracy = get_accuracy(x, y, i, j)
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                data = i, j
    return best_accuracy, data[0], data[1]


def main():
    resistors = generate_resistors(COMMON_VALUES)
    # resistors = list(yield_basic_resistors(COMMON_VALUES))
    resistors = sorted(resistors, key=attrgetter('resistants'))
    r_count = len(resistors)
    total = count_dip_switch_networks(resistors)
    best_accuracy = 0
    best_dip = None
    for dip, count in generate_dip_switch_networks(resistors):
        accuracy = dip.determine_accuracy()
        if accuracy > best_accuracy:
            best_dip = dip
            best_accuracy = accuracy
        print(count, total, f"{count/total * 100:.6f}", best_accuracy, best_dip)


if __name__ == "__main__":
    main()
