"""
This is the directors module and supports all the REST actions for the
directors and movies data
"""

from flask import make_response, abort, jsonify
from config import db
from models import Directors, Movies, MoviesSchema


def read_all():
    """
    This function responds to a request for /api/movies
    with the complete list of movies, sorted by movie id desc

    :return:                json list of all movies, message data empty
    """
    # Query the database for all the movies
    movies = Movies.query.order_by(db.desc(Movies.id)).all()

    # Serialize the list of movies from our data
    movie_schema = MoviesSchema(many=True)
    data = movie_schema.dump(movies)

    if(len(data) == 0):
        return abort(404, f"Movies data not found!")

    return data


def read_limit(limit, order, attribute):
    """
    This function responds to a request for /api/movies/{limit}/{order}
    with the complete list of movies, sorted by movie id (custom input asc or desc)

    :param limit:       for size return movies data
    :param order:       asc or desc order
    :return:            json list of limit movies order by request, message if data empty
    """

    # Create the list of movies from our data
    # match attribute:
    if attribute == 'id':
        movies = Movies.query.order_by(db.desc(
            Movies.id) if f'{order}' == 'desc' else db.asc(Movies.id)).limit(limit)
    elif attribute == 'director id':
        movies = Movies.query.order_by(db.desc(
            Movies.director_id) if f'{order}' == 'desc' else db.asc(Movies.director_id)).limit(limit)
    elif attribute == 'original title':
        movies = Movies.query.order_by(db.desc(
            Movies.original_title) if f'{order}' == 'desc' else db.asc(Movies.original_title)).limit(limit)
    elif attribute == 'budget':
        movies = Movies.query.order_by(db.desc(
            Movies.budget) if f'{order}' == 'desc' else db.asc(Movies.budget)).limit(limit)
    elif attribute == 'popularity':
        movies = Movies.query.order_by(db.desc(
            Movies.popularity) if f'{order}' == 'desc' else db.asc(Movies.popularity)).limit(limit)
    elif attribute == 'release date':
        movies = Movies.query.order_by(db.desc(
            Movies.release_date) if f'{order}' == 'desc' else db.asc(Movies.release_date)).limit(limit)
    elif attribute == 'revenue':
        movies = Movies.query.order_by(db.desc(
            Movies.revenue) if f'{order}' == 'desc' else db.asc(Movies.revenue)).limit(limit)
    elif attribute == 'title':
        movies = Movies.query.order_by(db.desc(
            Movies.title) if f'{order}' == 'desc' else db.asc(Movies.title)).limit(limit)
    elif attribute == 'vote average':
        movies = Movies.query.order_by(db.desc(
            Movies.vote_average) if f'{order}' == 'desc' else db.asc(Movies.vote_average)).limit(limit)
    elif attribute == 'vote count':
        movies = Movies.query.order_by(db.desc(
            Movies.vote_count) if f'{order}' == 'desc' else db.asc(Movies.vote_count)).limit(limit)
    elif attribute == 'overview':
        movies = Movies.query.order_by(db.desc(
            Movies.overview) if f'{order}' == 'desc' else db.asc(Movies.overview)).limit(limit)
    elif attribute == 'tagline':
        movies = Movies.query.order_by(db.desc(
            Movies.tagline) if f'{order}' == 'desc' else db.asc(Movies.tagline)).limit(limit)
    elif attribute == 'uid':
        movies = Movies.query.order_by(db.desc(
            Movies.uid) if f'{order}' == 'desc' else db.asc(Movies.uid)).limit(limit)
    else:
        abort(404, f"Movies not found for attribute {attribute}!")

    # Serialize the list of movies from our data
    movie_schema = MoviesSchema(many=True)
    data = movie_schema.dump(movies)

    if(len(data) == 0):
        return abort(404, f"Movies data not found!")

    return data


def read_one(director_id, movie_id):
    """
    This function responds to a request for
    /api/directors/{director_id}/movies/{movie_id}
    with one matching movie for the associated director

    :param director_id:       Id of director the movie is related to
    :param movie_id:          Id of the movie
    :return:                  json string of movie data, 404 if not found
    """
    check_director = (Directors.query.filter(
        Directors.id == director_id)).one_or_none()

    if check_director is not None:
        # Query the database for the movie
        movie = (
            Movies.query.join(Directors, Directors.id == Movies.director_id)
            .filter(Directors.id == director_id)
            .filter(Movies.id == movie_id)
            .one_or_none()
        )

        # Was a movie found?
        if movie is not None:
            movie_schema = MoviesSchema()
            data = movie_schema.dump(movie)
            return data

        # Otherwise, nope, didn't find that movie
        else:
            abort(404, f"Movie not found for ID: {movie_id}!")

    # Otherwise, nope, didn't find that movie
    else:
        abort(404, f"Director not found for ID: {director_id}!")


def create(director_id, movie):
    """
    This function creates a new movie related to the passed in director id.

    :param director_id:       Id of the director the movie is related to
    :param movie:            The JSON containing the movie data
    :return:                data and 201 on success, 404 if not found, 409 if movie exists already
    """
    # validate field
    budget = movie.get("budget")
    original_title = movie.get("original_title")
    overview = movie.get("overview")
    popularity = movie.get("popularity")
    release_date = movie.get("release_date")
    revenue = movie.get("revenue")
    tagline = movie.get("tagline")
    title = movie.get("title")
    uid = movie.get("uid")
    vote_average = movie.get("vote_average")
    vote_count = movie.get("vote_count")

    if budget is None or budget is "":
        abort(400, "Field budget must be required!")
    if original_title is None or original_title is "":
        abort(400, "Field original_title must be required!")
    if uid is None or uid is "":
        abort(400, "Field uid must be required!")
    if overview is None or overview is "":
        abort(400, "Field overview must be required!")
    if popularity is None or popularity is "":
        abort(400, "Field popularity must be required!")
    if release_date is None or release_date is "":
        abort(400, "Field release_date must be required!")
    if revenue is None or revenue is "":
        abort(400, "Field revenue must be required!")
    if tagline is None or tagline is "":
        abort(400, "Field tagline must be required!")
    if title is None or title is "":
        abort(400, "Field title must be required!")
    if vote_average is None or vote_average is "":
        abort(400, "Field vote_average must be required!")
    if vote_count is None or vote_count is "":
        abort(400, "Field vote_count must be required!")

    # get the parent director
    director = Directors.query.filter(
        Directors.id == director_id).one_or_none()

    # Was a director found?
    if director is None:
        abort(404, f"Director not found for ID: {director_id}!")

    uid = movie.get("uid")
    existing_movie = (
        Movies.query.filter(Movies.uid == uid).one_or_none()
    )

    # Can we insert this director?
    if existing_movie is None:

        # Create a movie schema instance
        schema = MoviesSchema()
        new_movie = schema.load(movie, session=db.session)

        # Add the movie to the director and database
        director.movies.append(new_movie)
        db.session.commit()

        # Serialize and return the newly created movie in the response
        data = schema.dump(new_movie)

        return data, 201

    # Otherwise, nope, director exists already
    else:
        abort(409, f"Movie with UID {uid} exists already!")


def update(director_id, movie_id, movie):
    """
    This function updates an existing movie related to the passed in
    director id.

    :param director_id:       Id of the director the movie is related to
    :param movie_id:         Id of the movie to update
    :param movie:            The JSON containing the movie data
    :return:                200 on success, 404 if not found, 409 if movie exists already
    """
    # validate field
    budget = movie.get("budget")
    original_title = movie.get("original_title")
    overview = movie.get("overview")
    popularity = movie.get("popularity")
    release_date = movie.get("release_date")
    revenue = movie.get("revenue")
    tagline = movie.get("tagline")
    title = movie.get("title")
    uid = movie.get("uid")
    vote_average = movie.get("vote_average")
    vote_count = movie.get("vote_count")

    if budget is None or budget is "":
        abort(400, "Field budget must be required!")
    if original_title is None or original_title is "":
        abort(400, "Field original_title must be required!")
    if uid is None or uid is "":
        abort(400, "Field uid must be required!")
    if overview is None or overview is "":
        abort(400, "Field overview must be required!")
    if popularity is None or popularity is "":
        abort(400, "Field popularity must be required!")
    if release_date is None or release_date is "":
        abort(400, "Field release_date must be required!")
    if revenue is None or revenue is "":
        abort(400, "Field revenue must be required!")
    if tagline is None or tagline is "":
        abort(400, "Field tagline must be required!")
    if title is None or title is "":
        abort(400, "Field title must be required!")
    if vote_average is None or vote_average is "":
        abort(400, "Field vote_average must be required!")
    if vote_count is None or vote_count is "":
        abort(400, "Field vote_count must be required!")

    check_director = (Directors.query.filter(
        Directors.id == director_id)).one_or_none()

    if check_director is not None:

        existing_movie = (
            Movies.query.filter(Movies.uid == uid).one_or_none()
        )

        # Can we insert this director?
        if existing_movie is None:

            update_movie = (
                Movies.query.filter(Directors.id == director_id)
                .filter(Movies.id == movie_id)
                .one_or_none()
            )

            # Did we find an existing movie?
            if update_movie is not None:

                # turn the passed in movie into a db object
                schema = MoviesSchema()
                update = schema.load(movie, session=db.session)

                # Set the id's to the movie we want to update
                update.director_id = update_movie.director_id
                update.id = update_movie.id

                # merge the new object into the old and commit it to the db
                db.session.merge(update)
                db.session.commit()

                # return updated movie in the response
                data = schema.dump(update_movie)

                return data, 200

            # Otherwise, nope, didn't find that movie
            else:
                abort(404, f"Movie not found for ID: {movie_id}!")

        # Otherwise, nope, director exists already
        else:
            abort(409, f"Movie with UID {uid} exists already!")

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for ID: {director_id}!")


def delete(director_id, movie_id):
    """
    This function deletes a movie from the movie structure

    :param director_id:   Id of the director the movie is related to
    :param movie_id:     Id of the movie to delete
    :return:            200 on successful delete, 404 if not found
    """
    check_director = (Directors.query.filter(
        Directors.id == director_id)).one_or_none()

    if check_director is not None:
        # Get the movie requested
        movie = (
            Movies.query.filter(Directors.id == director_id)
            .filter(Movies.id == movie_id)
            .one_or_none()
        )

        # did we find a movie?
        if movie is not None:
            db.session.delete(movie)
            db.session.commit()
            return make_response(
                "Movie with ID {id} deleted successfully!".format(
                    id=movie_id), 200
            )

        # Otherwise, nope, didn't find that movie
        else:
            abort(404, f"Movie not found for Id: {movie_id}")

    # Otherwise, nope, didn't find that movie
    else:
        abort(404, f"Director not found for Id: {director_id}")


def search_all(keyword):
    """search data by field title with like

    Keyword arguments:  keyword -- word for search data use like
    Return: data directors with title like keyword
    """
    search = "%{}%".format(keyword)
    movies = Movies.query.filter(Movies.title.like(search)).all()

    # Serialize the data for the response
    movie_schema = MoviesSchema(many=True)
    data = movie_schema.dump(movies)

    if(len(data) == 0):
        return abort(404, f"Movies data not found with keyword {keyword}!")

    return data
