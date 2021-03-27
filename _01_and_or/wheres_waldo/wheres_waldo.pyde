"""
Make a program where the user has to find Waldo!
"""

# =========== SOUND =================
# Some computers are unable to play sounds. 
# If you cannot play sound on this computer, set canPlaySounds to false.
# If you are not sure, ask your teacher 
can_play_sounds = False

def setup():
    # Find a Where's Waldo picture and drop it onto the sketch.    
    waldo = "waldo.jpg"
    # Change the line below to match your file name.
    
    # Use the size() function to set the width and height of your sketch
    size(800,600)
    # Resize your waldo picture to the same size as the sketch
    waldoimage = loadImage(waldo)
    waldoimage.resize(width,height)
    background(waldoimage)
    # Use the background() function to make the waldo image your
    # sketch background

    
    
def draw():
    # If the user presses the mouse...
    # *Hint* use the mousePressed variable
  if mousePressed:
      if mouseX < 550:
          if mouseX >500:
              if mouseY < 400:
                  if mouseY > 300:
                      text("Waldo Found!", mouseX,mouseY)
        # Use this print statement to help you find the location
        # of Waldo to use in the code below
    
        # Check if the location of the mouse is anywhere on the image of Waldo.
        # If it is, print “Waldo found!”  Use the text() command to write it
        # on the sketch.
          
            # Use the play_woohoo() method below.
        
        # However, if the mouse is not on Waldo, print "Not here!" 
        # Use the text() command to write it on the sketch.
          
            # Use the play_doh() method below.
pass     

# =================== This code is needed to play sounds. ===================
