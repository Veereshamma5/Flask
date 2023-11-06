from flask import Blueprint
from flask import request
from app.models import Allocation
from app.repo.sqlcontext import SqlContext
from http import HTTPStatus

study_bp = Blueprint('study_bp', __name__)


@study_bp.route('/scheduled/time', methods=['POST'])
def create_timetable():
    timetable_data = request.json

    study_obj = Allocation()

    study_obj.initial_percentage = timetable_data['initial_percentage']
    study_obj.final_percentage = timetable_data['final_percentage']
    study_obj.email = timetable_data['email']
    study_obj.created_on = timetable_data['created_on']
    study_obj.base_amount = timetable_data['base_amount']
    study_obj.allocation_date = timetable_data['allocation_date']
    study_obj.distribution_percentage = timetable_data['distribution_percentage']
    study_obj.threshold_amount = timetable_data['threshold_amount']

    with SqlContext() as sql_context:
        sql_context.session.add(study_obj)
    return 'Student time table created successfully', HTTPStatus.CREATED
