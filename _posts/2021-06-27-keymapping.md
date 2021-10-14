---
layout: post
title: Downsizing my keymap from 6x3 to 5x3
tags: [keyboard]
imgurl: 2021-06-27-crkbd-5x3.jpeg
description: Reducing my pinky load even further with a custom keymap.
---

*Note: Throughout this post, I'll refer to layers with zero-indexing. So with no layer mods active, I'm on layer 0.*

In this post, I'll summarize my high-level keymapping process so far for my [`crkbd` (Corne) keyboard](https://github.com/foostan/crkbd). You can find [updated copies of my keymap on Github](https://github.com/rfong/shibui).

I'm about 3 weeks in to using a `crkbd` and just downsized my map by two columns. While the 6x3 + 3 `crkbd` layout is an incredible ergonomic improvement over any standard keyboard layout, and I barely had to change any muscle memory to squash down my keymapping into it, it only reduced my pinky burden by about 50%. I found myself wanting to remove even more load from my pinkies, where my RSI is the worst.

I wanted to do what would have felt completely impractical before using a `crkbd`: to go down to 5x3.

<img alt="My crkbd split ergonomic keyboard. There are three keys for each thumb and a 6x3 staggered ortholinear grid for the other fingers. There are red X marks crossing out the outer column." src="{{site.baseurl}}/assets/images/2021-06-27-crkbd-5x3.jpeg" />

### High-level layout thoughts

For better or worse, I'm sticking with QWERTY for now. Personally, it doesn't bother me; most of my ergonomics complaints are around the positions of modifiers and special functions. So I don't feel a particular need to switch my alpha layout just yet.

<img alt="screenshot of keymap layers" src="{{site.baseurl}}/assets/images/2021-06-27-layout-0.png" />

[`miryoku`](https://github.com/manna-harbour/miryoku) is one of the most popular 5x3 + 3 keeb layouts, and its creator, `manna-harbour`, was actually the clincher for me deciding to buy a `crkbd` because they [hotswapped a Lenovo trackpoint](https://github.com/manna-harbour/crkbd/tree/master/trackpoint) into theirs, which is my dream setup.

However, `miryoku` doesn't personally appeal to me. I prefer having symbols on my right hand, don't really like numpad layouts, and wanted to capitalize on existing muscle memory while moving traditional pinky work to the thumbs.

`miryoku` also appears to assume Colemak, and alpha layout will have some effect on collision mapping for commonly used vim/terminal symbols. 

## Design priorities

- Minimize pinky work.
- Minimize layer switching for keys which are commonly used together. (Coding symbols, etc.)
- Other than pinky -> thumb reallocation, minimize changes in muscle memory from a standard laptop layout when possible.
- Every chorded standard key or common shortcut should be accessible without wrist repositioning.

### Some implementation choices

- The pinky is never required to access modifiers or special functions.
- All modifiers and most special functions are accessible through the thumb cluster.
- A chord may never require three keys in the same thumb cluster.
- A chord may require two keys in the same thumb cluster, so long as no non-thumb keys are also required on that hand. This allows another finger to help without contorting the hand.
- Numbers are in a row layout instead of a pad layout.
- Several functions can be accessed in multiple ways to simplify common shortcuts and coding/typing use cases.

## Saving my pinkies with mod-taps

It's pretty hard to reasonably downsize much smaller than a 6x3 + 3 layout if each key in each layer only corresponds to one function. That's where mod-taps come in.

[Mod-taps](https://docs.qmk.fm/#/mod_tap) are keys that perform one function when held, and a different function when tapped. Because modifier keys always need to be held in combination with other keys, and are functionally useless when tapped in isolation, this lets you layer additional tap functions onto your modifier keys without any loss in functionality.

I initially had a mixture of modifiers and tap keys assigned to my thumbs: the two layer modifiers, `Cmd`, `Space`, `Alt`, and `Tab`. This unfortunately left `Ctrl`, `Shift`, `Esc`, `Bksp`, and `Enter` in the 6th columns.

After taking advantage of mod-taps, I had 4 additional functions on my thumb cluster, and *all* modifiers became thumb-based.

|          | LH     | LH       | LH      | RH      | RH       | RH     |
| **Mods** | `Ctrl` | `Layer1` | `Cmd`   | `Shift` | `Layer2` | `Alt`  |
| **Taps** | `Tab`  |          | `Enter` | `Space` |          | `Esc`  |

`Bksp` is the only other special key I use heavily that isn't on the thumb cluster. I did try putting it there, but found that `Bksp` felt better as a non-thumb-based key, because it often needs to be tapped more than once in quick succession.

I don't love the thumb `Esc`, and have been using a second pinky-chorded `Esc` more often, but haven't yet figured out what else I'd rather put in that position. I live in a post-thumb-key-scarcity realm now! It's pretty wild.

The most confusing change to rebake my muscle memory around was `Shift`, since I use it heavily while typing at max speed. However, it's been settling into its new place fairly comfortably.

## One-hand vs. two-hand chords

I did a lot of tweaking based around chord handedness on the non-base layers.

<img alt="screenshot of keymap layers" src="{{site.baseurl}}/assets/images/2021-06-27-layout-1.png" />
<img alt="screenshot of keymap layers" src="{{site.baseurl}}/assets/images/2021-06-27-layout-2.png" />

**Two-handed chords** take ever so slightly more coordination and are a little slower. This is fine for plenty of use cases.

I use some heavily chorded (3-4 key) application-specific shortcuts, particularly for window management and in browsers and rich text editors. I prefer having such large chords spread across two hands. (I do assign a few of the most common combos to macros too.)

**One-handed chords** are simpler and faster; nice for accessing symbols.

The right-hand side of Layer 2 is populated with common symbols for coding and terminal navigation. I also added a secondary Shift in this layer to simplify chording; otherwise, I would have to hold down two thumb keys to access some of the symbols, which would be annoying. 

The top row of Layer 1 contains the num keys. This feels natural to me coming from a standard layout.

I populated most of the bottom row of Layer 1 with numrow-shift symbols, so I could access them with just a layer mod instead of burning an extra Shift to get them. The exception is parentheses, because I found those more natural to access from Layer 2.

## Redundancies

I duplicated a few keys when it helped simplify hand coordination and minimize layer switching for my most common use cases. For example:
- `Enter` lives in 3 places because it's so useful; as a single tap on the LH thumb cluster, as a one-hand RH chord, and as a one-hand LH chord in Layer 1, for when I'm already using my thumb to access Layer 1.
- Layer 2 has an auxiliary `Shift` to simplify shifted symbol chording, since my normal `Shift` key lives in the same thumb cluster as the Layer 2 modifier and I don't want any chord to *require* one finger to hold down multiple keys.
- `Tab` is duplicated onto Layer 2 for more ergonomic access to `Cmd-Tab` for application switching.
- `()` can either be shifted into from the numrow, or accessed directly on Layer 2. This is because Layer 2 also contains my `[]` and `{}` braces, and I wanted all braces available together on the same layer for coding.
- `-`/`_` can be found in different places, on Layers 1 and 2. The Layer 2 option is used for coding and arithmetic. The Layer 1 option is there because I often find it handy to insert hyphens and underscores into dates, phone numbers, and other numeric sequences that frequently come up in webforms and filenames. Having the extra hyphen there minimizes layer switching.

# 5x3 is...practical???

With the most important special keys and all the modifiers mapped into the thumb cluster, and all my symbols mapped by use case onto layers, my 6th columns were comfortably rendered obsolete.

Coding and navigating the terminal are definitely slower than usual right now, but the reduction in pinky finger pain is worth it. It feels amazing to never have to shift my hands off their resting position. I think once the muscle memory locks in, I'll be nearly as fast as before.

## Can I still use a standard keyboard?

Yes. I've been touch-typing on standard keyboards for so long that I don't think that muscle memory will be going away any time soon. The only downside is that I am filled with boundless rage whenever I contort my sad pinkies all over my laptop keyboard. 😂

So far I haven't had issues switching between my row-ortholinear `crkbd` and my staggered-row standard keyboard, or between vim in either layout.
