#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Telegram bot to play UNO in group chats
# Copyright (c) 2016 Jannes Höke <uno@jhoeke.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import json

with open("config.json","r") as f:
    config = json.loads(f.read())

TOKEN = 2125839096:AAEquwngQspHnA9emK8G_CC6Uh-JszqgYpU
WORKERS = 32
ADMIN_LIST = 1514078508
OPEN_LOBBY = True
ENABLE_TRANSLATIONS = False
DEFAULT_GAMEMODE = fast
WAITING_TIME = 120
TIME_REMOVAL_AFTER_SKIP = 20
MIN_FAST_TURN_TIME = 15
MIN_PLAYERS = 5
