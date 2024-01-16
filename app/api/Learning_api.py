from http import HTTPStatus

from flask import Blueprint, jsonify
from flask import request
from flask import current_app as learning_app
from flasgger import swag_from

from app.lib.custom_exceptions import DuplicateRecordException, CreateRecordFailedException, ForbiddenException
from app.service import LearningService
from app.api.authentication import authorize_role, authorize_role_access, authorize_admin
from app.lib.constants import ASSOCIATE_ROLE, ADMIN_ROLE, ACCESS
from app.tasks import send_new_learning_email

learning_bp = Blueprint('learning_bp', __name__)


@learning_bp.route('/learning/create', methods=['POST'])
# @authorize_role(ASSOCIATE_ROLE)
# @authorize_admin
@swag_from('/api/api_docs/learning_apis/create_learning.yml')
def create_timetable():
    learning_data = request.json
    try:
        learning_app.logger.info("/learning/create----- api called")
        learning = LearningService.create_learning_record(learning_data)
        print("Learning Information is:::::", learning)
    except DuplicateRecordException as ex:
        return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.BAD_REQUEST
    except CreateRecordFailedException as ex:
        return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.INTERNAL_SERVER_ERROR
    recipient_name = ' '.join(map(lambda item: item.capitalize(), learning_data['email'].split('@')[0].split('.')))
    # send_new_learning_email.s(learning_data['email'], recipient_name, learning_data['skill_name']).apply_async()
    return jsonify({'status': 'success', 'data': 'Record created successfully'}), HTTPStatus.CREATED


@learning_bp.route('/learning/update', methods=['PUT'])
# @authorize_role_access(ASSOCIATE_ROLE, ACCESS)
def update_timetable():
    learning_data = request.json
    try:
        learning_app.logger.info("/learning/update----- api called")
        learning = LearningService.update_learning_record(learning_data['learning_id'])
        # learning_schema = LearningSchema()
        # learning_serializer = learning_schema.dump(learning)
    except DuplicateRecordException as ex:
        return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.BAD_REQUEST
    except CreateRecordFailedException as ex:
        return jsonify({'status': 'error', 'data': str(ex)}), HTTPStatus.INTERNAL_SERVER_ERROR
    except ForbiddenException as ex:
        return jsonify({'status':'error', 'data': str(ex)}), HTTPStatus.FORBIDDEN
    recipient_name = ' '.join(map(lambda item: item.capitalize(), learning_data['email'].split('@')[0].split('.')))
    # send_new_learning_email.s(learning_data['email'], recipient_name, learning_data['skill_name']).apply_async()
    return jsonify({'status': 'success', 'data': 'Record created successfully'}), HTTPStatus.CREATED

    # timetable_data = request.json
    #
    # learning_obj = Learning()
    #
    # learning_obj.associate_id = timetable_data["associate_id"]
    # learning_obj.email = timetable_data['email']
    # learning_obj.skill_name = timetable_data['skill_name']
    # learning_obj.learning_resource = timetable_data['learning_resource']
    # learning_obj.resource_link = timetable_data['resource_link']
    # learning_obj.duration = timetable_data['duration']
    # learning_obj.end_datetime = timetable_data['end_datetime']
    # learning_obj.status = timetable_data['status']
    #
    # with SqlContext() as sql_context:
    #     sql_context.session.add(learning_obj)
    # return 'Learning time table created successfully', HTTPStatus.CREATED
