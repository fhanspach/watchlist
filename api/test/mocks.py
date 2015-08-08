import json

__author__ = 'felixhanspach'


class OMDBMock(object):
    @staticmethod
    def _request_api_success(movie_title, year):
        return {
            "Title": "Frozen",
            "Year": "2013",
            "Rated": "PG",
            "Released": "27 Nov 2013",
            "Runtime": "102 min",
            "Genre": "Animation, Adventure, Comedy",
            "Director": "Chris Buck, Jennifer Lee",
            "Writer": "Jennifer Lee (screenplay), Hans Christian Andersen (inspired by the story \"The Snow Queen\" by), Chris Buck (story), Jennifer Lee (story), Shane Morris (story), Dean Wellins (additional story)",
            "Actors": "Kristen Bell, Idina Menzel, Jonathan Groff, Josh Gad",
            "Plot": "Anna, a fearless optimist, sets off on an epic journey - teaming up with rugged mountain man Kristoff and his loyal reindeer Sven - to find her sister Elsa, whose icy powers have trapped the kingdom of Arendelle in eternal winter. Encountering Everest-like conditions, mystical trolls and a hilarious snowman named Olaf, Anna and Kristoff battle the elements in a race to save the kingdom. From the outside Anna's sister, Elsa looks poised, regal and reserved, but in reality, she lives in fear as she wrestles with a mighty secret-she was born with the power to create ice and snow. It's a beautiful ability, but also extremely dangerous. Haunted by the moment her magic nearly killed her younger sister Anna, Elsa has isolated herself, spending every waking minute trying to suppress her growing powers. Her mounting emotions trigger the magic, accidentally setting off an eternal winter that she can't stop. She fears she's becoming a monster and that no one, not even her sister, can help her.",
            "Language": "English, Icelandic",
            "Country": "USA",
            "Awards": "Won 2 Oscars. Another 76 wins & 53 nominations.",
            "Poster": "http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SX300.jpg",
            "Metascore": "74",
            "imdbRating": "7.7",
            "imdbVotes": "352,373",
            "imdbID": "tt2294629",
            "Type": "movie",
            "Response": "True"
        }
