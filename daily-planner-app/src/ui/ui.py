""""Rekisteröionnyn import """
from ui.registration_form import RegistrationForm
from ui.login_form import LoginForm
from ui.today_view import TodayView
from ui.survey_view import SurveyView
from ui.calendar_view import CalendarView
from ui.daily_planner_view import DailyPlanner
from ui.user_info_view import UserInfoView
from ui.advice_view import AdvicePageView


class UI:
    """"Näkymien hallinnan tiedosto """

    def __init__(self, root, user_service, daily_plan_service):
        self._root = root
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service
        self._current_view = None
        self._views = self._add_views_to_dict()

    def start(self):
        """start funktio rekisteröinty forumille"""
        self._show_registration_view()

    def _show_registration_view(self):
        RegistrationForm(self._root,
                         self._user_service,
                         self._daily_plan_service,
                         self._views)

    def _show_login_view(self):
        LoginForm(self._root,
                  self._user_service,
                  self._daily_plan_service,
                  self._views)

    def _show_today_view(self, user_id, choosen_date=None):
        TodayView(self._root,
                  user_id,
                  self._user_service,
                  self._daily_plan_service,
                  self._views,
                  choosen_date)

    def _show_survey_view(self, user_id):
        SurveyView(self._root,
                   user_id,
                   self._user_service,
                   self._daily_plan_service,
                   self._views)

    def _show_calendar_view(self, user_id):
        CalendarView(self._root,
                     user_id,
                     self._user_service,
                     self._daily_plan_service,
                     self._views)

    def _show_daily_planner_view(self, user_id, choosen_date=None):
        DailyPlanner(self._root,
                     user_id,
                     self._user_service,
                     self._daily_plan_service,
                     self._views,
                     choosen_date)

    def _show_user_info_view(self, user_id):
        UserInfoView(self._root,
                     user_id,
                     self._user_service,
                     self._daily_plan_service,
                     self._views)

    def _show_user_advice_view(self, user_id):
        AdvicePageView(self._root,
                       user_id,
                       self._user_service,
                       self._daily_plan_service,
                       self._views)

    def _add_views_to_dict(self):
        """Store view functions in a dictionary for easy access and management."""
        views = {
            'register': self._show_registration_view,
            'login': self._show_login_view,
            'today': self._show_today_view,
            'survey': self._show_survey_view,
            'calendar': self._show_calendar_view,
            'daily_planner': self._show_daily_planner_view,
            'user_info': self._show_user_info_view,
            'user_advice': self._show_user_advice_view
        }
        return views
