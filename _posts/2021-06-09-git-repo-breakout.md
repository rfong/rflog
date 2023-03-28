---
layout: post
title: Breaking out a git repo subdirectory
tags: [refactor, hot-tips, tutorial, workflow]
description: For when your micro-projects get too big and need to move into their own repo!
---

I've been sporadically doing some [creative coding](https://rfong.github.io/creative-coding) in a [sandbox repo](https://github.com/rfong/rc-sandbox) I made to play in during my time at Recurse Center. It's starting to become a real mishmash of languages. I just added some dependencies and a simple build system to my creative coding subdirectory, so it was about time to split that bad boy out into its own repo. But I was loath to lose my valuable commit history in the process.

[This blog post](http://tuxdiary.com/2015/08/13/move-subdir-new-git-repo-preserve-history/) tipped me off to the tricky `git filter-branch` command to filter your source and history down to a subdirectory, but overall my approach ended up taking a lot fewer steps than theirs.

## Warning: `filter-branch` vs. `filter-repo`

[`git filter-branch`](https://git-scm.com/docs/git-filter-branch#_warning) warning:
> `git filter-branch` has a plethora of pitfalls that can produce non-obvious manglings of the intended history rewrite (and can leave you with little time to investigate such problems since it has such abysmal performance).

The safer approach is [`git filter-repo`](https://github.com/newren/git-filter-repo/). Thanks very much to [Coby](https://github.com/acobster) for pointing this out to me!

`git filter-branch` comes built in to `git`, but note that `git filter-repo` requires some minimal setup to suit your `bin` preferences. I cloned it and then symlinked the executable.
```
git clone https://github.com/newren/git-filter-repo.git
cd git-filter-repo
`ln -s `pwd`/git-filter-repo` /usr/local/bin/git-filter-repo
```

## Approach

Let's say your original repo has this structure.
```
repo1
  - dir1
  - dir2
  - targetdir
  - file1
  - file2
```

And you want to break out the contents of `targetdir`, with intact revision history, as a new repo `repo2`.

(For purposes of this walkthrough, I'm assuming that `repo1` has a remote URL and that you also want your new `repo2` to have a remote URL. Also, note that this approach will ignore any uncommitted work in `repo1/targetdir`.)

1. Move to the directory you want your new `repo2` to live in.

2. Clone `repo1` into a folder named `repo2`.
```
mkdir repo2
git clone <repo1_git_URL> repo2
cd repo2
```

3. The following incantation removes all git content that is not relevant to `targetdir`, and brings `targetdir`'s contents up to the root.
```
git filter-repo --subdirectory-filter targetdir
```
(Note that this still works if your target dir is nested, e.g. `dirA/dirB/targetdir`.)

4. Double check that your desired log is intact and things are as expected!
```
git log
git status
```
If your original `repo1/.gitignore` defined recursive rules that are necessary for the contents of `targetdir`, you will probably notice those now. Copy over what you need.

5. When everything looks good, `git commit` what you want.

6. Swap your remote URL from `repo1`'s to reflect your new remote. Below I'm assuming that the remote is named `origin`, but you do you.
```
git remote rm origin
git remote add origin <repo2_git_url>
```

All done and ready to push!
