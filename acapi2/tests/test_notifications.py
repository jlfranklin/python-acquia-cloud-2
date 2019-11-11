#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Test Notifications Endpoint"""

import requests_mock

from acapi2.resources.notificationlist import NotificationList
from acapi2.tests import BaseTest


@requests_mock.Mocker()
class TestNotifications(BaseTest):

    def test_notifications(self, mocker):
        response = {
            "total": 1,
            "pagination": {
                "total": 1,
                "limit": 1,
                "offset": 0
            },
            "_links": {
                "self": {
                    "href": "https://cloud.acquia.dev/api/applications/"
                            "f027502b-ed6c-448e-97e8-4a0def7d25e1"
                            "/notifications"
                },
                "parent": {
                    "href": "https://cloud.acquia.dev/api/applications/"
                            "f027502b-ed6c-448e-97e8-4a0def7d25e1"
                },
                "limit": {
                    "href": "https://cloud.acquia.dev/api/applications/"
                            "f027502b-ed6c-448e-97e8-4a0def7d25e1"
                            "/notifications{?limit}",
                    "templated": True
                },
                "offset": {
                    "href": "https://cloud.acquia.dev/api/applications/"
                            "f027502b-ed6c-448e-97e8-4a0def7d25e1"
                            "/notifications{?offset}",
                    "templated": True
                },
                "sort": {
                    "href": "https://cloud.acquia.dev/api/applications/"
                            "f027502b-ed6c-448e-97e8-4a0def7d25e1"
                            "/notifications{?sort}",
                    "templated": True
                },
                "filter": {
                    "href": "https://cloud.acquia.dev/api/applications/"
                            "f027502b-ed6c-448e-97e8-4a0def7d25e1"
                            "/notifications{?filter}",
                    "templated": True
                }
            },
            "_embedded": {
                "items": [
                    {
                        "uuid": "1bd3487e-71d1-4fca-a2d9-5f969b3d35c1",
                        "event": "ApplicationAddedToRecents",
                        "label": "Application added to recents list",
                        "description": "Canary QA 11 - ACE was added "
                                       "to your recent applications list.",
                        "created_at": "2019-07-29T20:47:13+00:00",
                        "completed_at": "2019-07-29T20:47:13+00:00",
                        "status": "completed",
                        "progress": 100,
                        "context": {
                            "author": {
                                "uuid": "5391a8a9-d273-4f88-8114-7f884bbfe08b",
                                "actual_uuid": "5391a8a9-d273-"
                                               "4f88-8114-7f884bbfe08b"
                            },
                            "user": {
                                "uuids": [
                                    "5391a8a9-d273-4f88-8114-7f884bbfe08b"
                                ]
                            },
                            "application": {
                                "uuids": [
                                    "f027502b-ed6c-448e-97e8-4a0def7d25e1"
                                ]
                            }
                        }
                    }
                ]
            }
        }

        app_uuid = "f027502b-ed6c-448e-97e8-4a0def7d25e1"
        uri = f"{self.endpoint}/applications/{app_uuid}/notifications"
        mocker.register_uri("GET", uri, status_code=200, json=response)
        notif = self.acquia.application(app_uuid).notifications()

        self.assertIsInstance(notif, NotificationList)
