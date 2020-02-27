This is my mostly-code blog! It runs on [Jekyll](https://jekyllrb.com/) and is forked from the [Hyde theme](https://github.com/poole/hyde).

### Run server

Is Ruby working? If not:
```
rvm get stable --auto-dotfiles
rvm use ruby-2.6.3
```

Serve:
```
bundle exec jekyll serve
```

### Tag pages

Tag pages are auto-generated via a Python script which is auto-run on `:post_write` by a Jekyll hook.

Jekyll [hooks](https://jekyllrb.com/docs/plugins/hooks/) are a subtype of [plugins](https://jekyllrb.com/docs/plugins/installation/). The build tool expects to see `.rb` files placed in the `_plugins` directory.

### Implementation references

- [Implement tags in Jekyll](https://codinfox.github.io/dev/2015/03/06/use-tags-and-categories-in-your-jekyll-based-github-pages/)
- [Automatic generation of category/tag pages in Jekyll](https://github.com/jekyll/jekyll/issues/6952)
