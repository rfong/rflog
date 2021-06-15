---
layout: post
title: Ultralight and performant web development
tags: [web, lightweight, jekyll, shaders]
---

My intense personal avoidance of laggy, heavyweight stacks is well known, especially as I have rampant focus issues when waiting for pages in development to reload. In particular, I don't enjoy modern industrial web build systems, although I frequently tolerate them for job purposes.

Recently, I have been casually playing around with a couple of higher-performance web technologies evoking old-timey statically typed systems of yore. These may have significantly higher upfront frustration, but the runtime performance, compile-time errors, and consolidated logic just make me feel happy and nostalgic inside for some reason. Plus, it's fun to explore.

Here are some technologies I've been trying out lately!

## WebAssembly (WASM)

WASM is an intermediate representation for machine instructions which allows you to execute code in the browser significantly faster than JS in certain cases. For an overview on how it works and some of its pros and cons, check out [Lin Clark's illustrated intro to WASM](https://hacks.mozilla.org/2017/02/a-cartoon-intro-to-webassembly/).

Here is a [list of languages](https://github.com/appcypher/awesome-wasm-langs) with WASM build support. Stability may vary. Rust is one of the most common languages I've anecdotally seen compiled to WASM for projects, but I'm probably biased by Recurse Center.

I [tried it out](https://github.com/rfong/wasm-tinygo-hello) compiling TinyGo to WASM on account of my familiarity with Golang combined with my desire for a smaller binary. I got a small example setup working, but I'm not sure if I'll go much further with it on account of some possible versioning incompatibilities between Go 1.13+ and deprecations in [syscall/js](https://golang.org/pkg/syscall/js/), Go's package for dealing with JS/WASM architecture.

A bit tempted to try RustWASM's very thorough tutorial on how to make [Conway's Game of Life with Rust->WASM](https://rustwasm.github.io/book/game-of-life/implementing.html), and my RC batchmates seem to be having more luck with Rust->WASM, but I'm holding back because I'm already quite scattered and promised myself I wouldn't get distracted by any new languages this week.

## GLSL fragment shaders

I started out doing a lot of my weekly creative-coding experiments in [`p5`](https://p5js.org/), which has absolutely wonderful documentation and lots of features. However, I got frustrated pretty quickly with the extremely slow performance I was experiencing in development, so I redid [last week's](https://rfong.github.io/creative-coding/skymap/dist/p5.html) `p5` experiment as a GLSL fragment shader [here](https://rfong.github.io/creative-coding/skymap).

- A *[fragment shader](https://www.khronos.org/opengl/wiki/Fragment_Shader)* is the part of a GL pipeline that colors the per-vertex output. (Earlier stages in the pipeline include [vertex shaders](https://www.khronos.org/opengl/wiki/Vertex_Shader), which map vertex positions, and [geometry shaders](https://www.khronos.org/opengl/wiki/Geometry_Shader), which output primitives.)
- *[GLSL](https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language)*, or OpenGL Shading Language, is the principal language for OpenGL.
- *[WebGL](https://en.wikipedia.org/wiki/WebGL)* is a Javascript API for GPU-accelerated graphics & physics processing in the browser, and understands GLSL. Most major browsers have supported WebGL for several years.

For examples of the complex renders that can be instructed on obscenely small amounts of GLSL code, check out [ShaderToy](https://www.shadertoy.com), especially [this beautiful 200-line animated seascape](https://www.shadertoy.com/view/Ms2SD1).

Fragment shaders are mind-bending, powerful, and unbelievably frustrating to debug. Their typical inputs are pixel location and time, which feels a bit like a closure. However, they're also very low-level, so the code is extremely imperative. Every time I practice using them, I feel like my brain is a dry, crusty old rubber band getting stretched painfully over a watermelon. But in a good way?

[The Book of Shaders](https://thebookofshaders.com/) is the best interactive/explorable tutorial I've seen on conceptually understanding how fragment shaders work and how to think in their paradigm.

## snowpack

`webpack`, one of the most common frontend build tools, is powerful, but also large and frequently slow. I've been trying out a lighter-weight frontend build tool called [`snowpack`](https://www.snowpack.dev/) for tiny experimental repos where I want ES6 compatibility, clean module imports/exports, and bundling, but not with all the overhead of `webpack`.

I like it so far! It definitely has limitations, but it's really perfect for developing quickly when you don't need anything fancy.

# Classics

Here are some other approaches to minimal web stacks I've been using for a while.

## Jinja

I love simple static compilation of websites, particularly the [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templating framework for Python! It's a nice ultralight way to templatize websites and make your development process more readable without incurring much overhead.

My portfolio website (whose content is extremely outdated) is compiled with [about 20 lines](https://github.com/rfong/rfong.github.io/blob/master/compile.py) of Python/Jinja.

## Jekyll

[Jekyll](https://jekyllrb.com/) is a blog-aware static website generator. I'm using it for this blog! [Here's a post](http://localhost:4000/rflog/2020/02/28/jekyll-tags/) about my setup. It's very fast and I've experienced very few issues between development and deployment.

Being able to write to this blog in plain [Markdown](https://daringfireball.net/projects/markdown/) with native Github Pages support is an incredible boon and I love Github for baking that in.

## Google Sheets as a read-only database

If I had to count how many statically served websites I own that use [Google Sheets](https://sheets.google.com/)' ability to serve CSV output as their read-only database, it would be embarrassing, except it wouldn't because I love it. It has saved me so much time avoiding microservices or servers when I want to throw tiny websites on the Internet. Thanks, Big G.

## JSON as static CMS storage

Similarly, I have avoided countless heavyweight frontend frameworks for personal websites by writing ultra lightweight templates and [populating](https://github.com/ptsd-resources/ptsd-resources.github.io/blob/master/assets/index.js) them with the contents of JSON files. All of [innerdemons.me](https://innerdemons.me/) is templatized this way. I know it's not modern but I love the simplicity.

## Browser extension local storage

Even when I do want to make a web utility with per-user storage and configurability, I frequently fake out by just writing an extension that uses [local storage](https://developer.chrome.com/docs/extensions/reference/storage/).

- [Replacerator](https://chrome.google.com/webstore/detail/replacerator/gaajhenbcclienfnniphiiambbbninnp) is a generalized, completely user-configurable text replacement tool I made after I got tired of forking Cloud-To-Butt.
- [Snailman](https://chrome.google.com/webstore/detail/snailman/gnncgbnoacieamgkmommabmpchlfidca?hl=en) is a physical package-tracking extension I made when I had a bunch of exciting packages in the mail for a project.

I value [local-first storage](https://www.inkandswitch.com/local-first.html) quite a lot -- not just for privacy reasons but largely for convenience, reliability, performance, and freedom from constantly being tethered to a network while doing mundane things that aren't functionally predicated on having a network connection.

## Plain HTML

If you are still using plain HTML for websites, power to you. I smile with irrepressible joy any time I see an academician's website written in vanilla HTML and totally unstyled. It loads instantaneously to human perception and you rarely have to think about cross-platform support. What more could you want?
