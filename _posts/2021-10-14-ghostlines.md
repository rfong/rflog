---
layout: post
title: ghostlines
date: 2021-10-14 15:09:00
tags: [webcam, image-processing, creative-coding]
imgurl: 2021-10-14-ghostlines1.png
description: A ghostly trace of your motion on a webcam. Not really in real time.
---

<a href="https://rfong.github.io/creative-coding/ghostlines/">
<img alt="ghostlines example frame, with BMO moving swiftly toward stage right" src="{{site.baseurl}}/assets/images/2021-10-14-ghostlines1.png" />
</a>

[`ghostlines`](https://rfong.github.io/creative-coding/ghostlines/) was by far the least performant of my RC creative coding experiments, clocking in around 5 seconds per frame. This one was completely just for fun.

The Creative Coding prompts this day were "use lines wisely" (I used them quite unwisely), "self-portrait", and "look deep into the void". I decided I wanted to draw a sort of ghostly trace of pixels that had moved between frames.

The intuitive first thought was to draw the trace of every "object" that had moved between frames, but clustering pixels and identifying them as objects is a pretty heavyweight ML problem, which I tend to avoid in favor of old-school vanilla computation. I would expect this approach to also be a bit chaotic (but in an interesting way) because of the possibility of line crossings, depending on the exact implementation.

## Motion of "mass" in an image

The approach I came up with was to draw red lines representing the movement of the image's **center of "mass"**, from a sample of points which had "moved". Now to figure out what that actually means in practice.

### Center of "mass" of an image

<img alt="low-res screenshot of my center of mass debugger" src="{{site.baseurl}}/assets/images/2021-10-14-ghostlines-com.png" />

Once we know the CoM for each captured frame, we can then draw a bunch of vectors (represented as red lines) pointing in the direction of the *change* of CoM between frames.

I first greyscaled everything for simplicity. I then decided to treat dark pixels as "mass", and light pixels as lack of "mass". In other words, flip the numerical values so I'm counting 0 (black) as the high value, 256 (white) as the low value.

My visual center of "mass" calculation, paraphrased for context:
```javascript
function getCenterOfMass(image) {
  matrix = getInverseGreyscaleMatrix(image);
  m = 0;   // total mass
  cx = 0;  // X-center of mass
  cy = 0;  // Y-center of mass
  for (y in range(matrix.length)) { // row
    for (x in range(matrix.width)) { // col
      m += matrix[y][x];
      cx += matrix[y][x] * x;
      cy += matrix[y][x] * y;
    }
  }
  return [Math.round(cx/m), Math.round(cy/m)]
}
```
Basically, I find the X-center and Y-center, and normalize them by total mass to get the X-Y coordinates of the 2D center of mass. I can then get the vector of change between frames by calculating [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between two CoMs.

### Side note: inverse greyscale matrix

I also had a delightful time using [`lodash`](https://lodash.com/) to write a very [FP](https://mostly-adequate.gitbook.io/mostly-adequate-guide/) approach to getting the inverse greyscale matrix representation of a full-color image. 

```javascript
// Get 2d matrix containing just greyscale values at each RGBA pixel,
// inverted so that black=high, white=low
function getInverseGreyscaleMatrix(im) {
  return _.chunk(
    _.map(
      // Chunk the 1D list into RGBA 4-tuples
      _.chunk(im.data, 4),
      // Invert values
      (p) => (255 - _.min(p.slice(0,3))),
    // finally, reshape into a width x height 2D array
    ), im.width,
  );
}
```

For context, image data from the Canvas API in Javascript is provided as a 1-dimensional array of flattened RGBA pixel values: `[r, g, b, a, r, g, b, a, ...]`. However, I get to ignore the A (alpha) value, because I'm not using transparency.

I chunked each set of 4 values together, iterated over them, and grabbed the B&W value of each RGB-tuple, but inverted. I finally reshape into a 2D array of B&W values.

### Finding points that "moved"

An 800x600 image has 480k pixels, so even if only 5% of those pixels "move", I definitely want to downsample them *a lot*, lest my entire screen be a mass of red lines.

I first calculated which pixels had changed values between sampled frames. Because many changes are relatively imperceptible and because webcam metering frequently changes between frames anyways, I ended up picking a threshold requiring a 40% change in B&W value.

Even this was too cluttered, as I was still getting tens of thousands of moved points between frames where I wasn't sitting perfectly still. I raised the bar even more, giving each point a 1% chance of being sampled.

### Drawing the "motion"

Finally, using the canvas API, I then drew a bunch of vectors (represented as red lines), starting at each sampled coordinate that had registered a change, and pointing in the direction of the change in center of mass of the image.

<a href="https://rfong.github.io/creative-coding/ghostlines/">
<img alt="ghostlines example frame, with BMO flying slowly upward" src="{{site.baseurl}}/assets/images/2021-10-14-ghostlines2.png" />
</a>

It's too painfully slow right now to actually be used as a webcam, but I like the freeze frames a lot.
