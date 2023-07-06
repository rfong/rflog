---
layout: post
title: Maximizing your time at Recurse Center, 2023 edition
tags: [hot-tips, recurse-center]
techTags: haskell
description: With two full batches and a couple of mini-excursions to Recurse under my belt, I feel at ease summoning the spirit of RC any time. An updated summary of my hot tips for getting the most out of your RC batch.
---

As always, it's not a bootcamp. It's a (free) retreat for programmers who are enthusiastic about self-directed improvement and the power of community.

My time at [Recurse Center](https://recurse.com/) includes:
- an in-person 1-week minibatch in Feb 2020 (RIP)
- two remote full 12-week batches, in 2021 & 2023
- a few weeks of an unfortunately timed 2022 batch that I dropped out of early in order to provide end-of-life hospice care to [my old cat](https://reesekitty.com), because loved ones are more important than career.

# Before you even apply

If you have any flexibility in your timing: are you applying to a batch whose timing is seasonally and personally opportune for you?

I did my first full batch during summer, loved it, and met lovely people there I still keep in touch with. However, I chafed over the timing because gorgeous summer weather fills me with an uncontrollable craving to go backpacking, swim in alpine lakes, get on top of mountains, hike through redwood forests, meet new plants, tend to gardens, frolic outside with friends, and generally be as far away from a computer as humanly possible.

Since then, I've timed my batches not to coincide with peak gorgeous summer weather. My most recent batch overlapped with a lot of the rainy season, which was perfect.

# Preparing for RC

## Prepare a focus, but don't force yourself to stick to it

Go in with some well-defined focal points and goals just so that you have a clear starting point to work from. However, they might completely change over the course of RC, and that's ok.

I've met a few rare people who have the singular focus to make it through RC working on just one project the entire time. As a highly distractible and excitable person with a legendarily uncontrollable menagerie of hobbies, I am the polar opposite of that archetype. Most people fall somewhere in between.

## Examples of different RC goals & directions

A lot of programmers only think of technical goals at first. 

Topic | Vaguely defined direction | Example of a well-defined goal
--- | --- | ---
Technical | Get better at shaders | Work through [The Book of Shaders](https://thebookofshaders.com/) Chapter 1 today
Technical | Learn more about distributed systems | Have a reading group discussion about the [MapReduce paper](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf)
Technical | Learn how to implement computer science papers | Read the MapReduce paper and then implement the simplest possible local toy version of one section in Python today

Due to its open-ended nature, RC is a really valuable place not just to level up technically, but to improve your self-management skills and rediscover your sense of intrinsic motivation that has probably been snuffed out by industry and bureaucracy.

Topic | Vaguely defined direction | Example of a well-defined goal
--- | --- | ---
Self-management | Get better at managing my own time | Try working in 25-minute pomodoros today, then check in with myself to see if I want to tweak the approach
Self-management | Keep my body healthy during RC | Eat three meals today and go outside for a walk/run/bike before sunset, then try to do it again tomorrow
Self-management | Get better at focusing | Pick my top 2 interests and only work on those for this week
Fulfillment | Find out what sparks joy for me outside the stifling confines of industry | Attend Creative Coding meetup and spend 2 hours coding something silly from randomly generated prompts with no expectations
Fulfillment | Meet more wholesome and inclusive programmers | Have a coffee chat with one new RCer every week

(If you have trouble taking vaguely defined aspirations and breaking them down into bite-sized actionable goals, then you might enjoy my interactive worksheet-based zine, [Do The Thing: How To Do Anything](https://gum.co/dothething).)

### Interlude: pep talk about finding what motivates you (or doesn't)

You will hear the catchphrase "[volitional muscles](https://www.recurse.com/self-directives)" a lot at RC. It's your meta-ability to *know what intrinsically motivates you, and then make your own decisions based on that*, independent of societal norms about what everyone says is c0ol and hardk0re, or external job/money motivations. And really, what better way to improve your coding efficiency than to not write things you don't care about in the first place?

(Yes, at some point you will have to sell out again in order to pay for housing, food, and American "healthcare", but at least you can enter your next job search with a much better idea of how to align your work with your personal values and interests.)

### Interlude pt. 2: a Haskell anecdote

During my first ever RC experience, a minibatch in February 2020 (RIP), over half my batch (self included) unanimously said we wanted to learn Haskell and had never gotten around to it. So we all went to the Haskell 101 meetup, bristling with excitement. Haskell! We were finally going to do it!

The meetup organizer started livecoding Haskell and explaining what they were doing. To their credit, they were [super engaging and funny](/rflog/microblog/2020-02-20-rc-day-4/) and providing clear explanations. And yet, most of us, when faced with real Haskell exercises, quickly realized "Wow. I'm not actually interested in using Haskell at all; I just assumed I *should* be."

It was the single most valuable programmer-hour of my life in releasing ingrained programmer social norms about assuming I should automatically be interested in things that other programmers had always told me were cool and hardcore. I have saved many hours since then by *not* angsting about my lack of Haskell experience.

Knowing and doing what intrinsically motivates you is like any skill. It doesn't come naturally to everyone just because they thought of the concept. Like all skills, you need to *practice*, in little ways at first, and eventually in big ways.

## Grindy dependency setup

If you have any dependencies that are relevant to your planned starter projects, get them all set up before Day 1. Especially if they are horrifically big or weird installations like overdue operating system updates, core package manager updates, or anything that touches hardware or firmware.

Even with smaller routine dependencies, you'll be glad you set them up rather than wait until you are filled with extreme stoke during Week 1 and have grabbed a pairing station with someone you are excited to collaborate with, only to realize that you cannot start because your packages need an hour to install. 

If you'll be working in langs that may require you to have multiple versions installed on your machine simultaneously for reasons completely outside your control, such as Python or Ruby, I would **highly** recommend installing a language version manager for them, as it could save you several hours of mid-batch teeth-gnashing.

## Think about who you want to collaborate with (technically and energetically)

Your batchmates and their collective stoke are your best resource! Together, you become much greater than the sum of your parts. Without them, you'd just be hacking alone on your computer, which you could do any time at home.

I like to spend the day before a new batch plus much of my first week scoping out the interests of my batch and rolling with the flow for any intriguing topics that there is a lot of batch energy for. This is how I got into CRDTs, Rust, and [creative coding](https://rfong.github.io/creative-coding/)! 

Having enthusiastic accountabilibuddies also helped me overcome my activation energy to try things I'd always wanted to do, like work through [various distributed systems papers](https://pdos.csail.mit.edu/6.824/schedule.html) and play with [OpenSCAD](https://openscad.org/)!

I also like to scope out people whose personalities I feel kinship with, and try to reach out to them early. Of course, I never succeed at cramming every interesting person into my schedule, but I've made a lot of connections that feel good.

# During batch

I've written a lot about maximizing time during an RC batch, which you can find under my [#recurse-center](/rflog/tag/recurse-center/) tag.

- Mar 2023: [Having a body and goals](/rflog/2023/03/23/having-a-body/): on sedentary ergonomics and managing the inverse relationship between programmer flow state and physical self-care.
- Mar 2022: [Brain hygiene, spring cleaning edition](/rflog/2022/03/23/brain-hygiene-sp22/): my ultimate roundup of my brain hygiene arsenal, including unmedicated anti-distractibility & executive function tricks, mobile unengagement, maintaining the body, and my end of day routines at RC.
- Jun 2021: [Brain hygiene](/rflog/2021/06/25/brain-hygiene/): initial roundup post from 12 weeks of running Distractibility Accountability, a support group I created at RC for excessively distractible people to share tactics for staying focused.
- Feb 2020 (RIP): [RC Minimax](/rflog/2020/02/28/rc-mini-max/): my retrospective and tips from my first (and sadly only in-person) week at RC.
