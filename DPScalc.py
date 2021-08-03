import math
import configparser
import argparse

class skilltable:
    skills = {
        "Attack Boost": 0,
        "Critical Eye": 0,
        "Maximum Might": 0,
        "Weakness Exploit": 0,
        "Critical Boost": 0,
        "Resuscitate": 0,
        "Resentment": 0,
        "Dragonheart": 0,
        "Level 2 slots": 0,
    }

    a = 2

    def __add__ (self,other):
       return( self.a + other.a)




def parseini(file):
    # TODO: Validate inputs
    config = configparser.ConfigParser()
    config.sections()
    config.read(file)

    skills = {
        "Attack Boost": int(config['Skills']['Attack Boost']),
        "Critical Eye": int(config['Skills']['Critical Eye']),
        "Maximum Might": int(config['Skills']['Maximum Might']),
        "Weakness Exploit": int(config['Skills']['Weakness Exploit']),
        "Critical Boost": int(config['Skills']['Critical Boost']),
        "Resuscitate": int(config['Skills']['Resuscitate']),
        "Resentment": int(config['Skills']['Resentment']),
        "Dragonheart": int(config['Skills']['Dragonheart']),
        "Level 2 slots": int(config['Skills']['Level 2 slots '])
    }

    weapon = {
        "Raw Attack": int(config['Weapon']['Raw Attack']),
        "Raw Affinity": int(config['Weapon']['Raw Affinity']),
    }

    # Parse weapon sharpness
    if config['Weapon']['Sharpness'] == 'white':
        weapon['sharpness'] = 1.32
    elif config['Weapon']['Sharpness'] == 'blue':
        weapon['sharpness'] = 1.2
    elif config['Weapon']['Sharpness'] == 'purple':
        weapon['sharpness'] = 1.39
    elif config['Weapon']['Sharpness'] == 'green':
        weapon['sharpness'] = 1.05

    return skills, weapon


def rawattack(skills, weapon):
    Attack = 0

    # Attack Boost is applied first:

    if skills["Attack Boost"] < 4:
        Attack = weapon["Raw Attack"] + skills["Attack Boost"] * 3
    elif skills["Attack Boost"] == 4:
        Attack = math.floor(weapon["Raw Attack"] * 1.05) + 7
    elif skills["Attack Boost"] == 5:
        Attack = math.floor(weapon["Raw Attack"] * 1.06) + 8
    elif skills["Attack Boost"] == 6:
        Attack = math.floor(weapon["Raw Attack"] * 1.08) + 9
    elif skills["Attack Boost"] == 7:
        Attack = math.floor(weapon["Raw Attack"] * 1.1) + 10

    # Dragonheart multiplies Attack Boost but does not multiply any other modifiers

    if skills["Dragonheart"] == 4:
        Attack = math.floor(Attack * 1.05)
    elif skills["Dragonheart"] == 5:
        Attack = math.floor(Attack * 1.10)

    # Apply flat modifiers:
    if 0 < skills["Resuscitate"] < 3:
        Attack += skills["Resuscitate"] * 5
    elif skills["Resuscitate"] == 3:
        Attack += 20

    Attack += skills["Resentment"] * 5

    # +15 from powercharm + powertalon
    Attack += 15

    return Attack


def CEaffinity(CE):
    if CE < 7:
        return CE * 5
    elif CE == 7:
        return 40


def WEXaffinity(WEX):
    if WEX < 3:
        return WEX * 15
    elif WEX == 3:
        return 50


def affinitymod(skills, rawaffinity):
    affinity = rawaffinity + CEaffinity(skills["Critical Eye"]) + WEXaffinity(skills["Weakness Exploit"]) + 10 * skills[
        "Maximum Might"]

    if affinity > 100:
        affinity = 100

    return 1 + (affinity / 100) * (0.25 + 0.05 * skills["Critical Boost"])


def totalefr(skills, weapon):
    return math.floor(weapon["sharpness"] * rawattack(skills, weapon) * affinitymod(skills, weapon["Raw Affinity"]))

sample = skilltable()

'''
def searchskillset(spareskills,skillsetindex):
    #If all skill slots are used up, return immediately.
    #result is a list of skilltables
    if spareskills == 0:
        return None

    #if the skillsetindex is now a greater value the list of valid skills, return immediately.
    if skillsetindex > numberofvalid skills:
        return None



    #If skill slots are not 0, call spareskills on the next skill in the queue.
    result =[]
    for i in range(spareskills+1):
        possibleresult = searchskillset()

        if possibleresult

        result.extend(searchskillset(result)
'''

'''
def optimizeefr(skills,weapon):
    #First step: produce a list of dictionaries containing all possible skills.
    #Skills will be formatted as shown in the parseini file.

    possibleskills, skillboosts = allpossibleskills(skills,weapon)

'''
def main(args):
    skills, weapon = parseini(args.file)

    print("The effective raw damage of the build is:")
    print(totalefr(skills, weapon))

    if ((args.optimize == 'y') and (skills["Level 2 slots"] > 0)):
        print("Optimizing DPS with spare level 2 skill slots...")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tool for Calculating Effective Raw for Monster Hunter Rise')
    parser.add_argument('--file',
                        type=str,
                        help='the .ini file that is used to calculate the effective raw. default = weapon.ini',
                        default='weapon.ini')
    parser.add_argument('--optimize',
                        type=str,
                        help='argument that checks if extra skill slots in the build should be used to optimize dps (y/n). default = y',
                        default='weapon.ini')
    main(parser.parse_args())
