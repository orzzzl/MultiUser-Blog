# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
from handler import main_page
from handler import login_handler
from handler import register
from handler import front
from handler import newpost
from handler import permalink
from handler import logout_handler


app = webapp2.WSGIApplication([
    ('/', main_page.MainPage),
    ('/login', login_handler.LoginHandler),
    ('/register', register.RegisterHandler),
    ('/front', front.FrontHandler),
    ('/newpost', newpost.NewPostHandler),
    ('/permalink/([0-9]+)', permalink.Permalink),
    ('/logout', logout_handler.Logout)
], debug=True)
