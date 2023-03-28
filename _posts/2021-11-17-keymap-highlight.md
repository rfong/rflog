---
layout: post
title: Syntax highlighting my keymap quickref
techTags: bash
imgurl: 2021-11-17-keymap-withcolor.png
description: What did I fill all four layers on my keyboard with, anyway?
---

I realized I needed a CLI quickref to my keymap, which is now a QMK `.c` file that I am modding constantly. I didn't have to write any real code, because coders L O V E their syntax highlighters and string manipulation, and there are already open source packages for anything you can imagine in that space, but I learned about a couple of fun new packages and `awk`/`sed` tidbits in the process.

# Multiline string extraction

Originally I was going to lexically extract the keymap array by bracket matching a multiline pattern with `sed`. However, my keymap also uses a large quantity of macros and some functions which are defined outside of the keymap literal, which means the stuff I care about extracting from `keymap.c` is more semantically than lexically defined. 

I also don't want to just dump the entire file, because there is a lot of OLED and LED handling code and miscellaneous `#define`s that I don't need to reference.

So I inserted some comments to delineate the relevant blocks, and used `awk` to grab the text in between them.

```bash
cat $MY_KEYMAP_FILE | awk '/BEGIN KEYMAP/,/END KEYMAP/'
```

This inclusively returns multiline string matches where the first line matches the start pattern and the last line matches the end pattern. (Note that I was being lazy and did not bother to type out an exact match regex, because I knew there would not be any accidental partial matches in my keymap file.)

If you have *multiple* blocks matching this pattern in the input, it will return all of them.

There is probably some fancy regex `awk` approach to removing the start and end lines, but I found it easier and more readable to chop them the `bash` way.

### Chop the first line

```bash
tail -n +2
```

This passes through all *but* the first line, or to be more precise, it returns the input's tail starting from line 2.

### Chop the last line

There are some versions of `head` that will let you pass through all but the last line of the input with `head -n -2`, but unfortunately, this negative indexing format is not always supported. So for portability, a `sed` solution is recommended instead.

```bash
sed \$d
```

This deletes the last line of the input.

Of course, you could also get cute and reverse the entire input, run the previous command to chop what's now the first line (a.k.a. the original last line, reversed), and reverse it all back.

`rev` only reverses single-line strings. If you pass `rev` a multiline string, it will treat it as an array of strings, and individually reverse the lines while keeping their order the same.

```bash
$ echo 'line1
> line2
> line3' | rev
1enil
2enil
3enil
```

Instead, you'll want `tac` (its name is the reverse of `cat`). It outputs normal lines in reversed *order*.

```bash
$ echo 'line1
> line2
> line3' | tac
line3
line2
line1
```

We only need the line order reversed for this particular use case, not the entire string. If you wanted to completely reverse a multiline string, you could probably get away with `[input] | tac | rev`, but that potentially gets into hairy usability issues like what character encoding is expected, do multi-byte runes exist, etc. See why coders have such pedantic thought patterns?

(Ok, I actually checked out of morbid curiosity, and it looks like `rev` handles other language glyphs just fine.)
```bash
$ echo 'line1
> line2
> 日本語' | tac | rev
語本日
2enil
1enil
```

Anyway, if you were to chop the first and last line in this way, it would look like this:

```bash
[input] | tail -n +2 | tac | tail -n +2 | tac
```

### Extracted keymap

```bash
cat $MY_KEYMAP_FILE | \
  awk '/BEGIN KEYMAP/,/END KEYMAP/' | \
  tail -n +2 | \
  sed \$d
```

I also piped the output to `less` in order to make it easier to browse, since it takes up more than a page's worth of text.

# Colorization needed

The output is there, but it's visually difficult to scan an overwhelmingly monochromatic wall of text.

![Unhighlighted keymap dump]({{site.baseurl}}/assets/images/2021-11-17-keymap-nocolor.png)

## `source-highlight`

[GNU documentation here](https://www.gnu.org/software/src-highlite/source-highlight.html)

This package takes a source file and produces a document with syntax highlighting. It supports a pretty long list of languages and file formats.

Here are the instructions to [use `source-highlight` with `less`](https://www.gnu.org/software/src-highlite/source-highlight.html#Using-source_002dhighlight-with-less). This adds `less` syntax highlighting for files on the filesystem, but *not* for my piped text, which makes sense in retrospect since it's a partial C file with no metadata or file extension.

There is probably some way to enable or force this, but I found it easier to just pipe it into a different syntax highlighter instead. 

This was a general win anyways, as I didn't have syntax highlighting in `less` before and it's really convenient to have it now!

## `pygmentize`

[CLI documentation here](https://pygments.org/docs/cmdline/)

This package is a Python syntax highlighter that comes with a CLI and that knows how to lex and highlight a pretty large variety of languages. 

I piped my output (a partial excerpt of a `.c` file) to `pygmentize -l -c | less` to force C syntax highlighting in the `less` view.

# Keymap quickref macro
```bash
cat $MY_KEYMAP_FILE | \
  awk '/BEGIN KEYMAP/,/END KEYMAP/' | \
  tail -n +2 | \
  sed \$d | \
  pygmentize -l c | \
  less
```

![Highlighted keymap dump]({{site.baseurl}}/assets/images/2021-11-17-keymap-withcolor.png)

Much better!
