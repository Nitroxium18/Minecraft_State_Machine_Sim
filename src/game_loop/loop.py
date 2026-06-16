def tick_state(state):
    # iterate over hunger each hour & increment dict
    state["hour"] += 1
    state["hunger"] += 3 
    
    # hunger decreses hourly, per day decrement = n * 24
    if state["hunger"] >= 90:
            state["hp"] -= 6 
    elif state["hunger"] >= 70:
            state["hp"] -= 3 
    elif state["hunger"] >= 40:
            state["hp"] -= 1

    # cap to prevent negatives
    max_hp = 100
    state["hp"] = max(0, min(state["hp"], max_hp))
    state["hunger"] = max(0, min(state["hunger"], 100))

# for testing only
def run_sim(state):
    # end day -> stats show -> increment day
    while state["hp"] > 0:
        # day ends
        tick_state(state)
        # day progression stats
        if state["hour"] % 24 == 0 and state["hp"] != 0 and state["hour"] > 0:
            print (f"You survived day {state['day']}. Hunger level: {state['hunger']}. Health: {state['hp']}")
        # day increments
        if state["hour"] % 24 == 0:
            state["day"] += 1

    # note: this isn't a dual death state, death is purely based on HP
    completed_days = state['hour'] // 24
    remaining_hours = state["hour"] % 24

    if state["hunger"] >= 100:
        print (f"You starved to death. You survived for {completed_days} days & {remaining_hours} hours") 
    else:
        print(f"You ran out of HP. You survived for {completed_days} days & {remaining_hours} hours")

if __name__ == "__main__":
    state = {"hp": 100, "hunger":0, "hour":0, "day":1}
    run_sim(state)
