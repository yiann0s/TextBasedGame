from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter().0"
        exit(1)


class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n----------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    death_says = [
        "Your death will not be remembered. You suck."
        "Enjoy your death."
        "FAILURE"
        "No more worries for you. You dead."
    ]

    def enter(self):
        print Death.death_says[randint(0,len(self.death_says)-1)]
        exit(1)

class CentralAvenue(Scene):

    def enter(self):
        print "You wake up behind the steering wheel of red convertible."
        print "The needle in the dashboard marks 140mph and your hands"
        print "seem to be covered in white fur and red blood stains. A metallic"
        print "taste runs through your mouth and and you feel dizzy. The summer air"
        print "fills your lungs and you feel somwhat dizzy. 'W- W- What has happened to me?'"
        print "The image of a furry white rabbit is reflected in your top mirror ..."

        action = raw_input("> ")

        if action == "keep driving":
            print "After a few seconds, with the right corner of your eye, you catch a sign of a gas station at about 100km."
            return 'the_gas_station'
        elif action == "stop":
            print "The car slowly decelerates and after successfully coming to a complete stop, you get out."
            print "The scenery is beautiful! Palm trees, sandy coastline as far as the eyes can see...Mmmmm..."
            print "A vicious rattlesnake crawls behind you.  You feel a sudden sting on your right buttcheek."
            return 'death'
        elif action == "turn on the radio"
            print "80s synthwave music blasts through your speakers and you forget everything."
            print "'-I would give anything for a cocktail right now,hah'. As the wheels keep on"
            print "spinning, you hear a warm radio voice calling onto you...'Hey there, do you want'"
            print "'to have a blast?'-Of course I do' you hear yourself yelling..."
            print "'Well, since you asked for it...'"
            print "You notice a faint ticking sound, nah it can't be..."
            print "KABOOSH!!!"
            return 'death'
        else:
            print "NO."
            return 'central_avenue'


class TheGasStation(Scene):
    def enter(self):
        print "You slowly drive in the station, park the car and go out to ask for directions and a bathroom key"
        print "'I must get something to eat too...', your inner voice whispers. 'Howdy, partner. Where you'"
        print "'heading to?', a policeman asks while stepping out of his cop car . His colleague has his eyes fixed"
        print "on your blue eyes and you feel cold sweat running down your hairy back."

        action = raw_input("> ")

        if action == "run":
            print "The copper draws his gun and three shots are fired."
            print "You stumble and fall down the ground.You feel tired and cold and sleepy"
            return 'death'
        elif action == "go to car":
            print "The copper draws his gun and you jumpo into you car's driver seat."
            print "The engine revs and you speed off. You hear two shots fired and the screeching tires of the "
            print "cop car. 'Shit, shit shiiiit' . Both cars speed down the hot asphalt like bullets while your "
            print "heart races and you feel sick in the stomach."
            return 'the_quarry'
        elif action == "tell a joke":
            print "'You think it's all joke to you, huh? Put your hands on your head and kiss the earth, punk!'"
            print "Immidiately you freeze and drop as a log in the ground. 'Don't you dare to move. We had a call'"
            print "'for a rabbit criminal. Where do you keep the freaking body?"
            print "'-I don\'t know what you\'re talking about'"
            print "'-ANSWER ME AND PLAY NO GAMES WITH ME BOI!'"
            print "'-I KNOW NOTHING'"
            print "'Hey, Mark open the truck for me will ya? Now we'll see you damn lunatic what mess you've made'"
            print "'It/'s here, Ethan. Oh I'm gonna throw up man.'.'-Get a grip of yourself dammit!'"
            print "But how, what lead to this thing, why I am a bunny?. Everything spins and you lose consiousness..."
            return 'death'
        else
            print "You can feel your veins drumming on your skull and your heart rate twindling out of control"
            print "You smell of burned toast and your eyelids are getting heavy"
            return 'death'

class TheEndOfTheRoad(Scene):

    def enter(self):
        print "You find a narrow road leading to the high way. Pedal to the metal and now it's"
        print "time for action! Behind you the cop car makes progress and "
        print "the constant siren's sound gets your adrelanine pumpin"

        action = raw_input("> ")

        if action == "open glove compartment"
            print "Driver's license, chewing gum, a revolver"
            print "It has three bullets in its chambers. Are you got at shooting?"
            print "What the heck... Turnign around you pull the trigger thrice."
            print "Miss, Miss, Tire! The chasing car goes spinning and you raise your arms"
            print "in the air! Woohoo! Your body slams the seat and you hear this awful sound"
            print "of metals connecting. 'Shmawzaw, there was a dead end..'"
            print "The red car flies with the ocean as a destination. '-Am i dreaming?'"
            print "'-I never pinched myself...'"
            return 'death'
        elif action == "keep driving"
            print "You see a humongous road sign, saying 'END OF ROAD'"
            print "You hear the cop car smashing the breaks. '-Hah, losers!'"
            print "You get a tight grip of the steering wheel and BLAMO!"
            print "'Wooooo... I'm flying suuuuckers!!"
            return 'death'
        elif action == "stop car"
            print "Your foot suddenly steps on the brakes .The car behind you"
            print "doesn't follow your example and comes running to your rear at"
            print "flashing speed...BOOOOMMM!! Both cars go up in flames"
            return 'death'
        else
            print "NO."
            return 'the_end_of_the_road'

class TheQuarry(Scene):

    def enter(self):
        print "The convertible leaves the cops behind several meters before making a right turn."
        print "An abandondoned quarry fills your vision. Something rings a bell, you seem to "
        print "be familiar of this place for a strange reason. You pull the handbrake"

        action = raw_input("> ")

        if action == "open glove compartment"
            print "Driver's license, chewing gum, a revolver"
            print "It has three bullets in its chambers. You stash it in your pocket...Wait you have no pockets!!You are"
            print "a furry little bunny!Hah - Ok no time for jokes - What is my name? - Nevermind we will figure this later"
            print "'Oh, snap!'. The cops found you! You hear the siren wailing and storm out screaming."
            return 'the_end_of_the_road'
        elif action == "open trunk"
            print "As soon as the car stops, you hear a thump from behind. There's something"
            print "in the trunk. You look around . No sign of the police. You turn the lever"
            print "only to find a blood soaked orange fur of a motionless fox."
            print "'AAhhh shmaw! This can't be happening to me, darn it!'. Your trembling"
            print "fingers check for pulse. Cold as ice and stiff as wood. Who is that?"
            print "You look out for clues. Strapped in the fox's waist there is a fanny pack."
            print "Inside you find a white business card that writes :"
            print "'How far would anger get you?' You fall down your knees gasping for air while"
            print "tears of sadness stream down your cheeks. You feel your heart fluttering"
            return 'death'
        else
            print "NO."
            return 'the_quarry'



class Map(object):

    def __init__(self,start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_avenue')
a_game = Engine(a_map)
a_game.play()
