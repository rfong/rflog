---
layout: post
title: Clojure dev setup links
tags: [clojure, recurse-center, dev-setup]
description: Handy resources I collected while setting up my Clojure env.
---

Collected dev setup tips from my first week of playing with Clojure.

## Getting started

Download the [Clojure CLI](https://clojure.org/guides/getting_started) (invoked as `clj` on OSX). Here's the [starter guide](https://clojure.org/guides/deps_and_cli) on dependencies and running scripts using the CLI.

- [Clojure namespaces](https://clojure.org/guides/repl/navigating_namespaces) and [imports](https://clojure.org/reference/libs)
- [namespaces & importing](https://8thlight.com/blog/colin-jones/2010/12/05/clojure-libs-and-namespaces-require-use-import-and-ns.html)
- [@tomekw's quickstart guide to Clojure deps](https://tomekw.com/clojure-deps-edn-a-basic-guide/)

#### Build tooling
[Leiningen](http://leiningen.org/), invoked as `lein`, is a commonly used Clojure project manager that helps you manage dependencies, run tests, package your project, etc.
- [`lein` quickstart by BraveClojure](https://www.braveclojure.com/getting-started/), with bonus explanation of how Clojure utilizes the JVM

## Workflow tips

### When in doubt, pair!

After I complained about my confusion in the relevant RC chat channels, a kind soul offered to show me recommendations for an ergonomic Clojure workflow and point out some common beginner mistakes, almost all of which I was making. Thank you!! I wish I had gotten this walkthrough three days ago, but also am thankful that I got this walkthrough so soon into my functional programming journey.

### Recommendations

The aforementioned kind soul sent me a bunch of useful recommendations to improve my workflow:
- ["Afraid of Clojure Stacktraces? Fear no more"](https://www.youtube.com/watch?v=4fqGdt0-_is): A lightning talk at IN/Clojure that explains the traces, how to break them down and read them, and tooling support available to query/pretty-print the traces.

#### `vim` + Clojure/Script workflow
- 5 minute [video demonstration](https://www.youtube.com/watch?v=-MAmXT17EiI) of an ergonomic Vim-based Clojure(Script) workflow
- [Handy plugins](https://juxt.pro/blog/posts/vim-1.html)

#### Hot-loading ClojureScript
- [`figwheel`](https://github.com/bhauman/lein-figwheel/wiki/Using-the-Figwheel-REPL-with-Vim), a tool which builds & hot-loads ClojureScript into the browser as you write it
- [Video example](https://www.youtube.com/watch?v=KZjFVdU8VLI) of a `figwheel` workflow
- [Video](https://www.youtube.com/watch?v=j-kj2qwJa_E) of a fuller exposition of all the things `figwheel` enables


## Debugging frustrations

Very little of the open source Clojure I've been checking out contains comments for some reason. While I get my footing, I've been finding `clojure.core/pr-str` useful to sanity check what's happening inside my lazy sequences: `(println (pr-str x))`

I'm used to verbose error handlers, and Clojure error stacks are rather arcane. This is additionally frustrating when I clone a 3rd-party library and I don't know how to debug the examples without reading the entire library. There must be some way to debug the horrific error stacks coming out of functional that I just haven't found yet.

[notes on debugging Clojure - Eli Bendersky](https://eli.thegreenplace.net/2017/notes-on-debugging-clojure-code/)

#### Lazy sequences

Type errors involving lazy sequences seem to surface often in Clojure error stacks.
- [Great writeup here](http://theatticlight.net/posts/Lazy-Sequences-in-Clojure/) on lazy sequences in Clojure, how they're treated differently by various list operators, and why one might want to use them.
- [Making Clojure Lazier](https://clojure.org/reference/lazy)

