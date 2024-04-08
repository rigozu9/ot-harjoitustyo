#Class for survey application logic

class SurveyService:
    def __init__(self, survey_repository):
        self.survey_repository = survey_repository