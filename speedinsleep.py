from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n----------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    death_says = [
        "Your death will not be remembered. You suck.",
        "Enjoy your death.",
        "FAILURE",
        "No more worries for you. You dead."
    ]

    def enter(self):
        print(Death.death_says[randint(0,len(self.death_says)-1)])
        exit(1)

class CentralAvenue(Scene):

    def enter(self):
        print("""
            You wake up behind the steering wheel of red convertible.
            The needle in the dashboard marks 140mph and your hands
            seem to be covered in white fur and red blood stains. A metallic
            taste runs through your mouth and you feel dizzy. The summer air
            fills your lungs and you feel somwhat dizzy. 'W- W- What has happened to me?'
            The image of a furry white rabbit is reflected in your top mirror ...
            """)

        action = input("\nkeep driving\nstop\nturn on radio\n>")

        if action == "keep driving":
            print("""
            After a few seconds, with the right corner of your eye, you catch a sign of a gas station at about 3km.
            """)
            return 'the_gas_station'
        elif action == "stop":
            print("""
            The car slowly decelerates and after successfully coming to a complete stop, you get out.
            The scenery is beautiful! Palm trees, sandy coastlines as far as the eyes can see...Mmmmm...
            You fail to see a vicious rattlesnake crawling behind you. It leaps and stings your right buttcheek.
            """)
            return 'death'
        elif action == "turn on radio":
            print("""
            80s synthwave music blasts through the speakers and a blissful relaxation takes over.
            '-I would give anything for a cocktail right now, hah'. As the wheels keep on
            rolling, you hear a warm radio voice calling onto you...
            '-Hey there, do YOU want to have the thrill of your LIFE?'
            '-Of course I do!!', you hear yourself yelling.
            '-Well, since you asked for it...'
            ...You notice a faint ticking sound...
            .....KABOOSH!!!""")
            return 'death'
        else:
            print("""
            NO.""")
            return 'central_avenue'


class TheGasStation(Scene):
    def enter(self):
        print("""
            You slowly drive in the station, park the car and go out to ask for directions and a bathroom key.
            '-I must get something to eat too...', your inner voice whispers.
            '-Howdy, partner...Can I have a little chat with ye?', a policeman asks while stepping out of his cop car.
            '-Yes, of course, officer...W-What would you like to know?'
            '-I was wondering where are you heading to, this lovely mornin ?'
            His colleague remains seated inside and has his gaze fixed upon you.
            Cold sweat runs down your hairy back.
            """)


        action = input("\nrun\njump to car\ntell joke\n>")

        if action == "run":
            print("""
            The copper draws his gun and two shots are fired.
            You stumble and fall down to the ground.
            You feel tired and somewhat sleepy""")
            return 'death'
        elif action == "jump to car":
            print("""
            The copper draws his gun and you jump into the driver's seat.
            The engine revs and you speed off. You hear two shots fired and
            the screeching tires of the cop car.
            Both cars speed down the hot asphalt like bullets.
            Your heart races and you get sick in the stomach.""")
            return 'the_quarry'
        elif action == "tell joke":
            print("""
            '-You think it's all joke to ya, huh? Put yer hands on yo head an' kiss the earth, punk!'
            Immediately you freeze and drop as a log to the ground.
            '-Don't move a muscle bud. We had a call earlier bout a killer rabbit
            in a red convertible... Where do you keep the freaking body?'
            '-I..I don\'t k-know what you\'re talking about...s-s-sir'
            '-ANSWER ME AND PLAY NO GAMES WITH ME BOI!'
            You mumble incoherent words, failing to articulate anything to the cop.
            '-Hey, Mark open the truck for me will ya? Now we'll see what mess you've made...'
            '-It/'s here, Ethan...Yep, it's a dead body, alright...OOof.. the smell! I might throw up...Bleeergh'
            '-Get a grip of yo' self! Damn it, Mark...'
            What lead to this thing? Why are you a bunny? What is your name? How did this all get started?
            ...Everything spins and you lose consciousness...
            """)
            return 'death'
        else:
            print("""
            NO.""")
            return 'the_gas_station'

class TheQuarry(Scene):

    def enter(self):
        print("""
            The convertible leaves the cops behind several meters before making a right turn.
            An abandoned quarry fills your vision... something rings a bell...you seem to
            be familiar with this place for a strange reason. You pull the handbrake.""")

        action = input("\nopen glove compartment\nopen trunk\nturn on radio\n>")

        if action == "open glove compartment":
            print("""
            Driver's license, chewing gum, a revolver with three bullets in its chambers.
            You stash it in your pocket...Wait you have no pockets!!You are a furry
            little bunny! Hahah -Ok,no time for jokes - What is my name? - Nevermind, I will figure
            this later...
            Oh, snap! The cops found you!
            You hear the siren wailing and without a second thought
            your foot is on the gas.
            """)
            return 'the_end_of_the_road'
        elif action == "open trunk":
            print("""
            As soon as the car stops, you hear a thump from behind. There must be something
            in the trunk. You look around . No sign of the police. You turn the lever
            only to find a blood soaked orange fur of a motionless fox.
            'AAhhh shmaw! This can't be happening to me, darn it!'.
            Your trembling fingers check for pulse. Cold as ice and stiff as wood...
            Who is that? Strapped in the fox's waist there is a fanny pack.Inside it, you
            find a business card that writes :
            'How far would anger get you?'
            ...
            '-Have I really killed someone?'
            You fall on your knees... warm tears stream down your cheeks...
            You feel your heart fluttering...
            """)
            return 'death'
        elif action == "turn on radio":
            print("""
            You hear someone laughing...
            '-HAHAHAHAHAAHAH...Did you really think you would escape without a scratch?'
            '-But, how do you kn-'
            ....BABOOOM!!...
            """)
            return 'death'
        else:
            print("""
            NO.""")
            return 'the_quarry'

class TheEndOfTheRoad(Scene):

    def enter(self):
        print("""
            You find a narrow road leading to the high way.
            Pedal to the metal. Now it's time for action!
            Behind you the cop car makes progress and the constant
            siren sound gets your adrelanine pumpin'
            """)

        action = input("\nshoot\nkeep driving\nstop car\n>")

        if action == "shoot":
            print("""
            Turning around you pull the trigger thrice...
            Pow! - Miss
            Pow! - Miss
            Pow! - Tire!
            The chasing car goes spinning and you raise arms in the air!
            '-Woohoo!'
            All of a sudden, your body slams the seat and you hear this awful sound
            of metals connecting.
            '-Shmawzaw,I did not see that comin\'...'
            The red car flies with the ocean as a destination.
            '-Am I dreaming?...I never pinched myself...'
            SPLAAASSHH!
            """)
            return 'death'
        elif action == "keep driving":
            print("""
            You see a humongous road sign, saying \'END OF ROAD\'
            You hear the cop car smashing the breaks.
            '-Hah, losers!'
            You get a tight grip of the steering wheel and BLAMO!
            '-Wooooo... I\'m flying suuuuckers!!'
            SPLOOOSH!
            """)
            return 'death'
        elif action == "stop car":
            print("""
            Your foot suddenly steps on the brakes .The car behind you
            doesn\'t follow your example and comes running to your rear at
            tremendous speed...
            BOOOOMMM!!
            Both cars go up in flames.
            """)
            return 'death'
        else:
            print("""
            NO.""")
            return 'the_end_of_the_road'

class Map(object):

    scenes = {
        'central_avenue': CentralAvenue(),
        'the_gas_station': TheGasStation(),
        'the_quarry':TheQuarry(),
        'the_end_of_the_road':TheEndOfTheRoad(),
        'death':Death()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_avenue')
a_game = Engine(a_map)
a_game.play()
