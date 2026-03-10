"""
It's a Pokemon battle! Your task is to calculate the damage that a particular move would do using the following formula (not the actual one from the game):

damage = 50 * (attack / defense) * effectiveness
Where:
attack = your attack power
defense = the opponent's defense
effectiveness = the effectiveness of the attack based on the matchup (see explanation below)

Effectiveness:
Attacks can be super effective, neutral, or not very effective depending on the matchup. For example, water would be super effective against fire, but not very effective against grass.
Super effective: 2x damage
Neutral: 1x damage
Not very effective: 0.5x damage

To prevent this kata from being tedious, you'll only be dealing with four types: fire, water, grass, and electric. Here is the effectiveness of each matchup:

fire > grass
fire < water
fire = electric
water < grass
water < electric
grass = electric

For this kata, any type against itself is not very effective.
Also, assume that the relationships between different types are symmetric (if A is super effective against B, then B is not very effective against A).

The function you must implement takes in:

your type
the opponent's type
your attack power
the opponent's defense
"""


def calculate_damage(your_type, opponent_type, attack, defense):
    super_effective = [("fire", "grass"), ("water", "fire"), ("grass", "water"), ("electric", "water")]
    not_effective = [("grass", "fire"), ("fire", "water"), ("water", "grass"), ("water", "electric")]

    if (your_type, opponent_type) in super_effective: # checks the type matchup in the list
        effectiveness = 2
    elif (your_type, opponent_type) in not_effective or your_type == opponent_type:
        effectiveness = 0.5
    else: # assumes neutral otherwise
        effectiveness = 1

    damage = 50 * (attack / defense) * effectiveness
    return damage


print(calculate_damage("fire", "water", 100, 100))