init:
    
    
    #Defining Characters
    define t = Character('Taka',color="#f4f7fc", callback=speaker("t"),what_prefix='"', what_suffix='"')
    define c = Character('Charmin',color="#f4f7fc",callback=speaker("c"),what_prefix='"',what_suffix='"')
    ##base blush variable
    $ t_blush = False
    
    #Taka's Emotions TAG: TAKA EMOTIONS FOR SEARCH
   
   #Cold Eyes, Cold Mouth 1 
    image Taka coco1 = LiveComposite(
        (291,618),
        (0,0),"char/taka/body.png",
        (0,0),"char/taka/Cold/cold_0000s_0000_eyebrows.png",
        (0,0),"Taka Eyes Cold",
        (0,0),WhileSpeaking("t","Taka Mouth Cold","char/taka/Cold/cold_0000s_0004_mouth.png"),
        (0,0),ConditionSwitch(
            "t_blush == True","char/taka/blush.png",
            "t_blush == False","blank.png"))
    #Angry eyes, angry mouth 1            
    image Taka anan1 =   LiveComposite(
        (291,618),
        (0,0),"char/taka/body.png",
        (0,0),"char/taka/Angry/enraged_0000s_0000_eyebrows.png",
        (0,0),"Taka Eyes Angry",
        (0,0),WhileSpeaking("t","Taka Mouth Angry","char/taka/Angry/enraged_0000s_0004_mouth.png"),
        (0,0),ConditionSwitch(
            "t_blush == True","char/taka/blush.png",
            "t_blush == False","blank.png"))         
    #Smile eyes, Smile mouth 1            
    image Taka smsm1 =   LiveComposite(
        (291,618),
        (0,0),"char/taka/body.png",
        (0,0),"char/taka/Smile/smile_0000s_0000_eyebrows.png",
        (0,0),"Taka Eyes Smile",
        (0,0),WhileSpeaking("t","Taka Mouth Smile","char/taka/Smile/smile_0000s_0004_mouth.png"),
        (0,0),ConditionSwitch(
            "t_blush == True","char/taka/blush.png",
            "t_blush == False","blank.png"))              
               
               
    #Building Taka Eyes
    
    image Taka Eyes Cold:
        "char/taka/Cold/cold_0000s_0001_eyes.png"
        choice:
            2.0
        choice:
            3.1
        choice:
            4.2
        choice:
            3.3
        "char/taka/eyesclosed.png"
        .13
        repeat
    image Taka Eyes Angry:
        "char/taka/Angry/Enraged_0000s_0001_eyes.png"
        choice:
            2.0
        choice:
            3.1
        choice:
            4.2
        choice:
            3.3
        "char/taka/eyesclosed.png"
        .13
        repeat

    image Taka Eyes Smile:
        "char/taka/Smile/smile_0000s_0001_eyes.png"
        choice:
            2.0
        choice:
            3.1
        choice:
            4.2
        choice:
            3.3
        "char/taka/eyesclosed.png"
        .13
        repeat
               
    #Building Taka Mouths
    
    
    image Taka Mouth Cold:
        "char/taka/Cold/cold_0000s_0002_mouth.png"
        .2
        "char/taka/Cold/cold_0000s_0003_mouth.png"
        .2
        "char/taka/Cold/cold_0000s_0004_mouth.png"
        .2
        repeat
        
    image Taka Mouth Angry:
        "char/taka/Angry/Enraged_0000s_0002_mouth.png"
        .2
        "char/taka/Angry/Enraged_0000s_0003_mouth.png"
        .2
        "char/taka/Angry/Enraged_0000s_0004_mouth.png"
        .2
        repeat
    
    image Taka Mouth Smile:
        "char/taka/Smile/smile_0000s_0002_mouth.png"
        .2
        "char/taka/Smile/smile_0000s_0003_mouth.png"
        .2
        "char/taka/Smile/smile_0000s_0004_mouth.png"
        .2
        repeat
             
             
             
    #Charmin's Emotions TAG: Charmin  EMOTIONS FOR SEARCH
             
    #Charmin Angry eyes Angry mouth 1 
    image Charmin anan1 = LiveComposite(
        (291,618),
        (0,0),"char/charmin/body.png",
        (0,0),"char/charmin/Angry/Enraged_0000s_0000_eyebrows.png",
        (0,0),"Charmin Eyes Angry",
        (0,0),WhileSpeaking("c","Charmin Mouth Angry","char/charmin/Angry/Enraged_0000s_0004_mouth.png"),
        (0,0),ConditionSwitch(
            "t_blush == True","char/charmin/blush.png",
            "t_blush == False","blank.png"))
    
    
      #Charmin Relieved eyes Relieved mouth 1 
    image Charmin rere1 = LiveComposite(
        (291,618),
        (0,0),"char/charmin/body.png",
        (0,0),"char/charmin/Relieved/Eyebrows_0000s_0000_Layer-57.png",
        (0,0),"Charmin Eyes Relieved",
        (0,0),WhileSpeaking("c","Charmin Mouth Relieved","char/charmin/Relieved/Mouth_0000s_0004_mouth1-3-2.png"),
        (0,0),ConditionSwitch(
            "t_blush == True","char/charmin/blush.png",
            "t_blush == False","blank.png")) 

     #Charmin Wiseguy eyes Wiseguy mouth 1 
    image Charmin wiwi1 = LiveComposite(
        (291,618),
        (0,0),"char/charmin/body.png",
        (0,0),"char/charmin/Wiseguy/Eyebrows_0000s_0000_Layer-54.png",
        (0,0),"Charmin Eyes Wiseguy",
        (0,0),WhileSpeaking("c","Charmin Mouth Wiseguy","char/charmin/Relieved/Mouth_0000s_0004_mouth1-3-2.png"),
        (0,0),ConditionSwitch(
            "t_blush == True","char/charmin/blush.png",
            "t_blush == False","blank.png")) 
     
     
     #Building Charmin Eyes        
         
    image Charmin Eyes Angry:
        "char/charmin/Angry/enraged_0000s_0001_eyes.png"
        choice:
            2.0
        choice:
            3.1
        choice:
            4.2
        choice:
            3.3
        "char/charmin/eyesclosed.png"
        .13
        repeat 
     
    image Charmin Eyes Relieved:
        "char/charmin/Relieved/Eye_0000s_0001_eyes.png"
        choice:
            2.0
        choice:
            3.1
        choice:
            4.2
        choice:
            3.3
        "char/charmin/eyesclosed.png"
        .13
        repeat 
    image Charmin Eyes Wiseguy:
        "char/charmin/Wiseguy/Eye_0000s_0001_Base-Colors-for-Angry-Face-Copy-2.png"
        choice:
            2.0
        choice:
            3.1
        choice:
            4.2
        choice:
            3.3
        "char/charmin/eyesclosed.png"
        .13
        repeat 
     
     #Building Charmin Mouth
 
    image Charmin Mouth Angry:
        "char/charmin/Angry/Enraged_0000s_0002_mouth.png"
        .2
        "char/charmin/Angry/Enraged_0000s_0003_mouth.png"
        .2
        "char/charmin/Angry/Enraged_0000s_0004_mouth.png"
        .2
        repeat
         
    image Charmin Mouth Relieved:
        "char/charmin/Relieved/Mouth_0000s_0002_Layer-1.png"
        .2
        "char/charmin/Relieved/Mouth_0000s_0003_Layer-65.png"
        .2
        "char/charmin/Relieved/Mouth_0000s_0004_mouth1-3-2.png"
        .2
        repeat  
    image Charmin Mouth Wiseguy:
        "char/charmin/Wiseguy/Mouth_0000s_0002_Layer-60.png"
        .2
        "char/charmin/Wiseguy/Mouth_0000s_0003_Layer-59.png"
        .2
        "char/charmin/Wiseguy/Mouth_0000s_0004_mouth1.png"
        .2
        repeat
     
        
        
init -99 python:
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)