# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


image bg apartment03 = im.Scale("bgs/ApartmentRoom03.png",1920,1080)
# The game starts here.

label start:

   
    play music "audio/music/BattleTheme.wav"

    scene bg apartment03
    with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Taka coco1 at better_left
    show Charmin rere1 at better_right
    t "Hmph, so what exactly are you...?"
    show Charmin anan1 at better_right
    c "I’m a being of absolute power! Something that. . . um? Actually what the hell are you?" 
    t "I am a Nephilim?"
    c "Uhh... and that is...?"
    t "It’s the inbreed between an angel and demon. I thought for a moment there you were well educated," 
    extend "but I assume too highly of you."
    c "You take that back you damn brick house hussy!"
    t "Oh! This coming from the “being of absolute power!” My apologizes, clearly I over stepped in the face of such an amazing being! Obviously I’m quaking in fear of toilet paper mummy!"
    c "Oh that is it!!! If it’s roasting you want bitch, I’ll bring it down on you hard!"
    show Taka smsm1 at better_left
    t "Really. . .? What could you possibly say that would unhinge me?"
    show Charmin wiwi1 at better_right
    c "For starters, you are the type of Hoe that would hide behind their “I’m the cool and mysterious type” but in reality,"
    c "... you're just sad little girl who thinks their edgy when wearing black."
    show Taka anan1 at better_left
    c "Oh, and don’t get me started on the “I can wield light and darkness, and look like a total badass with a giant sword” because, honey"
    c "...you make literally zero sense! I mean seriously, you're like some sort of Horny Teenager’s OC. Let me guess your backstory, "
    extend " “My parents are dead, and I fight for everyone freedom” ya-da-ya bullshit."
    t "Well, looks like bitch is going to die tonight..."
    "The Battle rages on, as Apollo sits back eating popcorn watching the entire fight."

    # This ends the game.

    return
