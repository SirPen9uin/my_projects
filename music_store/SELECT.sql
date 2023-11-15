--Задача 2

SELECT track_name, track_length 
  FROM tracks AS t 
 WHERE track_length = 
	   (SELECT MAX(track_length) 
	      FROM tracks t);

SELECT track_name, track_length 
  FROM tracks AS t 
 WHERE track_length >= 210
 ORDER BY track_length;

SELECT collection_name, 
       release_year 
  FROM collection AS c 
 WHERE release_year BETWEEN 2016 AND 2020;

SELECT artist_name 
  FROM artists AS a
 WHERE artist_name NOT LIKE '% %'; 

SELECT track_name 
  FROM tracks AS t 
 WHERE track_name iLIKE '%my%';

--Задача 3

SELECT g.genre_name, 
       count(ga.artist_id) 
  FROM genres AS g 
       LEFT JOIN genresartists AS ga 
       ON g.genre_id = ga.genre_id 
 GROUP BY g.genre_name  
 ORDER BY g.genre_name;

SELECT a.album_name, 
       a.release_year, 
       count(t.track_id) 
  FROM albums AS a
       LEFT JOIN tracks AS t 
       ON a.album_id = t.album_id 
 WHERE a.release_year BETWEEN 2019 AND 2020
 GROUP BY a.album_name, a.release_year; 

SELECT a.album_name, 
       AVG(t.track_length) 
  FROM albums AS a 
       LEFT JOIN tracks AS t 
       ON a.album_id = t.album_id 
 GROUP BY a.album_name;

--SELECT a.artist_name 
--  FROM artists AS a 
--       LEFT JOIN artistsalbum AS a2 
--       ON a.artist_id = a2.artist_id
--       LEFT JOIN albums AS a3 
--       ON a2.album_id = a3.album_id 
-- WHERE a3.release_year != 2020;

SELECT DISTINCT a.artist_name 
  FROM artists a 
 WHERE a.artist_name NOT IN (
       SELECT DISTINCT a.artist_name 
       FROM artists AS a
       LEFT JOIN artistsalbum aa ON 
       a.artist_id = aa.artist_id
       LEFT JOIN albums al ON 
       al.album_id = aa.album_id
       WHERE al.release_year = 2020
       )
 ORDER BY a.artist_name;
       

SELECT DISTINCT a2.artist_name, 
       c.collection_name 
  FROM collection AS c 
       LEFT JOIN trackscollections AS tc 
       ON c.collection_id = tc.collection_id 
       LEFT JOIN tracks AS t 
       ON t.track_id = tc.track_id 
       LEFT JOIN albums AS a 
       ON a.album_id = t.album_id 
       LEFT JOIN artistsalbum AS aa 
       ON aa.album_id = a.album_id 
       LEFT JOIN artists AS a2 
       ON a2.artist_id = aa.artist_id 
 WHERE a2.artist_id = 2;

--Задача 4

SELECT a.album_name 
  FROM albums AS a 
       LEFT JOIN artistsalbum AS aa 
       ON aa.album_id = a.album_id 
       LEFT JOIN artists AS a2 
       ON a2.artist_id = aa.artist_id 
       LEFT JOIN genresartists AS g 
       ON a2.artist_id = g.artist_id 
 GROUP BY a.album_name 
HAVING count(g.artist_id) > 1;

SELECT t.track_name, t.track_id 
  FROM tracks AS t 
 WHERE t.track_id NOT IN 
       (SELECT track_id 
          FROM trackscollections);

SELECT a.artist_name, a.artist_id, 
       t.track_id 
  FROM artists AS a 
       LEFT JOIN artistsalbum AS aa 
       ON aa.artist_id = a.artist_id 
       LEFT JOIN albums AS a2 
       ON a2.album_id = aa.album_id 
       LEFT JOIN tracks AS t 
       ON t.album_id = a2.album_id 
 WHERE t.track_length = 
       (SELECT MIN(t.track_length) 
          FROM tracks AS t)
 GROUP BY a.artist_id, a.artist_name, t.track_id;

SELECT a.album_name, COUNT(*) AS count_t
  FROM albums AS a
       LEFT JOIN tracks AS t 
       ON t.album_id = a.album_id
 GROUP BY a.album_name
HAVING COUNT(*) = (
        SELECT MIN(count_t) 
          FROM 
               (SELECT album_id, COUNT(*) AS count_t
                  FROM Tracks
                 GROUP BY album_id)
         );





















