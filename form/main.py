#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import cgi

form = """
<form method="post">
	<textarea name="text" cols="30" rows="10">%(value)s</textarea>
        <br>
    	<input type="submit">
</form>

"""

class MainHandler(webapp2.RequestHandler):
    def write_form(self, value=""):
        self.response.out.write(form %{"value": value})
    def get(self):
	self.write_form()

    def post(self):
	user_input = self.request.get('text')
        rot13_output = self.rot13(user_input)
        self.write_form(rot13_output)

    def rot13(self, user_input):
        temp = ""
        for i in user_input:
            char = ord(i)
            if ( (char >= 65 and char <= 77) or (char >= 97 and char <= 109) ):
                temp = temp + chr(char + 13)
            elif char > 77 and char <= 90:
                temp = temp + chr(13 - (90 - char) + 64)
            elif char > 109 and char <= 122:
                temp = temp + chr(13 - (122 - char) + 96)
            else:
                temp = temp + i
        escape_temp = cgi.escape(temp, quote=True)
        return escape_temp
            
app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)
