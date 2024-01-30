from app.lib.custom_exceptions import DuplicateRecordException, CreateRecordFailedException, ForbiddenException
from app.repository import LearningRepo
from flask import current_app as cdp_app, g


class LearningService:
    @staticmethod
    def create_learning_record(learning_data):
        cdp_app.logger.info('Called Learning Service - create_learning_record')
        learning = LearningRepo.get_learning_record(
            learning_data["associate_id"], learning_data["skill_name"])
        if learning:
            msg = (f'Duplicate Record for associate_id {learning_data["associate_id"]}'
                   f' and {learning_data["skill_name"]}')
            cdp_app.logger.error(msg)
            raise DuplicateRecordException(msg)
        try:
            learning = LearningRepo.create_learning(learning_data)
        except Exception as ex:
            cdp_app.logger.error(f'DB Record creation failed | {ex}')
            raise CreateRecordFailedException

        cdp_app.logger.info('Service call create_learning_record created successfully')

        return learning

    @staticmethod
    def update_learning_record(learning_data):
        cdp_app.logger.info('Called Learning Service - create_learning_record')
        learning = LearningRepo.get_learning_record_by_id(learning_data["learning_id"])
        if not learning:
            msg = 'Record not exists with the learning_id {learning_data["learning_id"]}'
            cdp_app.logger.error(msg)
            raise DuplicateRecordException(msg)

        if learning.associate_id != g.jwt_payload.get('associate_id', ''):
            msg = f'You are not authorized to access this record'
            raise ForbiddenException(msg)

        try:
            learning = LearningRepo.create_learning(learning_data)
        except Exception as ex:
            cdp_app.logger.error(f'DB Record creation failed | {ex}')
            raise CreateRecordFailedException

        cdp_app.logger.info('Service call create_learning_record created successfully')

        return learning