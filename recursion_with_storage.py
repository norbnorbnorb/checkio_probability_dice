
def test_possibilities(current_val, dice_left, sides, target, possibility_count, known_outcomes, depth=0):
    known_outcome = known_outcomes.get(dice_left, {}).get(current_val, None)
    if known_outcome:
        print(f'outcome known for: d_left: {dice_left}, val: {current_val}, p: {known_outcome}')
        return known_outcome

    # base case
    if dice_left == 0:
        if current_val == target:
            return 1
        else:
            return 0
    else:
        for s in range(1, sides+1):  # do this for every side
            current_new_val = current_val + s
            new_dice_left = dice_left - 1

            # check reachable values
            min_reachable = current_new_val + new_dice_left
            max_reachable = current_new_val + (new_dice_left * sides)
            val_too_high = min_reachable > target
            val_too_low = max_reachable < target

            if val_too_high:
                break

            if not val_too_low:
                possibility_count += test_possibilities(
                    current_new_val, new_dice_left, sides, target, 0, known_outcomes, depth+1
                )
                if known_outcomes.get(new_dice_left, None):
                    known_outcomes[new_dice_left].update({current_new_val: possibility_count})
                else:
                    known_outcomes.update({new_dice_left: {current_new_val: possibility_count}})
    # print(f'depth: {depth}, p_count: {possibility_count}')
    return possibility_count


def probability(dice_number, sides, target):
    possibilities_total = sides**dice_number
    possibility_count = 0
    current_val = 0

    known_outcomes = {'': {'': ''}}  # TODO: store known outcomes at (value sum at dice number)

    valid_possibilities = test_possibilities(current_val, dice_number, sides, target, possibility_count, known_outcomes)
    print(f'v: {valid_possibilities}')
    probability_chance = round(valid_possibilities / possibilities_total, 4)
    print(f'p= {probability_chance}')
    return probability_chance
