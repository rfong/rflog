Jekyll::Hooks.register :posts, :post_write do
  # code to call after Jekyll writes a post
  system("python _plugins/compile_tags.py")
end

# When to use each method of launching a subprocess in Ruby?
#   https://stackoverflow.com/a/37329716/1006596
