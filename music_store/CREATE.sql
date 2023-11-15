CREATE TABLE IF NOT EXISTS Genres(
	PRIMARY KEY (genre_id),
	genre_id   INT,
	genre_name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artists(
	PRIMARY KEY (artist_id)
	artist_id   INT,
	artist_name VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS GenresArtists(
	genre_id  INT REFERENCES Genres(genre_id),
	artist_id INT REFERENCES Artists(artist_id),
	              CONSTRAINT pk_genres_artists PRIMARY KEY (genre_id, artist_id)
);

CREATE TABLE IF NOT EXISTS Albums(
	PRIMARY KEY (album_id)
	album_id     INT,
	album_name   VARCHAR(200) NOT NULL,
	release_year INT          NOT NULL
);

CREATE TABLE IF NOT EXISTS ArtistsAlbum(
	artist_id INT REFERENCES Artists(artist_id),
	album_id  INT REFERENCES Albums(album_id),
	              CONSTRAINT pk_artist_album PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS Tracks(
	PRIMARY KEY (track_id)
	track_id     INT,
	track_name   VARCHAR(200) NOT NULL,
	track_length INT,
	album_id     INT REFERENCES Albums(album_id)
);

CREATE TABLE IF NOT EXISTS Collection(
	PRIMARY KEY (collection_id)
	collection_id   INT,
	collection_name VARCHAR(200) NOT NULL,
	release_year    INT          NOT NULL
);

CREATE TABLE IF NOT EXISTS TracksCollections(
	track_id      INT REFERENCES Tracks(track_id),
	collection_id INT REFERENCES Collection(collection_id),
	                  CONSTRAINT pk_tracks_collections PRIMARY KEY (track_id, collection_id)
);