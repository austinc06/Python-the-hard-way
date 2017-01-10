from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #print out last scene_map
        current_scene.enter()


class Death(Scene):

    game_over = """
        Your journey ends here.
        A bag of water.
        Floating forever.
        """

    def enter(self):
        print(Death.game_over)
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print("""
        The derelict cruiser that crashed into your ship turned out to be full
        of husks. They have invaded your ship and killed your crew. You are the
        only survivor. You will need to get the neutron destruct bomb from the
        Weapons Armory, place it in the bridge, and blow the ship up after
        getting into an escape pod. \n
        You are running down the narrow central corridor to the Weapons Armory when
        you encounter a wandering husk. It is ghastly with its grey, pale skin,
        fluorescent blue vasculature visible underneath its dermal layer, and
        its dead blue eyes gazing into your soul. It gnashes its sharp teeth
        as it charges you. \n
        1. Dodge\n
        2. Shoot\n
        3. Charm it
        """)

        action = input("> ")

        if action == "1":
            print("""
            You dodge and weave trying to outmaneuver the husk to reach the room
            beyond it. However, the corridor is much narrower than you anticipated
            and the husk easily slams you into the wall. You bang your head against
            the metal bulkhead and lay on the ground, barely conscious. Thankfully
            you pass out as cold, jagged teeth bite into your neck.
            """)
            return 'death'

        elif action == "2":
            print("""
            You pull your blaster from its holster and take aim. A seasoned soldier,
            you have little trouble lining up your shot at the mindless creature.
            A single pull of the trigger later, the husk slides to a halt at your feet,
            half of its head missing from the kinetic missile you launched. You
            quickly move on, hoping the sound of your blaster didn't attract more
            attention.
            """)
            return 'laser_weapon_armory'

        elif action == "3":
            print("""
            Unfortunately, for all your smooth talking, you can't charm dead things.
            The husk ignores your pleas and bargains and slams you into the wall.
            You bang your head against the metal bulkhead and lay on the ground,
            barely conscious. Thankfully you pass out as cold, jagged teeth bite
            into your neck.
            """)
            return 'death'

        else:
            print("No action selected.")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("""
        You press yourself against the wall beside the door as you enter. It's
        dead quiet. Too quiet. You stand up and run to the far side of the room
        to find the neutron bomb in its container. There's a keypad lock on the
        box and you need the code to get the bomb out. Unfortunately, as per
        mandated by the Galactic Council, the keypad only unlocks when two authorized
        personnel present their bio-diagnostics at the same time, and your first
        mate was one of the first to fall to the husks. However, there is a
        randomized keycode, a remnant of a bygone era, that could also unlock
        the box. However, if you get the 3-digit code wrong 10 times, then the lock
        seals forever.
        """)

        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        guess = input("> ")
        guesses = 1

        while guess != code and guesses < 10:
            print("The light above the keycode blinks then flashes RED")
            guesses += 1
            guess = input("> ")

            if 3 > guesses >= 1:
                print(code[0])
            elif 9 > guesses >= 3:
                print(code[0:2])
            elif guesses == 9:
                print("Cheat", code[:])
            else:
                pass

        if guess == code:
            print("""
            The container clicks open and the seal breaks, releasing a blast of cool
            air. You grab the neutron bomb and run as fast as you can to the bridge.
            """)
            return 'the_bridge'
        else:
            print("""
            You hear the lock cycle and wait with baited breath. However, the light
            flashes RED once more and the pit of your stomach drops as you hear
            the mechano-fluid inside harden, sealing the box forever. In your
            despair, you fail to hear the sound of husks behind you until it's
            too late.
            """)
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print("""
        The neutron destruct bomb begins to whir dangerously now that it has
        been removed from its stabilization chamber. You know there is not much
        time left before the unstable reaction leads to a massive explosion.
        You burst onto the Bridge with the bomb under your arm
        to see 5 husks wandering around. They haven't noticed you yet, giving you
        a single moment to act as they begin to turn towards you.\n
        1. Throw the bomb and run \n
        2. Slowly place the bomb down \n
        """)

        action = input("> ")

        if action == "1":
            print("""
            In a panic, you throw the bomb at the husks and make a leap for the
            door. As the bomb leaves your fingers, you realize the insanity of your
            action. Sure enough, as the delicate munition makes contact with the
            metal flooring of your ship, the outer casing cracks. Blue energy flashes
            menacingly. The mindless husks charge you as you turn to run, but
            the ensuing surge of energy engulfs them, you, and everything in your
            vision.
            """)
            return 'death'
        elif action == "2":
            print("""
            Moving quickly and deliberately, you set the bomb right besides the door,
            knowing the mindless husks will ignore it and focus on you instead.
            Already the reaction within the bomb is already emitting blue light
            signifying the imminent end. You quickly turn and make a break for the
            escape pods as the husks charge after you. You have mere moments remaining;
            either the husks will get you or the neutron explosion will. That is,
            unless you can escape in the minutes ahead.
            """)
            return 'escape_pod'
        else:
            print("Not an action")
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print("""
        You rush through the ship, desperately trying to make it to the escape
        pod before the whole ship explodes. Fortunately, your path is clear of husks
        though the five behind you are quickly advancing. You get to the chamber with
        the escape pods only to realize some of them could have been damaged when
        your ship was rammed by the floating grave that carried the husks. Unfortunately,
        you don't have time to diagnose each pod. There are 3 pods, which one do you take?
        """)

        good_pod = randint(1,3)
        print("Cheat", good_pod)
        guess = input("> ")

        print("You jump into pod %s and hit the eject button." % guess)

        if int(guess) != good_pod:
            print("""The pod escapes out into the void of space. You begin to
            breathe a sigh of relief just as the emergency light begins to flash.
            You have one moment as your life flashes before your eyes as
            the damaged pod ruptures and your body explodes into the vacuum of
            space
            """)
            return 'death'
        else:
            print("""The pod escapes out into the void of space. You begin to
            breathe a sigh of relief just as your ship explodes into a brilliant
            blue-white ball of soundless fire. As your escape pod slips through
            the quiet of space, you give silently salute the fallen. You've won.
            """)
            return 'finished'

class Finished(object):
    def enter(self):
        print("You have survived.")
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
