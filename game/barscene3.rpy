label flashback3:
    #FLASHBACK 3
    scene bg_bar with fade
    play music "audio/Bar.mp3" loop fadeout 1.0 fadein 3.0
    # ciara_apologetic_wink_speaking
    show c_ap_w_sp at char_right with dissolve
    # lil_bar_neutral
    show l_bar_n at char_left with dissolve
    cra "Alright, not to hit you all with the literal Irish Goodbye, but I’d best be off."
    # ciara_chaotic_speaking
    hide c_ap_w_sp
    show c_ch_sp at char_right 
    cra "Although actually, before I go, gotta say. Total bullshit that’s a phrase at all."
    # ciara_dejected_speaking
    hide c_ch_sp
    show c_dj_sp at char_right 
    cra "Every time we had to leave anywhere, me mam would end up natterin’ away to the rest of the oul biddies forever."
    # ciara_apologetic_speaking
    hide c_dj_sp 
    show c_ap_sp at char_right 
    cra "Well can me and my friend go out and play then?” “No, we’ll be leaving any minute now!” Then still be chattin’ some shite or other hours later while we’re standing around lookin’ useless."
    # ciara_dejected
    hide c_ap_sp
    show c_dj at char_right 
    # nat_bar_neutral_smile_speaking
    nat bar_n_s_sp "Sounds like Irish Goodbye should be a phrase for what you’re doing now."
    # ciara_happy_speaking
    hide c_dj
    show c_h_sp at char_right 
    cra "Ha!"
    # ciara_neutral_smile
    hide c_h_sp 
    show c_n_s at char_right 
    # lil_bar_neutral_smile_speaking
    hide l_bar_n 
    show l_bar_n_s_sp at char_left
    lil "We shall propose the adjustment to the council of ridiculously incorrect English phrases immediately."
    lil "It can join the agenda alongside “sweating like a pig” and “sleeping like a baby."
    # ciara_happy
    hide c_n_s
    show c_h at char_right
    # lil_bar_happy
    hide l_bar_n_s_sp
    show l_bar_h at char_left
    nrt "You all laughed uproariously at that. Did you know that pigs don’t sweat? Or were you just assuming that Lillian was probably correct about whatever she was saying."
    nrt "Better question, did you even register what Lillian had said at all, or did you just recognise that she was saying something that sounded joke-shaped and laugh on command like a dog."
    # ciara_neutral_smile
    hide c_h
    show c_n_s at char_right
    # lil_bar_neutral_smile
    hide l_bar_h
    show l_bar_n_s at char_left
    # nat_annoyed
    nth an "(Hey I wasn’t that drunk. Yet.)"

    nrt "Your second drink had been looking dangerously low, and it’s not like you’ve ever been particularly renowned for handling your drink well."
    # nat_dejected
    nth dj "(White girl spice tolerance, Asian girl alcohol tolerance. Worst of both worlds for real.)"
    # nat_neutral
    nth ne "(But nah, neither of those drinks were all that strong. I would’ve been tipsy, sure, but nowhere near as smashed as I was this morning.)"

    nrt "True. And with Ciara leaving, you can’t even blame her for the state you ended up in."
    nrt "The hell was your third drink, absinthe? Neat vodka?"
    # nat_neutral_smile
    nth ne_s "(Maybe Lillian and I stayed at the bar for ages?)"
    # nat_shy_blush
    nth sh_bl "(Considering how well things are going today, it’d make sense.)"

    nrt "Do you really think that being subjected to your drunken bullshit for hours on end would have made Lillian more interested in you?"
    # nat_shy_blush
    nth sh_bl "(I mean… Apparently?)"

    nrt "Hopeless."
    # ciara_neutral_smile_speaking
    hide c_n_s 
    show c_n_s_sp at char_right
    cra "Anyway, for realsies now, I gotta head."
    # ciara_chaotic_wink_speaking
    hide c_n_s_sp
    show c_ch_w_sp at char_right
    cra "Although I reckon you two will get on juuust fine without me."
    # ciara_chaotic_wink
    hide c_ch_w_sp
    show c_ch_w at char_right
    # lil_bar_happy_blush
    hide l_bar_n_s
    show l_bar_h_bl at char_left
    nrt "She shot you both outrageous winks on her way out, as you stammered a goodbye and Lillian remained significantly more composed about the whole matter."
    # ciara leaves the scene
    hide c_ch_w with moveoutright
    hide l_bar_h_bl
    show l_bar_h_bl at move_to_centre
    nrt "Alright, pause for a second here. Stupid as you are, you’re not that dense. And Ciara is not that subtle at the best of times, and even by her standards, this was laying it on thick."
    nrt "Your old uni bestie was trying to wingwoman you. With Lillian. Why the hell was she doing that."
    # nat_dejected_smile
    nth dj_sm "(Girl I wish I knew.)"
    # nat_neutral_smile_blush
    nth ne_sd_bl "(I don’t think I ever told her I was into Lillian at uni but I guess it would have been obvious enough, right?)"

    nrt "Definitely."
    # nat_shy_blush
    nth sh_bl "(And judging by today, crazy as it is to even think, Lillian seems to be… Maybe a little bit… Kind of… Into me?)"

    nrt "You’re right, it is crazy to even think that. Delusional, even. The product of a diseased mind drunk on its own delirium."
    nrt "But also, based on the available evidence, seemingly true."
    nrt "That or this is all an elaborate long con, and when you admit that you fancied her back at uni and fancy her even harder now..."
    nrt "The walls will fall down revealing a camera crew and all your school bullies and your entire extended family laughing at you for your audacity."
    # nat_neutral
    nth ne "(OK but like, probably not, right?)"

    nrt "The chances are never zero."
    nrt "That or you’re misreading signs, it wouldn’t be the first time."
    # nat_annoyed
    nth an "(Alright we don’t have time for the highlight reel of my embarrassing secondary school crushes on straight girls.)"

    nrt "You sure?"
    # nat_annoyed
    nth an "(Let’s pretend we went through it in excruciating detail and I was very embarrassed and then get back to the point.)"

    nrt "If you insist."
    # nat_neutral_smile_blush
    nth ne_sd_bl "(Besides, Lillian’s actually gay, I’ve known that much for years.)"
    # nat_shy_blush
    nth sh_bl "(And maybe got a little first-hand evidence of that last night? If I can remember anything.)"

    nrt "Your attempts to remember the conversation after Ciara’s departure are a little hazy, yes. Mostly due to the fact that you were now alone with Lillian after Ciara all but yelled that she’d been wingwomaning for you."
    nrt "Time to see just how badly you missed the open goal she set up for you, eh?"
    # lil_bar_neutral_smile_talking
    hide l_bar_h_bl
    show l_bar_n_s_sp
    lil "I see she’s as lively a character as ever."
    # lil_bar_neutral_smile
    hide l_bar_n_s_sp
    show l_bar_n_s
    nrt "Oh. Yes it would make sense that you talked about the fact she just up and left, even while avoiding the elephant in the room of how she left."
    # nat_bar_happy_speaking
    nat bar_h_sp "Haha, yeah."
    # nat_neutral_sideeye_blush
    nth ne_sd_bl "(That laugh didn’t sound too awkward, did it?)"

    nrt "Girl you already know."
    # nat_bar_neutral_smile_speaking
    nat bar_ne_s_sp "As far as I can tell, she hasn’t really changed since uni, just become even more like herself."
    # nat_bar_happy_speaking
    nat bar_h_sp "Ciara Plus Plus."
    # lil_bar_happy_speaking
    hide l_bar_n_s
    show l_bar_h_sp
    lil "Haha!"
    # lil_bar_neutral_speaking
    hide l_bar_h_sp
    show l_bar_n_sp
    lil "Although, if you don’t mind my asking."
    # lil_bar_surprised_speaking
    hide l_bar_n_sp
    show l_bar_su_sp
    lil "“As far as you can tell?” I’d assumed the two of you were in regular contact."
    # lil_bar_surprised
    hide l_bar_su_sp
    show l_bar_su
    nrt "A sharp pang of guilt shot into you at that point. Your guilt at having not met up with Ciara in years had been mostly assuaged by the easy conversation tonight, and more to the point, the fact Ciara hadn’t brought it up."
    nrt "But the fact Lillian noticed, when she hasn’t seen either of you in even longer…"
    # lil_bar_surprised_speaking
    hide l_bar_su
    show l_bar_su_sp
    lil "You were thick as thieves back at RCS. Felt like the only time I saw you without her was in lectures or supervisions."
    # lil_bar_surprised
    hide l_bar_su_sp
    show l_bar_su
    # nat_bar_neutral_speaking
    nat bar_ne_sp "Pretty much, yeah. I basically became her little pet introvert from day one meeting in halls."
    # nat_bar_apologetic_speaking
    nat bar_ap_sp "Probably would’ve spent the whole of undergrad sat in my room watching gay cartoons if not for her dragging me out of my shell."

    nrt "As if you didn’t manage that anyway."
    # lil_bar_neutral_speaking
    hide l_bar_su
    show l_bar_n_sp
    lil "You say that as if you might have preferred it that way."
    # lil_bar_neutral
    hide l_bar_n_sp
    show l_bar_n
    # nat_bar_neutral_speaking
    nat bar_ne_sp "Not really? Maybe a little. She can be a lot, sometimes."
    # nat_bar_apologetic_speaking
    nat bar_ap_sp "Like, not every experience she took me to was the greatest night of my life or anything, but I’m still grateful she gave me the chance to find out, right?"
    # nat_bar_neutral_smile_blush_speaking
    nat bar_ne_sd_bl_sp "Or like, I’m really glad she invited me tonight, of course."
    # lil_bar_neutral_smile_blush_speaking
    hide l_bar_n
    show l_bar_n_s_bl_sp
    lil "As am I."
    # lil_bar_neutral_speaking
    hide l_bar_n_s_bl_sp
    show l_bar_n_sp
    lil "I suppose I’d simply assumed this was a regular hangout for you two that I had been graciously invited to."
    # lil_bar_neutral_smile_speaking
    hide l_bar_n_sp
    show l_bar_n_s_sp
    lil "I was actually feeling rather flattered with how welcomed you made me feel, despite the closeness you two share."
    # lil_bar_neutral_smile
    hide l_bar_n_s_sp
    show l_bar_n_s
    # nat_neutral_speaking
    nat bar_ne_sp "Oh. Yeah I guess we haven’t really hung out in a while. We chat on Facebook sometimes, I guess."
    nat bar_ne_sp "She helped me settle into my flat after I moved away from uni, so I saw her a few times that first year, but not really at all since then."
    # lil_bar_neutral_speaking
    hide l_bar_n_s
    show l_bar_n_sp
    lil "I see."
    # lil_bar_apologetic_speaking
    hide l_bar_n_sp
    show l_bar_ap_sp
    lil "Sorry, I didn’t mean to pry."
    # lil_bar_surprised_speaking
    hide l_bar_ap_sp
    show l_bar_su_sp
    lil "You just seemed… relieved, when she left. If that’s not impolite to say."
    # lil_bar_surprised
    hide l_bar_su_sp
    show l_bar_su
    # nat_bar_neutral_sideeye_speaking
    nat bar_sd_sp "Oh, really?"
    # nat_bar_sad_speaking
    nat bar_ap_sp "Sorry, pretty rude of me."
    # nat_bar_neutral_sideeye_speaking
    nat bar_sd_sp "Ciara’s meant to be one of my best friends, right?"
    # nat_bar_sad_speaking
    nat bar_sa_ec_s "So close that I’ve barely spoken to her in three years…"
    # lil_bar_sad_speaking
    hide l_bar_su
    show l_bar_s_sp
    lil "Did the two of you have a falling out, or something?"
    # nat_bar_neutral_sideeye_speaking
    # lil_bar_sad
    hide l_bar_s_sp
    show l_bar_sa
    nat bar_ne_sd_sp "No, not at all. It’s more like…"

    nrt "You hesitated for a moment then, chewing on your lip, unsure if you should say what you were going to say next."
    nrt "No, definitely sure that you shouldn’t say it. But the combination of alcohol and attraction and vulnerability and the whirlwind of actually having a night you’d enjoyed for the first time in months, if not years, all led to the surge of adrenaline that led to you blurting out,"

    # nat_bar_sad_speaking
    nat bar_sa_sp "I just feel so jealous of her. Any time I think of her."
    # nat_bar_sad_eyesclosed_speaking
    nat bar_sa_ec_sp "Like she has this amazing life, while I’m here being the girl everyone compares their life to just so they can say, “Well at least it’s not that bad!”"

    nrt "You laughed bitterly, swigging down the last of your drink as Lillian gazed on. Concerned? Worried? Intrigued? You couldn’t tell then and it’s harder to remember now."
    # nat_bar_sad_speaking
    nat bar_sa_ec_sp "Like I know it’s not fair. I know it’s not her fault. But any time I see her goddamn profile pic on Facebook, partying on some beach or other, I feel this horrible curdling in my stomach."
    # nat_bar_angry_speaking
    nat bar_ag_sp "Here I am coming up on my fifth year of service at fucking Tesco, while she waltzed into a high-paying finance job right out of uni."
    # nat_bar_annoyed_speaking
    nat bar_an_sp "I barely leave my flat, and she’s going out on amazing holidays to Spain with the money she makes from that great job, having sex with all the beautiful people she wants while I’ve not even had a girl look at me since uni—"

    nrt "You froze up after that one. That was too far. The whole thing had been too far. You were supposed to be catching up with friends, not going on a tirade about the fact your supposed closest friend actually enjoyed her life."
    nrt "Lillian was staring at you, not interrupting your rant. She was going to be so disappointed. She must have hated you. Who wouldn’t, after some shit like that."
    # lil_bar_sad_speaking
    hide l_bar_sa
    show l_bar_ap_ns_sp
    lil "…I didn’t realise you’d been having it so hard, Nat. I’m so sorry."
    # lil_bar_sympathetic
    hide l_bar_ap_ns_sp
    show l_bar_sy
    nrt "Against all odds, to your great surprise, Lillian reached out and brushed away the tears that had been forming on your cheek."
    nrt "You melted into her touch, all but sobbing into her. She pulled you closer, letting you shake in her arms. Maybe people were staring. You didn’t care."
    # nat_bar_sad_speaking
    nat bar_sa_ec_sp "And I feel so shitty cause it’s not like it’s her fault she has such a great life."
    # nat_bar_sad_speaking
    nat bar_sa_ec_sp "What’s she meant to do, not get a first on her extremely prestigious degree? Not get a great job with that qualification? Not spend the money from that job doing stuff that makes her happy?"
    # nat_bar_sad_eyesclosed_speaking
    nat bar_sa_ec_sp "Suffer like I have?"
    # lil_bar_sad_speaking
    hide l_bar_sy
    show l_bar_s_sp
    lil "Oh, Nat."
    # lil_bar_sad
    hide l_bar_s_sp
    show l_bar_sa
    nrt "Lillian started rubbing soothing circles into your hair. You were sobbing openly now. Good god you were pathetic."
    nrt "She whispered softly to you as you cried, giving you the comfort you hadn’t felt in… You couldn’t even remember the last time you felt like that."

    wai "Excuse me, miss, is everything alright? Anything I can do—"
    # lil_bar_angry_speaking
    hide l_bar_sa
    show l_bar_ag_sp
    lil "She’s fine."
    lil "Bring her a glass of water."
    # lil_bar_angry
    hide l_bar_ag_sp
    show l_bar_ag
    wai "Oh. Of course, right away."

    nrt "The waitress scurried away as you continued to sob, clutching to Lillian like the lifeline she was."

    # lil_bar_sad_speaking
    hide l_bar_ag
    show l_bar_s_sp 
    lil "Tell me about it."
    # lil_bar_sad
    hide l_bar_s_sp
    show l_bar_sa
    # nat_bar_surprised_speaking
    nat bar_su_sp "About… it? What?"
    # lil_bar_sad_speaking
    hide l_bar_sa
    show l_bar_s_sp 
    lil "Your life. Your worries. The things that make you so distressed."
    lil "I want to know what’s made you so hurt."
    # lil_bar_sad
    hide l_bar_s_sp
    show l_bar_sa
    # nat_bar_sad_speaking
    nat bar_su_sp "Oh. Um. Everything, kinda?"
    # nat_bar_sad_eyeclosed_speaking
    nat bar_sa_ec_sp "I hate my job. I hate knowing that I’m overqualified for it but feeling useless anyway. I hate that my boss keeps promoting white guys who suck his dick while I do way better numbers than them."
    # nat_bar_angry_speaking
    nat bar_ag_sp "I hate that I even know about my fucking numbers. I hate this fucking job so fucking much it makes me want to fucking kill myself, but that would require me to actually get off my lazy bitch ass and do it."
    # nat_bar_sad_eyeclosed_speaking
    nat bar_sa_ec_sp "I hate that I have nothing going on at all. "
    nat bar_sa_ec_sp "I hate that I have no hobbies and no friends, I hate that I don’t meet anyone. I hate that any time anyone asks me what I’ve done I don’t have anything to say cause I haven’t done anything cause I may as well not fucking exist."
    # nat_bar_angry_speaking
    nat bar_ag_sp "I hate that my parents are supporting my little brother the whole way through his uni while they barely did anything for me. I hate that I let Ciara talk shit on my family, and I hate that I didn’t join in shitting on them harder."
    # nat_bar_sad_speaking
    nat bar_sa_ec_sp "…I fucking hate being a lesbian sometimes. And I hate thinking that because then they fucking win. But I fucking hate that no one ever gets it, you know?"
    # lil_bar_sad_speaking
    hide l_bar_sa
    show l_bar_s_sp 
    lil "I know."
    # lil_bar_sad
    hide l_bar_s_sp
    show l_bar_sa
    nrt "And Lillian did know. You could tell, in that moment, as her grip tightened ever so slightly on you. She understood."
    nrt "She felt that alienation you did, the unspoken disconnect from everyone else you meet. The men for whom you’re either a punchline, a fetish, or both. "
    nrt "The women who become just a little more stand-offish once they know you might want to fuck them."
    nrt "It shouldn’t be so basic. It should be more complex than that, in this day and age. You have all the rights, all the societal acceptance. You get to see girls kissing girls on any TV shows you want."
    nrt "But it never stops the gut reactions. The little ways people change once they know. Consciously or subconsciously, but always there, always painting you in their minds as someone different. Someone other."
    nrt "As if you weren’t used to that already."

    wai "Your water, miss."
    # nat_bar_surprised_speaking
    nat bar_su_sp "Oh! Thank you. I’m sorry."

    nrt "She clearly looked at you with concern, taking in your tear-stained mascara and general state of distraught weeping."

    # lil_bar_angry_speaking
    hide l_bar_sa
    show l_bar_ag_sp
    lil "I’ll take that."
    # lil_bar_happy_speaking
    hide l_bar_ag_sp
    show l_bar_h_sp
    lil "Here, drink this."
    # lil_bar_sympathetic
    hide l_bar_h_sp
    show l_bar_sy
    nrt "The waitress scurried away as Lillian lifted the glass to your lips. You drank it down greedily, coming a little to your senses in the process."
    nrt "What the fuck were you doing."

    # nat_bar_surprised_speaking
    nat bar_su_sp "Shit, I’m sorry."
    # nat_bar_sad_speaking
    nat bar_sa_sp "I’m so sorry, I ruined everything."
    # nat_bar_awkward_speaking
    nat bar_aw_sp "I should go, I’m sorry."
    # lil_bar_neutral_smile_speaking
    hide l_bar_sy
    show l_bar_n_s_sp
    lil "Shhh, it’s alright."

    nrt "Lillian pulled you back close again, holding you tightly, whispering into your hair."
    # lil_bar_happy_blush_speaking
    hide l_bar_n_s_sp
    show l_bar_h_bl_sp
    lil "I’ve got you, Natalie."
    # lil_bar_happy_blush_speaking
    lil "I’m not going to let anyone hurt you ever again."
    # lil_bar_happy_blush
    hide l_bar_h_bl_sp
    show l_bar_h_bl
    nrt "You sobbed wordlessly into her shoulder, your breathing unsteady and ragged. You couldn’t even respond to her kindness with words. Fucking wretch."
    # lil_bar_flirting_speaking
    hide l_bar_h_bl
    show l_bar_fl_sp
    lil "Here, have a little more water."
    # lil_bar_flirting
    hide l_bar_fl_sp
    show l_bar_fl
    nrt "Lillian offered you the cup of water again. You weren’t sure if it was your head, the tears, the two cocktails already burning in your gut, or the shitty pub glasses, but for some reason this time it tasted kind of… weird?"

    # nat_bar_neutral_speaking
    nat bar_ne_sp "Thanks."
    # nat_bar_shy_blush_speaking
    nat bar_ne_sd_bl_sp "You’re… so amazing, Lillian."
    # lil_bar_happy_blush_speaking
    hide l_bar_fl
    show l_bar_h_bl_sp
    lil "Oh, not at all."
    # lil_bar_flirting_speaking
    hide l_bar_h_bl_sp
    show l_bar_fl_sp
    lil "I only want what’s best for you, Natalie."
    # lil_bar_flirting
    hide l_bar_fl_sp
    show l_bar_fl
    nrt "You think you might have been about to blurt out something about how much you wanted to kiss her. Or maybe you actually did try to kiss her. Maybe you just faceplanted back into her shoulder again."
    nrt "You can’t tell. You might never be able to tell. From that point on, the rest of the night is nothing but a hazy blur."

    jump scene4
