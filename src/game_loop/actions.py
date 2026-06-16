# this must contain only the functions which are to be exported to main.py via __init__.py packaging

"""
Action modifiers:
rest: small HP regen, no extra hunger
eat: reduce hunger, no HP change
gather: + hunger penalty (because effort)
mine: ++ hunger penalty (hard effort)
"""
# For future: make consumptions dynamic (more than 1 at a time)

ActionResult = {"consume_turn": True, "message":"You rested and recovered 5 HP","events": []}

def rest(state):
    state['hp'] += 5
    return {'consume_turn':True, 'message':"You rested and recovered 5 HP"}

def eat(state,item=None):
    inv = state['inv']
    if item not in inv or inv[item] <= 0:
        return {'consume_turn': False ,'message':f"No {item} left in neventory."}
    inv[item] -= 1
    state['hunger'] -= 5 # net effect for 5 is still 2 since tick_state will add 3 hunger immediately 
    return {'consume_turn': True, 'message':f'You ate {item} & feel satisfied'}

def mine(state, item=None):
    inv = state['inv']
    inv[item] = inv.get(item, 0) + 1
    state['hunger'] += 5
    return {'consume_turn': True, 'message':f'You mined {item} & feel hungry'}

def gather(state,item=None):
    state['hunger'] += 2
    inv = state["inv"]
    inv[item] = inv.get(item, 0) + 1
    return {'consume_turn': True, 'message':f'You collected {item} & feel hungry'}

def status(state):
    return {'consume_turn': False, 'message':f"Your current stats: {state}"}

def get_help(state):
    return {'consume_turn': False, 'message':"Rest to increase 5 HP. Eat to reduce 5 hunger. Mining costs 5 hunger. Gathering costs 2 hunger. Use command 'status' to check your stats"}


