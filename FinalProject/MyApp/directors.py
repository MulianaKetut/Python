"""
This is the directors module and supports all the REST actions for the
directors and movies data
"""

from flask import make_response, abort, jsonify
from config import db
from models import Directors, DirectorsSchema, Movies


def read_all():
    """
    This function responds to a request for /api/directors
    with the complete lists of directors order by id asc

    :return:        json string of list of directors, message data empty
    """
    # Create the list of directors from our data
    directors = Directors.query.order_by(Directors.id).all()

    # Serialize the data for the response
    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)
    if(len(data) == 0):
        return abort(404, f"Directors data not found!")

    return data


def read_limit(limit, order, attribute):
    """
    This function responds to a request for /api/directors
    with the complete lists limit directors order by request (asc or desc)
    default asc order

    :param limit:       for size return directors data
    :param order:       asc or desc order
    :param attribute:   request order by attribute in directors
    :return:            json string of list of limit directors order by req, message data empty
    """
    # check attribute
    if not hasattr(Directors, attribute):
        abort(404, f"Director not found for attribute {attribute}!")

    # Create the list of directors from our data
    # match attribute:
    if attribute == 'id':
        directors = Directors.query.order_by(db.desc(
            Directors.id) if f'{order}' == 'desc' else db.asc(Directors.id)).limit(limit)
    elif attribute == 'name':
        directors = Directors.query.order_by(db.desc(
            Directors.name) if f'{order}' == 'desc' else db.asc(Directors.name)).limit(limit)
    elif attribute == 'gender':
        directors = Directors.query.order_by(db.desc(
            Directors.gender) if f'{order}' == 'desc' else db.asc(Directors.gender)).limit(limit)
    elif attribute == 'uid':
        directors = Directors.query.order_by(db.desc(
            Directors.uid) if f'{order}' == 'desc' else db.asc(Directors.uid)).limit(limit)
    elif attribute == 'department':
        directors = Directors.query.order_by(db.desc(
            Directors.department) if f'{order}' == 'desc' else db.asc(Directors.department)).limit(limit)

    # Serialize the data for the response
    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)

    if(len(data) == 0):
        return abort(404, f"Directors data not found!")

    return data


def read_one(id):
    """
    This function responds to a request for /api/directors/{id}
    with one matching director from directors

    :param id:          Id of director to find
    :return:            director matching id, 404 if not found
    """
    # Build the initial query
    director = Directors.query.filter(Directors.id == id).one_or_none()

    # Did we find a director?
    if director is not None:

        # Serialize the data for the response
        director_schema = DirectorsSchema()
        data = director_schema.dump(director)
        return data

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for ID: {id}!")


def create(director):
    """
    This function creates a new director in the directors structure
    based on the passed in director data

    :param director:  director to create in directors structure
    :return:          201 on success, 409 on director exists
    """

    name = director.get("name")
    uid = director.get("uid")
    gender = director.get("gender")
    department = director.get("department")

    if name is None or name is "":
        abort(400, "Field name must be required!")
    if uid is None or uid is "":
        abort(400, "Field uid must be required!")
    if gender is None or gender is "":
        abort(400, "Field name must be required!")
    if department is None or department is "":
        abort(400, "Field name must be required!")

    existing_director = (
        Directors.query.filter(Directors.name == name)
        .filter(Directors.uid == uid)
        .one_or_none()
    )

    # Can we insert this director?
    if existing_director is None:

        # Create a director instance using the schema and the passed in director
        schema = DirectorsSchema()
        new_director = schema.load(director, session=db.session)

        # Add the director to the database
        db.session.add(new_director)
        db.session.commit()

        # Serialize and return the newly created director in the response
        data = schema.dump(new_director)

        return data, 201

    # Otherwise, nope, director exists already
    else:
        abort(409, f"Director with name {name} or UID {uid} exists already!")


def update(id, director):
    """
    This function updates an existing director in the directors structure

    :param id:          Id of the director to update in the directors structure
    :param director:    director to update
    :return:            updated director structure, 404 if not found
    """
    name = director.get("name")
    uid = director.get("uid")
    gender = director.get("gender")
    department = director.get("department")

    if name is None or name is "":
        abort(400, "Field name must be required!")
    if uid is None or uid is "":
        abort(400, "Field uid must be required!")
    if gender is None or gender is "":
        abort(400, "Field gender must be required!")
    if department is None or department is "":
        abort(400, "Field department must be required!")

    # Get the director requested from the db into session
    update_director = Directors.query.filter(
        Directors.id == id
    ).one_or_none()

    # Did we find an existing director?
    if update_director is not None:

        # turn the passed in director into a db object
        schema = DirectorsSchema()
        update = schema.load(director, session=db.session)

        # Set the id to the director we want to update
        update.id = update_director.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated director in the response
        data = schema.dump(update_director)

        return data, 200

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for ID: {id}!")


def delete(id):
    """
    This function deletes a director from the directors structure

    :param director_id:   Id of the director to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the director requested
    director = Directors.query.filter(Directors.id == id).one_or_none()

    # Did we find a director?
    if director is not None:
        db.session.delete(director)
        db.session.commit()
        return make_response(f"Director with ID {id} deleted successfully!", 200)

    # Otherwise, nope, didn't find that director
    else:
        abort(404, f"Director not found for ID: {id}!")


def search_all(keyword):
    """search data by field name with like

    Keyword arguments:  keyword -- word for search data use like
    Return: data directors with name like keyword
    """
    search = "%{}%".format(keyword)
    directors = Directors.query.filter(Directors.name.like(search)).all()

    # Serialize the data for the response
    director_schema = DirectorsSchema(many=True)
    data = director_schema.dump(directors)

    if(len(data) == 0):
        return abort(404, f"Directors data not found with keyword {keyword}!")

    return data
