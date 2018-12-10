from flask import Blueprint, jsonify

ErrorHandlerBlueprint = Blueprint('ErrorHandlerBlueprint', __name__)

@ErrorHandlerBlueprint.errorhandler(404)
def notFoundErrorHandler(error):
    response = {
        'status': False,
        'message': 'You\'re not allowed from this action'
    }
    return jsonify(response), 404

@ErrorHandlerBlueprint.errorhandler(401)
def unAuthorizedErrorHandler(error):
    response = {
        'status': False,
        'message': 'You\'re not allowed from this action'
    }
    return jsonify(response), 401