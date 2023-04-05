---
layout: post
title: Weird Javascript fun facts I stumbled over while building a Bezier curve editor
tags: [hot-tips]
techTags: javascript
imgurl: nullish_coalescing_op.png
description: The joys of navigating proper encapsulation when your first-class functions have gone wild
---

I spent today and yesterday building a little [educational interactive webpage](https://rfong.github.io/creative-coding/bezier/) that helps you get intuition for Bezier curves! Go play with it!

<style>
    img {
        height: 150px;
        display: inline-block;
    }
</style>
<img src="{{site.baseurl}}/assets/images/bezier/1.png" />
<img src="{{site.baseurl}}/assets/images/bezier/2.png" />
<img src="{{site.baseurl}}/assets/images/bezier/3.png" />
<img src="{{site.baseurl}}/assets/images/bezier/4.png" />

While encapsulating, refactoring, modularizing, and generally forcing JS to do horrible things it was never designed for (read: just about anything), to my heart's content, I dug up many a JS fun fact! Some were new to me, some were old, and all, like JS itself, are weird.

# JS fun facts

## setting default values with the [nullish coalescing operator `??`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) 

Usage: `a ?? b`. Returns `b` if `a` is `null` or `undefined`, otherwise returns `a`. In other words, `b` behaves like a default value.

The double question marks evoke just how I feel every time I learn something new about Javascript. Only an interrobang (?!) would be more apt.

A great way to shorthand explicit `null`/`undefined` checks while fishing variables out of the hilariously mutable objects that make up the beautiful trashfire that is the Javascript language.

## variadic functions with `...args` and `arguments`

(Or, functions which accept an indefinite or variable number of arguments. My headcanon term is "splat", since that's what it's called in Python.)

There are multiple ways to create a variadic function in JS. One way is the "[rest parameter syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters)", which looks like this:

```javascript
function fn1(...args) {}
function fn2(a, b, ...args) {}
```

Another approach is [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments), an array-like object (*important: not an actual array!!*) that you can access from within functions.

```javascript
function fn(a, b, c) {
    console.log(arguments.length);
    console.log(arguments[0], arguments[1], arguments[2]);
}
```

Although you can index into `arguments` and call `arguments.length`, it does not have `Array`'s other built-in methods, while the "rest parameters" are an actual `Array`. There are some other edge case distinctions you might care about in the Mozilla documentation pages, such as when named parameters are re-assigned.

## dynamically executing functions on arguments with [`apply`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply) or [`call`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call)

I love splatting an unknown-length array of arguments onto a variadic function!

[`Function.prototype.apply()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/apply) is a wonderfully useful buddy which calls a function with a given value of `this` and given arguments.

```javascript
const numbers = [5, 6, 2, 3, 7];
//...
Math.max.apply(null, numbers);
```

`p5` can be notoriously messy to encapsulate. I ended up using a lot of `apply` because I was writing a lot of class functions that casually use `p5` functions. For example:

```javascript
this.p.stroke.apply(this.p, args);
```
(the `p` is a `p5` instance)

[`Function.prototype.call()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call) is nearly identical except that you provide the arguments individually instead of in an array. I have never actually used it, because at the point where I need to use `apply`, I'm probably already passing the arguments around in an array anyways.

## [`Function.prototype.bind()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)

[`bind()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) creates a new function with its `this` keyword set to the provided value.

`bind()` came in handy quite a lot because I needed to define `p5` `setup()` and `draw()` functions for all my different little sketch environments in [my Bezier explorable](https://rfong.github.io/creative-coding/bezier/), which were scaffolded on a lot of shared functionality.

For example, I have a wrapper class `BezierSketch` which handles a lot of the functionality which stays the same across my different sketches. Its constructor accepts custom p5 `setup()` and `draw()` functions which can be run with knowledge of `p5` and the `BezierSketch` instances.

This allowed me to implement lots of different sketches with different setup and draw methods that I had defined externally while still getting to use the `p5` API and any functionality I had built into `BezierSketch`.

Here's an extremely abstract pseudocode outline of what I mean:

```javascript
class BezierSketch {
    constructor(p, setupFn, drawFn, ...) {
        ...
        p.setup = setupFn.bind(this, p);
        p.draw = drawFn.bind(this, p);
        ...
    }

    function coolFunction(...) { ...}
}

// sketch 1
new BezierSketch(p,
    // setup function
    function(p) {
        // Set up custom controls
        ...
    },
    // draw function
    function(p) {
        // Draw one Bezier curve!
        ...
    },
);

// sketch 2
new BezierSketch(p,
    // setup function
    function(p) {},
    // draw function
    function(p) {
        // Do something completely different!
        this.coolFunction(...);
        ...
    },
);
```

## `() => {}` ECMA arrow function fun facts

Before this project, I think I was only using `() => {}` to make small anonymous closures, such as when I need to pass a small lambda around for pseudo-functional programming.
```javascript
// Traditional version
_.map(arr, function(x) { return ... });
// With arrow function
_.map(arr, (x) => { ... });
```

[Today I learned](https://stackoverflow.com/questions/56503531/what-is-a-good-way-to-automatically-bind-js-class-methods) that the ECMA arrow function automatically binds `this` to the parent scope. (I was tripping over that a lot today before looking up where my mystery `this` values were coming from.)

From the [ECMA spec](http://www.ecma-international.org/ecma-262/6.0/#sec-arrow-function-definitions-runtime-semantics-evaluation):
> Any reference to arguments, super, this, or new.target within an ArrowFunction must resolve to a binding in a lexically enclosing environment. Typically this will be the Function Environment of an immediately enclosing function.

[This Stack Overflow discussion](https://stackoverflow.com/questions/22939130/when-should-i-use-arrow-functions-in-ecmascript-6) has some nice points about arrow function scoping and when to use or not use it.

## [so many ways to iterate over an array!](https://stackoverflow.com/questions/9329446/loop-for-each-over-an-array-in-javascript)

I usually just use a good old-fashioned `for` loop, performant and `async`-friendly.
```javascript
for (let i=0; i<arr.length; i++) {
    const element = arr[i];
    // ...use `element`...
}
```

I didn't actually know about the `for-of` loop until today and am thrilled it finally exists!! Apparently it was implemented in 2015, which tells you how much of a webdev Luddite I am.

```javascript
for (const element of array) {
    // ...use `element`...
}
```

# Bonus: CSS fun facts

[How to fit a div's height to wrap around its floated children](https://stackoverflow.com/questions/9329446/loop-for-each-over-an-array-in-javascript) :sobs in clearfix:
