
def test_possibilities(dice_val_sum, dice_left, sides, target, possibility_count, known_outcomes, depth=0):
    known_outcome = known_outcomes.get(dice_left, {}).get(dice_val_sum, None)
    if known_outcome:
        print(f'outcome known for: d_left: {dice_left}, val: {dice_val_sum}, p: {known_outcome}')
        return known_outcome

    # base case
    if dice_left == 0:
        if dice_val_sum == target:
            return 1
        else:
            return 0
    else:
        for s in range(1, sides+1):  # do this for every side
            dice_val_sum_s = dice_val_sum + s
            dice_left_s = dice_left - 1

            # check reachable values
            min_reachable = dice_val_sum_s + dice_left_s
            max_reachable = dice_val_sum_s + (dice_left_s * sides)
            val_too_high = min_reachable > target
            val_too_low = max_reachable < target

            if val_too_high:
                break
            if not val_too_low:
                possibility_count += test_possibilities(
                    dice_val_sum_s, dice_left_s, sides, target, 0, known_outcomes, depth+1
                )
                if known_outcomes.get(dice_left_s, None):
                    known_outcomes[dice_left_s].update({dice_val_sum_s: possibility_count})
                else:
                    known_outcomes.update({dice_left_s: {dice_val_sum_s: possibility_count}})
    # print(f'depth: {depth}, p_count: {possibility_count}')
    print(known_outcomes)
    return possibility_count


def probability(dice_number, sides, target):
    possibilities_total = sides**dice_number
    possibility_count = 0
    dice_val_sum = 0
    known_outcomes = {}  # dice left, sum of values, valid possibilities

    valid_possibilities = test_possibilities(dice_val_sum, dice_number, sides, target, possibility_count, known_outcomes)
    print(f'v: {valid_possibilities}')
    probability_chance = round(valid_possibilities / possibilities_total, 4)
    print(f'p= {probability_chance}')
    return probability_chance


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    # assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    # assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
