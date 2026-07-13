label start: 

    scene black_bg at double
    

    # Open on black screen. Not sure if it should be no music or like quiet ambient stuff, will have to ask Khaz.
    # All narrator text should be yellow and italicised. I don’t know if you can set the italicised part at the start so I can go through and add the italic marker to all of the narrator text if needed.

    nrt "You wake up feeling like shit."
    nrt "Wait, that probably needs a little clarification. After all, most days you feel kind of shit."
    nrt "Your terrible sleep pattern, poor diet, and general inability to look after yourself makes waking up a taxing ordeal at the best of times. "
    nrt "But even by your usual low standards, this is far above and beyond the normal, everyday feeling like shit."
    nrt "This is {b}advanced{/b} feeling like shit."
    nrt "Your brain feels like it’s being forced through a grated tube that it doesn’t quite fit through."
    nrt "Your dry mouth tastes distinctly of metal, like you spent the whole night chewing on copper coins."
    nrt "You could keep going, but you can barely even feel your limbs properly, so you’ll get to enjoy the steadily developing feeling of the {b}rest{/b} of your body feeling like shit soon enough."
    
    # Insert the visual background of the bedroom, with an iris opening transition, before the iris closes, returning to black screen.
    scene bedroom_day at half with in_eye:
        blur 25
    scene black_bg at double with out_eye
    
    nth ag_sd_sp "{i}That{/i} was a mistake."
    nth ne "Ow…"
    # Expression change to nat_ap
    nth ap "Just how much did I drink last night?"

    # Insert bar background shot. If we can make it look a bit hazier, possibly like a paint smudging effect, that would be great. Might ask Flor about that.
    scene bg_bar:
        blur 25    
 
    nrt "You try to remember the previous night. You were… out at a bar? Probably. Would definitely explain the whole {b}feeling like shit{/b} thing."
    nrt "You think you were with someone. Multiple someones? People you hadn’t seen for a while."
    nrt "Although given how badly you isolate yourself, that describes almost everyone except your work colleagues. So it wasn’t a work party, not that you ever go to those anyway."

    # Expression change to nat_ap
    nth ap "I think… I remember…"
    nrt  "Girl you don’t remember shit."

    # Return to black screen
    scene black_bg at double
    # Expression change to nat_sa_eyes_closed
    nth sa_ec "Can’t even remember how I got here…"
    # Expression change to nat_su_sp
    nat su_sp "WAIT SHIT."

    # Eyelid opening animation again, much quicker. Room background comes into view, slightly blurry.
    scene bedroom_day at half with in_eye:
        blur 16
    # Expression change to nat_su
    nth su "Where the hell {i}is{/i} here!?"
    nth su "This isn’t my room!"

    # Room background fully comes into focus, removing the blur.
    scene bedroom_day at half with dissolve

    play music "audio/casual.mp3" loop
    #Expression change to nat_n_s
    nth ne_s "Holy shit this place is {i}fancy.{/i} Hotel room?"
    nrt "What kind of hotel room has taxidermy butterflies on the wall, you idiot."
    #Expression change to nat_n
    nth ne "Right. Where {i}am{/i} I then?"
    #Expression change to nat_su
    nth su "Wait, is that…"

    # Image change to CG of banana and bottle of water on the side table

    nrt "Despite the immense disorientation and agony it causes, you’re able to turn your head to glance towards the bedside table."
    nrt "Upon the table stands salvation: A bottle of water, and a banana."
    # Expression change to nat_h
    nth h "Drunk Natalie I owe you my {i}life.{/i}"
    nrt "As you reach for your lifelines, something else becomes immediately apparent to you. Your pyjamas are a little too large, the sleeves hanging down practically to your fingers."

    # Image change to CG of Natalie reaching for banana and water.

    nrt "The first munch of banana comes with a startling realisation. These are not your pyjamas."

    # Image change to CG of empty table, then returns to the standard bed background

    nrt "You pat down your body with one limp, heavy arm struggling to even lift the blankets. Yep. Definitely not yours."
    nrt "They're a little too big, made of some comfortable material that {b}feels{/b} expensive, and have actually been washed some time in the past fortnight."
    # Expression change to nat_n_s
    nth ne_s"Huh, these are really nice too."
    # Expression change to nat_h_bl
    nth h_bl "Heh, looks like I finally landed that sugar mama!"
    nth "Damn, drunk Natalie, I wasn’t familiar with your game."
    nrt "The various aches and pains in your body are, by this point, almost queueing up to be processed. How polite."
    nrt "Your latest bout of self-congratulatory hubris has made those pains demand your attention more urgently, however, and through the haze, the {i}absence{/i} of a certain set of aches becomes apparent."
    # Expression change to nat_n
    nth ne "Doesn’t {i}feel{/i} like I’ve had sex though…"
    nrt "Do you even remember what that feels like?"
    # Expression change to nat_sa
    nth sa "Well, yeah it {i}has{/i} been a while since uni… But not {i}that{/i} long, right?"
    nrt "You’re probably right. Given that track record, what were the chances that anyone wanted to have sex with you anyway."
    # Expression change to nat_shy_b
    nth sh_bl "Maybe she was really gentle?"
    nrt "Well, it’s more likely than you having topped."
    # Expression change to nat_sa
    nth sa "…"
    # Expression change to nat_sy
    nth sy "Maybe I really did this time?"
    nrt "Get your head into gear, Natalie."
    nrt "You’re in a stranger’s bed, in a stranger’s house, wearing clothes you didn’t leave home in."
    nrt "Maybe worry about figuring out how the hell that happened, rather than worrying about your nonexistent sex life?"
    # Expression change to nat_n
    nth ne"I dunno, I guess I must’ve got drunk as shit."
    nrt "Starting with the obvious, we’ll make a detective of you yet."
    # Expression change to nat_n_sideeye
    nth ne_sd"And… I guess, maybe, I was too drunk to get myself home?"
    # Expression change to nat_n_s
    nth ne_s"So maybe it {i}wasn’t{/i} a stranger!"
    # Expression change to nat_h
    nth h "One of the people I was out with must’ve let me stay at their place, right?"
    # Expression change to nat_n_s
    nth ne_s "Yeah that makes sense. Ciara used to talk about crashing on people’s sofas all the time after house parties or socials or whatever."
    # Expression change to nat_n
    nth ne "Never really felt like my scene but, here I am I guess."
    # Expression change to nat_n_s
    nth ne_s "Explains the banana and the water too."
    nrt "Honestly, you’re really not sure why you ever attributed the water and banana to your drunken self from the night before. You barely ever remember to look after yourself {b}sober.{/b}"
    # Expression change to nat_n
    nth ne "Hmm…"
    nth "Doesn’t explain the pyjamas though…"
    # Expression change to nat_n_sideeye_b
    nth ne_sd_bl "Oh god I probably threw up didn’t I."
    nth "Shit, I really hope I didn’t get any on them."
    # Expression change to nat_sa
    nth sa "As if this couldn’t get any more embarrassing."
    nth "Some hero rescues me from the consequences of my own actions, I probably got sick all over them, and I can’t even remember who it was."

    # Change background back to the image of the bar
    scene bg_bar with fade
    nrt "You cast your mind back to the night before. You were out with two people, people you hadn’t seen in years…"
    # Expression change to nat_su
    nth su"Since uni!"
    nrt "Yes, that sounds right. Two friends from university. One of them must have been Ciara, yes?"

    # Background changes to have Ciara’s image come into focus. Either as a sprite, or as a drawing on the CG.
    show c_n_s at char_right with dissolve

    nrt "Yes, of course. She reached out to you a few days ago, set up this meetup, because you never would have organised it yourself. After all these years, she still knew you well enough to not fall into that trap."
    nrt "And you actually attended! Was that because you were such close friends? Clearly not close enough to keep regular contact over the past three years, but that’s hardly her fault. But maybe it wasn’t that."

    # Background image changes to show Lillian there as well.
    show l_bar_n_s at char_left with dissolve

    nrt "Oh, right, it’s because the other person she invited was—"

    # Expression change to nat_su_sp
    nat "Holy shit I was out with Lil—"
    #show lil_intro

    # Insert door opening SFX
    # Change music to Lillian’s Theme
    # Lillian appears, insert l_fl_bl_sp
    stop music

    scene bedroom_day at half
    show l_fl_bl_sp 
    lil "Nat! You’re awake!"
    # Expression change to nat_su_sp
    # Expression change to l_n_s
    hide l_fl_bl_sp
    show l_n_s
    nat su_sp "Lillian!"
    nat "I was hoping— I mean— I literally {i}just{/i} figured out I must be at your place!"
    # Expression change to nat_ap_sp
    nat ap_sp"Shit I’m so sorry for all the trouble. You really didn’t have to, I mean, thanks so much for doing this. And for the banana! And the water!"
    nrt "It’s honestly impressive how much you can run your mouth for someone your coworkers always describe as \"weirdly quiet.\""
    # Expression change to l_h_sp
    hide l_n_s
    show l_h_sp
    lil "Not a problem at all, glad I could help!"
    # Expression change to l_fl_bl_sp
    hide l_h_sp
    show l_fl_bl_sp
    lil "The banana should help a little with the hangover, and I can refill the water when you need it."
    # Expression change to nat_n_s_sp
    # Expression change to l_n_s
    hide l_fl_bl_sp
    show l_n_s
    nat ne_s_sp "You’re literally an angel, you know that."
    # Expression change to nat_sa_sp
    nat sa_sp"Seriously, I’m so sorry I got so drunk. I dunno what the hell happened, I usually know my limits better than that."
    # Expression change to l_fl_bl_sp
    hide l_n_s
    show l_fl_bl_sp
    lil "You weren’t a bother at all, don’t worry."
    # Expression change to l_n_sp
    hide l_fl_bl_sp
    show l_n_sp
    lil "Are you feeling alright?"
    # Expression change to l_sy
    hide l_n_sp
    show l_sy
    nrt "Obviously not, but really the last thing you should be doing is making that any {b}more{/b} of her problem."
    nrt "You’re the one who got piss drunk, ruined a catchup with far better people than you who you hadn’t bothered in years, and probably threw up all over her to boot."
    nrt "But Lillian’s looking at you with such gentle concern, and the last thing you should do is make yourself a fucking liar on top of it all."
    # Expression change to nat_n_sideeye_sp
    nat ne_sd_sp"…Feeling like shit, I gotta be honest."
    # Expression change to nat_ap_sp
    nat ap_sp"Not your fault! I’d probably be dead if not for that water."
    # Expression change to l_h_sp
    hide l_sy
    show l_h_sp
    lil "Then I’m glad to have assisted!"
    # Expression change to l_ap_sp
    hide l_h_sp
    show l_ap_sp
    lil "What’s feeling so bad, is it mostly your head?"
    # Expression change to l_sy
    hide l_ap_sp
    show l_sy
    nrt "Her soft voice makes you feel like she’s a particularly caring nurse, and you’re in the world’s most comfortable hospital."
    # Expression change to nat_n_s
    nth ne_s"Well she {i}was{/i} studying pharma, makes sense."
    nrt "You remembered that? A minute ago you couldn’t even remember her face. Are you having sexy nurse fantasies about Lillian, you sick pervert?"
    # Expression change to nat_shy_b
    nth sh_bl"No! She’s just… Really good at this, OK?"
    nrt "The lady doth protest too much."
    # Expression change to nat_n
    nth ne"I should probably answer her question anyway…"
    # Expression change to nat_sa_sp
    nat sa_sp"Mostly my head, yeah."
    nat "My mouth tastes all metallic too, and the rest of my body’s pretty sluggish."
    # Expression change to nat_n_sp
    nat n_sp"Banana helped a bit with the taste, but it’s not entirely going away."
    # Expression change to l_ap_sp
    hide l_sy
    show l_ap_sp
    lil "I can grab you some more food if you’d like? Would another banana be too much, or—"
    # Expression change to nat_ap_sp
    nat ap_sp"It’s fine! You’ve already done so much to help, I don’t wanna be any more of an imposition than I already have been."
    # Expression change to l_fl_bl_sp
    hide l_ap_sp
    show l_fl_bl_sp
    lil "Nonsense. I’m perfectly happy looking after you, Nat. I couldn’t bear the thought of leaving you to struggle when you clearly need support."
    # Expression change to l_n_s
    hide l_fl_bl_sp
    show l_n_s
    nrt "Wow. That might be the first time in your life someone’s ever said that to you. Or even suggested as much in that direction. You might start crying, if your body was actually responding to messages from your brain right now."
    # Expression change to nat_ap_sp
    nat ap_sp"Thanks. Seriously, I mean it."
    # Expression change to nat_n_sideeye_sp
    nat ne_sd_sp"It’s… Not common for…"
    nrt "You take a quick breath, trying to shake your head, then regretting the horrible pain that causes."
    # Expression change to nat_sa_sp
    nat sa_sp"No one really looks after me much, so this really means a lot to me Lillian, thanks."
    nrt "Actual sincerity! Who knew you had it in you. A bit self-pitying and over-sharing, but it was never going to be perfect, was it?"
    # Expression change to l_n_sp
    hide l_n_s
    show l_n_sp
    lil "I know."
    # Expression change to l_sa
    hide l_n_sp
    show l_sa
    nrt "Lillian’s expression changes, tinging her soft concern with a little sadness. She makes as if to reach a hand to you, then stops herself."
    # Expression change to l_sa_sp
    hide l_sa
    show l_sa_sp
    lil "That’s part of why it doesn’t bother me at all to give you the support you deserve, Natalie. It… seems like you need it."
    # Expression change to l_sa
    hide l_sa_sp
    show l_sa
    # Expression change to nat_ap_sp
    nat ap_sp "Was I {i}that{/i} much of a mess last night?"
    # Expression change to l_sa_sp
    hide l_sa
    show l_sa_sp
    lil "Not at all! It’s, well, you spent a lot of last night… venting, I think?"
    # Expression change to l_sa
    hide l_sa_sp
    show l_sa
    nrt "Of course you did, you fucking clown."
    # Expression change to l_sa_sp
    hide l_sa
    show l_sa_sp
    lil "About your work, your family, your, ah, love life."
    # Expression change to l_sa
    hide l_sa_sp
    show l_sa
    nrt "Or lack of one."
    # Expression change to nat_n_sideeye
    nth ne_sd "Shit, I probably actually said that."
    # Expression change to nat_sa_sp
    nat sa_sp"Oh {i}god{/i} I’m so sorry, I hope I didn’t ruin the mood."
    # Expression change to l_ap_sp
    hide l_sa
    show l_ap_sp
    lil "You were fine, don’t worry."
    lil "I’m glad I could be there to help ease the burden, actually."
    # Expression change to l_sa_sp
    hide l_ap_sp
    show l_sa_sp
    lil "Hearing you say, what was it, {i}\"This job makes me want to fucking kill myself, but that would require me to actually get off my lazy bitch ass and do it.\"{/i}"
    # Expression change to l_sa
    hide l_sa_sp
    show l_sa
    nrt "Girl."
    # Expression change to l_sa_sp
    hide l_sa
    show l_sa_sp
    lil "And then hearing how your parents have offered you the bare minimum in support, while giving your brother everything he could ever want?"
    # Expression change to l_ag_sp
    hide l_sa_sp
    show l_ag_sp
    lil "That your boss {i}just happened{/i} to pass you up for promotion for three cliquey white men in a row? That—"
    # Expression change to l_ag
    hide l_ag_sp
    show l_ag
    # Expression change to nat_sa_sp
    nat sa_sp"Shit Lillian, I’m sorry I {i}really{/i} didn’t mean to go into all that last night. I was just, I dunno, I thought we’d just be catching up."
    # Expression change to l_n_sp
    hide l_ag
    show l_n_sp
    lil "Well it sounds like that is what catching up on your life has become."
    lil "I’m so sorry, Natalie."
    # Expression change to l_n
    hide l_n_sp
    show l_n
    # Expression change to nat_sa_sp
    nat "{i}I’m{/i} the one who’s sorry! I upset you and Ciara all night…"
    # Expression change to l_ap_sp
    hide l_n
    show l_ap_sp
    lil "I’m upset {i}for{/i} you, Nat, not {i}because{/i} of you."
    lil "And, well, I thought you could really use somebody in your corner."
    # Expression change to l_sy
    hide l_ap_sp
    show l_sy
    # Lillian’s sprite moves to indicate it’s closer to Natalie on the bed. Not sure if that should be zooming in or moving from right to centre or centre to left or what.
    # Expression change to l_h_sp_b
    hide l_sy
    show l_h_sp_bl
    lil "Let you in on a little secret? I’m actually a little happy this happened. If no one else is going to look after you, then I will."
    # Expression change to l_n_s_b_sp
    hide l_h_sp_bl
    show l_h_sp_bl
    lil "And if it means I get to spend a little more time catching up? Then all the better."
    # Expression change to nat_shy_b
    # Expression change to l_h_b
    hide l_h_sp_bl
    show l_h_bl
    nth sh_bl "I’M DEAD"
    # Expression change to nat_shy_b_sp
    nat sh_bl_sp"O-Oh! That’s— That’s really sweet of you Lillian!"
    # Expression change to nat_h_b_sp
    nat h_bl_sp"Gotta be the number one experience I’ve had waking up with a hangover too, haha!"
    # Expression change to l_h_sp_b
    hide l_h_bl
    show l_h_sp_bl
    lil "Haha!"
    # Expression change to l_h_b
    hide l_h_sp_bl
    show l_h_bl
    nrt "Did she seriously just laugh at your terrible joke? There’s charity and then there’s too far, come on now."
    # Expression change to nat_ap_sp
    nat ap_sp"Anyway, thanks so much for all this, but I really gotta get ready for work now. I’m probably already late…"
    # Expression change to l_h_sp
    hide l_h_bl
    show l_h_sp
    lil "Oh, don’t worry about that."
    # Expression change to l_fl_bl_sp
    hide l_h_sp
    show l_fl_bl_sp
    lil "I already informed them you’d be unavailable."
    # Expression change to l_h
    hide l_fl_bl_sp
    show l_h
    # Expression change to nat_su_sp
    nat su_sp"What!?"
    # Expression change to nat_sa_sp
    nat sa_sp"Lillian, I can’t just take the day off for a hangover. And there’s no way they’d accept that as an excuse for a sick day either."
    # Expression change to l_n_sp
    hide l_h
    show l_n_sp
    lil "Natalie, you’re in no state at all to even leave that bed, never mind do a full shift at a job that leaves you so horribly drained."
    # Expression change to l_fl_bl_sp
    hide l_n_sp
    show l_fl_bl_sp
    lil "Doctor’s orders, a full day’s bed rest, at least."
    # Expression change to l_n_s
    hide l_fl_bl_sp
    show l_n_s
    nrt "The caring nurse voice again, but with a hint of playfulness to it. You’re {b}definitely{/b} having sexy nurse fantasies, aren’t you?"
    # Expression change to nat_sideeye_b
    nth sd_bl"Shut it. At least I can enjoy {i}something.{/i}"
    nrt "Are you {b}seriously{/b} going to try flirting back?"
    nth "No I’m just gonna be… jokey like she was?"
    nrt "You’re fooling no one."
    # Expression change to nat_n_s_sp
    nat ne_s_sp"Can pharmacists prescribe that kind of treatment?"
    # Expression change to l_fl_bl_sp
    hide l_n_s 
    show l_fl_bl_sp
    lil "This one can, for very special patients."
    # Expression change to l_n_s
    hide l_fl_bl_sp
    show l_n_s
    nrt "{b}It worked!?{/b}"
    # Expression change to l_fl_bl_sp
    hide l_n_s
    show l_fl_bl_sp
    lil "And I can {i}also{/i} prescribe you one proper lunch."
    # Expression change to l_n_sp
    hide l_fl_bl_sp
    show l_n_sp
    lil "You need a little more food in you than a single banana, and I’d be a terrible host if I didn’t offer to make you something more substantial."
    # Expression change to nat_n_s_sp
    # Expression change to l_n
    hide l_n_sp
    show l_n
    nat ne_s_sp"Seriously? You’ve already done so much."
    # Expression change to l_h_sp
    hide l_n
    show l_n_sp
    lil "Not at all, it’s really the least I can do."
    # Expression change to l_fl_bl_sp
    hide l_n_sp
    show l_fl_bl_sp
    lil "Besides, let you in on another secret?"
    # Expression change to l_h_sp_b
    hide l_fl_bl_sp
    show l_h_sp_bl
    lil "I really love cooking. I was kind of hoping you’d let me show off a bit."
    # Expression change to l_h_b
    hide l_h_sp_bl
    show l_h_bl
    # Expression change to nat_h_b_sp
    nat h_bl_sp"Haha!"
    # Expression change to nat_sd_bl_s_sp
    nat sd_bl_s_sp"OK, understood. You can spoil me a {i}little{/i} longer, so long as it’ll make you happy."
    nrt "Oh you think you’re {b}so{/b} smooth, hm?"
    # Expression change to l_h_sp_b
    hide l_h_bl
    show l_h_sp_bl
    lil "Absolutely! What do you want?"
    # Expression change to l_h_b
    hide l_h_sp_bl
    show l_h_bl
    nrt "A quiet terror grips you at the question. How come you’re going deer in the headlights {b}now?{/b} She was obviously going to ask you about food, you were just talking about food, idiot."
    nrt "Honestly, bacon and eggs sounds ideal right now. Your dad always said it was the best hangover cure, and a couple days into uni, you found out he was right. Apparently there’s even nutritional science proving it’s a great choice."
    nrt "But there’s just one problem."
    # Expression change to nat_n
    nth ne "Bacon and eggs is white as {i}hell.{/i}"
    nrt "Right. There’s no way any self-respecting Chinese woman would ask another self-respecting Chinese woman to make her bacon and eggs for lunch, right?"
    # Expression change to nat_n_sideeye
    nth ne_sd"May as well paint {i}adoptive white parents{/i} on my face."
    # Expression change to nat_n_sideeye_sp
    nat ne_sd_sp"Um…"

    # Make this one enormous paragraph. Have the text scroll, possibly speeding up as it goes? Or just being like 50% faster from the start. Having it kind of blur and not necessarily all be readable is basically the joke. If it auto-skips at the last word to have Lillian interrupt that’d be funny too.
    # Expression change to nat_sy
    nth "{cps=100}What the hell do actual Chinese people have as hangover cures? Not a stir fry, even if it’s the only Chinese thing I ever learned to cook, if I have a huge load of rice and carb right now I’m going to throw up {i}again.{/i} Hot and sour soup? No way, my spice tolerance is {i}painfully{/i} white. Even the takeaway recipe is too much for me, authentic stuff will kill mestone dead. Chicken noodle soup? No, too English menu on the Chinese takeaway. Wonton soup? That’s authentic, right? And you can make it with pork and eggs, so that’s basically like having bacon and eggs, righ—"
    # Expression change to l_fl_bl_sp
    hide l_h_bl
    show l_fl_bl_sp
    lil "Bacon and eggs sound good?"
    # Expression change to l_n_s
    hide l_fl_bl_sp
    show l_n_s
    # Expression change to nat_n_sp
    nat n_sp"Oh."
    nrt "Well that was a lot of overthinking for absolutely nothing, wasn’t it?"
    # Expression change to nat_ap_s
    nat ap_s"Sounds amazing, thanks!"

    # Lillian’s sprite moves away again
    # Expression change to l_fl_bl_sp
    hide l_n_s
    show l_fl_bl_sp
    lil "Bacon and eggs you shall have then! I won’t be a moment."
    # Expression change to l_ap_sp
    hide l_fl_bl_sp
    show l_ap_sp
    lil "…Actually I’ll be a few minutes frying it all up. Try to get some rest while I’m cooking, alright?"
    # Expression change to l_ap
    hide l_ap_sp
    show l_ap
    # Expression change to nat_apoogetic_sp
    nat ap_sp"Not like I can do much else, haha."
    # Expression change to nat_n_sideeye_sp
    nat ne_sd_sp"And I promise not to throw this up like I did whatever I had for dinner last night."
    # Expression change to nat_sa_sp
    nat sa_sp"Actually shit I’m {i}so{/i} sorry if I got any on you."
    # Expression change to l_n_sp
    hide l_ap
    show l_n_sp
    lil "Hm?"
    # Expression change to l_ap_sp
    hide l_n_sp
    show l_ap_sp
    lil "Oh, don’t worry, you didn’t reach the point of vomiting last night."
    # Expression change to l_sy
    hide l_ap_sp
    show l_sy
    # Expression change to nat_n_sp
    nat ne_sp"Oh."
    # Expression change to nat_ap_sp
    nat ap_sp"Well, spared {i}that{/i} embarrassment at least. Thanks for the reassurance."
    # Expression change to l_ap_sp
    hide l_sy
    show l_ap_sp
    lil "Any time, Nat."

    # Door closing SFX, remove Lillian’s sprite.
    hide l_ap_sp
    # Expression change to nat_n
    nth "…Huh."

    # Sizzling SFX

    nrt "Setting aside the pleasant revelation that you had not, in fact, thrown up all over yourself and Lillian, your mind turns again to the night before."

    jump flashback1
