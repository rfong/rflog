---
layout: post
title: Rust learnings from a simple temperature converter
tags: [exploration]
techTags: rust-lang, regex
description: Lazy static regexes, overflow checking, and praise for the Rust book
---

I recently started learning Rust by working through [the online book for the Rust programming language](https://doc.rust-lang.org/book/), and I appreciate it a lot!

(Why learn Rust? I dunno, I hear it's great for concurrency, type safety, and performance issues in distributed systems, and a lot of people in my Recurse batch are using Rust. So why not. Learning is always more fun with camaraderie.)

The Rust book explains the low-level nuances very thoroughly and socratically, and the documentation feels exceptional so far. The standard package manager / build tool, `cargo`, comes with a really nice command called [`cargo doc`](https://doc.rust-lang.org/cargo/commands/cargo-doc.html) that generates the HTML documentation for a package and all its dependencies!

Of course, what works for me may not work well for you. My **learning context**:
- my first languages were C and C++
- I tend to learn best visually or through text
- I've previously worked in Golang, another relatively young, concurrency-minded compiled language

The Rust book is pretty chock full of explanations, and is more geared toward people with experience in another strongly typed language, so I love it but it's obviously not ideal for everyone. However, the official Rust website offers multiple [beginner learning resources](https://www.rust-lang.org/learn) to cater to people whose learning style doesn't involve reading books, which I think is extra cool of them!

At the end of Chapter 3 of the Rust book, an innocuous example exercise was offered:

> Convert temperatures between Fahrenheit and Celsius.

My Python brain naively suggested that this would be a simple 5-line exercise, and of course was vastly wrong. I learned a lot more fun facts about Rust in the process than I had anticipated, and as usual, decided to lock in my learnings (at cost of 3x the labor) by writing up the process!

# Parsing an input string

First, let's take in an input string describing a temperature in either Fahrenheit or Celsius. For simplicity, I just started with positive integer values.

## Regexing the input

To match a positive integer followed by `F` or `C`, we might construct this regex:

`\d+ [FC]`

I figured I might as well make the space optional and match the `°` degree mark, in case I was pasting in a value from somewhere.

`\d+ ?°?[FC]`

I'm also going to match the start and end of the line, because I don't want to validate inputs with extra junk info. In other words, `10F` is valid, but `foo10Fbar` should not pass.

`^\d+ ?°?[FC]$`

Finally, I'm going to use named capture groups to match the numeric value and the `F`/`C` from the input string.

`^(?P<val>\d+) ?°?(?P<scale>[FC])$`

### Lazy static compilation for regexes

You could just use the vanilla [`regex` library](https://docs.rs/regex/1.7.1/regex/) to do the job.

However, the documentation included a helpful [heads up](https://docs.rs/regex/1.7.1/regex/#example-avoid-compiling-the-same-regex-in-a-loop) about making sure that regexes only get statically compiled exactly once if you're passing them around, since regex compilation is quite expensive. ([Statics](https://doc.rust-lang.org/std/keyword.static.html) are sort of like global variables.) I went this route since it seemed useful to know for future reference.

There's a `lazy_static` library that makes it simpler to declare lazily evaluated statics that are executed at runtime. In other words, it will make sure it's only compiled once the first time it's used, and the old value is globally reused thereafter.

For regexes specifically, there is also a [`lazy_regex` library](https://docs.rs/lazy-regex/latest/lazy_regex/) which makes things even simpler. It provides a `regex!` macro that wraps up the lazy static initialization out of sight for you.

```rust
let re = regex!(r"^(\d+) ?°?([FC])$");
```

## Validating & capturing inputs

First, here are some inputs that **shouldn't** match our regex.

```rust
// Test inputs that shouldn't parse, but also shouldn't panic
for s in ["10", " 10", "10 ", "10X", "foobar", "foo10Fbar", "30FFFF"] {
    assert_eq!(re.is_match(s), false, "'{s}' is not a valid input");
}
```

Here are some valid inputs.
```rust
// Test valid inputs
for s in ["10F", "10°F", "10 F", "10 °F", "10 C"] {
    assert_eq!(re.is_match(s), true, "failed to match '{s}'");
}
```

We can then extract the captured matches and unwrap them.
- `captures` pulls out the groups that we put in parentheses in the regex.
- `unwrap()` is a handler for a `Result` instance, which will either give us the value inside the `Result`, or panic if we received an error. Handy to not have to deal with errors you really shouldn't be getting, although in other cases, you might actually want to do something with that error other than crash the whole program.

```rust
// Test valid inputs
for s in ["10F", "10°F", "10 F", "10 °F", "10 C"] {
    assert_eq!(re.is_match(s), true, "failed to match '{s}'");
    let cap = re.captures(s).unwrap();
    println!("'{s}'\t captures: '{}', '{}'", &cap["val"], &cap["scale"]);
}
```

```
'10F'    captures: '10', 'F'
'10°F'	 captures: '10', 'F'
'10 F'	 captures: '10', 'F'
'10 °F'	 captures: '10', 'F'
'10 C'	 captures: '10', 'C'
```

# Temperature conversion

Great, let's actually convert some temperatures now!

```rust
let val: u32 = cap["val"].parse().expect("Not a number!");
// F -> C
if cap["scale"] == "F" {
  let converted = (val - 32) * 5/9;
  println!("{val}°F = {converted}°C")
}
```

```
Input an integer temperature value, e.g. '50F' or '10C'
> 30F
thread 'main' panicked at 'attempt to subtract with overflow', src/main.rs:42:25
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

Oh no, overflow! Are we supposed to be using [`checked_sub`](https://docs.rs/num/latest/num/trait.CheckedSub.html) instead of normal subtraction?? 😱

## Oops, types! Let's handle negative values.

Those of you with keener eyes for type declarations may have noticed that I messed up twice:
1. By absent-mindedly using an unsigned int type, `u32`, which doesn't reflect that the Celsius and Fahrenheit scales can have negative values
2. By procrastinating dealing with negative numeric values

Nevertheless, I was overjoyed to bump into Rust's overflow safety system so soon, and look forward to a future glorious day when it will surely divert me from silly errors that, in a less safe language, might otherwise wreck my day in prod.

After changing the type declaration to `i32` signed ints and going back to update the regex (and test cases!) to handle negative values, everything works fine.

```rust
let re = regex!(r"^(?P<val>-?\d+) ?°?(?P<scale>[FC])$");
let cap = re.captures(&input).unwrap();
let val: i32 = cap["val"].parse().expect("Not a number!");

if cap["scale"] == "F" {
  // F -> C
  let converted = (val - 32) * 5/9;
  println!("{val}°F = {converted}°C")
} else if cap["scale"] == "C" {
  // C -> F
  let converted = val * 9/5 + 32;
  println!("{val}°C = {converted}°F")
}
```

```
Input an integer temperature value, e.g. '-50F' or '10C'
> -61F
-61°F = -51°C
```

Note that -61°F is actually equivalent to -51.666...C, which should round to -52°C. Since I never added float handling, we're getting these integer values through truncation rather than rounding. In other words, the decimal part is just getting chopped off. Let's go back and fix that now.

## Float handling

The updated regex:

`^(?P<val>-?\d*\.?\d+) ?°?(?P<scale>[FC])$`

Yeah, no one likes reading another person's regex. The key change: `\d*\.?`.

```
'.5C'	 captures: '0.5', 'C'
'0.5C'	 captures: '0.5', 'C'
'-1.5C'	 captures: '-1.5', 'C'
```

I then went back and changed everything to floating point arithmetic, which I probably should have just done in the first place. I also looked up the [string formatting](https://doc.rust-lang.org/std/fmt/#precision) rules for float precision, because who ever needs more than three sig figs.

```
Input a temperature value, e.g. '-50F' or '10.5C'
> -61F
-61°F = -51.667°C
```

## Absolute zero

You may notice that it's possible to input some temperatures which are definitionally impossible in real life.

```
> -9000F
-9000°F = -5017.778°C
```

Let's add checks for [absolute zero](https://en.wikipedia.org/wiki/Absolute_zero).

```rust
const ABS_ZERO_C: f64 = -273.15;
const ABS_ZERO_F: f64 = -459.67;
```

```
> -9000F
Value must be >= absolute zero (-459.67°F)
```

## That's all I can think of for now

...until I get into using Rust to compile juicy homemade CLI tools, which I'm very excited for! 'Til then, I shall delve further into the Rust book.
