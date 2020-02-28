---
layout: post
title: My first few days of exploring Clojure
tags: [clojure, functional-programming, recurse-center]
---

In between many other delightful pursuits, I managed to allocate a few hours each day of my Recurse mini-batch to learning or implementing things in [Clojure](https://clojure.org/).

This particular choice of language was semi-arbitrary; my goal was to start learning a Lisp-like functional language, and one of my secondary concrete goals involved visualization as a side effect, so I went with whatever seemed to have the most convenient libraries, which was Clojure -- reputedly near-interchangeable syntactically with [ClojureScript](https://clojurescript.org/)?

Here are my collated notes from that exploration, which in no way reflect my recommendations for how a beginner ought to approach this subject, as I am still very much one.

## Dev setup

Broken out into a [separate post](/2020/02/27/clojure-dev-setup/).

## Online exploration

On Day 1, I wasn't able to set up the Clojure CLI for mysterious reasons which would become tragically apparent about 24-30 hours in the future (when I nuked my package manager), so I did a few hours of initial learning in online environments.

For a light introduction to the syntax and concepts, I went through several units of [ClojureScript Koans](http://clojurescriptkoans.com/) in concert with the documentation. This was a nice introduction to expressing things like inline higher-order functions in Clojure.
{% highlight clojure %}
; functions can also take other functions as input
(= 20 ((fn [f] (f 4 5)) _____ ))
; higher-order functions take function arguments
(= 25 ( _____ (fn [n] (* n n))))
{% endhighlight %}

I also fiddled a little with online REPLs that provided pre-made examples, such as [Quil](https://quil.info), a library for animated graphics and visualizations, analogous to [Processing.js](http://processingjs.org/).

## Thinking in Clojure

My brain has been shaped by the C-like languages and scripting languages I've dealt with most of my life. Although I have aggressively functional-lang preferences when using scripting languages, they are multi-paradigm enough that one can easily fall back to the imperative/OOP style.

Clojure is my first Lisp-like language, so I wanted some philosophy and examples on how to **think** in this paradigm before stumbling around blindly. Here's what I gleaned from the first chapter of [The Joy of Clojure (2nd ed.)](https://www.manning.com/books/the-joy-of-clojure-second-edition), which I dug up in the RC library.

### Infix order of operations

The Joy of Clojure blew my mind as early as page 12 with an example of how the [order of operations](https://en.wikipedia.org/wiki/Order_of_operations) can be elegantly implemented in a functional lang by assigning operation weights and shifting the evaluation order as needed.

Let's say we want to implement the order of operations for infix operators. Since Clojure uses prefix operators, we first to be able to handle infix expressions in both directions. The following functions simply translate infix expressions into prefix expressions which can then be evaluated in Clojure.
{% highlight clojure %}
; function that solves infix math expressions right to left
(defn r->lfix
  ([a op b]  (op a b))
  ([a op1 b op2 c] (op1 a (op2 b c)))
  ([a op1 b op2 c op3 c] (op1 a (op2 b (op3 c d))))
  ; you can probably extend this to handle expressions
  ; of arbitrary length by recursively using Clojure's
  ; equivalent of arg "splat", but let's keep this
  ; example simple
)

; function that solves infix math expressions left to right
(defn l->rfix
  ([a op b]  (op a b))
  ([a op1 b op2 c] (op2 c (op2 a b)))
  ([a op1 b op2 c op3 c] (op3 d (op2 c (op3 a b))))
)
{% endhighlight %}

Once we have those, we can quickly implement the order of operations.

{% highlight clojure %}
; map of operator weights
(def order {
  + 0  - 0
  * 1  / 1 })

; function that changes evaluation order depending on op weights
(defn infix3 [a op1 b op2 c]
  (if (< (get order op1) (get order op2))
    (r->lfix a op1 b op2 c)
    (l->rfix a op1 b op2 c)
  )
)
{% endhighlight %}

We only have addition and multiplication in this example, but we can easily add more operators as needed by extending the map.

This feels really elegant compared to implementing an order-of-operations evaluator in a verbose imperative language like Java, where you need to imperatively reconfigure your infix notation expression substring-by-substring into a nested stack of expressions anyways -- with an end result reminiscent of a Clojure-like explicitly nested arithmetic expression!

### Clojure philosophy

Paraphrased, a bit of Chapter 1 philosophy behind the language design.

There are many different styles of functional programming. Clojure was specifically created to address frustrations with the weaknesses of object-oriented programming (OOP) in facilitating concurrent programming. One language characteristic which addresses this is strict immutability, allowing objects to be shared without fear of concurrent state modification. Unlike OOP, where state and identity are conflated into mutable state:

> Clojure's implementation attempts to draw a clear separation between an object's state and identity as they relate to time.

A nice grammatical analogy: an OOP mindset encourages you to define an application domain in terms of nouns (classes), while the functional mindset encourages the composition of verbs (functions). Many of what we perceive to be classes may be expressed as data tables in Clojure (p.24).

### Local encapsulation example

Here's another neat code example from Chapter 1, where we look up a chessboard square by *rank* (rows, labelled 1-8) and *file* (columns, labelled a-h).

{% highlight clojure %}
(defn lookup3 [board pos]
  (let [[file rank] (map int pos)
        [fc rc] (map int [\a \0])
        f (- file fc)
        r (* 8 (- 8 (- rank rc)))
        index (+ f r)]
      (board index)))
(lookup3 (initial-board) "a1")
{% endhighlight %}

Note how information that would ordinarily be composed into temp variables and for loops in in a C-like language are instead heavily encapsulated into inline functions.

Gripe: I haven't yet gotten the knack of reading Clojure quickly. If functional langs are a purer translation of human-to-machine thought than imperative langs, then I dearly wish code examples came better commented than a lot of the relatively uncommented open source I've been looking at, because brains structure things in wildly different ways.


## Distractions

[Overtone](https://github.com/overtone/overtone): Oh no, someone wrote an open source synthesizer toolkit in Clojure! Bookmarking this for later.

