label scene2:
    #SCENE 2

    # Bedroom bg.
    show bed_day with fade
    # lil_neutral_smile
    show l_n_s with dissolve
    nrt "The door swings gently open, and Lillian enters, a steaming plate of bacon, sausages, and eggs in her hands."
    nrt "The smell is absolutely divine. The food, not Lillian. Well, maybe Lillian too."
    nrt "Definitely not you, anyway. Did you even fix up your hair while she was out?"
    # lil_happy_speaking
    hide l_n_s
    show l_h_sp
    lil "Lunch is served, hope you’re hungry!"
    # lil_happy
    hide l_h_sp
    show l_h
    # nat_happy_speaking
    nat h_sp "Smells amazing, thank you!"
    # lil_sympathetic
    hide l_h
    show l_sy
    nrt "Lillian’s expression turns softer, clearly concerned for you, for some reason."
    # lil_sympathetic_speaking
    hide l_sy
    show l_ap_sp
    lil "How are you feeling, can you sit up?"
    # lil_sympathetic
    hide l_ap_sp
    show l_sy
    nrt "You try to nod. {b}That{/b} was a mistake. Instead, you attempt to force your head higher on the bedframe."
    nrt "It feels like you’re pushing a giant lead ball with limbs made of jelly. You look, presumably, something like a caterpillar squirming in treacle."
    nrt "Seeing your situation, Lillian takes pity on you. She sets the plate down on the bedside table, next to the banana peel, and sits down on the bed."
    # possibly have Lillian’s sprite move closer, or move across to the left during this part?
    nrt "She gently puts her hand behind your shoulder, and her touch feels so soft and assured that any words of thanks you might have been attempting to form disappear entirely into the bliss of Lillian calmly rearranging your body."
    nrt "She helps you into a sitting position, leaning across you to grab a pillow."
    # nat_neutral_smile_sideeye_blush
    nth ne_s_sd_bl "(OK, definitely not just the food that smells nice.)"
    nrt "She slots the pillow behind your head, letting you finish wiggling into place."
    # lil_sympathetic_speaking
    hide l_sy
    show l_ap_sp
    lil "Better?"
    # lil_sympathetic
    hide l_ap_sp
    show l_sy
    # nat_neutral_smile_speaking
    nat n_s_sp "Yeah, thanks."
    # nat_shy_blush_speaking
    nat sh_bl_sp "You smell great."
    nrt "You fucking idiot."
    # nat_surprised_blush_speaking
    nat su_bl_sp "I mean the food! The, um, bacon. And eggs. And sausages too? They all smell, uh great."
    # lil_neutral_smile_speaking_blush
    hide l_sy
    show l_h_sp_bl
    lil "Thank you, Nat."
    # lil_neutral_smile
    hide l_h_sp_bl
    show l_n_s
    nrt "Lillian smiles kindly at you, and her response sounds genuine, which is crazy because right now you have all the charisma of a literal slug."
    nrt "She’s still sitting on the bed, close enough that the mattress is tilting you towards her. Definitely the only reason you can’t tear your eyes away from her face."
    # Possibly adjust the sprite here to show her moving or leaning? Idk maybe this part should just be cut
    nrt "Lillian leans over the side of the bed, and you quickly avert your eyes from the temptation to stare too intently at the results of that motion."
    nrt "Because apparently you’re a horny fourteen year old boy."
    nrt "While simultaneously being a sickly Victorian woman who will require weeks of bedrest and a hysteria diagnosis at the mere thought of your gorgeous friend’s boobs under the sway of gravity."
    nrt "The sudden motion of something being dropped over you on the bed startles you out of your consideration of the merits of dying of consumption."
    nrt "Lillian’s set down a bed tray… table… thing? You hadn’t even seen it down the side of the bed until she grabbed it just now, but the value is immediately obvious, as she sets the plate of food on top of it and it barely wobbles."
    # lil_happy_speaking
    hide l_n_s
    show l_h_sp
    lil "Bon appetit!"
    # lil_happy
    hide l_h_sp
    show l_h
    nrt "French phrase between two Chinese-Brits over a meal combination that was technically popularised in America by Sigmund Freud."
    nrt "You definitely watch too many pointless Youtube documentaries to know that tidbit, but it’s quite funny nonetheless."
    # nat_happy_speaking
    nat h_sp "Itadakimasu!"
    nrt "Alright fair enough, that was pretty clever. Don’t let it go to your head."
    # SFX of cutlery clinking on a plate throughout this section
    nrt "Lillian chuckles at your running with the language joke as you reach with slightly unresponsive fingers to cut off a small piece of bacon, carefully slicing and scooping some egg white onto the fork before chewing slowly."
    nrt "You’re trying not to just wolf everything down on a mostly-empty stomach, but wow, {b}wow{/b} that tastes {b}divine.{/b}"
    nrt "Maybe it’s the hangover talking, but this has to be the nicest bacon and eggs you’ve ever tasted. A quick bite confirms that the sausage is just as good too."
    nrt "{b}Way{/b} better than your dad’s, full offence intended. Only thing he ever even cooked was the Full English, maybe a barbecue on one of the three sunny days of the year, left the rest of the cooking to your mum."
    nrt "You’d think he’d have at least got the hang of not making the bacon too soggy by now, but honestly you could barely tell the difference between his signature fry up and the three-item breakfast you used to get from the campus cafeteria."
    nrt "Well, before you’d run out of the money for even that luxury, anyway."
    nrt "If you’d known Lillian was this good a cook back at uni, you never would have lifted another crappy plastic tray in that godforsaken place again."
    nrt "Hell, if you’d known she was willing to pamper you and feed you bacon and eggs in bed, you probably would’ve never made it to another lecture."
    nrt "Not that you were making it to many by the time you met Lillian in the first place. The first term of your Masters, sure, but by the end you were basically only attending the classes you were being paid to help with."
    nrt "Some scientist you turned out to be, eh?"
    nrt "Never mind that you probably would have died of shame at being looked after by one of your own undergrad students that you were ostensibly meant to be supervising."
    nrt "Honestly, actually stopping to think about it now, it still feels weird."
    nrt "Oh sure you can justify to yourself that she’s only a couple of years younger, that it was years ago, and that half the girls you knew in undergrad were dating PhD students anyway."
    nrt "You still feel a little bit ashamed at having Lillian take such good care of you."
    nrt "Dating? When did {b}dating{/b} become a part of this conversation? You think Lillian’s treating you with {b}girlfriend-like{/b} affection?"
    nrt "What part of this reads to you as {b}anything{/b} more than sympathy for her idiot fuckup of a former supervisor who couldn’t even finish her own Masters, let alone help Lillian with her second year of undergrad like you were supposed to?"
    nrt "The absolute fucking delusion on you, Natalie."
    # lil_neutral_speaking
    hide l_h
    show l_n_sp
    lil "So how was it?"
    # lil_neutral
    hide l_n_sp
    show l_n
    nrt "In your demented mental ramblings about ever being able to land a girlfriend on even a single percentage of Lillian’s level, you barely noticed that you’ve chewed your way through almost the entire plate of food."
    nrt "Clearly you needed it, although you could have paid a little more attention to your friend’s wonderful cooking."
    # nat_happy_speaking
    nat h_sp "Am-amashing."
    nrt "Finish swallowing your food, idiot."
    # nat_apologetic_speaking
    nat ap_sp "Sorry. That was so good Lillian, I know you said you were a good cook but like, holy shit that was exactly what I needed."
    # lil_neutral_smile_speaking
    hide l_n
    show l_n_s_sp
    lil "Thank you, Nat! It’s been a while since I’ve got to share my cooking with anyone, I’m really glad you enjoyed it."
    # nat_neutral_smile_speaking
    nat ne_s_sp "Seriously, best bacon and eggs I’ve ever had!"
    # lil_happy_blush
    hide l_n_s_sp
    show l_h_bl
    nrt "Lillian flushes a little, smiling in delight. Has nobody really ever complimented her cooking like this before?"
    # lil_happy_blush_speaking
    hide l_h_bl
    show l_h_sp_bl
    lil "You’re so sweet. Sweet enough that I might just cook you dinner as well, especially if you promise to be just as nice about that!"
    # lil_happy_blush
    hide l_h_sp_bl
    show l_h_bl
    # nat_neutral_smile_speaking
    nat ne_s_sp "Really? That would be great, thanks so much!"
    # nat_sideeye_blush_smile_speaking
    nat sd_bl_s_sp "I’ll be the absolute nicest I’ve ever been for you."
    # lil_flirting_speaking
    hide l_h_bl
    show l_fl_sp
    lil "Oh, but you’re always {i}such{/i} a good girl for me, aren’t you Nat?"
    # lil_flirting
    hide l_fl_sp
    show l_fl
    nrt "…"
    nrt "Holy shit."
    nrt "Did she just say that?"
    nrt "Earth to Natalie? You gonna respond any time soon?"
    # nat_surprised_blush_speaking
    nat su_bl_sp "I- uh- yuh- I can be, um, yeah?"
    nrt "Before you can utter any further inane drivel, Lillian lifts your hand and presses a soft kiss to your knuckles."
    # Sky Knuckle Kiss CG
    nrt "She does it so effortlessly, so confidently, that it takes a moment for you to register the enormity of what she just did. You can’t even babble now, simply staring at her in abject wonder, certain that your face is completely red."
    # no Lillian sprites here, just let the CG stay there
    hide l_fl
    show l_fl_sp
    lil "Then keep being good and rest up, OK? You don’t need to worry about anything."
    lil "I’ll take care of everything for you, Natalie."
    hide l_fl_sp
    show l_fl
    nrt "She all but whispers the words against your hand, it was almost a struggle to hear them over the frantic pounding of your heart."
    nrt "Lillian stands from the bed, holding your hand for just a moment longer, smiling down at you with such radiant care that you almost want to dissolve into nothingness, become a pure being of warmth under her care."
    hide l_fl with dissolve
    nrt "She turns towards the door, her soft footsteps the only sound in the room other than your beating heart."
    # nat_surprised_blush_speaking
    nat su_bl_sp "Thank you."
    nrt "You call after her as the door closes. You hope she understands just how desperately you mean it."
    jump flashback2