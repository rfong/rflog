serve:
	bundle exec jekyll serve

# spawn a daily new microblog post
# usage: `make daily title=my-title`
daily:
	./_plugins/make_daily_note.sh $(title)
