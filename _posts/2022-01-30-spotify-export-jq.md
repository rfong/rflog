---
layout: post
title: Compact human-readable Spotify export
tags: [own-your-data, hot-tips]
techTags: bash
imgurl: 2022-01-30-reasonable.png
description: Save your music curation data in case Spotify ever deletes it or implodes!
---

Annoyed at the inevitability that VC-backed software platforms you rely on will spontaneously close one day and drop your years of useful data with no good way to export it in time even though you pay for their services? Me too, constantly!

I've invested several years of music curation into Spotify and realized it's incredibly careless that I have never made a local human-readable backup. There are plenty of integrations that allow you to import your playlists into other streaming services, but it's always good to have a local backup of things you have put a lot of effort into.

Conveniently, a lot of people have already written export tools, so I didn't have to write any code; I just needed to gently massage my raw export a bit with `jq` filters to make it more compact and readable.

# Export tools

[This support thread](https://community.spotify.com/t5/Desktop-Windows/Export-Playlist-Backup/m-p/1092427) suggests [SpotMyBackup](http://www.spotmybackup.com/), a web-based tool which unfortunately did not seem to work for me at the time. I instead ran [`caseychu/spotify-backup`](https://github.com/bitsofpancake/spotify-backup), a small Python script.

The documentation doesn't include minor version info at the moment. I switched locally to Python 3.8 and it worked fine, but I didn't actually binary search to find out which minor version was necessary, so YMMV.

# Filtering exploration

There is a lot of extra data in there that you probably don't often need as a user, such as `available_markets`, various unique Spotify IDs, album art image metadata, and so on.

<img alt="spotify raw data dump *screams uncontrollably in watts*" src="{{site.baseurl}}/assets/images/2022-01-30-unnecessary_data.png" />

My raw text dump was a whopping 48.8 Mb, so I inspected it and sliced it up with [`jq`](https://stedolan.github.io/jq/), a truly spectacular and very powerful tool for command line manipulation of JSON files. 

First, quickly looked over the structure:
```
# This dumps the top level keys
keys
# This dumps the `name` values of the objects in the top level array
.[] | .name
# But we'll actually want those as an array at some point
[.[] | .name]
# Let's check out the first playlist
.[0]
# Too verbose, just grab its name
.[0] | .name
```

`.[0]`, "Liked Songs", was a pretty long playlist, so I switched over to testing with a shorter playlist, `.[1]`, for ease of reading.

We probably want playlists containing lists of track objects.
```
.[1] | {(.name): [.tracks[] | .track | {name}]}
# Grab more fields
.[1] | {(.name): [.tracks[] | .track | {name, uri, album: .album .name, artists: [.artists[] .name] }] }
```

Now let's actually include all playlists in a reasonable format.
```
# List of playlist names
[.[] | name]
# List of playlist objects (just name)
[.[] | {name}]
# List of playlist objects, with lists of track names
[.[] | {name, tracks: [.tracks[] | .track | name]}]
# ...and add back all the track fields we wanted
[.[] | {name, tracks: [.tracks[] | .track | {name, uri, album: .album .name, artists: [.artists[] .name] } ]}]
```

This is pretty much what I want! Ran it and dumped to a dated file.
```bash
cat dump.json | jq '[.[] | {name, tracks: [.tracks[] | .track | {name, uri, album: .album .name, artists: [.artists[] .name] } ]}]' > dump.concise.json
```
This is 0.2 Mb, which is a lot more reasonable for several years of textual track lists.

<img alt="compact filtered data export" src="{{site.baseurl}}/assets/images/2022-01-30-reasonable.png" />

Thank you so much `caseychu` and `stedolan` for writing these handy tools!
