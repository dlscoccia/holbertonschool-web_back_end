#!/usr/bin/env python3
"""python"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
from models.user import User
from os import getenv


class SessionExpAuth(SessionAuth):
    """Expiration"""

    def __init__(self):
        """init"""
        SESSION_DURATION = getenv('SESSION_DURATION')

        try:
            session_duration = int(SESSION_DURATION)
        except Exception:
            session_duration = 0

        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """Create session"""

        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """user_id"""

        if session_id is None:
            return None

        user_id = self.user_id_by_session_id.get(session_id)

        if user_id is None:
            return None

        if self.session_duration <= 0:
            return user_id

        session_dictionary = self.user_id_by_session_id.get(session_id)

        if session_dictionary is None:
            return None

        if 'created_at' not in session_dictionary:
            return None

        created_at = session_dictionary['created_at']

        expired_time = created_at + timedelta(seconds=self.session_duration)

        if expired_time < datetime.now():
            return None

        return session_dictionary.get('user_id')
