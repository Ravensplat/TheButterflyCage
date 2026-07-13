label scene4:
    #SCENE 4
    scene bed_night with fade
    
    # Night-time bedroom bg.
    # All Lillian sprites in this scene should be the bedclothes edit but I don’t know what the shorthand for that is

    nrt "The thought you have been trying not to think all day is now impossible to ignore."
    nrt "The itch at the back of your skull, the pieces that don’t add up, the nagging wrongness that takes your wandering mind down roads you’d rather not walk, all of it comes to the forefront now."

    # nat_neutral_sideeye
    nth ne_sd "(I didn’t have that much to drink…)"

    nrt "No, you didn’t."
    # nat_neutral_sideeye
    nth ne_sd "(I never have that much to drink anyway. I do know my limits…)"

    nrt "Yes, you do."
    # nat_sad
    nth sa "(And I’ve never been drunk enough to wake up in anyone else’s bed with no memory of how I got there…)"

    nrt "No, you haven’t."
    play music "audio/ambient.mp3" loop fadein 3.0
    # nat_neutral_sideeye
    nth ne_sd "(…)"
    # nat_neutral
    nth ne"(It was… pretty weird that Lillian messaged my work for me, wasn’t it?)"
    # nat_sad
    nth sa"(And then didn’t give me my phone back all day…)"

    nrt "You thought so even at the time, but didn’t press the matter too much."
    # nat_neutral_sideeye
    nth ne_sd"(…)"
    # nat_sad
    nth sa"(And she keeps talking about me being here… like I’m gonna be here forever.)"

    nrt "Like she knew this was going to happen all along."
    # nat_sad_eyesclosed
    nth sa_ec"(I… don’t wanna finish this thought…)"

    nrt "But you have to."
    # nat_sad_eyesclosed
    nth sa_ec"(…)"
    # nat_sad
    nth sa "(Why did that water Lillian gave me… taste so weird…)"

    nrt "You know why."

    # Running water SFX

    nrt "You all but jump out of your skin at the sudden intrusion of noise."
    nrt "Truthfully, it’s nothing more than gentle running water. You don’t hear rain at the window, and the sound is coming from elsewhere in the flat. Lillian must be having a shower."

    # nat_angry
    nth ag"(Shit. Shit!)"
    # nat_dejected_smile
    nth dj_s"(No. I must be panicking. Lillian wouldn’t… That’s crazy why would I ever think that.)"
    # nat_shy_blush
    nth sh_bl"(She’s been so nice to me, and listened to me, and held me when I cried, and—)"

    nrt "Enjoyed the fact that you’ve been entirely dependent on her?"
    # nat_angry
    nth ag "(No!)"
    # nat_sad
    nth sa "(That’s not… She wouldn’t…?)"

    nrt "But it explains everything, doesn’t it?"
    nrt "Why else would Lillian pay you any attention at all? You’re nothing. You’ve always been nothing, and nowadays you’re even less than that."
    nrt "So what can you offer her except for the fact that you are nothing. To anybody. You have no friends, no hobbies. You never talk to your work colleagues, you never talk to your family."
    nrt "No one will even notice you’re missing."
    # nat_sad
    nth sa "(That’s ridiculous! I…)"

    nrt "When was the last time you spoke to your family, Natalie?"
    # nat_dejected_smile
    nth dj_s "(Um… Does the groupchat count?)"

    nrt "You think sending cry-laughing emoji reactions every few weeks to jokes you don’t even find funny counts? "
    # nat_angry
    nth ag_sd "(That’s not the point! I don’t need them to come rescue me, I don’t need rescuing!)"
    # nat_dejected_smile
    nth dj_sm "(I’m just being paranoid. Lillian’s been so lovely to me all day, and yesterday. All I’ve done is complain about my shitty life.)"

    nrt "That’s all you ever do, isn’t it? You offer her nothing. You didn’t even ask how she’d been doing yesterday before you launched into bitching about your own uselessness."
    nrt "You were meant to be her supervisor, and you didn’t even ask if she finished the degree you were meant to be helping her with. Were you going to get jealous of her too?"
    nrt "It makes you wonder what Lillian could possibly be getting out of this relationship to show you such care and support…"
    # nat_angry
    nth ag_sd "(Shut up!)"

    nrt "Did you think her care for you was genuine? That she would just whisk you away to her fairytale mansion, validate your every bitter complaint all day, love you unconditionally despite you offering no possible reason to do so?"
    nrt "Did you think you were anything more to her than an easy target?"
    # nat_sad
    nth sa "(No! I mean. That’s not—)"

    nrt "Oh, that’s what has you so distressed."
    nrt "Even by your standards, that’s pathetic."
    nrt "You’re not worried about the fact Lillian’s kidnapped you, you’re worried about the fact that she didn’t do it because she loves you?"

    # nat_annoyed
    nth an "(No, because Lillian hasn’t kidnapped me! That’s insane!)"
    # nat_apologetic
    nth ap "(Honestly, I owe her an apology for even acknowledging that.)"

    # Shower SFX stops
    # nat_sympathetic
    nth sy "(Perfect timing. I’m gonna go talk to her now, clear everything up, and then apologise for even thinking such ridiculous shit.)"

    stop music fadeout 1.5
    # nat_sympathetic
    nth sy"(When she’s been so nice to me all day, too!)"

    nrt "Suit yourself."

    # Footsteps SFX, very slow.

    nrt "You stand shakily from the bed, your legs cramping almost immediately from a day’s disuse. You could barely even sit up a few hours ago. Probably a side effect from whatever Lillian put in your drink to knock you out."
    # nat_annoyed
    nth an "(No she didn’t!)"

    nrt "Stumbling across the floor, you can’t help but think how easy it must have been for her. Sobbing into her shoulder like that, you weren’t even looking. She barely even would have had to try."
    # nat_annoyed
    nth an "(I’m not thinking that!)"

    nrt "With the state you made of yourself, no one at the bar would have batted an eye when she carried you out."
    nrt "Ciara told you the bar was near her place too, right? Must have been her idea. Probably the only reason she even agreed to see you in the first place."
    # nat_angry
    nth ag_sd "(Shut up!)"

    nrt "You finally reach the door, your pathetic shambling efforts paying dividends at last. You hear nothing on the other side, Lillian having clearly finished her shower."
    nrt "Are you thinking about her fresh out of the shower, even though she literally kidnapped you?"
    # nat_dejected_smile
    nth ag_sd "(No. I’m thinking about how I’m gonna apologise to her once I open this do—)"
    
    play sound "audio/lock.mp3"
    nrt "The door is locked."


    # Music changes to something dark and spooky whatever Khaz comes up with lol
    # Rattling SFX of the handle being fruitlessly turned while the line stays on screen.
    play sound "audio/lock.mp3"
    nrt "It’s still locked, no matter how many times you try to deny reality by turning the handle again."
    # nat_surprised
    nth su "(I’m sure there’s… a perfectly normal… explanation…?)"

    nrt "Since when is being drugged and kidnapped and held in a locked room perfectly normal?!"
    # nat_surprised
    nth su "(The windows?)"
    play music "audio/ambient.mp3" loop
    # nat_neutral_sideeye
    nth ne_sd"(They’re… pretty high off the ground aren’t they?)"

    nrt "Yes. They are. You’re trapped here."
    # nat_neutral_sideeye
    nth ne_sd "(Well.)"
    # nat_sad
    nth sa "(Shit.)"

    nrt "You try the door handle one last time, for some reason."
    nrt "The door handle turns, the door opening to reveal Lillian on the other side."

    # gut instinct is that juxtaposing Lillian’s dialogue with something like lil_angry_speaking could go insane here, but maybe it’s easier to just go lil_happy_speaking idk
    show l_z_n_s_sp
    lil "Nat! You’re up! That’s wonderful!"
    # nat_sympathetic_speaking
    hide l_z_n_s_sp
    show l_z_n_s
    nat sy_sp "Oh. Uh. Yeah I— Um. Wanted to stretch my legs a bit. Y’know. Lying in bed all day haha."

    nrt "Are you crazy? She kidnapped you! Say something!"
    # same as above, angry could go super hard but maybe neutral smile is the sensible option
    hide l_z_n_s
    show l_z_n_s_sp
    lil "That’s lovely. It’s getting rather late, though. Unfortunate timing, I know, but let’s get you back to bed, shall we?"
    # nat_neutral_sideeye_speaking
    hide l_z_n_s_sp
    show l_z_n_s
    nat ne_sd_sp"Um. OK…"

    nrt "Lillian steps beside you, calmly but firmly hooking an arm under your shoulder as she closes the door behind her with a resounding click of finality."
    nrt "You say nothing as she slowly ushers you across the short expanse of floor to the bed. "
    nrt "Your body still feels sluggish, and the assistance is honestly quite helpful, considering how difficult it was for you to make it to the door in the first place."
    nrt "The irony should not be lost on you that, despite Lillian’s assistance, she is the reason you need help in the first place."
    # lil_happy_speaking
    hide l_z_n_s_sp
    show l_z_h_sp
    lil "There, that’s better."
    play music "audio/lilsus.mp3" loop fadeout 1.0 fadein 3.0
    # lil_sad_speaking
    hide l_z_h_sp
    show l_z_sa_sp
    lil "You still feel a bit weak, you should have been more careful."
    # lil_sad
    hide l_z_sa_sp
    show l_z_sa
    # nat_sad_eyesclosed_speaking
    nat sa_ec_sp "Sorry."

    nrt "Lillian pulls back the covers, ushering you into bed. You squirm in gracelessly cocooning yourself in a tangle of blanket so as not to take your eyes off Lilllian."
    nrt "Seriously."
    nrt "Seriously!?"
    nrt "With all that’s happened, with all that you’ve realised, you’re seriously making the time to stare at Lillian in sexy sleepwear?"
    # nat_neutral_sideeye_blush
    nth ne_sd_bl "(Well if she’s so dangerous, it’s not like I should be taking my eyes off her…)"

    nrt "You’re staring at her tits!"
    # nat_surprised_blush
    nth su_bl "(They’re at eye height!)"
    # lil_neutral_smile
    hide l_z_sa
    show l_z_n_s
    nrt "Your absurd horny-brain addled musings are interrupted, as are all other functions of your brain for the rest of time, as Lillian, quite unceremoniously, slips into bed alongside you."
    # nat_surprised_blush_speaking
    nat su_bl_sp "Oh!"

    # lil_happy_speaking_blush
    hide l_z_n_s
    show l_z_h_bl_sp
    lil "I hope this isn’t uncomfortable? There’s plenty of space."
    # lil_neutral_smile_blush
    hide l_z_bl_sp
    show l_z_n_s
    # nat_sympathetic_speaking
    nat sy_sp "No it’s… Fine. Great. Um… Yeah, mi casa es tu casa except with bed I can’t remember the Spanish word for bed I haven’t spoken it since Year 9 sorry."
    # lil_happy_blush
    hide l_z_n_s
    show l_z_h_bl
    nrt "Lillian laughs gently, her mirth rumbling through the bed you now share together."
    # lil_neutral_smile_blush
    hide l_z_h_bl
    show l_z_n_s_bl
    nrt "An hour ago, this would have been a dream. Hell, for the four-ish years you’ve known Lillian, this exact scenario was the frequent subject of your wildest fantasies."
    nrt "And yet now, no amount of awkward joking can assuage your pummeling heart, your panicked breathing, your body taught on springs, unsure whether to lean closer to Lillian or bolt away."
    # lil_flirting_speaking
    hide l_z_n_s_bl
    show l_z_fl_sp
    lil "Shhh, it’s alright."
    # lil_flirting
    hide l_z_fl_sp
    show l_z_fl
    nrt "Lillian makes the decision for you, reaching out for a warm embrace and pulling you closer. Your head nestles below her chin, leaving absolutely nothing to the imagination."
    nrt "And begins to sing."
    # Change to Alexis CG and Khaz music
    # No more character portraits during the CG.
    scene cuddleCG with fade
    play music "audio/lilsus_spook.mp3" loop fadeout 1.0 fadein 3.0
    nrt "She sings softly, wordlessly. A melody that is at once simple and complex, filling your senses. You don’t know whether to feel soothed or threatened, secured or trapped."
    nrt "You don’t know anything about music theory, is this melody major or minor? Both?"
    nrt "You had no idea Lillian was such a great singer. Does Lillian know music theory? Did she compose this song just for you? Or is she making it up on the spot?"
    nrt "The tenseness begins to leave your body as Lillian sings into your soul, rubbing the same soothing circles into your hair as she did last night at the bar."

    nth n"(At the bar…)"
    nat "Lillian…"

    nrt "You take in a quick breath, then choke it out. You can’t just ask this, surely? Not while she’s singing to you, holding you, giving you everything you could have ever dreamed of."
    nrt "But you must."
    nrt "You take in another breath, slower this time, shutting your eyes and feeling the calmness radiate through you, even as Lillian holds you close."

    nat "What did you put in my drink yesterday?"

    nrt "Lillian’s singing quiets to a gentle hum. She glances down at you, eyes gleaming in the faint light, arms ever so slightly gripping you tighter."
    nrt "You can’t breathe."

    lil "Ah. Yes, I’m… sorry about that. The side effects of mixing zopiclone with alcohol can be quite nasty. I had hoped that the little you had to drink, and my ability to care for you today would—"
    nat "You… put sleeping meds in my drink…?"
    lil "…Yes?"

    nrt "She says it like it’s the most obvious thing in the world. Like it’s honestly quite ridiculous of you to have only just pieced together why she hasn’t been blaming you at all for your supposedly drunken state."

    lil "I simply had no choice! Hearing you talk about your life being so miserable that you’ve fantasised about its end?"
    lil "I couldn’t bear to hear you suffer like that, Natalie."
    lil "I couldn’t allow it to continue."
    lil "You struggle so much to look after yourself, and nobody else will give you the support you need. So I did what I must."
    nat "Is that… why you took my phone? Brought me here?"
    lil "Yes."
    nat "Is that… why the door’s locked?"

    nrt "Lillian pauses, breathing deeply as she considers her response to your question."
    nrt "She pulls away slightly from your embrace, gazing into your eyes from above you on the bed."

    lil "Yes, Nat. That’s why the door’s locked."
    lil "You’re so terrible at accepting help. Why, it’s been a struggle all day just to get you to eat the food I was so happy to make for you."
    lil "I can’t just have you running back to your horrible life the moment I leave the flat for the day."
    nat "I… Why…?"
    lil "Isn’t it obvious?"

    nrt "She leans forwards, pressing a firm kiss to your forehead, squeezing you tightly."

    lil "Because I love you, Natalie."

    nrt "Warmth and fear blossom in your chest in equal measures. Words you had dreamed of hearing, and words you had been dreading for the past hour, cycle through your mind in equal measure."

    nat "I… I…?"
    lil "Shhh, it’s alright."
    lil "You don’t have to answer right away. My love for you is patient, Natalie."
    lil "We have all the time in the world."

    nrt "Lillian pulls you back into her chest. Your body still feels tense, so tense, like you don’t know whether to fight, flee, or kiss her. "
    nrt "Your hands clench and unclench uselessly somewhere around her stomach, your shoulders shaking beneath her all-encompassing embrace."
    nrt "Her singing returns anew, and you drift into the hypnotising melody."

    nth "(Her voice is so beautiful… She’s… perfect at everything…)"

    nrt "Your tenseness alleviates, your breathing steadying."

    nth "(It’s not like… There’s anything I can do…)"
    nth "(Might as well… Enjoy this…)"

    nrt "You settle into the protective cocoon of Lillian’s embrace, drifting off to sleep without resistance."
    nrt "Because that’s who you are, isn’t it? Who you’ve always been. A woman who will do anything so long as it means she has to do nothing."
    nrt "You deserve this."
    nrt "Lillian’s melody drifts to a close, and she presses another kiss to your head."
    scene black_bg at double with fade

    lil "I’m never letting you go, Nat."
    nrt "{cps=10}TO BE CONTINUED.{/cps}"
