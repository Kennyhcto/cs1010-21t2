# PyGame (and Game Concepts)

## Demo Summary


| # | Description |
|---|---|
| 1-0 | Display Frankie on the screen |
| 1-1 | Fullscreen mode |
| 2 | Increase Frankie's size and change location |
| 3 | Control Frankie's location using the arrow keys |
| 4 | Make Frankie unable to fall off the screen |
| 5 | Put other walls up so Frankie has to walk around them |
| 6 | Have Frankie change or walls change without user input (introduction to the clock) |
| 7-0 | Flappy Frankie introduction. Moving up and down based on space bar. |
| 7-1 | Draw pipes. |
| 7-2 | Many pipes. |
| 7-3 | Pipes that move up and down. |
| 7-4 | End of game based on collision with pipes. |


## Game Loop (animation) (demo 3 onwards)

Draw, update, repeat.

## Scanning for inputs (demo 3 onwards)

## Clock (demo 6 onwards)
clock.tick(frames) -- maximum number of frames per second. A low number your game will run slower, a high number your game will run fast.

## Flappy Frankie (demo 7 onwards)

Basically making this game: https://flappybird.io/

## State Machine (demo 7 onwards)

In our example:

Start: Paused Frankie, at the left of the screen, in the centre, ready to go. Pressing 'Space' moves us to the 'Playing' state.
Playing: The pipes are moving, and when we press 'Space' it changes Frankie's acceleration. When we collide with pipes, we move into the 'Dead' state.
Dead: Everything is still. The user gets to see how they died. Pressing 'Space' moves us back to the 'Start' state (resets the screen and waits for the user to press 'Space' to indicate they're ready to play again.)

