# encoding: utf-8

import logging

from app.core.utils.Exceptions import UnknownProjectException
from app.core.ProjectHandler import ProjectHandler


class ProjectsManager(object):

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self.__project_handlers_by_project_id = dict()    

    def get_project_handler(self, project_id):
        if project_id is None:
            raise ValueError("Project_id cannot be None")

        if project_id not in self.__project_handlers_by_project_id.keys():
            project_handler = ProjectHandler(project_id)
            self.__project_handlers_by_project_id[project_id] = project_handler

        return self.__project_handlers_by_project_id[project_id]

    

        
