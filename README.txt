# ErebusEngine

Erebus:
"Primordial god of darkness."



------ CREATOR ------: 
Name: Stuart (illusion)



------ IMPORTANT ------:
Game configs are .json extensions only.

If you are placing a game config into the engine (manually moving / copying a file into the "ErebusEngine/config" file directory), remember to include a "start" stage (if you don't already have one) as this is the FIRST stage which is loaded on all game configs.

When creating a game config using the engine, it will automatically create the start stage for you so you don't have to worry about it.



------ COMMANDS ------:
Using commands within game configs can be done with the following:

1. #SLEEP -> implements a sleep(1) for each line (can't stack multiple on one line).

2. $LOAD_START$ -> used to load different stages within your game config (stages are the objects which contain messages and decisions. For example, every game config should have a "start" stage).



------ SETUP ------:
Heres how you can start using the ErebusEngine:

Download the ErebusEngine folder which contains all the necessary files for it to run.
Place the ErebusEngine folder into your python project.
Create a python file (outside of the ErebusEngine folder) and include the following lines:

1. import ErebusEngine.display.render as render
2. def main():
3.     render.Render().start_screen()
4. if __name__ == "__main__":
5.     main()

Finally, run your python file and enjoy.
