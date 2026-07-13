label flashback1:
    scene bg_bar with fade
    play music "audio/Bar.mp3" loop fadeout 1.0 fadein 3.0

    nrt "A little more of the night seems to have become clear to you, thankfully. Or perhaps not so thankfully, given how badly you apparently embarrassed yourself."
    nrt "Although embarrassing yourself isn't really anything new for you, is it?"
    nrt "You remember your arrival, that the bar was busy enough that it took you a while of wandering around aimlessly to find the right table, but not quite so bustling that you’d struggle to hear each other."
    nrt "Upside, you got to hear Lillian all night without having to yell {b}\"What was that?\"{/b} every other sentence. Downside, Lillian got to hear {b}you{/b} without any benefit of the doubt as to what stupid shit you actually said."
    nrt "Lillian wasn't actually there when you arrived, you remember that now. You finally found Ciara tucked away in a corner on the least trashed looking sofa in the place, a half-empty pint of Guinness already on the table in front of her."

    show c_ch_sp with dissolve
    cra "Hey! You made it!"
    hide c_ch_sp
    show c_ch_ec

    nat bar_ap_sp "Of c ourse! Sorry I'm late."

    # Shuffling SFX to indicate Natalie sitting down next to her

    hide c_ch_ec
    show c_ch_w_sp
    cra "Ah don't worry about it, more like I'm too feckin' early for once."
    hide c_ch_w_sp
    show c_n_s

    nat bar_ne_sp "Still, sorry."
    nat bar_ne_s_sp "Oh, it's nice to see you again!"

    nrt "Almost impressive that you managed to forget the {b}absolute{/b} basics of politeness, less than ten seconds in. You had the whole night ahead of you to fuck up."

    hide c_n_s
    show c_n_s_sp
    cra "Aye, same! Been far too long."
    hide c_n_s_sp
    show c_n_s

    nat bar_ne_sd_bl_sp "Um... Where's Lillian?"

    nth "(Hope I didn't sound too desperate...)"
    nrt "You definitely did."

    hide c_n_s
    show c_n_sp
    cra "Late shift at the lab, said she'd be here in a wee bit."

    hide c_n_sp
    show c_ch_w_sp
    cra "I said we could do another day, but she was all, {i}\"No, no, don’t worry about it, Wednesday works better for Nat.\"{/i}"
    hide c_ch_w_sp
    show c_ch_ec

    nrt "Ciara rolled her eyes as she said that, laughing at some joke that clearly only she understood."

    nat bar_ne_sp "Oh, she really shouldn't have troubled herself so badly."

    hide c_ch_ec
    show c_h_sp
    cra "Nahhh it's grand."

    hide c_h_sp
    show c_n_s_sp
    cra "Apparently she has tomorrow off anyway, seemed to think that might come in handy after a night out drinking with us."

    hide c_n_s_sp
    show c_ch_w_sp
    cra "For some reason."
    hide c_ch_w_sp
    show c_ch_ec

    nrt "Your memories of just how much Ciara could drink at uni came flooding back to you, at roughly the same time as your memory of your 9AM opening shift the next day."
    nrt "This might go a long way to explaining the state you've found yourself in, now that aforementioned next day has arrived."

    nat bar_ne_s_sp "With {i}us?{/i} I'm not sure I'm contributing more than a drop in the bucket compared to you."

    hide c_ch_ec
    show c_ag_ec_sp
    cra "Hey, that's an unfair and harmful stereotype of Irish people!"

    hide c_ag_ec_sp
    show c_ag_ec_l_sp
    cra "And furthermore-"

    hide c_ag_ec_l_sp
    show c_ag_ec

    nat bar_aw_sp "Oh my god I'm so sorry."

    hide c_ag_ec
    show c_ca_sp
    cra "Nat. I'm fuckin' with you. It's fine."
    hide c_ca_sp

    hide c_ag_ec
    show c_sy_sp
    cra "Figure if my heritage is gonna get potato jokes thrown at me all through undergrad, least it can do is give me the metabolism of a feckin’ mule."
    hide c_sy_sp
    show c_sy

    nat bar_ag_sp "That was awful, though."

    hide c_sy
    show c_n_sp
    cra "Eh, you had it worse."
    hide c_n_sp
    show c_n

    nrt "She was right, of course. Before, during, and after uni. But you {b}really{/b} didn’t feel like getting into that particular can of worms, so you decided to just leave it with:"

    nat bar_ap_sp "I’ll drink to that."

    nat bar_ne_sp "Speaking of, I should probably go grab a drink, since you’ve already started."

    hide c_n
    show c_n_s_sp
    cra "Oh yeah, there’s a whole app for that here."
    hide c_n_s_sp
    show c_n_s

    nat bar_ne_s_sp "Oh, of course there is."

    show c_n_s_sp
    cra "Bit of a hanlin, but you scan this wee QR code here with your phone, brings up the menu."
    hide c_n_s_sp
    show c_n_s

    nat bar_ne_s_sp "Right, thanks."

    nrt "You scanned through the menu, idly skimming past beers you knew you were never going to order."
    nrt "You’re still struggling to remember exactly what you ordered. A cocktail, right? You usually prefer cocktails. And it must have been pretty strong to leave you as destroyed as you are now."

    nat bar_ne_sp "How long did yours take to arrive?"

    hide c_n_s
    show c_n_sp
    cra "Only a minute or two, they’re pretty quick here. Helps that the place isn’t totally heaving."
    hide c_n_sp
    show c_n

    nat bar_ne_sp "Is it usually busier than this, then?"

    show c_n_sp
    cra "Probably? I’ve not actually been til now, picked it cause it’s basically round the corner from Lillian’s place."
    hide c_n_sp
    show c_ch_w_sp
    cra "And I guess it’s somewhere a bit more low-key than my usual haunts, so we can actually hear ourselves."
    hide c_ch_w_sp
    show c_ch_ec
    hide c_ch_ec
    #############
    show c_ch_w_sp
    cra "Doesn’t hurt that the staff are all stunnin’ as well."
    hide c_ch_w_sp
    show c_ch_w
    nrt "You hadn’t been paying close attention while scanning around the room for Ciara herself, but once you had a minute to follow her eyeline, she was not wrong."
    nrt "Naturally, you skimmed right past the bartender with the man-bun and close-cropped beard that you are all too aware is **exactly **Ciara’s type, and landed on the pretty waitress next to him."
    # ciara_chaotic_wink_speaking
    hide c_ch_w
    show c_ch_w_sp
    cra "You seeing what I’m seeing?"
    # ciara_chaotic_wink
    hide c_ch_w_sp
    show c_ch_w
    nrt "That she had incredible legs, and was wearing thigh-high stockings that drew both sets of eyes directly to that fact? Yes. Yes you were very much seeing that."
    nrt "But you also knew your part in this little skit. You’d play coy, while Ciara acted the horndog, and many a laugh would be shared."
    # nat_neutral_smile_sideeye
    nat bar_an_sp "Oh, behave."
    # ciara_happy
    hide c_ch_w
    show c_h
    nrt "You both laughed along at that, your wandering eyes returning from the pleasant view."
    nrt "Normally, that was the height of it, just looking and appreciating. Sometimes, depending on how much alcohol had been consumed, Ciara would end up approaching someone."
    nrt "Whether that was on your behalf or her own really depended on how the night had been going, and was unlikely to have been on the cards last night."
    hide c_h
    show c_n_s_sp
    cra "Anyway, what ye been up to since uni? Done anythin’ interesting? Done anyone interesting?"
    ####################
    hide c_n_s_sp
    show c_ch_ec

    nrt "She raised an eyebrow, smirking again at some hidden joke."

    nat bar_ne_sd_bl_sp "Um… Maybe we should wait til I’ve had a drink to start on kissing and telling, haha."

    nrt "Girl {b}what{/b} was there to tell."

    hide c_ch_ec
    show c_ch_ec_sp
    cra "Suit yersel’. I was gonna tell you all about finally getting to live out the bi dream last year. Met this {i}gorgeous{/i} couple out in Spain, an’ {i}Jesus Mary and Joseph,{/i} Nat, when I tell you they were both fit as {i}fuck—{/i}"
    hide c_ch_ec_sp
    show c_ch_ec

    wai "Ahem. Your aperol spritz, miss."

    nat bar_ap_sp "Oh, thank y—"

    nrt "You glanced up at the pretty waitress with enough gratitude that you hoped it might almost make up for how badly you and Ciara had been ogling her earlier."
    nrt "However, that appreciation was immediately discarded as a goddess truly worth appreciating arrived."

    hide c_n
    hide c_ca_sp
    show c_ch_ec at move_to_right

    show l_bar_h_sp at char_left with moveinleft
    lil "Good evening, both of you!"

    jump scene2
    # hide l_bar_h_sp
    # hide c_ch_ec

    # show l_bar_n 
    # wai "Could I get you anything else, hun?"
    # nat bar_su_sp "Oh!, uh-"
    # hide l_bar_n
    # show l_bar_ag_sp
    # lil "She's fine."





