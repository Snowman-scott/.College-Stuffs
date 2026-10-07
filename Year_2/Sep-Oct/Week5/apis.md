# API research

## Pre flight
1. The client is a webapp or browser
2. The server returns JSON to the browser
3. The Browser is responsible for rendering and displaying the HTML + CSS + Js, The backend Is responsible for putting the allotted variables into the template.
4. No The server does not need to Know what the client looks like, It is good for blocking bots but not required
5. Response A is a HTML page that has been returned with all the variables filled out in a nice easy to read format, Response B is easier for machines to read as it is raw dictionaries so they are less easy for users to read

## Section A
1. Application Programming Interface
2. An API is a set of rules and protocols that allows different software applications to communicate and exchange data with each other.
3. An API solves the problem of fragmentation and redundant work in software development. Without APIs every single application would have to be built as a self contained island, reinventing and re writing fundamental features from scratch and finding custom, fragile ways to talk to external systems
4. One piece of software may produce valuable data like a weather api, and another app might be really good at displaying the data from that specific backend, so they use the API to pull the data needed to make the data look presentable and easy to look at
5. an api endpoint is a location a request is sent to like `https://api.example.com/v1/home/data` which may pull data for the homepage from an API
6. A request is the client asking for a piece of information or data from the backend / API
7. A response is the API/Backend returning a piece of information or data the client requested, or an Error message
8. HTTP is the protocol used to make the requests and responses
9. An API returns a payload for something or someone to use, usually in JSON or XML Usually used for software. A Webpage returns information for an Audience of people to easily scroll through, read and understand without needing to read lines and lines of json data
10. An API is usually just JSON so it does not have a visual interface, you can read API responses in your browser, they are just JSON
11. They would use an API as it allows them to query and pull any products they may have in a database rather than a webpage that is set to only one product, it makes the webpage more user friendly and less annoying as you don't need different pages set for one specific product

## Section B

### LRCLIB 
1. LRCLIB is a lyrics database, it allows users to search for lyrics to any song, and allows most people to commit lyrics to the database too
2. Developers of music applications, people trying to add lyrics to their songs, live productions needing synced lyrics for their music etc...
3. It allows you to search up an album, track, artist and get the lyrics to that track in plain text and synced lyrics
4. The request usually contains a track name, An artist name and an album name but is not tied to only those, these are just the most common ones used
5. A response would contain the track name, album name, artist name, duration, and the plain + synced (if it has them) lyrics
6. An audio lyric tagging applicaton like [golrc](https://github.com/KillAllChickens/golrc) or people on the [lrclib.net](https://lrclib.net) webpage
7. there are a lot of songs, and a lot of lyrics, it is good as you are querying a database that you can add and remove lyrics from rather than storing them in the static HTML

### ListenBrainz
1. Listenbrainz is a music scrobbling service their API allows you to pull recent listens via Username. You can search for a users listens by querying their API with the correct username, it is also the way scrobblers send your listens to listenbrainz, and ways you can verify accounts exist
2. Anybody making a scrobbler, anyone listening to music, anybody wanting to look at their listens (if they have set up scrobbling)
3. Listen tracking, when a user listened to what, what music they may like, their music phases (like spotify wrapped but every week, month, year, day)
4. A request may contain listens, succesful scrobbles, what the scrobbled track is including Album name artist name track name etc..
5. A response may be data being returned or a validation message saying the data was successfully taken in by the listenbrainz backend.
6. The User scrobbling listens, or the application pulling data to show you your patterns
7. You are constantly adding tracks and displaying new tracks on users profiles, updating HTML to add these tracks and scrobbles would mean multiple updates a second, which causes a lot of issues for HTML on live prod servers

### MusicBrainz
1. It is a metadata and album tagging and tracking database run by the community. you can add releases to the database for artists like the beatles, then people add the track lengths, titles, artists, etc to the information, then when people go to tag tracks and albums the metadata gets added to the database for other users to use when tagging their tracks.
2. Track taggers, data analysis, developers pulling track and album information
3. Metadata, what the album track artist are, where it came form, etc...
4. A request may have data about a track, or a request for data about a track
5. A response may be validation saying the DB accepted the data or the information about the track that the user requested
6. A browser requesting data, the user tagging data for a track.
7. There is a lot of data that is being added and submitted that updating the front every time would be too costly for the server
