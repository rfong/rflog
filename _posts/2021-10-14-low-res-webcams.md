---
layout: post
title: Low-res webcam processing experiments
date: 2021-10-14 14:09:00
tags: [image-processing, creative-coding]
techTags: webcam, javascript, python, opencv
imgurl: 2021-10-14-dithercam.png
description: What can I say, I love old-school image compression.
---

I played around a lot with live image processing during RC Creative Coding meetups, in the form of weird webcam filters. The inspiration for these was a videochat I attempted to have with another RCer who was on a really low-bandwidth connection, so our Zoom call kept freezing.

We eventually turned off the video altogether, but it was really frustrating! I wish I could tell Zoom to send me an ultra-ultra low-resolution video stream, when I don't need colors or high fidelity, but only want enough frames per second to get the visual sensation that a real human is present on the other side.

As a result, I wanted to test out how it would feel to look at a significantly lower-res video stream in real time.

# [`asciicam`](https://rfong.github.io/creative-coding/asciicam/)

<a href="https://rfong.github.io/creative-coding/asciicam/">
<img alt="ASCII image filter example, featuring our completely normal house decor" src="{{site.baseurl}}/assets/images/2021-10-14-asciicam.png" />
</a>

[`asciicam`](https://rfong.github.io/creative-coding/asciicam/) is an ASCII filter on top of a webcam stream, sampling at 10fps. Click the image to try it for yourself!

I was on a big ASCII kick from earlier in my batch, having recently made [`langmap`](https://rfong.github.io/creative-coding/langmap/) (an ASCII map colored with a shader that also displays geographical origins of languages that use various phonemes).

Although it's obviously quite low fidelity, I think it has enough fidelity for this purpose. It's also surprisingly performant, clocking around 30ms per frame -- good job optimizing, `aalib`! Uncompressed, a 240x144 char frame costs 242Kb, although it can get significantly better with string compression.

Besides finding ASCII generally charming, I also really liked the idea that a single 7-bit char could potentially represent many 1-bit pixels, and large uniform areas could be easily string-compressed, providing good compression. In a use case where the limiting reagent is network bandwidth rather than local processing, this might work out well.

# [`dithercam`](https://rfong.github.io/creative-coding/dithercam/)

<a href="https://rfong.github.io/creative-coding/dithercam/">
<img alt="Dithered filter example, featuring our completely normal house decor again" src="{{site.baseurl}}/assets/images/2021-10-14-dithercam.png" />
</a>

[Click to try!](https://rfong.github.io/creative-coding/dithercam/) This uses 1-bit [Floyd-Steinberg dithering](https://en.wikipedia.org/wiki/Floyd%E2%80%93Steinberg_dithering) written in vanilla JS as a filter over the webcam stream.

This is performant to around 8fps, and the image blob size seems to range around 90-125Kb for an 800x600 image (e.g., 480,000 pixels).

Image fidelity is clearly better than `asciicam` -- dithering is a tried and true way of massively compressing images, and I'll definitely be playing more with it in the future.

# Older experiments (server side only)

You may also enjoy these much older creative-coding webcam experiments I did in OpenCV back in 2016. However, I haven't written web clients for them, so you'll have to run them yourself.

## [Canny edge detection](https://gist.github.com/rfong/49ee29e46ef0166fc78b496698063922)

This is simply OpenCV's built-in Canny edge detection algorithm, applied onto a webcam capture.

Here's an example of the kind of visual output you get:
<a href="https://en.wikipedia.org/wiki/Canny_edge_detector#/media/File:Valve_monochrome_canny_(6).PNG"><img alt="Image from Simpsons_contributor on Wikipedia." src="{{site.baseurl}}/assets/images/canny_edge_example.png" /></a>

And here's [the original paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.420.3300&rep=rep1&type=pdf) on the algorithm, published by John Canny in 1986.

## [slinky people](https://gist.github.com/rfong/1627a348dd8e8655f0647ccb4c7adae2)

This is a simple, surprisingly performant, and delightful OpenCV filter [I wrote](https://gist.github.com/rfong/1627a348dd8e8655f0647ccb4c7adae2) that delays each successive image row by an additional timestep.

It's very computationally straightforward, but if you're moving with knowledge of how the delay works, you can get really fun and complex effects, like turning your body into a stretchy helix made out of hair, having too many arms, or melting the top of your body into ice cream.

<iframe src="https://player.vimeo.com/video/183155228?h=f706d36aa8" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
<p><a href="https://vimeo.com/183155228">Slinky People</a> from <a href="https://vimeo.com/rfong">rfong</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
