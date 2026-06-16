"""
Print status after every turn
Ask user input after each turn
Define basic actions (mine, eat .etc)
Call tick_status(state) & update stauts based on the actions & display updated stats after each action
Repeat until dead (either HP or starved)
"""
from game_loop import tick_state, rest, eat, mine, gather, status, get_help

state = {"hp": 100, "hunger": 0, "hour": 0, "day": 1, "inv": {"apple": 2, "stone": 2}}

commands = {'rest':rest, 'eat':eat, 'mine':mine, 'gather':gather, 
            'status':status, 'help': get_help}
needs_item = {"eat", "mine", "gather"}


# tick_state(state)

"""
while state["hp"] > 0:
    read input
    normalize input
    handle empty input
    parse into command and maybe item

    validate command exists
    validate item if required

    dispatch action
    print result message

    if result says consume turn:
        tick_state(state)
        handle day rollover
        handle death
"""

while state["hp"] > 0:
    # parser
    ui = input("What do you want to do this turn? ")
    ui = ui.strip().lower()

    if ui == "":
        print("No action was passed")
        continue

    parts = ui.split()
    cmd = parts[0]
    item = parts[1] if len(parts) > 1 else None

    # validator
    if cmd not in commands:
        print("Invalid action selected.")
        continue

    if cmd in needs_item and item is None:
        print(f"{cmd} needs an item.")
        continue

    if cmd not in needs_item and item is not None:
        print(f"{cmd} does not take an item.")
        continue

    # dispatcher
    if item is None:
        result = commands[cmd](state)
    else:
        result = commands[cmd](state, item)

    print(result["message"])

    if result["consume_turn"]:
        tick_state(state)
        print(status(state)["message"])

        if state["hour"] % 24 == 0:
            print(f"You survived day {state['day']}. Hunger level: {state['hunger']}. Health: {state['hp']}")
            state["day"] += 1

        if state["hp"] <= 0:
            completed_days = state["hour"] // 24
            remaining_hours = state["hour"] % 24

            if state["hunger"] >= 100:
                print(f"You starved to death. You survived for {completed_days} days & {remaining_hours} hours")
            else:
                print(f"You ran out of HP. You survived for {completed_days} days & {remaining_hours} hours")
