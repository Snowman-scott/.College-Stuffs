# hell yeah

## Music
the music industry is pretty self explanitory, they offer music streaming services, and CDs, records, Tapes, Etc..
Every track has specific metadata that is tracked so we can identify the songs with just bland files. 

the music industry provides Entertainment to people in the form of audio, allowing people. Spotify is an example of an app that.

## Manga
The manga industry provides entertainment, Specifically yen press provided translated manga to the world which you can buy on many store fronts.

there is a site called anilist.co which lists anime, manga and have an API where you can search and pull info from anilist about different mangas and anime, manga and anime also pose a UI/UX decision too.

## anilist.co

### Features
Anilist is an anime and manga database, they hold entries for loads of anime's and manga's. It is a newer better version of MyAnimeList (MAL).
Anilist has an GraphQL API that you can query to pull info about specific manga's and anime's including Characters and Voice actors from the anime's, Anilist allows you to search up manga's and anime's on their site, show you the blurb about them, episode count / release count, if it is still being released or if it has ended and Images from the manga or anime. They also have reviews on each episode / volume, It has recommendations based on the manga or anime your looking at. Shows when an anime was made from a manga, and shows what type of release it was too.

AniList has a Login and signup system that allows users to make their own lists of manga and anime they may want to read or watch, This also allows users to write comments on the manga/anime and review it, give it an overall rating/ranking  of the anime / manga, and allow you to talk to people in forums about any of the manga and anime (or anything really)

### How it works
To make a login system you need a database, username checking, password hashing for security, Just make the login safe and secure T_T,

Reviews need to be stored in another db table with username of the reviewer, the review itself, and the rating they gave like 4/5 stars.

The pages showing the main metadata for the manga or anime needs to have that in a table where it list the name, release date and all the links to the images.

The forum, uhm live chat idfk how that shi works (I'm not using AI for this task nor searching it up T-T) for a static one that updates every so often, you can just have a table for it and append the newest chat to the bottom of it, again not too sure.

Recommendations is an algo that pulls tags about the current anime/manga and recommends more anime/manga that share the same tags and type of plot.

User lists are just a table in their user area that has the basic link it the main manga / anime on it so they can view it 

Comments are similar to the forum just scoped for the overall anime/ manga and not in a forum type of thing.

## Why?

Making anilist will benifit the community, It will stop the need to bounce between 10 different sites just to find the one specific manga someone was looking for. It can also drive more engagement towards the smaller niche anime's and manga's as people can review them highly, find them easily and talk about them in forum drawing attention to them.

The goal is to make a platform where people can come, Find anime or manga, See what other people think about it, talk to other anime and manga fans about their fave manga's and anime's, Make it easy for the community to find sources for the more niche anime's and find where to buy manga easily without needing to look through scummy websites and dangerous providers, anilist will just have a list of the safe providers so the community can safley buy manga and safely watch anime. 

Anilist will just make the whole process faster, more streamlined, safer and easier for everyone. the API will also allow people to have easy access to a database of all things anime and manga without needing to interface with a website that looks and feels like it was stolen straight from 2008.
