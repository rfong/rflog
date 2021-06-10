---
layout: post
title: A summary of Linguistics Week (a.k.a. Recurse Center)
tags: [recurse-center, linguistics]
---

Like most monotonically linear-time-bound entities, I originally journaled this blog chronologically. It turns out there are a lot of learners and native speakers of other languages at RC, which led to some really interesting conversations about the structure and encoding of language! As Recurse veered from what I'd naively assumed would be a week of code into a week of linguistics, I realized it would make more sense to collate blogthoughts by the various themes that emerged.

## Fun facts about Arabic

On day 2, there was a fantastic lightning talk about the [Arabic script](https://en.wikipedia.org/wiki/Arabic_script), which, although it was designed for the Arabic language, has been borrowed and adapted to a huge variety of other spoken languages across the Middle East, Asia, Africa, and even Spanish and [certain dialects of Chinese](https://en.wikipedia.org/wiki/Xiao%27erjing). Thus, different styles of writing the script say a lot about one's background.

Apparently, as Semitic languages, [Hebrew](https://en.wikipedia.org/wiki/Hebrew) and [Arabic](https://en.wikipedia.org/wiki/Arabic) share a lot of overlap in their word roots, which are distinguishable by their consonants and have the vowels swapped out for different conjugations and meanings. A native Hebrew speaker said that they could actually puzzle out a fair bit of spoken Arabic just by the shared word root cognates.

Related links:
- [Why Arabic Is Terrific](https://idlewords.com/2011/08/why_arabic_is_terrific.htm)
- [Kufic](https://en.wikipedia.org/wiki/Kufic), an Arabic script variant well-suited to tile mosaics

## Linguistics puzzles!

On day 3, I went to linguistics puzzle club night! Linguistics puzzles don't actually require specific linguistics knowledge, although having your brain pre-stretched by multiple languages may be helpful. They're logic puzzles which provide exactly the set of uniquely identifying information needed to determine enough of the structure and vocabulary of a language to then construct and translate certain sentences in that language.

They're usually constructed using relatively obscure or endangered languages. On tonight's puzzle buffet, we had:
- [Apinayé](https://en.wikipedia.org/wiki/Apinay%C3%A9_language): a Brazilian language with ~2300 speakers
- [Manam Pile](https://en.wikipedia.org/wiki/Manam_language): ~8000 speakers, only natively spoken on an island off the coast of New Guinea
- [Hmong Daw](https://en.wikipedia.org/wiki/Hmong_language): a Southeast Asian dialect with ~1.6 million speakers, but the puzzle was given in a writing system developed for the language around 1950.

It was really fun to stretch our brains on many different axes of how we thought a script ought to represent phonetic information. And as I'm privileged to be a native speaker of English, it felt important to expand my awareness of how much local and cultural context is encoded and optimized for within indigenous languages, and how many languages have become endangered or died out because of [forced assimilation](https://en.wikipedia.org/wiki/Cultural_assimilation_of_Native_Americans) & [cultural genocide](https://en.wikipedia.org/wiki/Genocide_of_indigenous_peoples) spawned by Western hegemony & colonialism. It was interesting to use these puzzles to help break down my preconceived Western notions about how the world is perceived, sort of like RPG worldbuilding but in a way that relates to actual non-fictional cultures.

*Gimme those puzzles!*
- [International Linguistics Olympiad](https://ioling.org/problems/)
- [North American Computational Linguistics Open (NACLO)](https://www.nacloweb.org/practice.php)

## Pipe dream thoughts on generative writing systems

My original RC mini idea was to build an interactive web overview of subtractive synthesis, but then [Baltazar](https://github.com/baltazarortiz) told me about [Ableton's version](https://learningsynths.ableton.com/). It is everything I wanted and more and also appears to work flawlessly on mobile, I love it. So I brainstormed some other ideas, and started thinking about generative writing systems, a concept that I free associated out of too many hobbies.

### Linguistic context

I've been casually self-studying Japanese for a couple years. Japanese *kana* are [*syllabaries*](https://en.wikipedia.org/wiki/Syllabary) (phonetic writing systems for syllables, as opposed to separating consonants/vowels), and are some of the most shallow natural [*phonemic orthographies*](https://en.wikipedia.org/wiki/Phonemic_orthography). In other words, the phonetic writing system is an almost perfect mapping/representation to the phonemic distinctions within the spoken language, with some pretty consistent known modification rules, and some exceptions for different dialects. This is very satisfying. (Written English, on the other hand, is a [*defective orthography*](https://en.wikipedia.org/wiki/Phonemic_orthography#Defective_orthographies), which is a sick linguistics burn for "totally fails to represent the spoken language's phonemic distinctions.")

Last week while studying 日本語, I took a half hour break to start learning [한글 (Hangeul)](http://learn-hangul.com/), the Korean alphabet which was designed 500 years ago to be learnable in one day. That speaks for itself.

I find both kana and Hangeul satisfying because of aspects of their visual construction and phonetic mappings that make them extraordinarily learnable. In general, [I am interested in writing systems](https://www.instagram.com/p/Bi_eyx3HAet/) and encodings, which is not surprising because it's probably what computer scientists did before computers existed.

### How this all ties together

I manually mapped out a rough algorithm for generating fictional writing systems from primitives of arcs & lines. My implementation ties together a few disparate themes from my RC experience, so I'll write this up as a separate post once I have more code to show.

