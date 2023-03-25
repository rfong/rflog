---
layout: post
title: RC sp1'23&#58; having a body and goals
tags: [having-a-body, recurse-center, brain-hygiene]
description: 6 weeks of debugging physical issues, within the accountability timebox of Recurse Center's core hours
---

So far, I've spent much of the first half of my current RC batch becoming intimately re-acquainted with sedentary ergonomics, as well as **the inverse relationship between my computer flow state and my ability to take care of my physical body**.

This worked out in my youth when I could mystically bounce back from horrific sleep deprivation and no ergonomics in a matter of 24 hours, but proves to be very hard in my 30s.

As a result of my Nonstop Catastrophe Pileup Year of 2022 (the capstone project of my Ph.D in Myself, which I began long ago, but only started working on full-time during the highly nonconsensual Great Unpleasantness of 2020), it was very challenging to jump back into computer "work hours" from a cold-turkey 10-month emergency leave, even though my time at Recurse is fully self-structured.

A 6-week overview of workflow obstacles, and what I did about them.

## Week 1 - Oops, acute illness! 😷
I briefly had some kind of flu at the very beginning of my batch, which threw me off for most of the week. Getting sick seems to be my body's post-2020 reflexive response to returning to full-time desk job hours, which kind of makes sense when you think about [how the lymphatic aspect of the immune system works](https://rfong.github.io/rflog/2022/03/23/brain-hygiene-sp22#movement).

I tried to stare at my screen, but quickly realized that was unproductive. Then I let my body sleep as much as it wanted, because I know from extensive experience how much of a difference that makes for recovery.

On the bright side, since I'm currently in remission, this was the shortest and least severe illness I've had in 4 years!

## Week 2 - Mental spinup 🧠
I spent this week spinning up my [brain hygiene scaffolding](https://rfong.github.io/rflog/2022/03/23/brain-hygiene-sp22/) and stretching my programmer muscles again. I was worried after my 10-month break that I'd completely lost my code mojo, but it started coming back after a few good exercises.

I'm thankful for all the work and development I've put into my brain hygiene routines, and felt ready to fling myself into projects. Little did I remember to account for...

## Week 3 - Being in my 30s means I actually have to take care of my body 😬

### Temperature 🥶
The place I live is metaphorically freezing (literally, about 55-60F or 13-15C) when the (very expensive) heating isn't on. Some people can function indoors like this, but I have exceptionally bad cold resistance, so my extremities and brain go fully numb at this temperature. My place is very badly insulated, and is often mysteriously colder than the outdoors.

I weatherstripped our drafty front door, noticeably improving our heat retention. I also built a habit of putting on all my warm winter triple-layers and thick wool socks immediately after waking up in the morning, instead of waiting until I was already freezing and brain-dead.

### Office & computer ergonomics ⌨️
Very thankful for the [split ergonomic mechanical trackpoint-enabled keyboard](https://rfong.github.io/rflog/tag/keyboard/) I built in 2021 to relieve my tendonitis and RSI. All the other changes I made this time around were minor efforts by comparison.

- Got low back pain, acquired a new chair to try, reviewed PT exercises
- Got some mouse-related hand pain. Tried the [Ploopy trackball mouse](https://ploopy.co/) I assembled recently -- unfortunately too big for my hand
- Made a todo list of minor ergonomic tweaks I want to make to my trackpoint module
- Got a new personal computer

**Don't try to practice your profession with an inadequate core tool.** My personal computer successfully lasted me from 2014-2023, where by "successfully" I mean that it can compile my code just fine. However, it is unable to deal with modern bloatware, which was holding me back from participating at Recurse in important ways, such as pair programming over Zoom. I finally ordered a new computer, and subsequently spent chunks of later weeks setting it up.

### Nutrition 🌯
I kept getting really hungry for some reason, to the point of hypoglycemia / fainting. Then there was a day where I ate 5 full hearty meals and still felt starved, which was very suspicious. From experience, it probably meant that I wasn't getting enough of some macronutrient (protein/fat/carb). 

My coop housemates are still getting accustomed to scaling up their cooking for 6+ people, and I realized that the others were not cooking enough protein to sustain my high basal metabolism. 

We had a check-in about **macronutrient ratios in house meals**, and I started buying more **nutty snacks** to patch my disproportionately high protein requirements, since none of my other housemates were fainting from hunger. (All bodies are different!)

My hypoglycemia issue seemed to be fixed after about a week of protein-rich snacky experimentation and meal adjustment, by the end of Week 4. 

## Week 4 - Flow state, goal alignment, & followups 🌊

### Followups ➡️

As previously stated, I spent a decent chunk of Week 4 following up from Week 3 by fixing my nutrition-related fatigue and setting up my new computer, which arrived at the end of Week 4!

### Scheduling the day to avoid interrupts & facilitate flow 📢

Programmers and ADHD-folk work best in large chunks of time with minimal interrupts. I had previously been able to cowork on some of my more administrative work out in the living room with my housemates, but switched back to strictly headphones-coworking or quiet-coworking for RC.

I've been facilitating flow state by hosting **Minimum Viable Code (MVC)**, a 45-minute timebox where you stop overthinking things and just take the fastest path to write at least one line of code on a project you've been procrastinating or feeling stalled on. (After the first line, you can write more if you feel like it -- the first is the hardest.)

MVC has been working fantastically well for me, but I had ambitiously scheduled MVC too early for me to finish all my morning wake-up chores. This meant:
1. I would make incredible progress during MVC,
2. shut my computer and rush off to make breakfast and feed the cats,
3. and promptly lose flow state for the rest of the day.

I **rescheduled** the event to a slightly later time that would allow me to fully wrap up my morning chores before MVC, and be free to continue coasting through the rest of the morning on my MVC momentum.

### Consciously trimming my commitments ✂️

Although I love the distributed systems paper discussion group and have often found it industry-relevant, I realized that my participation in it this time around didn't align with my RC goal of writing more code.

With more standalone algorithms papers, you can actually implement them yourself on your personal computer in a satisfying way. 

**Modern industry-based distributed systems papers** are very different. They're generally quite dense, with 20+ references to various other distsys component frameworks (often [Apache Foundation](https://apache.org/) or similar), with specific pros, cons, and background context accompanying each of those references.

It's also somewhat unlikely you'll get a satisfying implementation exercise out of them, because they're all something along the lines of: "here is a very simple and intuitive abstract systems concept, which we needed to build into a reliable, high-throughput global service transferring petabytes of data a day between multi-region servers. *It was really hard.* Here's a slightly proprietary-censored summary of how several teams of software engineers spent years doing it."

First of all, **I simply needed way more time to thoroughly read the weekly paper** than I was allotting myself. I tried addressing this by scheduling a **Paper Reading Accountability group** the day before the discussion. 

This gave me enough time to get a decent shallow understanding of the paper, but I was left with so many more followups that I didn't have time to pursue. (What did the authors actually do for implementation in the gaps that they didn't adequately explain in the paper? Which of the 20 followups, side references, and use cases was I going to prioritize learning about?) It might take 15-20 hrs/week of my precious RC time to actually give this material a fraction of the attention it deserves, and I wouldn't even be writing code during that time.

After this experiment, I decided to suspend my commitment to distsys reading group until I'm back in industry again with a specific use case motivating me to read some paper.

## Week 5 - MacOS-Ruby environment 💢

At the end of Week 4, I realized that my code blog (written in Jekyll) no longer compiled because my Ruby version manager was broken for some reason. I then got stuck for a few days, bleeding over into the start of Week 5, on **fixing my Ruby environment**.

(This was a problem I kept revisiting in little spurts; I wasn't working on it *nonstop* for two days, because I find it extremely demoralizing to be in OS-level dependency hell.)

Background context: MacOS ships with a system version of Ruby. If you try to mess with that particular version, you may get into a bad state where you need to factory reset the whole machine. This is why developers must use Ruby version managers to manage version switching without destroying their environments, and why managing Ruby on MacOS is notoriously riddled with tricky pitfalls. (NEVER call a `gem` command with `sudo` on a Mac.)

My usual version manager, `rvm`, didn't seem to want to work on my new OS (or chip architecture; not sure), and as a bonus, `rvm` is also very weird to uninstall. I successfully did not destroy my environment in the process of attempting to salvage `rvm`, giving up and manually deleting all references to its existence, unsuccessfully trying `chruby`, and finally switching to `rbenv`, **and now I can post to this blog again**.

### There was also a shooting near my house 😩

It was scary, and we have a quantity of followup logistics to deal with as a result of it! That is all.

## Week 6 - Tackling seasonal depression ☀️

California receives so little rain that we have been in a declared emergency state of drought for several years. This is very bad for the environment, but great for not having seasonal depression, which I moved away from the East Coast to escape.

This year, we mystically received so much rain that we slingshotted around to being in an emergency state of flooding, and **the sky has been overcast for weeks at a time**, for months longer than usual. 

I crucially need to get blasted in the face with sunlight in the morning to have any hope of functioning, so I have been very drowsy this winter, and I keep accidentally passing out in the middle of the day. It's not very conducive to spending my daytime hours attending (virtual) Recurse!

I bought a **sun clock and a super-bright SAD (Seasonal Affective Disorder) lamp** to try fixing my circadian rhythm with. Set them up last night and so far so good; I actually woke up on time this morning and felt good doing it!

## And that's where I am now! 🙌

I spent 6 weeks doing Recurse less fully than I would have liked, but I did indeed write some neat code (to be revealed) while successfully debugging my previously crippling:
- macronutrient intake
- computer setup & physical office setup
- sleep schedule & narcolepsy issues
- schedule blocking & RC time commitments
- temperature issues & bad thermoregulation

My college self would have scoffed at this entire list as the work of a fussy hypochondriac, but my present-day self is all too aware of the difference a decade makes in a body. What new unknown-unknown blockers will rear their heads next and rudely remind me that my body is aging?? 

Hopefully I won't encounter anything else too rude going forward, because I have so many projects I want to blaze forward on! I'm tired of being sleepy all day. Give me that sun juice, or I'll get it myself, with the power of fake sun.
